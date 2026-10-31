# Registry Policy

**Version:** 1.0 · **Owner:** Registry Custodian · **Applies to:** the LOSDA Registry, the
issuers register, the key register, the works register, and the Enforcement Register.

## 1. Purpose

The Registry is the framework's memory. It answers one question for the whole world: *is this
deployment permitted, by whom, for what, and right now?*

If the Registry is wrong, the framework is wrong. Everything in this policy is designed to make
the Registry correct, complete, and hard to corrupt.

## 2. What the Registry contains

| File | Contents | Access |
|---|---|---|
| `registry/losda-registry.json` | Every LOSDA, with scope, term, status, hash | Public read |
| `registry/issuers.json` | Registered issuer codes and delegated authority | Public read |
| `registry/works.json` | Works that have adopted the framework | Public read |
| `registry/keys/` | Public keys for verifying issuer signatures | Public read |
| `registry/enforcement-register.json` | Enforcement actions and outcomes | Public read (redacted) |
| Private annexes | Confidential fee terms, identity documents | Custodian only |

## 3. Data model

### 3.1 LOSDA record

Every record conforms to `schemas/losda-v1.schema.json` and contains:

1. `losda_id`
2. `version`
3. `class`
4. `work` — name, repo URL, commit or release reference
5. `issuer` — legal name, issuer code, capacity
6. `licensee` — legal name, country, public display name or anonymized identifier
7. `scope` — deployment type, territory, field of use, scale limits
8. `conditions` — condition codes and any bespoke text
9. `fees` — present or `none`; amounts may be marked confidential
10. `term` — start, end or perpetual
11. `effective_date`
12. `status` and `status_history`
13. `registry` — record hash, previous record hash, entry timestamp
14. `verification_url`

### 3.2 Status history

Status changes are appended, never overwritten. Each entry records:

```json
{ "date": "2026-05-01T12:00:00Z", "from": "active", "to": "suspended",
  "reason_code": "R-SERIOUS-VIOLATION", "reference": "ENF-2026-0044",
  "actor": "BSD C Registry Custodian" }
```

### 3.3 Immutability

1. Entries are append-only.
2. A correction is a new entry that references the corrected entry.
3. The Registry's Merkle root is published monthly to a public location, so tampering is
   detectable after the fact.
4. Each release of the Registry is tagged in git with a signed tag.

## 4. Who may write

| Action | Who | Approval required |
|---|---|---|
| Add a LOSDA | Registry Custodian, on receipt of a signed LOSDA from an authorized issuer | Custodian + second Custodian review |
| Change status (active → expired) | Automated process | None, if deterministic |
| Change status (suspension, revocation) | Registry Custodian | Issuer's signed decision + second reviewer |
| Correct an entry | Registry Custodian | Custodian + issuer acknowledgment |
| Add an issuer | Registry Custodian | License Council |
| Revoke a key | Registry Custodian | Custodian + issuer notification |
| Add an enforcement entry | Registry Custodian | Enforcement authority's signed decision |
| Add a work | Author or Custodian | Author verification |

## 5. Verification URL

Every record has a stable verification URL:

```
https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/registry/losda-registry.json#LOSDA-XXXX-YYYY-NNNNNN
```

Where a hosted verification service exists, it must display the same fields, may not vary the
data, and must link back to the canonical file.

## 6. Record hash

**6.1 Canonical form.** JSON with keys sorted lexicographically, UTF-8 encoding, arrays in
declared order, no insignificant whitespace, and timestamps in RFC 3339 with `Z`.

**6.2 Algorithm.** SHA-256 over the canonical UTF-8 bytes.

**6.3 Publication.** The hash is printed on the LOSDA letter and stored in the record. A letter
whose hash does not match the Registry has been altered.

**6.4 Chain.** Each new record may include the previous record's hash to form a hash chain,
making insertion, deletion, or reordering detectable.

## 7. Correction and dispute

| Situation | Procedure |
|---|---|
| Typo in a licensee's name | Correction entry; Custodian + licensee confirmation |
| Wrong scope recorded | Correction entry; issuer confirmation; the narrower of the two governs until corrected |
| A LOSDA was never issued | Mark record `void`; publish a fraud notice |
| Two records for one LOSDA | Mark both, investigate, publish the correct one |
| A third party disputes a record | Open a Registry Dispute; 30-day resolution target; appeal to the Appeals Panel |

## 8. Deletion

**Nothing is deleted.** A record may be marked `withdrawn`, `void`, or `anonymized`, but the
entry remains. This protects third parties who relied on the record and prevents a licensee
from erasing a revocation.

**Exception — personal data:** where the privacy policy requires anonymization, personal data
fields are replaced with an anonymized identifier, and the change is recorded.

## 9. Availability and integrity

1. The Registry is served from the canonical repository and at least one mirror.
2. A read-only copy is escrowed with a third party (`DISSOLUTION-AND-SUCCESSION.md`).
3. Availability target: 99% monthly for read access.
4. Integrity check: CI validates every record against the schema on every commit.
5. Recovery: any party may verify the Registry against the published Merkle roots.

## 10. Enforcement Register

**10.1 What is published.** Date, reference, class of action, provision breached, stage,
outcome, appeal status, and a redacted party identifier.

**10.2 What is withheld.** Personal data beyond a name or anonymized identifier, confidential
evidence, information that would endanger a person, and information subject to legal privilege.

**10.3 Duration.** Stage 0–1 matters are aggregated, not listed. Stage 2 and above are listed
permanently, with a note if the action was overturned on appeal.

**10.4 Overturned actions.** If an appeal overturns a sanction, the entry must say so
prominently. A wrong entry must be corrected within 5 business days of the decision.

## 11. Access control

1. Repository write access is limited to named Custodians.
2. Branch protection requires signed commits and a second review.
3. Two-factor authentication is mandatory.
4. Access is reviewed quarterly; departures lose access within 24 hours.
5. All writes are logged with the actor's identity and timestamp.

## 12. Fees

Reading the Registry is free. The Steward may not charge for access, for verification, or for a
copy. A processing fee for a LOSDA must be published and must not be conditional on being
listed.

## 13. Service targets

| Action | Target |
|---|---|
| Record an issued LOSDA | 2 business days |
| Expire on the stated date | Automated, within 1 hour |
| Reflect a suspension | 1 business day |
| Reflect a revocation | 1 business day |
| Correct a factual error | 5 business days |
| Respond to a Registry dispute | 10 business days |

## 14. Annual audit

An independent auditor verifies, at least every two years:

1. a sample of LOSDAs against their signed letters;
2. that every revocation decision is properly authorized;
3. access logs and change history;
4. the Merkle root chain;
5. that no record was silently deleted.

The audit summary is published in the transparency report.
