# Roadmap

Where the framework is going. Dates are intentions, not promises; the license does not change
without the Amendment Process.

## Phase 0 — Publication (2026 Q1) ✅

- [x] Publish PASVL-1.0 and the LOSDA specification
- [x] Publish the governance charter and policies
- [x] Publish the schema, templates, and examples
- [x] Publish the registry with the initial issuer
- [x] Publish the Bengali translation
- [x] Open the RFC process

## Phase 1 — Adoption (2026 Q2–Q3)

- [ ] Ten reference adoptions across different languages and sectors
- [ ] Five issuing authors registered
- [ ] First 50 LOSDAs recorded
- [ ] Licensing page generator (a static site from a NOTICE)
- [ ] GitHub Action that checks license headers and NOTICE consistency
- [ ] Bengali and English documentation parity
- [ ] First public webinar and office hours

## Phase 2 — Tooling (2026 Q4)

- [ ] `pasvl` CLI: initialize a repository, validate a NOTICE, generate a LOSDA, verify a record
- [ ] Registry verifier web service (read-only, no cookies, no tracking)
- [ ] Reference implementation of a deployment gate (optional, disclosed, disableable)
- [ ] SBOM integration: emit PASVL license identifiers correctly
- [ ] Package-manager guidance for npm, PyPI, Maven, Cargo, NuGet, and Docker

## Phase 3 — Institutional (2027 H1)

- [ ] Jurisdiction reviews for the top ten markets
- [ ] Model contract clauses for public procurement
- [ ] Insurance guidance for authors and deployers
- [ ] Escrow provider partnerships
- [ ] University curriculum pack
- [ ] First independent audit of the Registry

## Phase 4 — Maturity (2027 H2)

- [ ] 100 issuing authors
- [ ] 1,000 recorded LOSDAs
- [ ] Second-language translation set (Spanish, French, Arabic, Indonesian)
- [ ] Appeals Panel operating with a published casebook
- [ ] Annual transparency report and audited accounts
- [ ] PASVL-1.1 clarifying release

## Long-term questions

These are open, and the community should decide them through the RFC process:

1. **Should there be a standard public license for "Class O" works?** A work whose author wants
   to permit public deployment within the framework still needs a per-work standing grant. A
   standard instrument might simplify this.
2. **Should the framework support machine-readable permission negotiation?** A protocol for
   requesting and issuing a LOSDA automatically, with human approval at the end.
3. **Should there be a collective license pool?** Small authors could delegate issuance to the
   Steward for a small fee.
4. **How should model weights be treated?** The `non-software-works.md` guidance is a starting
   point, not a settled answer.
5. **Should the framework propose treaty language?** A license cannot change copyright law, but
   the framework could advocate for a recognized category of "publicly visible, permission-gated
   software".

## What will not happen

- PASVL will not be submitted for OSI approval. It would fail, and submitting it would be
  dishonest.
- The framework will not add a clause that forbids all commercial use. That is a different
  license.
- The Steward will not take a share of authors' fees.
- Rights already granted will not be withdrawn.
- The Registry will not be sold or paywalled.

## How to influence the roadmap

Open an RFC in [`../rfcs/`](../rfcs/) or comment on the roadmap issue. Priorities are set by the
License Council with input from the Authors' Assembly.
