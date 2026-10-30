## What this changes

<!-- One paragraph. What, and why. -->

## Type of change

- [ ] Editorial (typo, link, formatting)
- [ ] Clarifying (no change in rights)
- [ ] Minor amendment (adds a permission or improves a process) — RFC required
- [ ] Major amendment (removes or restricts a permission) — RFC + 45-day comment required
- [ ] Tooling / CI
- [ ] Translation
- [ ] Template
- [ ] Registry data

## The rights test

> **Does this change alter what a reader, deployer, contributor, or author may or must do?**

- [ ] No — normal review
- [ ] Yes, it adds permission — RFC linked below
- [ ] Yes, it removes permission — RFC linked below

RFC: <!-- link, or "n/a" -->

## Documents affected

<!-- List every file, including cross-references that must stay consistent. -->

## Checklist

- [ ] Commits are signed off (`git commit -s`) under the Developer Certificate of Origin 1.1.
- [ ] I have the right to contribute this content, and my employer does not own it.
- [ ] No content under an incompatible licence has been included.
- [ ] Cross-references, numbering, and definitions are consistent.
- [ ] `python3 -m pytest scripts/tests -q` passes.
- [ ] `python3 scripts/validate_registry.py` passes (if the registry changed).
- [ ] `python3 scripts/check_license_headers.py --path scripts` passes (if scripts changed).
- [ ] `CHANGELOG.md` has been updated for a substantive change.
- [ ] The change does not describe the licence as open source.

## For legal text changes

- [ ] I have identified every clause affected, including cross-references.
- [ ] Any new term is defined in Article 1 (or the document's definitions section).
- [ ] The change does not accidentally introduce normative language ("may" vs "must").
- [ ] The change does not withdraw any right already granted (PASVL §19.5, §26.3).

## Notes for reviewers

<!-- Anything you are unsure about. It is fine to be unsure. -->
