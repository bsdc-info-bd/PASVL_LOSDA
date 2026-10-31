# Contributing

Thank you for helping build the framework. This repository contains legal texts, governance
documents, templates, schemas, and tooling. Contributions are welcome to all of them — including
contributions that disagree with us.

---

## 1. Before you contribute

### 1.1 Understand what you are licensing

By contributing, you agree to the inbound license in **PASVL Article 12**: you keep copyright,
and you grant the Author and BSD C a perpetual, worldwide, royalty-free, irrevocable license to
use, modify, distribute, sublicense, and relicense your contribution.

This is necessary so the framework can be published, translated, and enforced.

### 1.2 Sign your commits

```bash
git commit -s -m "legal: clarify reliance period in §19.2"
```

This adds:

```
Signed-off-by: Your Name <you@example.com>
```

You are certifying the [Developer Certificate of Origin 1.1](https://developercertificate.org/).

### 1.3 Check your employer's rights

If you contribute in the course of employment, your employer may own the work. Obtain permission
or have your employer sign [`templates/CONTRIBUTOR-AUTHORIZATION.md`](templates/CONTRIBUTOR-AUTHORIZATION.md).

---

## 2. What kind of change are you making?

| You want to… | Do this |
|---|---|
| Fix a typo, link, or formatting | Open a pull request directly |
| Clarify an ambiguous sentence without changing rights | Pull request + note in the description |
| Propose a substantive change to the License | Open an RFC in [`rfcs/`](rfcs/) |
| Add a translation | See [`translations/`](translations/) |
| Add an example or template | Pull request + update `templates/README.md` |
| Report a security issue | **Do not open a PR** — see [`SECURITY.md`](SECURITY.md) |
| Report a conduct issue | See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |
| Report a license violation elsewhere | Use [`templates/VIOLATION-REPORT.md`](templates/VIOLATION-REPORT.md) |

---

## 3. Contributing to the legal texts

Legal text is different from code. A misplaced comma can change a right. Please:

1. **Keep the change minimal.** One issue per pull request.
2. **State the intent.** Does the change (a) fix an error, (b) clarify without changing meaning,
   or (c) change rights? If (c), it needs an RFC.
3. **Show the effect.** Identify every clause affected, including cross-references.
4. **Check the definitions.** Article 1 controls; a new term must be defined.
5. **Check the whole document** for consistent numbering and references.
6. **Do not introduce normative language accidentally.** "May" is permission; "must" is
   obligation.

### 3.1 The rights test

Before proposing any change, answer this question in the pull request:

> **Does this change alter what a reader, deployer, contributor, or author may or must do?**

- **No** → normal review.
- **Yes, it adds permission** → minor amendment, RFC required.
- **Yes, it removes permission** → major amendment, 45-day comment period and two-thirds vote.

If you are unsure, treat it as a change of rights.

### 3.2 Style

- British spelling in legal text ("license" as a noun, "license" as a verb); American spelling
  in code.
- One sentence per idea.
- Define before you use.
- Avoid "and/or".
- Prefer "must" over "shall", except in quoted legal forms.
- Use inclusive language.
- Mark normative statements clearly.

---

## 4. Contributing to the tooling

### 4.1 Requirements

| Item | Requirement |
|---|---|
| Python | 3.9+ for `scripts/` |
| Dependencies | Standard library only, unless justified |
| Style | PEP 8, type hints on public functions |
| Tests | A test for any new validation rule |
| CI | Must pass `python -m pytest` and the validators |

### 4.2 Running the checks

```bash
python3 scripts/validate_registry.py
python3 scripts/check_license_headers.py --path .
python3 -m pytest scripts/tests -q
```

### 4.3 Adding a schema field

1. Add the field to `schemas/losda-v1.schema.json` as **optional** unless a major version change
   is approved.
2. Update `templates/LOSDA-TEMPLATE.md`.
3. Update `legal/losda-specification.md` §7 and Appendix A of the license if it becomes required.
4. Add an example to `examples/`.
5. Bump the patch or minor version and update `CHANGELOG.md`.

---

## 5. Contributing documentation

- Put yourself in the reader's shoes. Most readers are not lawyers.
- Every claim about the license must cite the article or section.
- Do not promise outcomes ("this will protect your code") — describe mechanisms.
- Do not describe the license as open source.
- Keep the FAQ answerable: if a question is common, it belongs there.

---

## 6. Translations

1. Work in `translations/<language-code>/`.
2. Never edit the English text to make a translation easier.
3. Mark the translation "For convenience only — the English text prevails."
4. A second native speaker must review before merge.
5. Record the translation's status in `translations/README.md`.

---

## 7. Review process

| Step | Who | Time |
|---|---|---|
| Acknowledgment | Maintainer | 5 business days |
| Review | Maintainer + 1 reviewer | 10 business days |
| Legal review (if rights change) | License Council | 30 days |
| Merge | Maintainer | After approval |
| Changelog | Maintainer | At merge |

A pull request that changes rights without an RFC will be closed with a link to
[`governance/AMENDMENT-PROCESS.md`](governance/AMENDMENT-PROCESS.md). This is not hostility; it
is the rule that protects everyone's rights from casual edits.

---

## 8. What we will not accept

- Changes that make the license describe itself as open source.
- Changes that remove the visibility grant.
- Changes that make revocation easier without cause.
- Changes that reduce appeal rights.
- Content under an incompatible license.
- Plagiarized text.
- Harassment, personal attacks, or legal threats in a discussion.
- Changes proposed in bad faith to make the framework look absurd.

---

## 9. Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). We want disagreement;
we do not want contempt.

---

## 10. Recognition

Contributors are listed in `CONTRIBUTORS.md`. Substantive contributions to the legal text are
noted in `CHANGELOG.md`.

---

## 11. Questions

If you are unsure whether a change needs an RFC, open a discussion and ask. Asking is cheap.
Breaking a license is not.
