# RFC 0001 — Publish PASVL-1.0 and LOSDA-1.0

| Field | Value |
|---|---|
| RFC number | 0001 |
| Title | Publish PASVL-1.0 and LOSDA-1.0 |
| Author(s) | BSD C License Council |
| Status | **Accepted** |
| Class | Major (creates the framework) |
| Created | 2025-09-01 |
| Sponsor | License Council |
| Comment period | 2025-09-15 to 2025-10-30 (45 days) |
| Decision date | 2025-11-15 |
| Effective | 2026-01-01 |

---

## 1. Summary

Publish a new licensing framework consisting of two instruments: a public license that makes
source code permanently visible while reserving the right to deploy (**PASVL-1.0**), and a named,
scoped, recorded permission instrument that grants deployment individually (**LOSDA-1.0**).
Publish the framework with registry, governance, templates, tooling, and translations.

## 2. Problem statement

Two licensing models dominate, and both force a trade many authors do not want:

1. **Permissive open source** grants everyone the right to deploy, including large organizations
   that capture most of the value. The source is visible, but the author is not funded. The
   predictable result is burnout, abandonment, and unpatched security defects in software that
   the world depends on.
2. **Proprietary licensing** preserves commercial control but removes visibility. Buyers cannot
   audit, researchers cannot study, and students cannot learn from the work.

Three specific gaps follow:

- **No middle instrument.** Source-available licenses exist (BUSL, Elastic, PolyForm), but they
  are almost all framed as time-limited or non-commercial restrictions. None combines permanent
  public visibility with a formal, scoped, per-deployer permission process.
- **No verifiable permission.** Where source-available authors do grant commercial permission, it
  is usually an email or a private contract. A customer, auditor, or regulator cannot verify it.
- **No governance.** License changes are unilateral. There is no appeal, no register of decisions,
  and no separation between the author's interests and the framework's integrity.

## 3. Proposed text

The full text of `LICENSE` (28 Articles, 4 Appendices) and `legal/losda-specification.md`
(23 sections) as published in this repository at version 1.0.0.

## 4. Rationale

The framework separates two things that open-source licenses bundle together:

- **Visibility** — reading, studying, auditing, teaching, contributing. It costs the author almost
  nothing and creates enormous public value.
- **Deployment** — running the software to serve customers, operate infrastructure, or ship
  devices. It is where commercial value is captured.

Separating them produces a license that is more permissive than proprietary (visibility is
unconditional) and more restrictive than open source (deployment is licensed) — and, critically,
honest about both.

The LOSDA turns the reservation into a usable instrument rather than a wall: it has a template,
a class taxonomy, a service target, a registry, a verification URL, a revocation procedure with
cause and wind-down, and an appeal route.

## 5. Effects

| Party | Effect |
|---|---|
| Authors | Gain a way to publish publicly while funding deployment; gain administration work |
| Deployers | Gain auditability and a predictable permission; gain a fee and an application |
| Contributors | Gain visibility of their contributions; accept an inbound license allowing relicensing |
| Readers, students, researchers | Gain permanent free visibility; lose nothing |
| The registry | New operational burden: recording, verification, corrections, audits |
| Existing LOSDAs | None — this is the first version |

## 6. Compatibility and migration

No migration is required, because the framework is new. Adoption guidance is published in
`docs/migration-guide.md` and `templates/ADOPTION-CHECKLIST.md`.

Known incompatibilities:

- **GPL / AGPL**: structurally incompatible in both directions. Documented in
  `legal/compatibility.md`.
- **OSI-approved lists**: PASVL will not appear on them and will not be submitted. Tools that
  require an OSI identifier must use `LicenseRef-PASVL-1.0` or `SEE LICENSE IN LICENSE`.

## 7. Alternatives considered

| Alternative | Why rejected |
|---|---|
| **Do nothing** | The status quo produces underfunded maintainers and unauditable software |
| **MIT / Apache-2.0** | Gives away deployment rights; does not solve the funding or control problem |
| **BUSL-1.1** | Time-limited conversion to open source; not a permanent permission model, and the "eventual open" promise is a different trade |
| **Elastic-2.0 / PolyForm** | Service-provider restrictions without a formal permission process or a registry |
| **Proprietary EULA with source access** | Visibility is conditional and revocable; no contribution culture; no public-interest classes |
| **A CLA-only commercial model on an open license** | Does not reserve deployment; a competitor may still host it |
| **A pledge, not a license** ("fair-code" style) | Unverifiable, unenforceable, and not a license at all |

## 8. Who this hurts

This section is mandatory, and the answer is not "nobody".

1. **Companies that cannot accept gated deployment.** Organizations with an OSI-only procurement
   policy will be unable to use PASVL works. That is a real cost, borne by the project's adoption.
2. **Projects that need ubiquity.** Standards, protocol implementations, and libraries benefit
   from unconditional rights. PASVL is wrong for them.
3. **Developers who believe all software must be freely runnable.** They will regard the license
   as a betrayal of open source, and some will fork. The framework accepts that criticism rather
   than hiding from it.
4. **Small deployers facing administration.** A sole trader who wants to run a tool must now
   obtain a document. The no-fee classes and the 20-day target reduce, but do not eliminate, this
   cost.
5. **Authors themselves.** Enforcement is work. Most authors will not enjoy writing an NNC. The
   framework's processes are designed to keep that work rare and proportionate.
6. **The Steward.** A public registry, an appeals process, and an audit obligation are expensive.
   The framework must publish its costs and remain small enough to remain honest.

## 9. Legal review

| Question | Answer |
|---|---|
| Does this change rights? | It creates them; no prior grants exist |
| Jurisdictions reviewed at publication | Bangladesh, India, UK, EU, US (preliminary) |
| Known enforceability concerns | Deployment restriction depends on jurisdiction, notice, and distribution model |
| Advice obtained | External review of the Bangladesh governing-law and arbitration clauses; the rest flagged as needing local review (`legal/jurisdiction-matrix.md`) |

## 10. Implementation plan

1. Publish the license, specification, governance, templates, schemas, and registry. ✅
2. Open the RFC process. ✅
3. Publish the Bengali translation of the summaries. ✅
4. Obtain and publish ten reference adoptions. ☐
5. Commission jurisdiction reviews for the top five markets. ☐
6. Publish the first annual transparency report. ☐

## 11. Open questions

1. Should Class O (Open Deployment) have a standard standing instrument? Deferred to a later RFC.
2. How should model weights be treated beyond the guidance in `legal/non-software-works.md`?
   Deferred.
3. Should the Steward offer a collective licensing pool for small authors? Deferred.

## 12. Decision

| Field | Value |
|---|---|
| Outcome | **Accepted** |
| Vote | For: 7 · Against: 0 · Abstain: 0 |
| Reasons | The framework fills a real gap, is honest about its limits, and provides the governance that source-available licenses typically lack |
| Effective date | 2026-01-01 |
| Review date | 2027-01-01 |
