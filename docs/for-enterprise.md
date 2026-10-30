# For Enterprise

You are evaluating a PASVL work for use in a company. This document is written for the people
who have to say yes: engineering leads, procurement, security, and legal.

---

## 1. The thirty-second summary

| Question | Answer |
|---|---|
| Can we read the code? | Yes, always, free |
| Can we audit it? | Yes, always |
| Can we use it in production? | Only with a LOSDA |
| Is there a warranty? | No (Article 21) |
| Is there a patent grant? | Yes, limited and defensive (Article 16.2–16.3) |
| Can we modify it? | Yes, within your LOSDA scope |
| Can we host it for customers? | Class H LOSDA |
| Can we ship it in a product? | Class D LOSDA |
| Can we train a model on it? | Class M LOSDA |
| Can we sublicense it? | No, unless expressly permitted |
| What if the author disappears? | Continuity LOSDA (Class C) |
| What if we breach? | Notice, cure, appeal, wind-down |
| Is it open source? | No — and it must not be described as such |

## 2. The procurement conversation

### 2.1 Typical objections and honest answers

**"Our policy requires OSI-approved open source."**
Then you cannot adopt PASVL under your current policy. Ask whether the policy permits
source-available software with a paid deployment licence — many do, once the risk is documented.
Do not misclassify it.

**"We can't accept a licence that can be revoked."**
Revocation requires cause, notice, a 30-day response, a second reviewer, and a 180-day wind-down
(§18.7–18.8, §19.2). A perpetual LOSDA may be revoked only for breach, fraud, sanctions, a court
order, or serious harm (§19.4). Compare that with a proprietary vendor's termination rights.

**"We can't accept no warranty."**
Almost all open-source licences and most SaaS terms disclaim warranty. Mitigate with your own
testing, insurance, and an optional support agreement.

**"We can't accept the indemnity gap."**
Indemnity is available where a paid LOSDA says so (§21.8). Negotiate it.

**"What if the author refuses to license us?"**
Refusals must be reasoned and are appealable. Refusal on protected grounds is prohibited
(`legal/ethics-policy.md`, Section 5).

**"What if the author's company is acquired?"**
§25.4 requires the successor to assume the Author's obligations, with a Registry update. §19.5
prevents retroactive tightening.

### 2.2 Questions to ask the Author in diligence

1. Who owns the copyright in every file? Are there contributors, and are their grants recorded?
2. Is any component under an incompatible or unknown licence?
3. Is there an existing exclusive grant that conflicts with our proposed scope?
4. What is the Author's funding, and does a funder have rights?
5. Who signs LOSDAs, and what happens if that person is unavailable?
6. Is the work subject to export control or sanctions restrictions?
7. Does the work incorporate the Ethics Policy, and what does that mean for our use?
8. What is the support and security-patch commitment?
9. What is the author's succession plan?
10. Are there any pending disputes about the work's provenance?

## 3. Your internal process

```
Engineering ──► Licence review ──► Security review ──► LOSDA request ──► Contract
     │                 │                  │                  │              │
  scope, data    compatibility,     SBOM, CVEs,        scope, term,   fees, indemnity,
  classification  obligations       hardening          scale          support
```

### 3.1 Engineering

- Confirm the work is not in an excluded domain (see `legal/ethics-policy.md`).
- Produce a bill of materials including transitive dependencies.
- Classify the deployment type and estimate scale with headroom.
- Identify hosting locations and sub-processors.

### 3.2 Licence review

- Check the NOTICE and the LICENSE version.
- Confirm no incompatible components.
- Check whether the work is under a dual licence.
- Identify obligations: attribution, reporting, incident notice, audit.
- Map obligations to owners inside your organisation.

### 3.3 Security review

- Review the code or commission a review.
- Check the vulnerability disclosure history.
- Confirm whether a deployment gate or telemetry exists and how to configure it.
- Add the Author to your incident notification process.

### 3.4 Contracting

- Request a Class S, E, H, or D LOSDA as appropriate.
- Negotiate: term, scale headroom, indemnity, support, and the right to assign in an M&A.
- Consider a perpetual LOSDA for core infrastructure (but check §19.4).
- Record the LOSDA ID in your software inventory.

## 4. Operating in compliance

| Control | Implementation |
|---|---|
| Inventory | Add the LOSDA ID to your SBOM or asset register |
| Scope monitoring | Alert when a product, region, or scale threshold is exceeded |
| Attribution | Automate the third-party licences page |
| Incident notification | Include the issuer in your security escalation |
| Records | Retain compliance evidence for 3 years |
| Renewal | Calendar reminder 90 days before expiry |
| Change of control | Include LOSDA assignment in M&A diligence |
| Audit | Include licence obligations in internal audit scope |

## 5. Risk register for an enterprise adopter

| Risk | Likelihood | Mitigation |
|---|---|---|
| Unenforceability in a key jurisdiction | Low–medium | Legal opinion; the licence remains the agreed standard between the parties |
| Author disappears | Medium | Continuity LOSDA; source escrow; vendor risk |
| Author's fees rise at renewal | Medium | Multi-year LOSDA; fixed renewal formula |
| Scope creep triggers a breach | Medium | Automated scope monitoring |
| Security vulnerability in the work | Medium | Your own review; patch SLAs; monitoring |
| Reputational risk from the "not open source" label | Medium | Honest communication; explain the trade |
| Incompatible dependency found later | Low | SBOM and licence scanning in CI |

## 6. Contracting clauses you may want

1. **Indemnity** for IP infringement, limited to the unmodified work.
2. **Support**: response times, security patches, and end-of-life notice.
3. **Escrow**: source escrow with a release trigger.
4. **Assignment**: the right to assign in a merger or acquisition without consent, or with
   deemed consent.
5. **Audit**: a lighter audit right than the default, with notice and confidentiality.
6. **Scale headroom**: a 24-month growth allowance before an amendment is required.
7. **Price protection**: a cap on renewal increases.
8. **Continuity**: a right to a Continuity LOSDA if the Author ceases trading.

## 7. What you must not do

- Do not represent the work as open source in your SBOM.
- Do not vendor it into an MIT-licensed project and present the combined work as MIT.
- Do not let an affiliate deploy under the parent's LOSDA unless the affiliate is named.
- Do not deploy first and license later.
- Do not ignore a Notice of Non-Compliance; escalate it to legal immediately.

## 8. Bottom line for the decision-maker

PASVL gives you **auditable transparency** — you can see everything — and **contractual
predictability** — you know exactly what you may do. What it does not give you is a free ride.
If your organisation's risk appetite cannot accept a paid, revocable, warranty-free permission,
the honest decision is to choose different software. If it can, the framework is unusually
well-documented, and the obligations are finite and knowable.
