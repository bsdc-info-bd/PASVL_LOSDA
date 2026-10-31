# License Compatibility

**Version:** 1.0 · **Normative summary:** PASVL Appendix C

PASVL is source-available with deployment reserved. That makes compatibility a real engineering
question: can you include PASVL code in your project, and can you include other people's code in
a PASVL project? This document answers both directions.

## 1. The two directions

| Direction | Question | Answer lives in |
|---|---|---|
| **Inbound** | May I include third-party code in a PASVL Work? | Sections 3–5 |
| **Outbound** | May I include PASVL code in my project? | Sections 6–8 |

## 2. The golden rule

**PASVL does not grant you rights in anyone else's code, and nobody else's license grants you
the right to deploy PASVL code.** Compatibility decisions must satisfy both licenses
independently. When in doubt, do not combine; use a process boundary instead.

## 3. Inbound: including permissive code in a PASVL Work

| License | Include? | What you must do |
|---|---|---|
| MIT, BSD-2-Clause, BSD-3-Clause, ISC, 0BSD | ✅ Yes | Retain copyright and permission notices |
| Apache-2.0 | ✅ Yes | Retain notices, `NOTICE` file, and state changes; comply with patent clause |
| MPL-2.0 | ✅ Yes (file-level) | Keep MPL files under MPL; do not relicense those files |
| CDDL-1.0 | ⚠️ File-level only | Keep file boundaries; do not create a larger work |
| EPL-2.0 | ⚠️ File-level only | Same caution |
| LGPL-2.1 / LGPL-3.0 | ⚠️ Dynamic linking only | Allow relinking; provide LGPL notices; do not statically link |
| GPL-2.0, GPL-3.0, AGPL-3.0 | ❌ No | Including the code would require releasing the combined work under GPL terms that conflict with PASVL's deployment restriction |
| CC BY 4.0 (docs) | ✅ Yes | Attribute |
| CC BY-SA 4.0 (docs) | ⚠️ Share-alike conflicts | Avoid, unless the documentation is kept separate |
| CC0 / public domain | ✅ Yes | Attribution still required for the PASVL Work as a whole |

### 3.1 Why GPL is incompatible

The GPL requires that the entire combined work be licensed under the GPL, granting everyone the
right to run the software for any purpose. PASVL reserves the right to deploy. The two cannot
both be satisfied for the same combined work. Including GPL code in a PASVL Work would put the
Author in breach of the GPL. Including PASVL code in a GPL project would purport to grant GPL
rights the Author never granted.

This is not a statement that GPL is wrong; it is a statement that the two licenses are
incompatible, as Apache-2.0 and GPL-2.0 are incompatible for similar structural reasons.

### 3.2 Process boundaries

If you need GPL functionality alongside PASVL functionality, do not link or embed. Use:

- a separate process communicating over a documented interface;
- a network boundary with independent services;
- a data file format with no code linkage.

Whether a particular architecture creates a derivative work is a legal question, not a
packaging question. Get advice for high-stakes cases.

## 4. Inbound: proprietary and source-available code

| License | Include? | Notes |
|---|---|---|
| Proprietary with a written permission | ✅ With permission | Keep the written permission on file |
| BUSL-1.1 | ⚠️ Case-by-case | Check the change date and the additional-use grant |
| Elastic-2.0 | ⚠️ Case-by-case | Check the permitted purposes |
| PolyForm Noncommercial/Strict | ⚠️ Case-by-case | Noncommercial limits conflict with commercial LOSDA deployment |
| PASVL-1.0 | ✅ Yes | Same framework; deployment still requires a LOSDA for the combined Work |

## 5. Inbound: what your NOTICE must say

A PASVL Work that includes third-party components must publish:

1. a `THIRD-PARTY-NOTICES` file listing each component, its license, and its copyright notice;
2. any source-offer obligations flowing from the third-party license;
3. any additional restrictions the Author has agreed to (for example, attribution text required
   by a CC BY-NC asset).

## 6. Outbound: using PASVL code in your own project

| Your project's license | Include PASVL code? | Why |
|---|---|---|
| MIT / BSD / Apache-2.0 | ⚠️ Only with separation | You cannot relicense PASVL code; you may link to it as a dependency that users must obtain separately |
| GPL / AGPL | ❌ No | Incompatible both ways |
| LGPL | ⚠️ Only with a clean boundary | Same caution as inbound |
| Proprietary | ⚠️ Only with separation + your own LOSDA | Your users would still need permission to deploy the PASVL component |
| PASVL | ✅ Yes | Obtain a LOSDA for the combined deployment |

### 6.1 The dependency pattern

The cleanest pattern is:

```
your-project/          (your license)
  ├── src/
  └── deps/
        └── pasvl-work/  (not vendored — fetched at build time, with a LOSDA)
```

Vendoring PASVL code into an MIT project does not make it MIT. It creates a combined work with
a PASVL component, and the PASVL conditions continue to attach to that component and, depending
on how it is integrated, to the combined work.

## 7. Outbound: what you may say about PASVL

You may say:

- "This project depends on `<work>`, licensed under PASVL-1.0."
- "Deployment of `<work>` requires a LOSDA."
- "Our deployment is licensed under LOSDA-BSDC-2026-000123."

You may not say:

- "This project is MIT licensed" if it contains PASVL code;
- "PASVL is open source";
- "You may deploy this freely" if a LOSDA is required.

## 8. License identifiers in manifests

| Ecosystem | Recommended value |
|---|---|
| SPDX expression | `LicenseRef-PASVL-1.0` |
| `package.json` | `"license": "SEE LICENSE IN LICENSE"` plus a README statement |
| `pyproject.toml` | `license = { file = "LICENSE" }` |
| `Cargo.toml` | `license-file = "LICENSE"` |
| Maven `pom.xml` | `<licenses>` entry with a `<name>` and `<url>`; no SPDX identifier |
| NuGet | `<license type="file">LICENSE</license>` |
| Docker labels | `org.opencontainers.image.licenses="LicenseRef-PASVL-1.0"` |

Never use a false recognized identifier to silence a tool.

## 9. Dual licensing

An Author may dual-license a Work, for example under PASVL for the public and under a
commercial agreement for large deployers. If so:

1. the NOTICE must state the dual-licensing arrangement clearly;
2. the commercial agreement must not grant rights that contradict the public license for those
   who rely on it;
3. the Author must not use dual licensing as a bait-and-switch: releases already published
   under PASVL remain available under PASVL (§19.5).

## 10. License compatibility requests

If you believe your license is compatible with PASVL and it is not listed here, open an RFC at
[`../rfcs/`](../rfcs/) with:

- the license text;
- the proposed combination pattern;
- a legal analysis;
- a description of the obligations each license imposes.

The License Council will publish an interpretation within 90 days.
