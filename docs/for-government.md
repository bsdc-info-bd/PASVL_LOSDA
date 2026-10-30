# For Government and Public Sector

Public bodies have a dual interest in software: they need to deliver services reliably, and they
must spend public money responsibly, transparently, and in a way that protects the public's
rights. PASVL is designed to serve both.

---

## 1. Why a public body might choose PASVL

| Interest | How PASVL serves it |
|---|---|
| Transparency and auditability | Source is public; anyone, including auditors and the press, can inspect it |
| Value for money | No fee for Class G; you pay only for the deployment permission, if at all |
| Vendor independence | The source is available to you; you are not locked into a black box |
| Sovereignty and continuity | A Continuity LOSDA protects essential services if a supplier disappears |
| Procurement clarity | The permission is a written instrument with defined scope, not an ambiguous "free" licence |
| Public-interest uses | Article 9 grants emergency and public-interest pathways |
| Accountability | The Registry and the Enforcement Register are public |

## 2. The classes you will use

| Need | Class | Fee |
|---|---|---|
| Departmental system used by civil servants | G | None by default |
| Public-facing service | G | None by default |
| Emergency response | P | None, expedited |
| Research or pilot | R | None |
| Continuous service where the author is gone | C | None; requires evidence |
| Training for staff | A (if academic) or I | Depends on the author |

**Class G** requires an authorising officer and a statement of public purpose. It is granted
for public service delivery, not for onward commercial exploitation.

## 3. Procurement compatibility

### 3.1 Framing the acquisition

You are procuring **software and a deployment permission**, not open-source software. Your
contract documents should say so. Suggested description:

> "The supplier will provide software licensed under PASVL-1.0. The source code will be publicly
> readable and auditable. Deployment by the authority is permitted under a Letter of Software
> Deployment Approval (LOSDA) recorded in the public LOSDA Registry, scope: [territory], [field
> of use], [scale], term: [term]."

### 3.2 Questions for suppliers

1. Will you provide a Class G LOSDA, and on what terms?
2. Will the LOSDA be perpetual or multi-year?
3. What happens to the LOSDA if your company is acquired or dissolved?
4. Will you provide source escrow?
5. What are your support and security commitments?
6. Will you permit publication of the LOSDA scope for accountability?
7. Are there any restrictions that could interrupt service delivery?
8. Will you provide a Continuity LOSDA undertaking?

### 3.3 Clauses to include

- Delivery of a signed LOSDA before go-live.
- A perpetual or multi-year term aligned to the service life.
- Assignment on change of control without consent.
- Security patch SLAs.
- Escrow and Continuity LOSDA upon supplier failure.
- Indemnity, where available.
- A requirement that the supplier not describe the software as open source.

## 4. Freedom of information and transparency

The License and the Registry support transparency. A public body that deploys PASVL software:

- may publish its LOSDA (it contains no confidential information by default);
- should record the LOSDA ID in its asset register and, where appropriate, in its publication
  scheme;
- may receive a request for the licence terms under freedom-of-information law — the answer is
  that the terms are public.

## 5. Accessibility, security, and data protection

PASVL does not change your statutory obligations. You remain responsible for:

- accessibility of the service;
- security of the deployment;
- lawful processing of personal data;
- records management and retention;
- procurement integrity.

A LOSDA condition C13 (sub-processor disclosure) and C6 (incident notification) help you meet
your own obligations — use them.

## 6. Emergency use

Article 9.1 permits a public body or humanitarian organisation to deploy without a prior LOSDA
during a declared emergency for up to 90 days, provided it:

1. notifies the author or the Steward within 14 days;
2. does not sell the deployment;
3. applies for a regular LOSDA within 90 days if the use continues.

Keep a record of the notice. It is your evidence of good faith.

## 7. Continuity

If a supplier becomes unavailable, insolvent, or unresponsive for 60 days, and the deployment
supports an essential service, the Steward may issue a Continuity LOSDA on the author's behalf
(Article 9.2, Class C). You will need:

- evidence of the essential service;
- evidence of the supplier's unavailability;
- a description of the deployment;
- the name of the accountable officer.

## 8. Model contract language

> **Software licence.** The Supplier shall deliver a Letter of Software Deployment Approval
> (LOSDA) issued under version 1.0 of the Public Availability with Source-Code Visibility
> License (PASVL-1.0), recorded in the LOSDA Registry, permitting the Authority to deploy the
> Software in [territory] for [purpose] at a scale of [limits] for a term of [term]. The LOSDA
> shall be delivered no later than [date]. The Supplier warrants that it has authority to issue
> the LOSDA and that the LOSDA is valid and recorded at the time of delivery.
>
> **Continuity.** The Supplier shall grant the Authority a right to obtain a Continuity LOSDA
> from the Steward if the Supplier ceases to operate or fails to respond to the Authority for
> sixty (60) consecutive days.
>
> **Source escrow.** The Supplier shall deposit the source code with [escrow agent] under the
> attached escrow agreement.

## 9. Risks specific to public bodies

| Risk | Mitigation |
|---|---|
| Supplier unable to issue the LOSDA (not the copyright owner) | Require proof of ownership in diligence |
| LOSDA scope too narrow for a growing service | Negotiate headroom; review annually |
| Political controversy over a non-open licence | Publish an honest explanation; the code is still public |
| Audit finding on licence compliance | Register the LOSDA and record it in asset management |
| Supplier dissolution | Continuity LOSDA + escrow |
| Data protection breach | Your DPA and incident process; use condition C6 and C13 |

## 10. When to choose an open licence instead

Use an OSI-approved licence when:

- the software is a standard that public bodies must all be able to adopt without a vendor;
- the procurement model is "buy support, not permission";
- your national policy mandates open source;
- the software is small and the permission overhead exceeds its value.

PASVL is a tool, not a doctrine. The right licence depends on the public purpose.

## 11. Contacts and templates

- [`../templates/LOSDA-REQUEST.md`](../templates/LOSDA-REQUEST.md) — apply for Class G or P
- [`../templates/DATA-PROCESSING-ADDENDUM.md`](../templates/DATA-PROCESSING-ADDENDUM.md)
- [`../legal/plain-language.md`](../legal/plain-language.md) — for briefing ministers and boards
- [`../legal/enforcement-policy.md`](../legal/enforcement-policy.md) — your rights if an author
  treats you unfairly
