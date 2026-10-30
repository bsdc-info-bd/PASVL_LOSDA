# Example LOSDA — Class H (Hosted Service / SaaS)

> Worked example, fictitious names. Class H is the most commercially significant class: the one
> that answers "can we build a business on top of this?"

---

# LETTER OF SOFTWARE DEPLOYMENT APPROVAL

**LOSDA ID:** `LOSDA-ACME-2026-000512`
**Status on issue:** ACTIVE
**Verification URL:** `…/losda-registry.json#LOSDA-ACME-2026-000512`

## 1. Parties

| Role | Details |
|---|---|
| Issuer | Acme Labs Ltd (`ACMELAB`), Author |
| Licensee | Cloudscale Systems Inc., Delaware, USA (EIN 00-0000000) |
| Public display name | Cloudscale |
| Contact | legal@cloudscale.example |
| Compliance officer | A. Okafor, VP Engineering |
| Affiliates covered | Cloudscale EMEA Ltd (Ireland) |

## 2. The work

| Field | Value |
|---|---|
| Work | Acme Scheduler |
| Repository | https://github.com/acmelabs/scheduler |
| Version | 3.2.x |
| Third-party notices | https://github.com/acmelabs/scheduler/blob/main/THIRD-PARTY-NOTICES.md |

## 3. Scope

### 3.1 Class

**H** — Hosted Service / SaaS

### 3.2 Deployment type

Hosted multi-tenant service, with a single-tenant offering for enterprise customers.

### 3.3 Territory

Worldwide, excluding comprehensively sanctioned territories. Customer data hosted in the
European Union (Ireland, Frankfurt) and the United States (Virginia, Oregon).

### 3.4 Field of use

> Cloudscale "Flow" — a managed workflow product that exposes scheduling through the Licensee's
> own interface and API. End customers interact with Cloudscale's branding only. The Work is
> not exposed directly, and no documentation identifies it as a standalone service.

### 3.5 Scale

| Measure | Limit |
|---|---|
| End users | 500,000 |
| Monthly API requests | 250,000,000 |
| Production instances | 200 |
| Tenants | 20,000 |
| Revenue attributable to the Work's functionality | No cap |

### 3.6 Explicitly excluded

1. Reselling the Work as a standalone scheduling API to third-party developers.
2. White-labelling the Work for another platform operator (Service Bureau Use).
3. Distribution of the Work in source or binary form.
4. Machine Learning Use.

## 4. Term

| Field | Value |
|---|---|
| Effective | 2026-11-01 |
| End | 2028-10-31 (three years) |
| Renewal | Automatic, 12 months, unless either party gives 90 days' notice |
| Review | Annual security and scale review |

## 5. Fees

| Field | Value |
|---|---|
| Structure | USD 60,000 per year base, plus 2% of Flow gross revenue above USD 5,000,000 |
| Floor | USD 60,000 per year |
| Cap | None |
| Payment | Quarterly in arrears, with a revenue statement within 30 days of each quarter's end |
| Audit right | The Issuer may appoint an independent auditor once per year, on 30 days' notice, to verify revenue statements — costs borne by the Issuer unless an understatement of more than 5% is found |
| Refund | Pro rata if the Issuer revokes without cause |

## 6. Conditions

| Code | Applied | Notes |
|---|---|---|
| C1 notices preserved | Yes | In source, and in the product's legal pages |
| C2 attribution to end users | Yes | "Built with Acme Scheduler" in the About dialog |
| C3 territory and field | Yes | |
| C4 scale reporting | Yes | Quarterly, with the revenue statement |
| C5 no sublicensing / Service Bureau | Yes | |
| C6 security incident notice | Yes | Within 72 hours of discovery |
| C7 registry contact | Yes | |
| C8 records | Yes | 3 years |
| C9 no hostile IP assertions | Yes | |
| C13 sub-processor disclosure | Yes | AWS, Cloudflare, Stripe, Datadog |
| C15 annual attestation | Yes | Compliance attestation signed by the VP Engineering |

### 6.1 Bespoke conditions

1. **Availability.** The Licensee must publish a status page and notify the Issuer of any outage
   exceeding four hours.
2. **Security baseline.** The Licensee must maintain SOC 2 Type II or ISO 27001 certification, or
   an equivalent audited programme.
3. **No competitive scheduling API.** The Licensee may not expose the Work's scheduling
   functionality as a public developer API competing with Acme Scheduler's own hosted offering.
4. **Data protection.** A Data Processing Addendum is attached as a confidential annex.
5. **Escalation.** If the Licensee's end-user count exceeds 500,000, it must request an
   amendment within 30 days.

## 7. Reliance period

180 days, plus migration assistance: the Issuer will provide documentation and a reasonable
technical contact for the first 90 days of any wind-down that it initiates without cause.

## 8. Support (bespoke, paid)

| Item | Commitment |
|---|---|
| Security patches | Critical: 7 days; High: 30 days |
| End-of-life notice | 12 months |
| Escalation contact | Named engineer, business hours (UTC+6) |
| Fee | Included in the base fee |

## 9. Acknowledgements

As per the standard template, plus:

The Licensee acknowledges that the revenue-share obligation is auditable, that the audit right is
limited to once per year and to the revenue attributable to the Field of Use, and that the audit
is conducted under confidentiality.

## 10. Signatures

**Issuer:** R. Chowdhury, Director — qualified e-signature, 2026-10-26
**Licensee:** A. Okafor, VP Engineering — qualified e-signature, 2026-10-27

## 11. Registry record

| Field | Value |
|---|---|
| Recorded at | 2026-10-30T11:02:44Z |
| Record hash | `c41e…` |
| Status | ACTIVE |
| Confidential annex | Yes — DPA and fee schedule |

---

## Notes for authors drafting a Class H LOSDA

| Question | Why it matters |
|---|---|
| Is the Work exposed directly or only through the licensee's interface? | Determines whether it is a service or a resale |
| Is there a per-user or revenue metric? | Scale limits without a metric are unenforceable |
| Who audits a revenue share? | Without an audit right, a percentage fee is a hope |
| What happens at 10× growth? | An escalation clause prevents an accidental breach |
| Are sub-processors disclosed? | Required by C13, and useful for the licensee's own compliance |
| Is there a competing-API clause? | Protects the author's own hosted offering |
| Is support inside the fee? | Ambiguity here is the most common source of disputes |
| What is the security baseline? | A hosted service with weak security damages the author's reputation too |
