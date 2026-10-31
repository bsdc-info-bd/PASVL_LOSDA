# The Legal Instruments of the PASVL/LOSDA Framework

This directory contains the binding instruments, the operating rules, and the interpretive
guidance for the framework. Everything here is published so that authors, deployers, auditors,
courts, and the public can read the same text at the same time.

## 1. Instrument index

| Document | Status | Purpose |
|---|---|---|
| [`../LICENSE`](../LICENSE) | **Binding** | PASVL-1.0, the public license |
| [`losda-specification.md`](losda-specification.md) | **Binding operating rules** | The LOSDA instrument: classes, issuance, registry |
| [`plain-language.md`](plain-language.md) | Non-binding summary | The whole framework in human words |
| [`hierarchy-and-interpretation.md`](hierarchy-and-interpretation.md) | Interpretive | Order of precedence and reading rules |
| [`platform-reality.md`](platform-reality.md) | Interpretive | How PASVL interacts with GitHub and host terms |
| [`enforcement-policy.md`](enforcement-policy.md) | **Binding policy** | How violations are detected, noticed, cured, escalated |
| [`privacy-policy.md`](privacy-policy.md) | **Binding policy** | Personal data in the Registry and enforcement |
| [`ethics-policy.md`](ethics-policy.md) | **Binding for adopters who incorporate it** | Prohibited uses and ethical review |
| [`sanctions-and-export.md`](sanctions-and-export.md) | Interpretive | Export control and restricted parties |
| [`anti-corruption.md`](anti-corruption.md) | **Binding policy** | Integrity of the licensing process |
| [`compatibility.md`](compatibility.md) | Interpretive | Combining PASVL code with other licenses |
| [`jurisdiction-matrix.md`](jurisdiction-matrix.md) | Interpretive | Country-by-country notes and open questions |
| [`non-software-works.md`](non-software-works.md) | Interpretive | Extending the framework to docs, models, data, hardware |
| [`risk-register.md`](risk-register.md) | Governance | Known legal and operational risks |

## 2. How to read this repository

1. **Start with the plain-language summary** if you are new.
2. **Read the License itself** — all of it — before you rely on any summary.
3. **Read the LOSDA specification** if you intend to deploy, issue, or administer.
4. **Read the enforcement policy** if you are deploying commercially, because that is the
   document that tells you what happens when something goes wrong.
5. **Check the version.** This repository publishes Version 1.0. If the NOTICE of the software
   you are using names a different version, that version governs your use.

## 3. What is binding and what is not

| Kind of text | Binding? |
|---|---|
| `LICENSE` | Yes — it is the license |
| LOSDA letter, signed and registered | Yes — for that licensee only |
| LOSDA specification, parts marked **Binding** | Yes — as operating rules of the framework |
| NOTICE file supplied by an Author | Yes — as terms additional to the license |
| Governance documents | Yes — for the Steward and its bodies |
| Guides, FAQs, tutorials, this index | No — explanatory only |
| Translated texts | No — unless expressly designated authoritative |

## 4. Version policy

The framework is versioned in lock-step:

- **License:** `PASVL-<major>.<minor>`
- **LOSDA:** `LOSDA-<major>.<minor>`
- **Schema:** `losda-v<major>.schema.json`

A major version change may alter rights. A minor version change may not. See
[`../governance/AMENDMENT-PROCESS.md`](../governance/AMENDMENT-PROCESS.md).

## 5. Citing the instruments

Academic citation, legal citation, and machine-readable identification formats are in
[`../docs/citation.md`](../docs/citation.md) and [`../CITATION.cff`](../CITATION.cff).

## 6. Contact

- Licensing and LOSDA enquiries: see [`../GOVERNANCE.md#contact`](../GOVERNANCE.md)
- Security reports: [`../SECURITY.md`](../SECURITY.md)
- Conduct complaints: [`../CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md)
- Enforcement reports: [`../templates/VIOLATION-REPORT.md`](../templates/VIOLATION-REPORT.md)

## 7. Not legal advice

Nothing in this directory is legal advice. Authors and deployers are responsible for obtaining
advice appropriate to their jurisdiction and circumstances.
