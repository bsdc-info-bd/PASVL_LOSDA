# LETTER OF SOFTWARE DEPLOYMENT APPROVAL (LOSDA)

## Specification and Operating Rules — Version 1.0

| Field | Value |
|---|---|
| Instrument | Letter of Software Deployment Approval (LOSDA) |
| Version | LOSDA-1.0 |
| Operates within | PASVL-1.0 (Public Availability with Source-Code Visibility License) |
| Issued by | The Author, or the Steward where authorized under PASVL §10.2 |
| Steward | Bangladesh Software Development Community (BSD C) |
| Formal template | [`templates/LOSDA-TEMPLATE.md`](../templates/LOSDA-TEMPLATE.md) |
| Machine-readable schema | [`schemas/losda-v1.schema.json`](../schemas/losda-v1.schema.json) |
| Public register | [`registry/losda-registry.json`](../registry/losda-registry.json) |
| Status | In force from 2026-01-01 |

---

## 1. Purpose of this document

This document is the operating manual for the LOSDA. It answers, for every party who touches
the instrument: what a LOSDA is, who may issue one, what it must contain, how it is granted,
how it is verified, how it can be changed, and how it ends.

It is normative for Issuers and Registry Custodians. It is explanatory for applicants and
deployers. Where this document conflicts with [the License](../LICENSE), the License
prevails.

---

## 2. What a LOSDA is

A LOSDA is a **written, identified, individually granted, scope-limited permission instrument**
by which the Author authorizes a named person or entity to deploy a specific Work within a
specific scope, for a specific term, under stated conditions.

A LOSDA is:

- **an instrument, not a contract of sale** — it grants permission, never ownership;
- **individually granted** — it is issued to a named licensee, not to the world;
- **scoped** — it authorizes only what it states, no more (PASVL §10.5);
- **recorded** — it has no effect until it exists in the Registry;
- **verifiable** — any third party can confirm its current status without contacting the
  licensee;
- **revocable only for cause** — with notice, a hearing, and a wind-down period (PASVL
  Article 18, Article 19);
- **publicly reportable** — the licensee may say it holds a LOSDA, and the Registry will say
  so too.

## 3. What a LOSDA is not

A LOSDA is **not**:

| It is not | Because |
|---|---|
| A purchase receipt | A fee may be zero; the instrument still governs |
| A copyright assignment | Copyright never transfers (PASVL §16.1) |
| A sublicence | Sublicensing requires express permission (PASVL §10.8) |
| An open-source grant | PASVL is source-available, not open source (PASVL §28.5) |
| A warranty or SLA | Support is only what the LOSDA states (PASVL §21.1) |
| A trademark license | Brand use is governed separately (PASVL Article 17) |
| A permanent entitlement | It runs for its term, and it can be revoked for cause |
| A waiver of compliance duties | The licensee remains bound by the whole License |

## 4. Legal architecture

The framework separates **what everyone may do** from **who may deploy**.

```
                    ┌──────────────────────────────────────────┐
                    │  PASVL-1.0  —  the public license        │
                    │  Grants: read, study, audit, fork, cite, │
                    │  teach, contribute.                      │
                    │  Reserves: the right to deploy.          │
                    └───────────────────┬──────────────────────┘
                                        │ deployment reserved
                                        ▼
                    ┌──────────────────────────────────────────┐
                    │  LOSDA  —  the deployment permission     │
                    │  Grants: named licensee may deploy a     │
                    │  named Work, in a named scope, for a     │
                    │  named term, under named conditions.     │
                    └───────────────────┬──────────────────────┘
                                        │ recorded in
                                        ▼
                    ┌──────────────────────────────────────────┐
                    │  Registry  —  the public source of truth │
                    │  Status, scope, term, revocation.        │
                    └──────────────────────────────────────────┘
```

Two instruments, one system. The License is public and identical for everyone. The LOSDA is
individual and specific. Neither is valid without the other: a LOSDA is void if it purports to
grant rights the Author does not hold, and deployment is unlicensed if the LOSDA is missing,
expired, suspended, or revoked.

## 5. Authority to issue

| Issuer | May issue | Conditions |
|---|---|---|
| The Author | Any class, for its own Work | Full authority |
| A co-Author | Any class, for the joint Work | Must act jointly unless the NOTICE names an issuing agent |
| An authorized agent named in the NOTICE | Classes named in the NOTICE | Within the stated delegation only |
| The Steward as Continuity Issuer | Class C only | After 60 days of Author unresponsiveness (PASVL §9.2) |
| The Steward as Extension Issuer | Class X only | Only where the Author has not objected in writing (PASVL §6.5) |
| Anyone else | Nothing | Purported issuance is fraudulent under PASVL §13.8 |

**5.1 Register of Issuers.** The Steward maintains a public list of registered issuer codes in
`registry/issuers.json`. An issuer code that is not in that list cannot appear in a valid
LOSDA ID.

**5.2 Delegation.** A delegation of issuing authority must be in writing, must be recorded in
the NOTICE or in `registry/issuers.json`, and may be withdrawn at any time. Withdrawal does
not invalidate LOSDAs validly issued before withdrawal, unless the LOSDA itself says so.

## 6. LOSDA classes

The class determines the default term library, the default conditions, the fee policy, and the
review depth. Classes may be combined only where the Request states the combination and the
Issuer records it.

### 6.1 Class S — Standard Commercial

For a single organization deploying a Work in its own commercial operations or products,
within stated scale limits. Default term: one year, renewable. Default conditions: C1–C9.
Review depth: standard. Fee: set by the Author.

### 6.2 Class E — Enterprise / Portfolio

For a group of Affiliates or a portfolio of Works under common ownership. Default term: up to
three years. Requires an entity list, a named responsible officer, and a compliance contact.
Review depth: enhanced. Fee: negotiated.

### 6.3 Class I — Internal Use

For deployment inside one organization, not exposed to persons outside it. Default term: one
year. Scale limits expressed in seats. Review depth: standard. Fee: set by the Author,
frequently reduced.

### 6.4 Class H — Hosted Service / SaaS

For providing the Work's functionality to third parties over a network. Requires capacity
disclosure, sub-processor disclosure, security commitments, and an incident-notification
undertaking. Default term: one year. Review depth: enhanced. Fee: negotiated, often
usage-based.

### 6.5 Class D — Distribution / OEM / Embedded

For distributing the Work in executable form, including in devices, appliances, firmware, or
bundled products. Requires a device list or product line, a volume cap, a notice-preservation
plan, and an update/security-patch undertaking. Default term: per product cycle or perpetual
with royalties. Review depth: enhanced.

### 6.6 Class A — Academic / Non-Commercial

For accredited educational and research institutions, for teaching and non-commercial research
infrastructure. Fee: none. Requires institutional identity and a statement of non-commercial
use. Default term: two years. Review depth: light.

### 6.7 Class G — Government / Public Sector

For public bodies deploying a Work in public service delivery. Fee: none by default.
Requires an authorizing officer and a statement of public purpose. Default term: two years.
Review depth: standard, with procurement compatibility review.

### 6.8 Class P — Public Interest

For disaster response, public health, accessibility, civil liberties, and digital public
infrastructure. Fee: none. Issued on an expedited basis, target three (3) business days.
Default term: one year. Review depth: light.

### 6.9 Class R — Research

For research deployments that exceed the Article 7 exception, including research testbeds
serving participants. Fee: none. Requires an ethics statement and a data-handling plan.
Default term: project duration. Review depth: light.

### 6.10 Class X — Evaluation Extension

Extends or widens Evaluation Use under PASVL §6.5. Maximum ninety (90) days. Fee: none or
nominal. Review depth: light. Not renewable more than twice consecutively without conversion
to another class.

### 6.11 Class C — Continuity

Issued by the Steward where an essential-service deployer loses access to its Author. Maximum
twelve (12) months, renewable while the Author remains unavailable. Requires evidence of the
essential service and of unresponsiveness. Review depth: enhanced, with legal sign-off.

### 6.12 Class M — Machine Learning / AI Data

For Machine Learning Use under PASVL Article 14. Must state: the permitted use (training,
fine-tuning, evaluation, embedding), the model families, whether outputs may be released, and
whether the resulting model may be monetized. Requires provenance records, model-card
attribution, and an output-laundering prohibition. Review depth: enhanced. Fee: negotiated.

### 6.13 Class O — Open Deployment

For Authors who choose to permit public deployment of their Work under this framework. A Class
O LOSDA may be issued as a **standing public grant** recorded once in the Registry and
available to anyone who accepts the stated conditions. It is the framework's way of letting an
Author open a Work up without abandoning the framework.

## 7. Required elements of a LOSDA

Every LOSDA must contain the eighteen elements in [PASVL Appendix A](../LICENSE). The
canonical list, with validation rules, is in
[`schemas/losda-v1.schema.json`](../schemas/losda-v1.schema.json). The minimum validity set is:

`losda_id`, `version`, `work.repo_url`, `issuer.legal_name`, `licensee.legal_name`,
`class`, `term.start`, `term.end` (or `perpetual: true`), `effective_date`, `signature`, and
`registry.record_hash`.

A LOSDA missing any of these is **void ab initio** and confers no permission.

## 8. Identifier format

```
LOSDA-<ISSUER>-<YYYY>-<NNNNNN>
```

| Component | Rule |
|---|---|
| `LOSDA` | Fixed prefix, uppercase |
| `<ISSUER>` | Registered issuer code, uppercase alphanumeric, 3–8 characters; `BSDC` is reserved for the Steward |
| `<YYYY>` | Four-digit year of issuance, Gregorian |
| `<NNNNNN>` | Six-digit zero-padded serial, unique per issuer per year, never reused |

Examples:

```
LOSDA-BSDC-2026-000001
LOSDA-ACMELAB-2026-000417
LOSDA-OSM-2027-000002
```

**8.1 Permanence.** An identifier is never reassigned, even after revocation or expiry. A
revoked LOSDA remains visible in the Registry with status `revoked` so that third parties can
detect forged or stale instruments.

**8.2 No reuse across Works.** One LOSDA authorizes one Work (or one expressly listed set of
Works in a Class E instrument). It cannot be stretched across unrelated Works.

## 9. Issuance procedure

Issuers must follow the same nine steps. The Steward's own issuance follows the same process
with the License Council as second reviewer.

| Step | Action | Actor | Target time |
|---|---|---|---|
| 1 | Submit request using `templates/LOSDA-REQUEST.md` | Applicant | — |
| 2 | Acknowledge and assign a request reference | Issuer | 3 business days |
| 3 | Triage: class, completeness, sanctions check | Issuer | 5 business days |
| 4 | Due diligence: identity, use case, scale, risk | Issuer | 10 business days |
| 5 | Decision: approve, approve with conditions, or refuse | Issuer | 10 business days |
| 6 | Generate the LOSDA letter from the template | Issuer | 3 business days |
| 7 | Sign the letter; compute the canonical record hash | Issuer | 1 business day |
| 8 | Record in the Registry; publish Verification URL | Registry Custodian | 2 business days |
| 9 | Notify the licensee and deliver the signed letter | Issuer | 1 business day |

**9.1 Clock stops.** The clock stops while the Issuer waits for information from the applicant.
A request that is incomplete for thirty (30) consecutive days may be closed.

**9.2 Total target.** From complete request to effective LOSDA: twenty (20) business days for
Classes S, I, A, G, P, R, X; forty (40) business days for Classes E, H, D, M, C.

**9.3 Expedited handling.** Classes P and X must be expedited. Any class may be expedited
where the applicant shows urgency, including an imminent launch, a regulatory deadline, or a
humanitarian need.

**9.4 Refusal.** Refusal must be reasoned and must identify the ground. Grounds are listed in
Section 14. A refusal is appealable under `governance/APPEALS.md`.

**9.5 Silence is not approval.** No response from an Issuer is never permission. There is no
"deemed approval" under this framework.

**9.6 Cooling-off.** An applicant refused for fraud, misrepresentation, or a sanctions issue
may not reapply within twelve (12) months, unless the refusal is overturned on appeal.

## 10. Standard condition library

Issuers select conditions by code. A LOSDA must list the codes it applies. Codes may be
modified, but modifications must be written out in full in the LOSDA.

| Code | Condition | Default for |
|---|---|---|
| C1 | Preserve all copyright, license, and attribution notices in source and in product documentation | All |
| C2 | Present license identification and attribution to end users in an accessible location | H, D, O |
| C3 | Deploy only within the stated Territory and Field of Use | All |
| C4 | Do not exceed the stated scale limits; report scale annually | S, H, E, D |
| C5 | No sublicensing, resale, or Service Bureau Use without express written permission | All |
| C6 | Notify the Issuer of a material security incident within 72 hours | H, D, M, G |
| C7 | Keep the Registry contact details current; respond to Registry verification within 15 days | All |
| C8 | Maintain records sufficient to demonstrate compliance for 3 years | All paid classes |
| C9 | Do not assert IP rights against the Author or Contributors except defensively | All |
| C10 | Publish a model card and record the Work as training provenance | M |
| C11 | Do not use model outputs to reproduce the Work as a substitute | M |
| C12 | Provide security updates to distributed devices for the stated support window | D |
| C13 | Disclose sub-processors and hosting locations | H, E |
| C14 | Comply with the Ethics Policy incorporated by reference | Optional |
| C15 | Participate in an annual compliance attestation | E, G, C |
| C16 | Offer the Issuer a right of first refusal on a transfer of the LOSDA | Optional |

## 11. Scope construction

**11.1 Expressio unius.** What is not stated is not granted. Silence is not permission.

**11.2 Beneficiary.** Only the named licensee and its named Affiliates may deploy. Contractors
may deploy only as agents of, and on systems controlled by, the licensee, and only within the
same scope; the licensee remains fully liable.

**11.3 Territory.** "Worldwide" means all territories except those excluded by sanctions.
A named territory includes the licensee's own personnel traveling temporarily.

**11.4 Field of Use.** Field-of-use limits are interpreted by the described purpose, not by
the licensee's internal labelling. Re-labelling a product to fit an existing Field of Use is a
Violation.

**11.5 Scale.** Where scale is capped by users, the cap counts unique natural persons served
in any rolling twelve-month period. Where capped by instances, each independently functioning
deployment counts. Where capped by revenue, the licensee's audited revenue for the relevant
period governs.

**11.6 Affiliates and M&A.** A new Affiliate requires an amendment unless the LOSDA grants
"all current and future Affiliates". On a merger or acquisition, the surviving entity inherits
the LOSDA only if it assumes the obligations in writing and notifies the Issuer within thirty
(30) days.

**11.7 Modifications.** A licensee may modify the Work for its own Deployment within scope.
Modifications must not remove notices, must not introduce malicious code, and must be
disclosed on request.

**11.8 Downgrades and forks of the Work.** A licensee may deploy newer releases of the Work
within the same major version without a new LOSDA, unless the LOSDA fixes a version. A major
version increase may be conditioned on a new LOSDA if the Author states that in the NOTICE.

## 12. Validity and verification

**12.1 Registry prevails.** The Registry record determines current status. A PDF, email, or
screenshot is evidence of what was issued, not of what is currently valid.

**12.2 Verification URL.** Every LOSDA carries a Verification URL of the form:

```
https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/registry/losda-registry.json#LOSDA-...
```

Where the Steward operates a verification service, the URL must resolve to a page showing the
same fields as the Registry record.

**12.3 Status values.** `active`, `suspended`, `expired`, `revoked`, `superseded`,
`pending`, `withdrawn`.

**12.4 Canonical record hash.** The Registry stores a SHA-256 hash of the canonical JSON form
of the LOSDA record (keys sorted, UTF-8, no insignificant whitespace). The hash is printed on
the letter. A letter whose hash does not match the Registry has been altered.

**12.5 Third-party reliance.** A third party may rely on an `active` Registry entry as
evidence of permission, unless it has actual knowledge of a breach. Reliance on a `suspended`
or `revoked` entry is not reasonable.

**12.6 Clock skew.** An expiry takes effect at 23:59:59 UTC on the stated end date.

## 13. Amendment, renewal, and transfer

**13.1 Amendment.** Only the issuing authority may amend, and only by a written Amendment
Notice recorded in the Registry. Amendments that reduce the licensee's rights require the
licensee's written consent (PASVL §10.11).

**13.2 Renewal.** The licensee must apply for renewal at least thirty (30) days before expiry.
A late renewal may be granted with a continuity bridge that back-dates the new term to the
expiry date, provided no breach occurred in the gap.

**13.3 Transfer.** A LOSDA is non-transferable except with the Issuer's written approval,
recorded in the Registry. The Issuer may charge an administration fee. Transfers must carry
over all accrued obligations.

**13.4 Change of control.** A change of control of the licensee is a deemed transfer request
and must be notified within thirty (30) days.

## 14. Refusal

An Issuer may refuse a LOSDA where:

1. the applicant's identity cannot be verified to a reasonable standard;
2. the applicant is subject to sanctions or is a restricted party;
3. the applicant has an active revocation for the same Work;
4. the applicant has a record of repeated, uncured Violations;
5. the proposed use is prohibited by the Ethics Policy incorporated in the NOTICE;
6. the proposed use would breach applicable law;
7. the requested scope is materially beyond what the Author offers;
8. the applicant refuses the standard conditions without a lawful justification;
9. issuing would create a conflict of interest the Issuer cannot resolve; or
10. the Work is subject to an exclusive grant that conflicts with the request.

Refusal must be reasoned, in writing, and must state the appeal route. Refusal on grounds 1–4
must be reported in aggregate in the annual transparency report.

## 15. Suspension, revocation, and wind-down

**15.1 Suspension.** Up to 30 days, once renewable, on credible evidence of a serious
Violation. Recorded in the Registry with a reason code.

**15.2 Grounds for revocation.** The six grounds in PASVL §18.7. No other ground exists.

**15.3 Procedure.** Notice, 30-day response, reasoned decision, second reviewer, Registry
entry, appeal notice (PASVL §18.8).

**15.4 Wind-down.** A 180-day Reliance Period applies unless the revocation is for the
licensee's material breach, sanctions, or a court order (PASVL §19.2).

**15.5 Notice to dependants.** Where a revoked LOSDA supported third-party products, the
licensee must use reasonable efforts to notify affected customers of the change.

**15.6 Reinstatement.** Per PASVL §18.11–18.12 and `governance/APPEALS.md`.

## 16. Registry obligations

**16.1 What is published.** LOSDA ID, Work, class, licensee display name (or anonymized
identifier if permitted), country, Effective Date, term, territory, scale band, status, and
the record hash.

**16.2 What is not published.** Fees, personal contact details, national identity numbers,
negotiated conditions that the parties mark confidential, and security details. Confidential
terms must be listed in the record as "confidential annex" without content.

**16.3 Integrity.** The Registry is append-only for status changes. Corrections are recorded
as new entries referencing the old, never by silent edits. A periodic Merkle root or digest of
the Registry is published to make tampering detectable.

**16.4 Transparency report.** Annually: number of requests, approvals, refusals by ground,
suspensions, revocations, appeals and outcomes, average processing time, and complaints
received about the framework.

**16.5 Availability.** The Registry must be publicly readable, machine-readable, and free of
charge. A read-only mirror must be maintained at a second location.

## 17. Machine-readable record

Every LOSDA has a canonical JSON record conforming to
[`schemas/losda-v1.schema.json`](../schemas/losda-v1.schema.json). The record is authoritative
for status. The human-readable letter is authoritative for the narrative terms, and the two
must agree.

Validation is performed in CI by [`scripts/validate_losda.py`](../scripts/validate_losda.py).

## 18. Signatures and anti-fraud

**18.1 Permitted signatures.** Handwritten signature (scanned), qualified electronic
signature, platform-issued signature, or PGP/GPG detached signature over the canonical record
hash.

**18.2 Signatory.** The Author or an authorized signatory. The authority basis must be stated
in the LOSDA.

**18.3 Verification.** A third party verifies by (a) checking the Registry entry, (b) checking
the record hash on the letter, and (c) where present, verifying the detached signature against
the issuer's published key in `registry/keys/`.

**18.4 Fraud.** Forging a LOSDA, altering a letter, or misrepresenting Registry status is a
Violation under PASVL §13.8 and may be a criminal offense. The Steward will report credible
fraud to the relevant platform and, where appropriate, to authorities.

**18.5 Key compromise.** An Issuer whose key is compromised must notify the Steward within
72 hours. The Steward must publish a key-revocation notice and re-verify affected records.

## 19. Disputes

Disputes about a LOSDA follow PASVL Article 24: negotiation, mediation, then arbitration in
Dhaka under the UNCITRAL Rules, with carve-outs for urgent relief and consumer fora. The
License Council's appeal process is a condition precedent only where the LOSDA says so and
only for issues within the Council's competence.

## 20. Records and retention

| Record | Retention |
|---|---|
| LOSDA letters and signed records | Permanent (Registry is append-only) |
| Applications, including refused applications | 5 years |
| Due-diligence material | 5 years after end of term |
| Enforcement files | 7 years, or longer if litigation is reasonably anticipated |
| Personal data in Registry | Minimized; reviewed annually |

## 21. Fees

**21.1** Fees are set by the Author and stated on the Author's public pricing page or in the
LOSDA.

**21.2** Fees are consideration for permission, not for copies, and not for any transfer of
rights.

**21.3** No-fee classes: A, G, P, R, X, C, and O (Class O by definition, since it is a
standing public grant).

**21.4** The Steward may not take a share of fees except a published administrative fee for
Registry operation, which must be disclosed in `GOVERNANCE.md`.

**21.5** Refunds follow the policy stated in the LOSDA. Where no policy is stated, fees are
non-refundable once the term begins, except where the Issuer revokes without cause, in which
case the unexpired portion is refunded pro rata.

**21.6** Hardship. An Issuer may reduce or waive fees for small organizations, non-profits,
and public-interest uses, and must do so consistently with its published policy.

## 22. Forms and templates

| Form | Location |
|---|---|
| LOSDA letter | `templates/LOSDA-TEMPLATE.md` |
| Application | `templates/LOSDA-REQUEST.md` |
| Denial letter | `templates/LOSDA-DENIAL.md` |
| Amendment notice | `templates/LOSDA-AMENDMENT.md` |
| Revocation notice | `templates/REVOCATION-NOTICE.md` |
| NNC | `templates/NOTICE-OF-NON-COMPLIANCE.md` |
| Appeal | `templates/APPEAL-FORM.md` |
| Violation report | `templates/VIOLATION-REPORT.md` |

## 23. Change control

This specification is versioned with the License. Changes follow
`governance/AMENDMENT-PROCESS.md`. Corrections to typography, links, and examples may be made
by the Steward with a `CHANGELOG.md` entry.

---

**Document control**

| Field | Value |
|---|---|
| Document | LOSDA Specification and Operating Rules |
| Version | 1.0 |
| In force | 2026-01-01 |
| Owner | BSD C License Council |
| Review cycle | Annual |
| Next review | 2027-01-01 |
