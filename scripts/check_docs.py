#!/usr/bin/env python3
"""Deterministic prose and Markdown checks for this repository.

These checks catch the errors that a spellchecker cannot see: inconsistent spelling,
doubled words, wrong articles, unbalanced delimiters, duplicated headings, and stray
whitespace. They are fast, offline, and have no false positives by design.

Rules
  1. No British spellings. The framework's instrument is the "PASVL License", and every
     document must use one variant consistently. American is the reference variant.
  2. No doubled words ("the the", "of of").
  3. "a" must not precede a vowel sound ("a applicable" -> "an applicable").
  4. Delimiters must balance within a file: parentheses, brackets, bold markers.
  5. No duplicate headings within a file (duplicate anchors break deep links).
  6. No trailing whitespace, tabs, or carriage returns.
  7. No double spaces inside prose (alignment in code blocks is exempt).
  8. No "shall" in this framework's own drafting; the house style is "must".

Usage
    python3 scripts/check_docs.py
    python3 scripts/check_docs.py --path docs legal governance
    python3 scripts/check_docs.py --quiet

Exit codes: 0 clean, 1 problems found, 2 bad invocation.

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

# British -> American. Only forms that differ; words spelled the same in both are absent.
BRITISH = {
    "licence", "licences", "licenced", "licencing",
    "authorise", "authorised", "authorises", "authorising",
    "authorisation", "authorisations",
    "organisation", "organisations", "organised", "organise", "organising",
    "recognise", "recognised", "recognises", "unrecognised",
    "summarise", "summarised", "summarises",
    "anonymise", "anonymised", "anonymisation",
    "regularise", "regularised", "regularisation",
    "minimise", "minimised", "minimisation",
    "behaviour", "behaviours",
    "favour", "favours", "favoured",
    "honour", "honours",
    "colour", "colours",
    "defence", "defences", "offence", "offences",
    "programme", "programmes",
    "acknowledgement", "acknowledgements",
    "catalogue", "catalogues",
    "analyse", "analysed", "analysing",
    "criticise", "criticised", "publicise", "publicised",
    "monetise", "monetised", "localise", "localisation",
    "capitalise", "capitalisation", "marginalise", "marginalised",
    "normalise", "normalises", "initialise", "initialised",
    "containerise", "containerised", "containerisation",
    "plagiarise", "plagiarised", "apologise", "apologised",
    "deputise", "deputises", "unauthorised",
    "travelling", "modelled", "modelling", "cancelled", "labelled",
    "signalling", "fulfilment", "enrolment", "practising",
    # Prepositions and connectives with a British and an American form.
    "towards", "whilst", "amongst", "amidst", "learnt", "spelt", "burnt",
    "judgement", "judgements", "artefact", "artefacts",
    "sceptic", "sceptical", "scepticism", "labour", "harbour",
    "hypothesise", "hypothesised", "initialisation",
}

DOUBLED_OK = {"that", "had", "is", "n"}  # "had had" can be correct

# Words starting with a vowel letter but pronounced with a consonant sound.
CONSONANT_SOUND = ("one", "once", "eu", "uni", "us", "ut", "ur")

SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", "__pycache__", ".venv"}
PROSE_SUFFIXES = {".md", ".txt", ""}
# Configuration files are not prose and may quote spellings deliberately.
SKIP_NAMES = {"VERSION", "CODEOWNERS", ".codespellrc", ".gitignore", ".gitattributes"}


def strip_code(text: str):
    """Return prose lines with fenced code replaced by blanks, plus a fence-parity flag."""
    out, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            out.append("")
            continue
        out.append("" if fence else line)
    return out, fence


INLINE_CODE = re.compile(r"`[^`]*`")


CODE_TOKEN = "ZCODEZ"


def strip_inline_code(line: str) -> str:
    """Replace `inline code` with a consonant-initial token.

    A sentinel rather than a blank keeps "a `FILE` entry" from being read as "a entry",
    which would be a false positive: the article agrees with the code span, not the
    following word.
    """
    return INLINE_CODE.sub(CODE_TOKEN, line)


def is_quoted(line: str, start: int, end: int) -> bool:
    """True when the match sits inside a quoted phrase, e.g. the word under discussion."""
    before = line[:start]
    after = line[end:]
    opener = max(before.rfind('"'), before.rfind("\u201c"), before.rfind("'"))
    if opener == -1:
        return False
    closer_candidates = [
        i for i in (after.find('"'), after.find("\u201d"), after.find("'")) if i != -1
    ]
    return bool(closer_candidates)


def check_file(path: pathlib.Path, rel: str) -> list[str]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    problems: list[str] = []
    is_markdown = path.suffix == ".md"

    if "\r" in raw:
        problems.append(f"{rel}: contains carriage returns (CRLF line endings)")
    if "\t" in raw:
        for i, line in enumerate(raw.splitlines(), 1):
            if "\t" in line:
                problems.append(f"{rel}:{i}: tab character")

    lines, unclosed_fence = strip_code(raw)
    if unclosed_fence:
        problems.append(f"{rel}: unclosed code fence")

    prose = "\n".join(lines)

    if prose.count("(") != prose.count(")"):
        problems.append(
            f"{rel}: unbalanced parentheses ({prose.count('(')} vs {prose.count(')')})"
        )
    if prose.count("[") != prose.count("]"):
        problems.append(
            f"{rel}: unbalanced brackets ({prose.count('[')} vs {prose.count(']')})"
        )
    if prose.count("**") % 2:
        problems.append(f"{rel}: unbalanced bold markers ({prose.count('**')})")

    headings: collections.Counter[str] = collections.Counter()
    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        if line != line.rstrip():
            problems.append(f"{rel}:{i}: trailing whitespace")

        if is_markdown and re.match(r"^#{1,6}\s", stripped):
            key = re.sub(r"\s+", " ", stripped.lower())
            headings[key] += 1
            if headings[key] > 1:
                problems.append(f"{rel}:{i}: duplicate heading '{stripped[:60]}'")

        if not stripped or stripped.startswith(("|", ">", "#")):
            continue

        prose_line = strip_inline_code(line)

        for match in re.finditer(r"\b([A-Za-z][\w'-]*)\s+\1\b", prose_line, re.I):
            word = match.group(1).lower()
            if word not in DOUBLED_OK:
                problems.append(f"{rel}:{i}: doubled word '{match.group(0)}'")

        for match in re.finditer(r"\ba\s+([A-Za-z][\w-]*)", prose_line):
            word = match.group(1)
            if (
                word[0].islower()
                and word[0] in "aeio"
                and not word.startswith(CONSONANT_SOUND)
            ):
                problems.append(
                    f"{rel}:{i}: 'a {word}' should be 'an {word}' (vowel sound)"
                )

        for match in re.finditer(r"\bshall\b", prose_line):
            if is_quoted(prose_line, match.start(), match.end()):
                continue
            problems.append(
                f"{rel}:{i}: uses 'shall'; the house style is 'must' ({match.group(0)})"
            )

        for match in re.finditer(r"\b(&nbsp;)\b", prose_line):
            problems.append(f"{rel}:{i}: avoid non-breaking space entities")

    # Spelling consistency: one variant everywhere. Quoted mentions are exempt, because
    # documentation may legitimately name a spelling while explaining that it is wrong.
    for line_no, raw_line in enumerate(lines, 1):
        clean = strip_inline_code(raw_line)
        for word in BRITISH:
            for match in re.finditer(rf"\b{word}s?\b", clean, re.I):
                if is_quoted(clean, match.start(), match.end()):
                    continue
                problems.append(
                    f"{rel}:{line_no}: British spelling '{match.group(0)}'; use the American form"
                )

    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check prose consistency and Markdown hygiene.")
    parser.add_argument(
        "--path", nargs="+", type=pathlib.Path, default=[pathlib.Path(".")],
        help="files or directories to check (default: the whole repository)",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    files: list[pathlib.Path] = []
    for entry in args.path:
        if not entry.exists():
            print(f"error: {entry} does not exist", file=sys.stderr)
            return 2
        if entry.is_file():
            files.append(entry)
        else:
            for path in entry.rglob("*"):
                if (
                    path.is_file()
                    and path.suffix in PROSE_SUFFIXES
                    and not any(part in SKIP_DIRS for part in path.parts)
                    and path.name not in SKIP_NAMES
                ):
                    files.append(path)

    problems: list[str] = []
    for path in sorted(files):
        rel = str(path) if args.path == [pathlib.Path(".")] else str(path)
        problems.extend(check_file(path, rel))

    for problem in problems:
        print(f"FAIL {problem}")

    print()
    print(f"checked {len(files)} file(s), {len(problems)} problem(s)")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
