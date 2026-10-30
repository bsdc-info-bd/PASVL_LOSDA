# Templates

Fill-in-the-blank documents for every step of the framework. Every template is published so
that no one has to invent the paperwork, and so that a small author can look as professional as
a large one.

## Which template do I need?

| I want to… | Use |
|---|---|
| Ask for permission to deploy | [`LOSDA-REQUEST.md`](LOSDA-REQUEST.md) |
| Receive a permission | [`LOSDA-TEMPLATE.md`](LOSDA-TEMPLATE.md) |
| Change a permission | [`LOSDA-AMENDMENT.md`](LOSDA-AMENDMENT.md) |
| Refuse a permission, with reasons | [`LOSDA-DENIAL.md`](LOSDA-DENIAL.md) |
| Take a permission away | [`REVOCATION-NOTICE.md`](REVOCATION-NOTICE.md) |
| Tell someone they are in breach | [`NOTICE-OF-NON-COMPLIANCE.md`](NOTICE-OF-NON-COMPLIANCE.md) |
| Challenge a decision | [`APPEAL-FORM.md`](APPEAL-FORM.md) |
| Report someone else's breach | [`VIOLATION-REPORT.md`](VIOLATION-REPORT.md) |
| Report a vulnerability | [`SECURITY-REPORT.md`](SECURITY-REPORT.md) |
| Prepare a platform complaint | [`TAKEDOWN-REQUEST.md`](TAKEDOWN-REQUEST.md) |
| Adopt PASVL for my project | [`ADOPTION-CHECKLIST.md`](ADOPTION-CHECKLIST.md) + [`NOTICE-TEMPLATE`](NOTICE-TEMPLATE) |
| Put a header in my source files | [`LICENSE-HEADER.txt`](LICENSE-HEADER.txt) |
| Regulate personal data in a deployment | [`DATA-PROCESSING-ADDENDUM.md`](DATA-PROCESSING-ADDENDUM.md) |
| Record consent to contribute | [`CONTRIBUTOR-AUTHORIZATION.md`](CONTRIBUTOR-AUTHORIZATION.md) |

## Rules for using these templates

1. **Do not delete the required fields.** A LOSDA without its required fields is void.
2. **Do not use a template to hide a term.** Anything surprising must be stated plainly.
3. **Keep the identifiers.** References let the Registry and the parties trace a document.
4. **Adapt the language, not the substance.** You may add fields; you may not remove the ones
   the specification requires.
5. **Publish what you issue.** A LOSDA is valid only when recorded in the Registry.

## Versioning

Templates carry their own version number, independent of the Licence. A template update does not
invalidate an instrument issued under an earlier template, provided the earlier instrument
contained the required elements.

| Template | Version |
|---|---|
| LOSDA letter | LOSDA-TEMPLATE-1.0 |
| LOSDA request | LOSDA-REQUEST-1.0 |
| Amendment | AMD-1.0 |
| Denial | DEN-1.0 |
| Revocation | REV-1.0 |
| NNC | NNC-1.0 |
| Appeal | APL-1.0 |
| Violation report | VR-1.0 |
| Security report | SEC-1.0 |
| Takedown | TD-1.0 |
| DPA | DPA-1.0 |
| Contributor authorisation | CA-1.0 |

## Machine-readable forms

Where a template is used in the Registry, the values must also be captured as JSON conforming to
[`schemas/losda-v1.schema.json`](../schemas/losda-v1.schema.json). The human-readable letter and
the JSON record must agree.
