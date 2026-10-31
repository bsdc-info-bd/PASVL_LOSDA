# Security Report

Use this form to report a vulnerability in a PASVL-licensed Work or in the framework's own
infrastructure (the Registry, the schemas, or the tooling). Good-faith research conducted under
PASVL Article 8 is protected.

**Do not open a public issue for a vulnerability.** Send this form to the address in the Work's
`SECURITY.md` or `NOTICE`, or to the Steward's security contact in `GOVERNANCE.md`.

---

## 1. Reporter

| Field | Value |
|---|---|
| Name or handle | |
| Email | |
| PGP key (optional) | |
| Preferred contact | |
| Credit preference | ☐ Named ☐ Anonymous ☐ Ask me first |

## 2. Affected product

| Field | Value |
|---|---|
| Work / component | |
| Version or commit | |
| Deployment configuration | |
| Environment (OS, runtime, arch) | |

## 3. Vulnerability

| Field | Value |
|---|---|
| Class | RCE / auth bypass / injection / XSS / SSRF / path traversal / DoS / info leak / crypto / other |
| CVSS estimate (if you have one) | |
| Attack vector | Network / adjacent / local / physical |
| Authentication required | None / low / high |
| User interaction required | Yes / No |

## 4. Summary

```
[One paragraph a non-specialist can understand.]
```

## 5. Reproduction steps

```
[Numbered steps. Include a proof-of-concept if you have one.]
```

## 6. Impact

What can an attacker do? Who is affected? Is exploitation observed in the wild?

```
[Impact]
```

## 7. Suggested fix

```
[Optional but appreciated.]
```

## 8. Disclosure intentions

| Question | Answer |
|---|---|
| Do you intend to publish? | ☐ Yes ☐ No ☐ Undecided |
| Proposed publication date | |
| Have you shared this with anyone else? | |

The framework's default coordinated-disclosure period is **90 days** from acknowledgment, or
such shorter period as the maintainer agrees.

## 9. Legal acknowledgments

- ☐ I accessed only systems I was authorized to access, or systems the project provides for
  testing.
- ☐ I did not exfiltrate, retain, or publish personal data.
- ☐ I did not degrade service or access another person's data.
- ☐ I will not demand payment or use the vulnerability for advantage.

---

## For the maintainer

| Field | Value |
|---|---|
| Report reference | `SEC-[YYYY]-[NNNN]` |
| Acknowledged (target: 7 days) | |
| Severity assigned | |
| Remediation target (default: 30 days) | |
| Fix released in version | |
| Advisory published | |
| Reporter credited | |
| CVE requested | ☐ Yes ☐ No |

---

*Template version: SEC-1.0. Related: PASVL Article 8, `SECURITY.md`.*
