"""Tests for the prose and link linters.

Run with:
    python3 scripts/tests/test_docs_lint.py
or:
    python3 -m pytest scripts/tests -q

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from check_docs import check_file  # noqa: E402
from check_links import slugify, strip_code  # noqa: E402


class TestProseLint(unittest.TestCase):
    def lint(self, content: str, suffix: str = ".md") -> list[str]:
        with tempfile.NamedTemporaryFile(
            "w", suffix=suffix, delete=False, encoding="utf-8"
        ) as handle:
            handle.write(content)
            path = pathlib.Path(handle.name)
        try:
            return check_file(path, path.name)
        finally:
            path.unlink()

    def test_clean_prose_passes(self) -> None:
        self.assertEqual(
            self.lint("# Title\n\nThe author grants a license to deploy the work.\n"), []
        )

    def test_british_spelling_flagged(self) -> None:
        problems = self.lint("The licence is granted under this agreement.\n")
        self.assertTrue(any("British spelling 'licence'" in p for p in problems))

    def test_quoted_spelling_is_a_mention_not_an_error(self) -> None:
        self.assertEqual(self.lint('The word "licence" is not used here.\n'), [])

    def test_inline_code_is_exempt(self) -> None:
        self.assertEqual(self.lint("Run `licence-check` before committing.\n"), [])

    def test_doubled_word_flagged(self) -> None:
        problems = self.lint("The the author must sign.\n")
        self.assertTrue(any("doubled word 'The the'" in p for p in problems))

    def test_wrong_article_flagged(self) -> None:
        problems = self.lint("This is a applicable term.\n")
        self.assertTrue(any("should be 'an applicable'" in p for p in problems))

    def test_correct_article_not_flagged(self) -> None:
        self.assertEqual(self.lint("This is an applicable term.\n"), [])

    def test_shall_flagged(self) -> None:
        problems = self.lint("The parties shall comply.\n")
        self.assertTrue(any("shall" in p for p in problems))

    def test_quoted_shall_not_flagged(self) -> None:
        self.assertEqual(self.lint('The house style prefers "must" to "shall".\n'), [])

    def test_unbalanced_parentheses_flagged(self) -> None:
        problems = self.lint("A term (with a parenthesis.\n")
        self.assertTrue(any("unbalanced parentheses" in p for p in problems))

    def test_duplicate_heading_flagged(self) -> None:
        problems = self.lint("## Scope\n\ntext\n\n## Scope\n\nmore text\n")
        self.assertTrue(any("duplicate heading" in p for p in problems))

    def test_trailing_whitespace_flagged(self) -> None:
        problems = self.lint("A line with trailing space. \n")
        self.assertTrue(any("trailing whitespace" in p for p in problems))

    def test_code_fence_contents_ignored(self) -> None:
        content = "```\nlicence authorise the the\n```\n"
        self.assertEqual(self.lint(content), [])

    def test_unclosed_code_fence_flagged(self) -> None:
        problems = self.lint("```\nunclosed\n")
        self.assertTrue(any("unclosed code fence" in p for p in problems))


class TestLinkHelpers(unittest.TestCase):
    def test_slugify_matches_github_style(self) -> None:
        self.assertEqual(slugify("Article 3 — The Visibility Grant"), "article-3--the-visibility-grant")
        self.assertEqual(slugify("§5.2 No implied license"), "52-no-implied-license")
        self.assertEqual(slugify("`LICENSE` file"), "license-file")

    def test_slugify_strips_bold_and_links(self) -> None:
        self.assertEqual(slugify("**Bold** and [link](x.md)"), "bold-and-link")

    def test_strip_code_removes_fenced_blocks(self) -> None:
        body = strip_code("keep\n```\nremove\n```\nkeep\n")
        self.assertIn("keep", body)
        self.assertNotIn("remove", body)

    def test_strip_code_blanks_fenced_content(self) -> None:
        body = strip_code("before\n```\nsecret\n```\nafter")
        self.assertIn("before", body)
        self.assertIn("after", body)
        self.assertNotIn("secret", body)


if __name__ == "__main__":
    unittest.main(verbosity=2)
