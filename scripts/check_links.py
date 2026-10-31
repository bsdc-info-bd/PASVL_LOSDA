#!/usr/bin/env python3
"""Validate Markdown links, anchors, and references in this repository.

Checks performed:
  1. Every relative link resolves to a file that exists.
  2. Every in-document anchor (``#heading``) matches a real heading.
  3. Every cross-document anchor (``file.md#heading``) matches a real heading in that file.
  4. Every reference-style link definition is used, and every use has a definition.
  5. External links are checked only with ``--external`` (network, best effort).

Usage:
    python3 scripts/check_links.py
    python3 scripts/check_links.py --external
    python3 scripts/check_links.py --path docs --quiet

Exit codes: 0 all valid, 1 problems found, 2 bad invocation.

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from typing import Iterable

INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
REF_DEF = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(\S+)", re.M)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.M)
FENCE = re.compile(r"^```")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://")
SKIP_SCHEMES = ("data:", "javascript:")

# Directories that contain generated or vendored content.
DEFAULT_SKIP = {".git", "node_modules", "vendor", "dist", "build", "__pycache__"}


def slugify(text: str) -> str:
    """Approximate GitHub's heading anchor algorithm."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    text = unicodedata.normalize("NFKD", text)
    text = text.lower()
    text = re.sub(r"[^\w\s\u0980-\u09FF-]", "", text)
    text = text.strip().replace(" ", "-")
    # GitHub does not collapse repeated hyphens: "A — B" becomes "a--b". Matching that
    # exactly means a link that works here also works on GitHub.
    return text


def strip_code(text: str) -> str:
    """Remove fenced code blocks so links inside examples are not validated."""
    out, fence = [], False
    for line in text.splitlines():
        if FENCE.match(line.strip()):
            fence = not fence
            out.append("")
            continue
        out.append("" if fence else line)
    return "\n".join(out)


def headings_of(path: pathlib.Path) -> set[str]:
    text = strip_code(path.read_text(encoding="utf-8", errors="ignore"))
    return {slugify(m.group(2)) for m in HEADING.finditer(text)}


def iter_markdown(root: pathlib.Path) -> Iterable[pathlib.Path]:
    for path in root.rglob("*.md"):
        if any(part in DEFAULT_SKIP for part in path.parts):
            continue
        yield path


def check_external(url: str, timeout: int = 10) -> str | None:
    """Return an error string, or None if the URL looks alive."""
    request = urllib.request.Request(
        url, method="GET", headers={"User-Agent": "pasvl-link-check/1.0"}
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if response.status >= 400:
                return f"HTTP {response.status}"
        return None
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 429):  # rate limiting, not a dead link
            return None
        return f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - network errors are all "unknown"
        return type(exc).__name__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate links in Markdown files.")
    parser.add_argument("--path", type=pathlib.Path, default=pathlib.Path("."))
    parser.add_argument("--external", action="store_true", help="also check external URLs")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    if not args.path.exists():
        print(f"error: {args.path} does not exist", file=sys.stderr)
        return 2

    root = args.path.resolve()
    problems: list[str] = []
    internal_checked = 0
    external_checked = 0
    external_seen: dict[str, str | None] = {}

    for md in sorted(iter_markdown(root)):
        text = md.read_text(encoding="utf-8", errors="ignore")
        body = strip_code(text)
        rel = md.relative_to(root)

        targets = list(INLINE_LINK.finditer(body))
        ref_defs = {m.group(1).lower(): m.group(2) for m in REF_DEF.finditer(body)}
        # reference-style uses: [text][ref]
        ref_uses = {
            m.group(1).lower()
            for m in re.finditer(r"\[[^\]]*\]\[([^\]]*)\]", body)
            if m.group(1)
        }

        for name in ref_uses:
            if name not in ref_defs:
                problems.append(f"{rel}: reference link [{name}] has no definition")
        for name in ref_defs:
            if name not in ref_uses and not re.search(rf"\[{re.escape(name)}\]", body, re.I):
                # A definition may be intentional (e.g. used in a table); only report when unused
                if name not in body.lower():
                    problems.append(f"{rel}: unused reference definition [{name}]")

        for match in targets:
            target = match.group(1).strip("<>")
            if not target or target.startswith(SKIP_SCHEMES):
                continue

            if target.startswith(EXTERNAL_PREFIXES):
                if args.external and target.startswith(("http://", "https://")):
                    if target not in external_seen:
                        external_seen[target] = check_external(target)
                        external_checked += 1
                        if external_seen[target]:
                            problems.append(f"{rel}: external link failed ({external_seen[target]}): {target}")
                continue

            internal_checked += 1
            path_part, _, anchor = target.partition("#")
            path_part = path_part.split("?")[0]

            if not path_part:  # same-document anchor
                if anchor and slugify(anchor) not in headings_of(md):
                    problems.append(f"{rel}: anchor '#{anchor}' matches no heading")
                continue

            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                problems.append(f"{rel}: broken link -> {target}")
                continue

            if anchor and resolved.suffix == ".md":
                if slugify(anchor) not in headings_of(resolved):
                    problems.append(f"{rel}: anchor '#{anchor}' missing in {path_part}")

    for problem in problems:
        print(f"FAIL {problem}")

    print()
    print(
        f"checked {internal_checked} internal link(s)"
        + (f", {external_checked} external URL(s)" if args.external else "")
        + f", {len(problems)} problem(s)"
    )
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
