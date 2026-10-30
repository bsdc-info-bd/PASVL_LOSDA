# Quickstart

Two quickstarts: one for authors, one for deployers. Both take under thirty minutes.

---

# Part 1 — Author: adopt PASVL in 30 minutes

## Minute 0–5: decide honestly

Ask yourself one question: *Do I want the source public and the deployment controlled?*

- Yes → continue.
- No, I want maximum adoption → use MIT or Apache-2.0. PASVL is not for you.
- No, I want no commercial use at all → use a non-commercial licence instead.

## Minute 5–10: add the licence files

```bash
# 1. Copy the licence into your repository root
cp /path/to/PASVL_LOSDA/LICENSE ./LICENSE

# 2. Create your NOTICE from the template
cp /path/to/PASVL_LOSDA/templates/NOTICE-TEMPLATE ./NOTICE
# then edit NOTICE: fill in Work, Author, Contact, Mode, and issuing agent

# 3. Add the deployment statement to your README (see Part 1, Minute 15)
```

## Minute 10–15: protect your title

- Confirm that no employer, university, or funder owns the work. If they do, get a written
  waiver before publishing.
- If you have contributors, add the DCO requirement to `CONTRIBUTING.md`:

```
By contributing, you certify the Developer Certificate of Origin 1.1 and agree to the
inbound licence in PASVL Article 12.
Sign off every commit with: git commit -s
```

## Minute 15–20: communicate

Add this block to your README, near the top:

```markdown
> **Licence: PASVL-1.0 — source is public, deployment is licensed.**
>
> ✅ You may read, study, audit, fork, teach with, and contribute to this code. Free, forever.
> ❌ You may **not** run it in production, offer it as a service, ship it in a product, or train
>    a model on it without a **Letter of Software Deployment Approval (LOSDA)**.
>
> [Read the licence](LICENSE) · [Request deployment approval](https://example.com/licensing)
> · [Plain-language summary](https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/legal/plain-language.md)
```

Add the badge from [`../assets/`](../assets/):

```markdown
[![PASVL-1.0](https://img.shields.io/badge/licence-PASVL--1.0-blue)](LICENSE)
[![Deployment requires LOSDA](https://img.shields.io/badge/deployment-LOSDA%20required-orange)](https://github.com/bsdc-info-bd/PASVL_LOSDA)
```

## Minute 20–25: technical hygiene

```bash
# Put a header on every source file. Example for Python:
# Copyright (c) 2026 Your Name
# Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
# SPDX-License-Identifier: LicenseRef-PASVL-1.0

# In package.json
"license": "SEE LICENSE IN LICENSE"

# In pyproject.toml
license = { file = "LICENSE" }

# In container builds
LABEL org.opencontainers.image.licenses="LicenseRef-PASVL-1.0"
```

Do **not** put `"license": "MIT"` anywhere to silence a tool.

## Minute 25–30: set up the permission process

1. Create a licensing page with: classes, fees, response target, and contact.
2. Make a copy of `templates/LOSDA-TEMPLATE.md`.
3. Decide where you will record issued LOSDAs (a `registry/` folder in your repo is enough to
   start, with the same JSON format).
4. Write your first entry in your changelog: "Licence changed to PASVL-1.0, effective DATE."

## Done

You now have: a public, auditable codebase; a clear, honest licence; and a documented path for
anyone who wants to deploy.

---

# Part 2 — Deployer: get permission in 30 minutes

## Minute 0–5: find out what you need

Open the work's `NOTICE` and `README`. Look for:

- the **Mode** (S or U);
- the **classes** offered;
- the **contact** for licensing;
- whether there is a **fee schedule**.

If there is no NOTICE, assume Mode S and contact the author at the address in the repository.

## Minute 5–10: classify your use

| Your use | Class |
|---|---|
| Internal tool, staff only | I |
| Customer-facing product, one organisation | S |
| Hosted service for third parties | H |
| Embedded in a device or distributed installer | D |
| Training or fine-tuning a model | M |
| University teaching or research | A or R (usually free) |
| Government service | G (usually free) |
| Disaster response or public interest | P (free, expedited) |

## Minute 10–20: fill in the application

Copy [`../templates/LOSDA-REQUEST.md`](../templates/LOSDA-REQUEST.md) and complete every field.
The three that matter most:

1. **Field of use** — be specific. "Use it in our platform" is not specific.
2. **Scale** — give real numbers with room to grow.
3. **Data and security** — say if you process personal data, and who you notify after an
   incident.

## Minute 20–25: send it

Email the issuer, or open a licensing request in their tracker. Keep a copy. Ask for:

- an acknowledgement within 3 business days;
- a target decision date;
- confirmation of any fee.

## Minute 25–30: prepare for compliance

Before you deploy, set up:

- [ ] a third-party licences page in your product;
- [ ] a record of your permitted scope;
- [ ] a calendar reminder for scale reporting;
- [ ] the issuer's security contact in your incident runbook;
- [ ] a monitored licensing mailbox.

## After the LOSDA arrives

1. Verify it in the Registry using the verification URL.
2. Check the hash on the letter matches the Registry.
3. Check the scope covers what you actually plan to do.
4. If something is missing, request an amendment **before** you launch.
5. Save a copy of the signed letter where your legal team can find it.

---

## The ten-second version

> **Reading is free. Running is licensed. Ask first, record it, stay inside the scope.**
