# Changelog

All notable changes to the PASVL/LOSDA framework are recorded here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: see
[`docs/versioning.md`](docs/versioning.md).

---

## [Unreleased]

### Fixed

- Corrected `a applicable` to `an applicable restricted-party list` in PASVL §22.2.
- Replaced the three remaining uses of "shall" in Articles 24.4 and 25.1 with "must", matching
  the framework's house style.
- Replaced "etc." in Appendix A with an explicit statement of the permitted deployment types.
- Renamed the duplicated headings in `examples/losda-academic.md` so that every deep link has a
  unique anchor.

### Changed

- **Spelling is now consistent.** The documents mixed British and American forms: 482 uses of
  "licence" against 318 of "license", including 33 inside the License itself, alongside
  "authorised", "organisation", "behaviour", "defence" and about forty other variants. All 723
  occurrences were converted to the American forms, matching the instrument's official name,
  the *PASVL **License***. The word "licence" no longer appears anywhere in the repository.
- Rewrote the CI workflow. The `Prose and Markdown lint` job now runs `scripts/check_docs.py`
  and `scripts/check_links.py` as hard gates. Spellcheck runs `codespell` from pip with the
  repository's `.codespellrc`, so the same command works locally. External link probing moved to
  an advisory job, because third-party hosts rate-limit and go down.
- Removed the third-party `markdown-link-check` action and its configuration in favor of
  `scripts/check_links.py`, which validates internal links and heading anchors deterministically
  and offline.
- Bumped the workflow actions to `actions/checkout@v5` and `actions/setup-python@v6` to clear the
  Node 20 deprecation warnings.

### Added

- `scripts/tests/test_docs_lint.py` — 18 tests covering the two new linters, and 8 covering the
  reference checker.

- `scripts/check_docs.py` — prose lint covering spelling consistency, doubled words, wrong
  articles, unbalanced delimiters, duplicate headings, trailing whitespace, and "shall".
- `scripts/check_links.py` — link and anchor validation, with optional external probing.
- `scripts/check_refs.py` — resolves every section citation against the instrument it names.
  193 citations are checked against the 257 sections of the License and the 63 sections of the
  LOSDA specification. Citations of foreign statutes, such as `BGB §§305 ff.` or `§1201(f)`,
  are recognized and skipped.
- `.codespellrc` — shared spelling configuration with every exemption justified in a comment.

---

## [1.0.0] — 2026-01-01

**Status:** Published and in force.

### Added — the license

- `LICENSE` — Public Availability with Source-Code Visibility License, Version 1.0 (PASVL-1.0),
  comprising a Preamble, 28 Articles, and 4 Appendices.
- Article 1: 41 defined terms.
- Article 3: the Visibility Grant (read, study, audit, clone, fork, archive, learn, teach, cite,
  comment, contribute, build to verify, personal study copy).
- Article 5: reservation of the right to deploy.
- Article 6: Evaluation Use envelope with Mode S and Mode U.
- Article 7: non-commercial research, teaching, and study exception.
- Article 8: security research safe harbor and coordinated disclosure.
- Article 9: public-interest and humanitarian uses, including Continuity LOSDAs.
- Article 10: the LOSDA and its thirteen classes.
- Article 11: obligations of a deployment licensee.
- Article 12: inbound contribution license and DCO.
- Article 13: fourteen prohibited categories, including licensing laundering, fork abuse, Service
  Bureau Use, model laundering, and sanctions evasion.
- Article 14: machine-learning and automated-processing rules.
- Article 16: copyright, patent, moral-rights, and database-rights provisions.
- Article 18: termination, cure, revocation grounds, suspension, and reinstatement.
- Article 19: reliance protection, 180-day wind-down, and release-based certainty.
- Article 20: monitoring, audit, and the six-stage enforcement ladder.
- Article 21: warranty disclaimer, liability cap, and indemnity structure.
- Article 22: sanctions and export control.
- Article 23: privacy and data protection.
- Article 24: Bangladesh governing law, UNCITRAL arbitration, and consumer carve-outs.
- Article 26: versioning, amendment, and compatibility.
- Article 27: the Steward and the License Council.
- Article 28: interpretation, and express statement that the license is not open source.

### Added — the instrument

- `legal/losda-specification.md` — LOSDA-1.0: definition, authority to issue, thirteen classes,
  18 required elements, identifier format, nine-step issuance procedure with service targets,
  16 condition codes, scope construction rules, verification, amendment, renewal, transfer,
  refusal grounds, suspension, revocation, registry obligations, signatures, and records
  retention.

### Added — legal materials

- `legal/plain-language.md` — the framework in human words, with an honest-limits section.
- `legal/hierarchy-and-interpretation.md` — precedence ladder and ten interpretation rules.
- `legal/platform-reality.md` — what the license can and cannot do on GitHub, including the
  license-detection problem.
- `legal/enforcement-policy.md` — seven principles, six stages, severity matrix, sanctions.
- `legal/compatibility.md` — inbound and outbound compatibility with nine license families.
- `legal/jurisdiction-matrix.md` — 17 jurisdictions with confidence levels.
- `legal/privacy-policy.md` — data minimization, anonymized listing, retention.
- `legal/ethics-policy.md` — prohibited uses and high-risk review.
- `legal/sanctions-and-export.md` — screening and self-certification.
- `legal/anti-corruption.md` — gifts, conflicts, procurement, whistleblowing.
- `legal/risk-register.md` — 25 risks with likelihood, impact, and mitigation.
- `legal/non-software-works.md` — docs, models, data, hardware.

### Added — governance

- `governance/CHARTER.md` — powers, duties, limits, and structure of the Steward.
- `governance/LICENSE-COUNCIL.md` — seven seats, officers, voting.
- `governance/REGISTRY-POLICY.md` — data model, immutability, hashes, corrections.
- `governance/AMENDMENT-PROCESS.md` — five classes of change, RFC flow, retroactivity bar.
- `governance/APPEALS.md` — grounds, procedure, panel independence, timeline.
- `governance/CONFLICT-OF-INTEREST.md` — declarations, recusal, consequences.
- `governance/REGISTRY-CUSTODIAN.md` — duties, access control, service targets.
- `governance/ETHICS-REVIEW-BOARD.md` — composition and substantive tests.
- `governance/ELECTIONS.md` — eligibility, campaigning rules, recall.
- `governance/DISSOLUTION-AND-SUCCESSION.md` — what survives, escrow, trustee fallback.
- `governance/TRANSPARENCY-REPORT-TEMPLATE.md` — the annual report, including regrets.

### Added — documentation

- `docs/quickstart.md`, `docs/for-authors.md`, `docs/for-deployers.md`,
  `docs/for-contributors.md`, `docs/for-enterprise.md`, `docs/for-government.md`,
  `docs/for-education.md`, `docs/for-open-source-projects.md`.
- `docs/deployment-scopes.md` — 40 worked examples and a decision tree.
- `docs/losda-guide.md`, `docs/checklist-deployer-compliance.md`.
- `docs/faq.md` — 62 questions, including uncomfortable ones.
- `docs/glossary.md`, `docs/why-this-exists.md`, `docs/anti-patterns.md`,
  `docs/migration-guide.md`, `docs/roadmap.md`, `docs/badge-usage.md`,
  `docs/versioning.md`, `docs/citation.md`.

### Added — templates

- LOSDA letter, request, amendment, denial, revocation notice, Notice of Non-Compliance, appeal
  form, violation report, security report, takedown request, DPA, contributor authorization,
  adoption checklist, NOTICE template, and license header set.

### Added — machine-readable

- `schemas/losda-v1.schema.json` — validation for LOSDA records.
- `schemas/registry-v1.schema.json` — validation for the registry.
- `registry/losda-registry.json`, `registry/issuers.json`, `registry/works.json`,
  `registry/enforcement-register.json`.
- `examples/` — three complete LOSDA examples and a JSON record.
- `scripts/` — validators, a record hash tool, and a license-header checker.

### Added — community

- `README.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `TRADEMARK.md`, `NOTICE`, `CITATION.cff`.
- `rfcs/` — the amendment proposal process.
- `translations/bn/` — Bengali summaries.
- `.github/` — issue templates, pull request template, CI.

### Known limitations

- Not OSI-approved and will not be submitted.
- Enforceability of the deployment restriction varies by jurisdiction.
- Several contact addresses in `GOVERNANCE.md` are placeholders that adopters must replace.
- The Bengali translation covers summaries, not the full license text.
- No hosted verification service yet; verification is by inspecting the registry file.
- Legal review has not yet been completed for all 17 jurisdictions in the matrix.

---

## How to read this changelog

| Symbol | Meaning |
|---|---|
| **Added** | New documents, clauses, or features |
| **Changed** | Substantive modifications to existing text |
| **Deprecated** | Still valid, but a successor is planned |
| **Removed** | Withdrawn; never affects rights already granted |
| **Fixed** | Corrections that do not change meaning |
| **Security** | Changes made in response to a vulnerability |

---

## Version history

| Version | Date | Class | Notes |
|---|---|---|---|
| 1.0.0 | 2026-01-01 | Initial | First publication of the framework |
