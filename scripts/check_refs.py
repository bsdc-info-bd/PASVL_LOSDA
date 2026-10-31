#!/usr/bin/env python3
"""Validate every cross-reference to a numbered clause in this repository.

A legal framework is only as good as its cross-references. A document that says
"see §6.7" when there is no §6.7 sends a reader — or a court — to a clause that
does not exist. This script resolves each citation against the instrument it
names:

  * ``PASVL §5.2`` and a bare ``§5.2`` resolve against ``LICENSE``.
  * ``LOSDA spec §6.7`` resolves against ``legal/losda-specification.md``.

Citations of foreign statutes (BGB, UrhG, DMCA, USC and the like) are left
alone: they point outside this repository.

Usage:
    python3 scripts/check_refs.py
    python3 scripts/check_refs.py --quiet

Exit codes: 0 all references resolve, 1 unresolved reference found.

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

# A citation is "<instrument> §N" or "<instrument> §N.M".
REFERENCE = re.compile(
    r"(?:(?P<instrument>PASVL|LOSDA\s+spec(?:ification)?)\s*)?"
    r"§§?\s*(?P<article>\d+)(?:\.(?P<section>\d+))?"
)

# Foreign statutes cited as authority. These are not clauses of this framework.
FOREIGN_STATUTE = re.compile(
    r"(BGB|UrhG|StGB|ZPO|GG|DMCA|USC|CFR|CDPA|UCC)\b",
)

# Specific external provisions the framework cites by number. Listed explicitly so
# that a genuinely mistyped PASVL section is never silently ignored.
EXTERNAL_PROVISION = re.compile(r"§\s?(1201|512|305|69d?)(?![\d.])")

# Articles are numbered headings in the License and plain headings in the spec.
ARTICLE_NUMBERING = re.compile(
    r"^(?:#{2,4}\s+ARTICLE\s+(\d+)\b|##\s+(\d+)\.\s+)", re.M
)

# Sub-sections are bold leads ("**5.2 Title.**") or, for the LOSDA class list,
# sub-headings ("### 6.1 Class S").
SECTION_NUMBERING = re.compile(
    r"^(?:\*\*(\d+)\.(\d+)|#{3,5}\s+(\d+)\.(\d+)\s)", re.M
)
FENCE = re.compile(r"^\s*```")


def strip_code(text: str) -> str:
    """Blank out fenced code blocks so examples are not treated as citations."""
    out, inside = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return "\n".join(out)


def outline(path: pathlib.Path):
    """Return (set of article numbers, set of 'N.M' sections) for one instrument."""
    text = strip_code(path.read_text(encoding="utf-8"))
    articles = {
        a or b for a, b in (m.groups() for m in ARTICLE_NUMBERING.finditer(text))
    }
    sections = set()
    for m in SECTION_NUMBERING.finditer(text):
        first, second = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        sections.add(f"{first}.{second}")
    return articles, sections


def instruments():
    return {
        "pasvl": outline(ROOT / "LICENSE"),
        "losda": outline(ROOT / "legal" / "losda-specification.md"),
    }


def check(root: pathlib.Path, outlines) -> list[str]:
    problems: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        rel = path.relative_to(root)
        for line_no, line in enumerate(
            strip_code(path.read_text(encoding="utf-8", errors="ignore")).splitlines(), 1
        ):
            if FOREIGN_STATUTE.search(line) or EXTERNAL_PROVISION.search(line):
                continue
            for match in REFERENCE.finditer(line):
                article = match.group("article")
                section = match.group("section")
                instrument = match.group("instrument") or "PASVL"
                key = "losda" if instrument.upper().startswith("LOSDA") else "pasvl"
                articles, sections = outlines[key]
                prefix = "L" if key == "pasvl" else "LOSDA"
                label = f"§{article}" + (f".{section}" if section else "")

                if article not in articles:
                    problems.append(
                        f"{rel}:{line_no}: {label} -> {prefix} has no Article {article}"
                        if key == "pasvl"
                        else f"{rel}:{line_no}: {label} -> LOSDA spec has no §{article}"
                    )
                elif section and f"{article}.{section}" not in sections:
                    problems.append(
                        f"{rel}:{line_no}: {label} -> Article {article} has no §{label[1:]}"
                    )
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate cross-references to numbered clauses.")
    parser.add_argument("--path", default=str(ROOT), help="repository root to scan")
    parser.add_argument("--quiet", action="store_true", help="print only failures")
    args = parser.parse_args(argv)

    root = pathlib.Path(args.path).resolve()
    outlines = instruments()
    for name, (articles, sections) in outlines.items():
        if not articles:
            print(f"error: could not read the outline of {name}", file=sys.stderr)
            return 2

    problems = check(root, outlines)
    for problem in problems:
        print(f"FAIL {problem}")

    if not args.quiet:
        counts = ", ".join(
            f"{name}: {len(a)} Article(s)/{len(s)} section(s)"
            for name, (a, s) in outlines.items()
        )
        print(f"\nreference check: {counts}")
        print(f"{len(problems)} unresolved reference(s)")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
