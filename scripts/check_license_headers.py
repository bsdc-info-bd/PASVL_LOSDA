#!/usr/bin/env python3
"""Check that source files carry a PASVL licence header.

A licence header is not a formality: it is the notice that a deployer relies on and that a
court looks for. This script fails CI when a source file is missing one.

Usage:
    python3 scripts/check_license_headers.py --path .
    python3 scripts/check_license_headers.py --path src --fix --year 2026 --author "Acme Labs"
    python3 scripts/check_license_headers.py --path . --exclude vendor --exclude node_modules

Exit codes: 0 all good, 1 missing headers, 2 bad invocation.

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

EXTENSIONS = {
    ".py": "python",
    ".js": "c",
    ".jsx": "c",
    ".ts": "c",
    ".tsx": "c",
    ".java": "c",
    ".kt": "c",
    ".kts": "c",
    ".c": "c",
    ".h": "c",
    ".cc": "c",
    ".cpp": "c",
    ".hpp": "c",
    ".cs": "c",
    ".go": "c",
    ".rs": "c",
    ".swift": "c",
    ".scala": "c",
    ".php": "c",
    ".rb": "hash",
    ".sh": "hash",
    ".bash": "hash",
    ".zsh": "hash",
    ".yaml": "hash",
    ".yml": "hash",
    ".toml": "hash",
    ".tf": "hash",
    ".dockerfile": "hash",
    ".html": "html",
    ".htm": "html",
    ".xml": "html",
    ".svg": "html",
    ".md": "html",
    ".css": "c",
    ".scss": "c",
}

MARKER = "SPDX-License-Identifier: LicenseRef-PASVL-1.0"

TEMPLATES = {
    "python": (
        "# Copyright (c) {year} {author}\n"
        "# Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.\n"
        "# {marker}\n"
    ),
    "hash": (
        "# Copyright (c) {year} {author}\n"
        "# Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.\n"
        "# {marker}\n"
    ),
    "c": (
        "/*\n"
        " * Copyright (c) {year} {author}\n"
        " * Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.\n"
        " * {marker}\n"
        " */\n"
    ),
    "html": (
        "<!--\n"
        "  Copyright (c) {year} {author}\n"
        "  Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.\n"
        "  {marker}\n"
        "-->\n"
    ),
}

DEFAULT_EXCLUDES = {
    ".git",
    ".github/ISSUE_TEMPLATE",
    "node_modules",
    "vendor",
    "dist",
    "build",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "coverage",
}


def has_header(path: pathlib.Path) -> bool:
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            head = handle.read(2000)
    except OSError:
        return True  # unreadable files are not this script's problem
    return MARKER in head


def add_header(path: pathlib.Path, style: str, year: str, author: str) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    header = TEMPLATES[style].format(year=year, author=author, marker=MARKER)
    if style in {"python"} and text.startswith("#!"):
        first, _, rest = text.partition("\n")
        path.write_text(f"{first}\n{header}{rest}", encoding="utf-8")
    elif text.startswith("<?xml"):
        first, _, rest = text.partition("\n")
        path.write_text(f"{first}\n{header}{rest}", encoding="utf-8")
    else:
        path.write_text(header + "\n" + text, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check for PASVL licence headers.")
    parser.add_argument("--path", type=pathlib.Path, default=pathlib.Path("."))
    parser.add_argument("--exclude", action="append", default=[])
    parser.add_argument("--fix", action="store_true", help="insert missing headers")
    parser.add_argument("--year", default="2026")
    parser.add_argument("--author", default="")
    parser.add_argument(
        "--allow-missing",
        action="append",
        default=[],
        help="files that legitimately have no header (e.g. LICENSE, NOTICE)",
    )
    args = parser.parse_args(argv)

    if args.fix and not args.author:
        print("error: --fix requires --author", file=sys.stderr)
        return 2

    excludes = DEFAULT_EXCLUDES | set(args.exclude)
    allow = set(args.allow_missing) | {
        "LICENSE",
        "NOTICE",
        "README.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
        "TRADEMARK.md",
        "GOVERNANCE.md",
        "CITATION.cff",
    }

    missing: list[pathlib.Path] = []
    checked = 0

    for path in sorted(args.path.rglob("*")):
        if not path.is_file():
            continue
        if any(part in excludes for part in path.parts):
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if path.name in allow:
            continue

        checked += 1
        if has_header(path):
            continue

        missing.append(path)
        if args.fix:
            add_header(path, EXTENSIONS[path.suffix], args.year, args.author)
            print(f"fixed  {path}")

    for path in missing:
        print(f"missing licence header: {path}")

    print()
    print(f"{checked} file(s) checked, {len(missing)} missing a header")
    if missing and not args.fix:
        print("Add the header from templates/LICENSE-HEADER.txt, or run with --fix.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
