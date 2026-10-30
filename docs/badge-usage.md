# Badge Usage

Badges are the fastest way to tell a reader what the licence does. They are also easy to misuse.
This document sets out the official badges, where they may be used, and what they mean.

## 1. The official badges

| Badge | Meaning | Who may display | File |
|---|---|---|---|
| `licence-PASVL-1.0` | This work is licensed under PASVL-1.0 | Any author of a PASVL work | `assets/badge-pasvl.svg` |
| `deployment-LOSDA required` | Deployment requires a LOSDA | Any author of a PASVL work | `assets/badge-losda-required.svg` |
| `source-available` | Not open source; source is public | Any author of a PASVL work | `assets/badge-source-available.svg` |
| `LOSDA active` | The licensee holds a valid, active LOSDA | A licensee | `assets/badge-losda-active.svg` |
| `LOSDA verified` | The Registry confirms the LOSDA | A licensee, after verification | `assets/badge-losda-verified.svg` |
| `steward-BSDC` | The work is stewarded by BSD C | Only BSD C and works it stewards | `assets/badge-steward-bsdc.svg` |

## 2. Markdown

```markdown
[![PASVL-1.0](https://img.shields.io/badge/licence-PASVL--1.0-blue)](LICENSE)
[![Deployment requires LOSDA](https://img.shields.io/badge/deployment-LOSDA%20required-orange)](https://github.com/bsdc-info-bd/PASVL_LOSDA)
[![Source-available](https://img.shields.io/badge/source-available-informational)](https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/legal/plain-language.md)
```

For a licensee:

```markdown
[![LOSDA active](https://img.shields.io/badge/LOSDA-active-brightgreen)](https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/registry/losda-registry.json#LOSDA-BSDC-2026-000123)
```

Use the **plain-text** shields.io form so that the badge renders without hosting assets. If you
prefer the SVG assets in this repository, host them yourself and link back to the licence.

## 3. HTML

```html
<a href="LICENSE">
  <img alt="PASVL-1.0" src="https://img.shields.io/badge/licence-PASVL--1.0-blue">
</a>
```

## 4. Rules

### 4.1 You may

- display the licence badge on a work you publish under PASVL;
- display the "LOSDA required" badge to warn deployers;
- display "LOSDA active" on your own product if your LOSDA is currently `active` in the Registry;
- link the badge to the licence or to your Registry entry;
- translate the badge text into another language, preserving the meaning and the colours.

### 4.2 You must not

- display "LOSDA active" while your LOSDA is `suspended`, `expired`, or `revoked`;
- display "LOSDA verified" without having checked the Registry;
- display the BSDC steward badge unless BSD C has designated you;
- alter the badge colours to imply a different licence (for example, green "MIT-style" green for
  a restricted licence);
- remove the badge from a fork while continuing to distribute the work;
- use a badge to imply endorsement, certification, or partnership;
- use the badges in a way that suggests the work is open source.

### 4.3 Accuracy requirement

A badge is a statement of fact. If the fact changes, the badge must change within **7 days**.
A misleading badge is a breach of PASVL §4.3 (no misrepresentation) and §17.3 (badge misuse).

## 5. Static alternatives

If you do not want to depend on a badge service, use text:

> **Licence:** PASVL-1.0 — source is public; deployment requires a LOSDA.

Text is always acceptable and never breaks.

## 6. Colour conventions

| Colour | Meaning |
|---|---|
| Blue `#0969da` | Licence identity |
| Orange `#bc4c00` | Permission required |
| Green `#1a7f37` | Verified active permission |
| Grey `#57606a` | Informational / source-available |
| Red `#cf222e` | Suspended or revoked (should not appear in a public badge; remove it instead) |

## 7. Reporting misuse

If you see a badge used to misrepresent a licence or a permission, report it with
[`../templates/VIOLATION-REPORT.md`](../templates/VIOLATION-REPORT.md), attaching a screenshot
and the URL.
