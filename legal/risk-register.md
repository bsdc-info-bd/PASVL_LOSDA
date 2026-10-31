# Risk Register

**Version:** 1.0 · **Owner:** BSD C License Council · **Review:** quarterly

A framework that hides its weaknesses is a framework that will fail loudly. This register lists
the known legal, operational, and reputational risks of the PASVL/LOSDA framework, their
likelihood, their impact, the mitigation in the instruments, and the residual risk that
remains.

## Scoring

- **Likelihood:** 1 = rare, 2 = unlikely, 3 = possible, 4 = likely, 5 = almost certain
- **Impact:** 1 = minor, 2 = moderate, 3 = major, 4 = severe, 5 = critical
- **Score:** likelihood × impact (1–25). Red ≥ 15, amber 8–14, green ≤ 7.

## Register

| ID | Risk | L | I | Score | Mitigation | Residual |
|---|---|---|---|---|---|---|
| R-01 | A court holds the deployment restriction unenforceable in a key jurisdiction | 3 | 5 | 15 | Severability (§25.1); contract and infringement claims pleaded separately; purpose-built wind-down; local counsel review | High; framework survives because visibility grant stands |
| R-02 | Users assume public availability means permission and violate unknowingly | 4 | 4 | 16 | Plain-language README; badges; NOTICE; first-breach reinstatement; Stage 0 courtesy process | Medium |
| R-03 | Perception that the license is "not really open source" and therefore hostile | 4 | 3 | 12 | Honest labelling as source-available; no-fee classes; ethics policy; public-interest program | Medium |
| R-04 | Low adoption because deployers fear legal uncertainty | 4 | 4 | 16 | Published LOSDA process with SLAs; registry transparency; standard terms; example LOSDAs; appeals | Medium–High |
| R-05 | Registry becomes a bottleneck or a single point of failure | 3 | 4 | 12 | Static JSON registry; mirror; signed commits; documented recovery; successor provisions (§26.7) | Medium |
| R-06 | Fraudulent or forged LOSDAs circulate | 3 | 4 | 12 | Record hash; public registry; signature verification; key registry; reporting route | Low–Medium |
| R-07 | An author uses the framework to oppress users or competitors | 2 | 4 | 8 | Reasoned refusal; anti-discrimination; ethics policy; appeals; transparency reporting | Medium |
| R-08 | The Steward's impartiality is compromised | 2 | 5 | 10 | Conflict-of-interest register; recusal; independent appeals; external audit; anti-corruption policy | Low–Medium |
| R-09 | Personal data over-published in the registry | 3 | 3 | 9 | Minimization; anonymized listing; privacy policy; retention limits | Low |
| R-10 | A fork or mirror is used to deploy outside a LOSDA | 4 | 3 | 12 | Fork prohibition (§13.4); platform complaints; detection guidance | Medium–High; unavoidable in practice |
| R-11 | A model is trained on the source, laundering the license | 4 | 4 | 16 | Article 14; Class M; model-card attribution; detection heuristics | High; practical enforcement is limited |
| R-12 | Sanctions or export-control breach through a licensee | 2 | 5 | 10 | Screening; self-certification; notification duties; suspension on change of law | Low–Medium |
| R-13 | Competition-law challenge to refusal or exclusive licensing | 2 | 4 | 8 | Non-exclusivity by default; published criteria; appeals; market-power guidance | Low |
| R-14 | Consumer-rights conflict in a jurisdiction with mandatory protections | 3 | 3 | 9 | Consumer carve-out (§21.6); evaluation use; no-waiver clause | Low |
| R-15 | The framework's governance collapses (absence of successor) | 2 | 5 | 10 | Successor provisions (§26.7, §27.6); dissolution plan; registry escrow | Low |
| R-16 | Bad-faith DMCA or platform complaints by adopters damage the framework's reputation | 3 | 3 | 9 | Enforcement policy requires good faith; false-report sanctions; Council oversight | Low–Medium |
| R-17 | Overclaiming marketing by an adopter creates liability | 3 | 3 | 9 | Platform reality document; charter prohibition on overclaiming | Medium |
| R-18 | License incompatibility breaks real projects | 3 | 3 | 9 | Compatibility appendix; dependency pattern; RFC process | Medium |
| R-19 | A security incident in registry infrastructure exposes confidential data | 2 | 4 | 8 | Access control; encryption; incident plan; minimization | Low–Medium |
| R-20 | Authors abandon their works, leaving deployers without an issuer | 3 | 3 | 9 | Continuity LOSDA (§9.2); source escrow recommendations | Medium |
| R-21 | Version confusion: users rely on an outdated summary | 4 | 2 | 8 | Version pinning in NOTICE; changelog; canonical URLs | Low |
| R-22 | The Bengali translation diverges from the English text | 3 | 2 | 6 | Translation review; English prevails clause | Low |
| R-23 | The framework is co-opted by a hostile actor who registers marks or issues fake LOSDAs | 2 | 4 | 8 | Trademark policy; issuer registry; takedown playbook | Low–Medium |
| R-24 | Legal costs of enforcement exceed recoveries | 4 | 3 | 12 | Graduated enforcement; cost-benefit gate before litigation; insurance recommendation | High |
| R-25 | Author lacks standing because contributions were not properly licensed | 2 | 4 | 8 | DCO sign-off; inbound license in Article 12; contribution records | Low |

## Top five risks and the response plan

1. **R-02 (misunderstanding).** Every six months, review the README, the badges, and the FAQ
   against real support questions and update them.
2. **R-04 (adoption friction).** Keep the LOSDA to ten meaningful fields, publish sample
   letters, and hold the twenty-day target for standard classes.
3. **R-11 (model laundering).** Maintain a public position, publish a Class M template, and
   track emerging case law on model training and derivative works.
4. **R-01 (enforceability).** Commission a jurisdiction review for the top five markets in
   2026 and update `jurisdiction-matrix.md`.
5. **R-24 (cost of enforcement).** Adopt a cost-benefit gate: no litigation below a documented
   harm threshold unless a principle is at stake and funding is approved.

## Risk acceptance

The License Council may accept a residual risk explicitly, recording the reason and the
review date. Accepted risks are reported in the annual transparency report.

## Change log

| Date | Change | By |
|---|---|---|
| 2026-01-01 | Initial register | License Council |
