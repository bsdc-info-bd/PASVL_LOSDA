# Security Policy

## 1. What this applies to

| Asset | In scope |
|---|---|
| This repository's scripts | Yes |
| The JSON schemas | Yes |
| The registry files | Yes — integrity issues are security issues |
| The framework's hosted services (when they exist) | Yes |
| Software licensed under PASVL by third-party authors | No — report to that author |

## 2. Reporting a vulnerability

**Do not open a public issue.**

Use [`templates/SECURITY-REPORT.md`](templates/SECURITY-REPORT.md) and send it to the security
contact in [`GOVERNANCE.md`](GOVERNANCE.md), or use GitHub's private vulnerability reporting if
enabled on this repository.

### What to include

1. The affected component and version.
2. Reproduction steps or a proof of concept.
3. The impact you believe it has.
4. Your disclosure intentions.
5. Whether you want credit.

### What not to include

- Personal data of third parties.
- Credentials or tokens.
- Material obtained by unauthorised access.

## 3. Our commitments

| Commitment | Target |
|---|---|
| Acknowledge your report | 7 days |
| Initial assessment | 14 days |
| Remediation plan | 30 days |
| Fix for a critical issue | 30 days, or a public explanation |
| Public advisory | After the fix, or at 90 days, whichever is sooner |
| Credit | Offered, unless you prefer anonymity |

## 4. Safe harbour

Good-faith security research conducted under **PASVL Article 8** is protected:

- It is not a licence violation.
- It is not a circumvention of a technical measure.
- We will not pursue legal action for research that follows the rules below.

### The rules

1. Access only systems you are authorised to access, or that are provided for testing.
2. Do not degrade, disrupt, or deny service to others.
3. Do not exfiltrate, retain, or publish personal data or trade secrets.
4. Report privately and without undue delay, before public disclosure.
5. Allow 90 days for coordinated disclosure, unless we agree otherwise.
6. Do not use the vulnerability for extortion, advantage, or commercial exploitation.
7. Comply with applicable law.

If you are unsure whether your research falls inside this safe harbour, ask first.

## 5. Out of scope

The following are generally not treated as vulnerabilities:

- Missing security headers on documentation-only static pages.
- Reports from automated scanners without a demonstrated impact.
- Social engineering of maintainers.
- Denial of service by resource exhaustion on a public repository host.
- Issues in third-party dependencies that have no exploitable path here.
- The absence of a deployment gate — gates are optional under the framework.

## 6. Registry integrity incidents

A suspected tampering with the registry — a record that does not match its hash, a record that
vanished, a divergence between the canonical copy and a mirror — is a **critical** security
issue. Report it immediately. The Registry Custodian will:

1. freeze status changes;
2. compare against the Merkle roots and the escrow copy;
3. publish an incident notice within 72 hours;
4. restore and re-sign.

## 7. Key compromise

If an issuer's signing key is compromised:

1. Notify the Registry Custodian within 72 hours.
2. The Custodian publishes a key-revocation notice.
3. Records signed with the revoked key are re-verified with the issuer.
4. Records signed before the compromise remain valid, subject to issuer confirmation.

## 8. Disclosure policy

We follow coordinated disclosure:

- We publish advisories for confirmed vulnerabilities.
- We do not publish details before a fix is available, except where exploitation is active.
- We credit reporters who wish to be credited.
- We do not pay a bounty at this time. If that changes, it will be published here.

## 9. Contact

See [`GOVERNANCE.md#contact`](GOVERNANCE.md#contact). If the security contact is compromised or
unresponsive, escalate to the License Council's integrity contact.
