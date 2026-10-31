<div align="center">

# PASVL · LOSDA

### The public-source, permission-to-deploy licensing framework

**Public Availability with Source-Code Visibility License (PASVL-1.0)**
**Letter of Software Deployment Approval (LOSDA-1.0)**

[![License](https://img.shields.io/badge/license-PASVL--1.0-blue)](LICENSE)
[![Deployment](https://img.shields.io/badge/deployment-LOSDA%20required-orange)](legal/losda-specification.md)
[![Status](https://img.shields.io/badge/status-published%20%C2%B7%20in%20force-brightgreen)](CHANGELOG.md)
[![Version](https://img.shields.io/badge/version-1.0-0969da)](CHANGELOG.md)
[![Steward](https://img.shields.io/badge/steward-Bangladesh%20Software%20Development%20Community-57606a)](GOVERNANCE.md)
[![Language](https://img.shields.io/badge/docs-English%20%C2%B7%20%E0%A6%AC%E0%A6%BE%E0%A6%82%E0%A6%B2%E0%A6%BE-informational)](translations/bn/)

</div>

---

> **Read the source. Ask to deploy. Get it in writing.**

This repository contains the complete, official, international legal framework for software whose
**source code is public forever** but whose **deployment is licensed individually**.

It is not open source. It says so plainly, everywhere, on purpose.

---

## What this is

Two instruments, designed to work together:

| Instrument | What it does | Grants |
|---|---|---|
| **[PASVL-1.0](LICENSE)** — the license | Makes the source public and permanently visible | Read, study, audit, fork, cite, teach, contribute — free, worldwide, forever |
| **[LOSDA-1.0](legal/losda-specification.md)** — the permission | Authorizes a named party to deploy | Run, host, embed, distribute — scoped, term-limited, recorded, revocable only for cause |

The license is public and identical for everyone. The permission is individual and verifiable.
The **registry** is the memory that makes both enforceable in practice.

```
     ┌─────────────────────────────────────────────────────────────┐
     │  EVERYONE                                                   │
     │  ✅ Read   ✅ Audit   ✅ Fork   ✅ Teach   ✅ Cite            │
     │  ❌ Deploy without permission                               │
     └───────────────────────────┬─────────────────────────────────┘
                                 │  applies for a LOSDA
                                 ▼
     ┌─────────────────────────────────────────────────────────────┐
     │  LICENSEE                                                   │
     │  ✅ Deploy within scope   ✅ Host   ✅ Embed   ✅ Distribute  │
     │  ❌ Exceed scope   ❌ Sublicense   ❌ Remove notices          │
     └───────────────────────────┬─────────────────────────────────┘
                                 │  recorded in
                                 ▼
     ┌─────────────────────────────────────────────────────────────┐
     │  PUBLIC REGISTRY — anyone can verify the permission          │
     └─────────────────────────────────────────────────────────────┘
```

---

## The 60-second summary

### You can, without asking anyone

- Read every line of the source.
- Study it, learn from it, teach with it.
- Audit it for security, privacy, and correctness.
- Fork it, clone it, archive it.
- Quote it in papers, books, and reviews.
- Submit pull requests and improvements.
- Build it privately to see whether it works.

**All of that is free, worldwide, perpetual, and irrevocable.**

### You cannot, without a Letter of Software Deployment Approval

- Run it in production.
- Offer it as a hosted service.
- Ship it in a product or a device.
- Use it to train or fine-tune a model.
- Sublicense it, resell it, or rebrand it.
- Call it "open source" — because it is not.

### What a LOSDA gives you

A numbered, signed, publicly recorded permission that states:

`who` may deploy · `what` version · `where` · `for what purpose` · `at what scale` · `for how long` · `under what conditions`

And a **verification URL** that lets anyone — your customer, your auditor, your regulator — check
it in seconds.

---

## Start here

| I am… | Start with |
|---|---|
| **An author** considering this license | [docs/for-authors.md](docs/for-authors.md) → [docs/quickstart.md](docs/quickstart.md) |
| **A team** that wants to deploy | [docs/for-deployers.md](docs/for-deployers.md) → [templates/LOSDA-REQUEST.md](templates/LOSDA-REQUEST.md) |
| **A lawyer or auditor** | [LICENSE](LICENSE) → [legal/losda-specification.md](legal/losda-specification.md) → [legal/risk-register.md](legal/risk-register.md) |
| **A journalist or skeptic** | [docs/why-this-exists.md](docs/why-this-exists.md) → [legal/platform-reality.md](legal/platform-reality.md) |
| **An enterprise** | [docs/for-enterprise.md](docs/for-enterprise.md) |
| **A public body** | [docs/for-government.md](docs/for-government.md) |
| **A teacher or researcher** | [docs/for-education.md](docs/for-education.md) |
| **A contributor** | [CONTRIBUTING.md](CONTRIBUTING.md) → [docs/for-contributors.md](docs/for-contributors.md) |
| **A translator** | [translations/](translations/) |
| **Confused** | [docs/faq.md](docs/faq.md) → [docs/glossary.md](docs/glossary.md) |

---

## The repository at a glance

```
PASVL_LOSDA/
├── LICENSE                      ← PASVL-1.0, the full binding license
├── NOTICE                       ← adoption notice for this repository
├── GOVERNANCE.md                ← who decides what
├── CONTRIBUTING.md              ← how to contribute
├── CODE_OF_CONDUCT.md           ← how we treat each other
├── SECURITY.md                  ← vulnerability disclosure
├── TRADEMARK.md                 ← brand rules
├── CHANGELOG.md                 ← every change, dated
├── CITATION.cff                 ← how to cite this
│
├── legal/                       ← the instruments and their operating rules
│   ├── losda-specification.md   ← the permission instrument, in full
│   ├── plain-language.md        ← the whole thing in human words
│   ├── enforcement-policy.md    ← what happens when rules are broken
│   ├── hierarchy-and-interpretation.md
│   ├── platform-reality.md      ← what a license can and cannot do on GitHub
│   ├── compatibility.md         ← combining with other licenses
│   ├── jurisdiction-matrix.md   ← 17 jurisdictions, honestly assessed
│   ├── ethics-policy.md         ← prohibited uses
│   ├── sanctions-and-export.md
│   ├── privacy-policy.md
│   ├── anti-corruption.md
│   ├── risk-register.md         ← 25 risks, with mitigations
│   └── non-software-works.md
│
├── governance/                  ← the institutions
│   ├── CHARTER.md
│   ├── LICENSE-COUNCIL.md
│   ├── REGISTRY-POLICY.md
│   ├── APPEALS.md
│   ├── AMENDMENT-PROCESS.md
│   ├── ELECTIONS.md
│   ├── ETHICS-REVIEW-BOARD.md
│   ├── CONFLICT-OF-INTEREST.md
│   ├── REGISTRY-CUSTODIAN.md
│   ├── DISSOLUTION-AND-SUCCESSION.md
│   └── TRANSPARENCY-REPORT-TEMPLATE.md
│
├── docs/                        ← practical guides for every audience
│   ├── quickstart.md
│   ├── for-authors.md · for-deployers.md · for-contributors.md
│   ├── for-enterprise.md · for-government.md · for-education.md
│   ├── deployment-scopes.md     ← 40 worked examples
│   ├── losda-guide.md
│   ├── faq.md · glossary.md · why-this-exists.md
│   ├── checklist-deployer-compliance.md
│   ├── migration-guide.md · anti-patterns.md · roadmap.md
│   └── badge-usage.md · versioning.md · citation.md
│
├── templates/                   ← every form you need
│   ├── LOSDA-TEMPLATE.md · LOSDA-REQUEST.md · LOSDA-AMENDMENT.md
│   ├── LOSDA-DENIAL.md · REVOCATION-NOTICE.md
│   ├── NOTICE-OF-NON-COMPLIANCE.md · APPEAL-FORM.md
│   ├── VIOLATION-REPORT.md · SECURITY-REPORT.md · TAKEDOWN-REQUEST.md
│   ├── DATA-PROCESSING-ADDENDUM.md
│   ├── CONTRIBUTOR-AUTHORIZATION.md
│   ├── ADOPTION-CHECKLIST.md · NOTICE-TEMPLATE · LICENSE-HEADER.txt
│
├── schemas/                     ← machine-readable validation
│   ├── losda-v1.schema.json
│   └── registry-v1.schema.json
│
├── registry/                    ← the public source of truth
│   ├── losda-registry.json
│   ├── issuers.json
│   ├── works.json
│   └── enforcement-register.json
│
├── examples/                    ← complete worked examples
│   ├── losda-standard-commercial.md
│   ├── losda-academic.md
│   ├── losda-hosted-service.md
│   ├── losda-record.json
│   └── NOTICE-example
│
├── scripts/                     ← validation and tooling
│   ├── validate_losda.py
│   ├── validate_registry.py
│   ├── new_losda.py
│   ├── hash_record.py
│   ├── check_license_headers.py
│   ├── check_docs.py            ← prose consistency
│   ├── check_links.py           ← links and anchors
│   └── check_refs.py            ← section cross-references
│
├── rfcs/                        ← how the framework changes
├── translations/                ← বাংলা and more
└── .github/                     ← issue templates, PR template, CI
```

---

## The rules, in one page

### The license grants (Article 3)

| Right | Scope |
|---|---|
| Read and study | Any purpose, any person, forever |
| Audit and verify | Including security testing |
| Clone, fork, archive | With notices retained |
| Learn and teach | Including classroom execution |
| Cite and comment | With attribution |
| Propose changes | Contributions welcome |
| Build to verify | Private, non-production |
| Personal study copy | Not for deployment |

### The license reserves (§5)

- Deployment, in every form.
- Hosted service provision.
- Distribution in executable form.
- Machine-learning use.
- Sublicensing and resale.
- Brand use beyond nominative reference.

### The limited free-use envelope (Articles 6–9)

| Envelope | Limit |
|---|---|
| **Evaluation Use** | 30 private, non-production days per work per year (Mode S) |
| **Teaching** | Classroom only, not institutional infrastructure |
| **Research** | Controlled environment, non-commercial, no external service |
| **Security research** | Good faith, coordinated disclosure, 90 days |
| **Emergency** | 90 days, notify within 14 |
| **Everything else** | A LOSDA |

### The LOSDA classes (§10.14)

| | Class | For | Fee |
|---|---|---|---|
| **S** | Standard Commercial | A product or business use | Author's schedule |
| **E** | Enterprise / Portfolio | Groups of affiliates and works | Negotiated |
| **I** | Internal Use | Inside one organization | Often low or zero |
| **H** | Hosted Service / SaaS | Serving third parties online | Often usage-based |
| **D** | Distribution / OEM | Devices, binaries, installers | Often per unit |
| **A** | Academic / Non-Commercial | Universities and colleges | None |
| **G** | Government | Public service delivery | None |
| **P** | Public Interest | Disaster, health, accessibility | None, expedited |
| **R** | Research | Testbeds and studies | None |
| **X** | Evaluation Extension | Short-term trial | None or nominal |
| **C** | Continuity | Rescuing an essential service | None |
| **M** | Machine Learning / AI Data | Training, tuning, evaluation | Negotiated |
| **O** | Open Deployment | Standing public grant by the author | Per the author |

### Enforcement, in order (§20.6)

`0` friendly message → `1` formal notice + cure → `2` suspension → `3` revocation + registry →
`4` platform action → `5` legal action

Every step is documented, proportionate, and appealable.

---

## The ten principles

1. **Visibility is a right. Deployment is a permission.**
2. **No implied licenses.** Permission exists only in writing and in the registry.
3. **Cure before escalation.** Most breaches are mistakes.
4. **Proportionality.** The response matches the harm.
5. **No retroactive tightening.** Rights already granted stay granted.
6. **Revocation needs cause**, notice, a hearing, and a wind-down.
7. **Everything is appealable** once.
8. **No discrimination** in licensing on protected grounds.
9. **Free for the public good.** Academia, government, research, and public interest pay nothing.
10. **Honesty.** It is not open source. We will never pretend otherwise.

---

## Honest positioning

| Claim | True? |
|---|---|
| The source is public and auditable | ✅ Yes, permanently |
| Anyone can read, fork, teach, and contribute | ✅ Yes, free |
| Deployment requires permission | ✅ Yes, in the framework |
| The license is enforceable everywhere, perfectly | ❌ No — jurisdiction-dependent, like every license |
| The license is open source | ❌ No — and it must not be described as such |
| The framework guarantees compliance | ❌ No — it provides clear rules, records, and remedies |
| Enforcement is easy | ❌ No — read [legal/platform-reality.md](legal/platform-reality.md) |

If you need a license that allows anyone to run your software for any purpose, use MIT or
Apache-2.0. This framework is for authors who want visibility to be universal and deployment to
be deliberate.

---

## Adopting the license

```markdown
<!-- Put this in your README -->

> **License: PASVL-1.0 — source is public, deployment is licensed.**
>
> ✅ Read, study, audit, fork, teach, and contribute — free, forever.
> ❌ Deploy, host, embed, or train a model on it without a **Letter of Software Deployment
>    Approval (LOSDA)**.
>
> [License](LICENSE) · [Request deployment approval](https://example.com/licensing)
```

Then follow [templates/ADOPTION-CHECKLIST.md](templates/ADOPTION-CHECKLIST.md).

**Never** set your package manifest to a permissive identifier to silence a tool. Use
`LicenseRef-PASVL-1.0` or `SEE LICENSE IN LICENSE`.

---

## Getting permission

1. Read [docs/for-deployers.md](docs/for-deployers.md) and classify your use.
2. Complete [templates/LOSDA-REQUEST.md](templates/LOSDA-REQUEST.md).
3. Apply. Standard classes target **20 business days** from a complete application.
4. Receive a signed letter with a **verification URL**.
5. Verify it in the registry. **Deploy only when the registry says `active`.**

---

## Contributing to the framework

The framework is meant to survive criticism. Bring it.

- **Ideas and changes:** [rfcs/](rfcs/) using [rfcs/0000-template.md](rfcs/0000-template.md)
- **Corrections:** pull requests against the documents
- **Translations:** [translations/](translations/)
- **Conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Security:** [SECURITY.md](SECURITY.md)

Major amendments require a 45-day public comment period and a two-thirds vote of the License
Council. Rights already granted cannot be withdrawn.

---

## Stewardship

The framework is stewarded by the **Bangladesh Software Development Community (BSD C)** — a
community organization, not a vendor. BSD C publishes the text, operates the registry, holds the
marks, and is bound by the [Charter](governance/CHARTER.md) to act in the interests of the
framework as a whole.

- Governance: [GOVERNANCE.md](GOVERNANCE.md)
- Appeals: [governance/APPEALS.md](governance/APPEALS.md)
- Transparency: [governance/TRANSPARENCY-REPORT-TEMPLATE.md](governance/TRANSPARENCY-REPORT-TEMPLATE.md)
- Succession: [governance/DISSOLUTION-AND-SUCCESSION.md](governance/DISSOLUTION-AND-SUCCESSION.md)

**BSD C does not take a share of any author's licensing fees.**

---

## Status

| Item | Status |
|---|---|
| License version | 1.0 |
| LOSDA specification | 1.0 |
| In force from | 2026-01-01 |
| Registry | Open — initial issuer registered |
| Amendments | Open for RFC |
| Translations | English (authoritative), Bengali |
| OSI approved | No, and will not be submitted |

---

## License of this repository

The **legal texts** in this repository (`LICENSE`, `legal/`, `governance/`, `templates/`) are
published under **PASVL-1.0 itself**, so that anyone may read, copy, translate, and adapt them.
The templates may be used, filled, and distributed freely by authors and licensees. Attribution
to the framework is required but a LOSDA is not required to *use* the documents — only to deploy
software licensed under it.

Documentation and badges are published under PASVL-1.0 as well. See [NOTICE](NOTICE).

---

<div align="center">

**See the source. Ask to deploy. Get it in writing.**

*PASVL-1.0 · LOSDA-1.0 · A project of the Bangladesh Software Development Community*

*Not open source. Deliberately.*

</div>
