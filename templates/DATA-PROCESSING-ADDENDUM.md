# Data Processing Addendum (DPA)

**Attached to LOSDA:** `LOSDA-[ISSUER]-[YYYY]-[NNNNNN]`
**Version:** 1.0
**Applies where:** the Licensee processes personal data in the course of a Deployment, and a
data-protection law requiring a written processor agreement applies (for example, GDPR Article
28, UK GDPR, or a comparable regime).

This Addendum is a starting point. It must be reviewed by the parties' counsel for the facts of
the deployment.

---

## 1. Roles

| Party | Role |
|---|---|
| Issuer | Not a processor. The Issuer supplies software, not a data-processing service. |
| Licensee | Controller (or processor for its own customers) |

Where the Issuer also operates a hosted service on the Licensee's behalf, the Issuer acts as a
processor and this Addendum applies to that service.

## 2. Scope

| Item | Detail |
|---|---|
| Subject matter | [Describe] |
| Duration | The term of the LOSDA |
| Nature and purpose | [Describe] |
| Categories of data subjects | [Employees / customers / users / others] |
| Categories of personal data | [Identify; avoid special-category data] |
| Special-category data | ☐ None ☐ Present — additional safeguards: __________ |
| Retention | [Period] |

## 3. Processor obligations (where applicable)

The processor must:

1. process only on documented instructions, including for transfers;
2. ensure authorised personnel are bound by confidentiality;
3. implement appropriate technical and organisational security measures (Annex II);
4. assist the controller with data-subject requests;
5. assist with security, breach notification, and impact assessments;
6. delete or return data at the end of the term, subject to legal retention;
7. make available information necessary to demonstrate compliance, and allow audits;
8. notify the controller without undue delay, and within 72 hours where required, of a breach;
9. not engage a sub-processor without prior written authorisation;
10. impose the same obligations on any authorised sub-processor.

## 4. Sub-processors

| Name | Service | Location | Safeguard |
|---|---|---|---|
| | | | |

A 30-day objection right applies to new sub-processors. If the parties cannot resolve an
objection, the controller may terminate the affected service.

## 5. International transfers

Where data leaves the EEA, UK, or another restricted jurisdiction, the parties rely on:

☐ Standard Contractual Clauses (specify module and version)
☐ UK International Data Transfer Addendum
☐ Adequacy decision
☐ Another lawful mechanism: __________

A transfer risk assessment is attached at Annex III where required.

## 6. Security measures (Annex II)

| Domain | Measure |
|---|---|
| Access control | Least privilege; MFA; named accounts |
| Encryption | In transit (TLS 1.2+); at rest (AES-256 or equivalent) |
| Logging | Immutable audit logs; retention period |
| Vulnerability management | Patch SLA: critical __ days; high __ days |
| Backup | Frequency; restore testing |
| Segregation | Tenant isolation approach |
| Physical | Hosting provider certifications |
| Personnel | Background checks where lawful; training |

## 7. Breach management

| Step | Owner | Deadline |
|---|---|---|
| Detection | Processor | Immediate |
| Notification to controller | Processor | Without undue delay, max 72h |
| Notification to authority | Controller | Where required by law |
| Notification to data subjects | Controller | Where required by law |
| Post-incident review | Both | Within 30 days |

## 8. Audit

The controller may audit once per year on 30 days' notice, or more often after a breach, using a
recognised certification or an independent auditor where available.

## 9. Liability

Liability under this Addendum follows the liability provisions of the LOSDA and of PASVL Article
21. Data-protection fines imposed on one party by reason of the other party's breach are
recoverable from the breaching party to the extent permitted by law.

## 10. Termination

On termination, the processor must delete or return personal data within 30 days, except where
retention is required by law, and must certify deletion on request.

---

## Signatures

**Issuer** Signature: ____________________ Date: __________
**Licensee** Signature: ____________________ Date: __________

Annexes: ☐ I — Description of processing ☐ II — Security measures ☐ III — Transfer assessment

---

*Template version: DPA-1.0.*
