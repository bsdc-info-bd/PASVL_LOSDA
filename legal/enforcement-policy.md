# Enforcement Policy

**Status:** Binding policy of the framework for Authors who adopt this policy, and for the
Steward in all cases.
**Version:** 1.0
**Related:** PASVL Articles 18, 19, 20; [`../governance/APPEALS.md`](../governance/APPEALS.md)

---

## 1. Principles

Enforcement under this framework is **documented, proportionate, graduated, and appealable**.
The purpose of enforcement is compliance, not punishment. An enforcement system that destroys
the goodwill the framework depends on has failed, even if it wins.

### 1.1 Seven principles

1. **Cure before escalation.** Every capable-of-cure breach gets a cure period.
2. **Proportionality.** The response is matched to the harm and to the size and capacity of the
   party.
3. **Consistency.** Similar breaches are treated similarly. Departures must be reasoned and
   recorded.
4. **Transparency.** Enforcement statistics and the Enforcement Register are public.
5. **Fair hearing.** No sanction without notice and an opportunity to respond, except in
   urgent cases, which must be regularised within five business days.
6. **No vendettas.** Enforcement is for the licence, not for personal disputes, competition, or
   inconvenience.
7. **Protection of reporters.** Retaliation is itself a Violation.

### 1.2 Who may enforce

| Actor | Powers |
|---|---|
| Author | Full enforcement in respect of its Work, including revocation of its LOSDAs |
| Co-Authors | Joint enforcement; a co-Author may act alone only in urgent cases and must notify the others |
| Steward | Framework integrity, Registry integrity, trademark matters, Continuity LOSDAs, appeals, and coordination |
| Contributors | May report; may enforce Article 4, 11, and 13 as intended third-party beneficiaries (PASVL §25.9) |
| Beneficiaries | May report; may not demand payment or threaten publicity (§20.8) |
| Anyone else | Report only |

## 2. Detection

### 2.1 Sources of evidence

- Public package registries, app stores, and container registries;
- Public job postings referencing the Work;
- Public documentation, status pages, and security disclosures;
- Automated code-search and fingerprinting of publicly served assets;
- Customer and community reports;
- The Registry itself, where a deployer has claimed a LOSDA that does not exist;
- Voluntary disclosure by the deployer.

### 2.2 Prohibited investigation methods

Enforcement must never rely on:

- unauthorised access to a system;
- social engineering of a deployer's staff;
- purchase or use of stolen data;
- surveillance of individuals;
- impersonation of authorities;
- pretexting.

Evidence obtained by prohibited methods must be disregarded and may itself be a Violation.

### 2.3 Evidence standard

- **Stage 0–1 (informal, NNC):** credible evidence — a reasonable belief on documented facts.
- **Stage 2 (suspension):** substantial evidence — more likely than not.
- **Stage 3 (revocation, public Register entry):** clear and convincing evidence.
- **Stage 5 (litigation):** the standard of the forum.

Every enforcement file must record the evidence and the standard applied.

## 3. The enforcement ladder

### Stage 0 — Informal resolution

**When:** first contact, low harm, likely ignorance, non-commercial party.
**Action:** a private, courteous message identifying the Work, the conduct, the licence term,
and how to regularise.
**Time limit:** 14 days to respond.
**Record:** internal only; the Enforcement Register records only aggregated counts.
**Escalation:** if ignored or refused, proceed to Stage 1.

### Stage 1 — Notice of Non-Compliance and cure

**When:** Stage 0 fails or is inappropriate (commercial scale, repeat conduct, or harm).
**Action:** issue an NNC using `templates/NOTICE-OF-NON-COMPLIANCE.md`.
**Contains:** the Work, the conduct, the provision breached, the evidence (redacted where
necessary), the cure period, the consequences, and the appeal route.
**Cure period:** 30 days standard; 60 days for good-faith non-commercial; 7 days where harm to
persons is ongoing.
**Record:** Registry entry with status `notice_issued`, redacted for personal data.
**Escalation:** if no cure, proceed to Stage 2 or 3 per severity.

### Stage 2 — Suspension

**When:** continuing breach, credible serious evidence, or risk of imminent harm.
**Action:** suspend the LOSDA (max 30 days, once renewable) and/or suspend the Visibility Grant
in respect of that party.
**Requires:** written decision stating grounds, the evidence, and the review date.
**Effect:** deployment must stop unless the Reliance Period applies, which it generally does
not where the suspension is for the licensee's own breach.
**Record:** Registry status `suspended`, Enforcement Register entry.
**Escalation:** if unresolved at the end of suspension, proceed to Stage 3.

### Stage 3 — Revocation and public entry

**When:** uncured breach, fraud, harm, sanctions, or a final adverse finding.
**Action:** revoke the LOSDA, publish a redacted Enforcement Register entry, and start the
Reliance Period clock where applicable.
**Requires:** the full procedure in PASVL §18.8 — notice, response, reasoned decision, second
reviewer, Registry entry, appeal notice.
**Record:** permanent, append-only.
**Escalation:** if the deployer continues, proceed to Stage 4.

### Stage 4 — Platform and registry action

**When:** continued unlicensed deployment, infringing distribution, or fraudulent
representation.
**Action:** complaints to hosting providers, package registries, app stores, cloud providers,
payment processors where the conduct is fraudulent, and domain registrars where a confusingly
similar domain is used.
**Evidence pack:** the NNC, the Registry state, the licence, the proof of authorship, and a
description of the specific infringing material.
**Caveat:** platform processes are independent. Outcomes are not guaranteed, and deadlines
(e.g. counter-notice periods) must be respected.

### Stage 5 — Legal action

**When:** material commercial harm, refusal to engage, repeat infringement, or a need to
establish a precedent.
**Action:** civil proceedings for infringement, breach of licence conditions, or both, together
with injunctive relief where available.
**Requirements before filing:** documented attempts at resolution, an assessment of costs and
recoverability, compliance with pre-action protocols, and a proportionality review by the
License Council where the Steward is a party.
**Publicity:** litigation is announced only in the transparency report, not as a press
campaign.

## 4. Severity matrix

| Conduct | Baseline severity | Typical entry stage | Cure available |
|---|---|---|---|
| Accidental evaluation use beyond 30 days | Low | 0 | Yes, 60 days |
| Internal deployment without a LOSDA, small organisation | Low–Medium | 1 | Yes, 30–60 days |
| Commercial deployment without a LOSDA | Medium | 1 | Yes, 30 days |
| Hosted service without a LOSDA | Medium–High | 1 | Yes, 30 days |
| Distribution in a product without a LOSDA | High | 2 | Yes, if stopped promptly |
| Removing licence notices | High | 2 | Yes, restore notices |
| Relicensing or sublicensing | High | 2–3 | Yes, cease and correct |
| Repo-laundering or model laundering | High | 3 | Limited; requires cessation and disclosure |
| Forged or altered LOSDA | Critical | 3 | No |
| Malicious code in a contribution | Critical | 3 | No |
| Sanctions violation | Critical | 3 | No; referral |
| Retaliation against a reporter | Critical | 3 | No |
| Ignoring an NNC entirely | Aggravating | 3 | Case-by-case |

Aggravating factors: repeat conduct, concealment, commercial gain, harm to persons,
misrepresentation, targeting a small author.

Mitigating factors: self-report, prompt cure, good faith, small capacity, public-interest use,
cooperation, first offence.

## 5. Sanctions available

1. A written warning and a compliance plan.
2. A retroactive LOSDA with a regularisation fee, where the Author consents.
3. Suspension of the LOSDA.
4. Revocation of the LOSDA.
5. Exclusion from applying for new LOSDAs for a period (12–36 months for severe cases).
6. Public Enforcement Register entry (redacted).
7. Removal of contributor privileges.
8. Platform and registry complaints.
9. Civil proceedings.
10. Referral to authorities where fraud, sanctions, or malicious code is involved.

Sanctions 5 and 6 require the second-reviewer step. Sanctions 9 and 10 require License Council
approval where the Steward is the complainant.

## 6. Cure

### 6.1 What cure means

Cure requires all of: (a) the breach has stopped; (b) its effects have been remediated where
reasonably possible; (c) the breaching party has confirmed cure in writing; and (d) where fees
are owed, they are paid or a payment plan is agreed.

### 6.2 What cure does not mean

Cure does not erase liability for past harm, does not restore a revoked LOSDA automatically,
and does not prevent the Author from requiring an audit of the deployment period.

### 6.3 Automatic reinstatement

A first, good-faith, non-commercial breach cured within 30 days of notice results in automatic
reinstatement (PASVL §18.12), provided the party did not conceal the breach.

## 7. Deadlines and limitation

| Step | Deadline |
|---|---|
| Acknowledgment of a report | 5 business days |
| Triage decision | 10 business days |
| NNC issue after triage | 5 business days |
| Response to an NNC | 15 business days |
| Cure | as stated in the NNC |
| Appeal filing | 20 business days from the decision |
| Appeal decision | 45 business days |
| Limitation on starting proceedings | as allowed by applicable law; the framework targets 3 years from discovery |

## 8. Confidentiality and publicity

1. Pre-Stage-3 communications are confidential.
2. Stage 3 entries are public and redacted to minimum necessary detail.
3. A party may request that its identity be anonymised where disclosure would create a safety
   risk; the Steward decides, recording the reason.
4. The framework does not engage in "name and shame" for Stage 0–1 matters.
5. The Steward publishes annual statistics under `governance/TRANSPARENCY-REPORT-TEMPLATE.md`.

## 9. Appeals and reinstatement

Every sanction above Stage 1 is appealable under [`../governance/APPEALS.md`](../governance/APPEALS.md).
Reinstatement applications are permitted 6 months after a Stage 3 sanction, and 12 months after
an exclusion under Section 5(5).

## 10. Misuse of the enforcement process

Knowingly false reports, coordinated false reporting, or using the process to harass are
Violations. Sanctions include warnings, loss of reporting privileges, and, where the conduct is
unlawful, referral to authorities. The accused party has the same appeal rights as any other
party.

## 11. Enforcement in practice: a worked example

> **Facts.** A 40-person SaaS startup deploys a PASVL work as part of its customer portal
> without a LOSDA. Its public status page references the work by name. It has been live for six
> months.
>
> **Stage 0.** The author sends a private message. The startup's CTO responds within two days,
> apologises, and explains it believed the repository was MIT-licensed because the README said
> so.
>
> **Assessment.** The README was indeed stale — the author's own fault in part. Severity is
> reduced. The conduct is a commercial deployment without a LOSDA, but was not concealed.
>
> **Resolution.** The author offers a Class H LOSDA backdated to the start of the deployment,
> at a regularisation fee equal to six months of standard fees. The startup accepts, records
> the LOSDA in the Registry, and fixes its dependency audit process.
>
> **Record.** Enforcement Register: one Stage 0 matter, resolved by regularisation, no public
> entry naming the party. Annual transparency report: counted in aggregate.
>
> **Lesson for authors:** keep your README accurate. A stale README weakens your enforcement
> position and is unfair to users.

## 12. Review

This policy is reviewed annually by the License Council. Proposed changes go through
`governance/AMENDMENT-PROCESS.md`.
