# Platform Reality: What PASVL Can and Cannot Do on GitHub

This document is written for authors considering adoption of PASVL and for deployers who want
to understand exactly what the license can and cannot enforce. It is deliberately candid.
A framework that oversells its powers is a framework that will disappoint the people who rely
on it.

## 1. The short version

A license is a legal instrument. GitHub is a hosting platform governed by a separate contract.
A license can define rights and obligations under copyright law. It cannot change how GitHub's
software behaves, cannot force a fork to be taken down, and cannot prevent all copying.

What PASVL **can** do:

- establish, in clear writing, what permission the Author grants and what it withholds;
- create a legally recognisable permission instrument (the LOSDA) with identity, scope, term,
  and evidence;
- satisfy the notice requirements that copyright enforcement depends on;
- give a court or a platform a clear statement of the rules the parties agreed to;
- support takedown requests, package-registry complaints, and app-store complaints with
  evidence;
- create a durable public record that makes "I didn't know" a weak defense;
- support a professional, non-hostile permission culture around deployment.

What PASVL **cannot** do:

- prevent someone from cloning a public repository;
- prevent a static mirror, a Telegram channel, or a torrent of the source;
- prevent someone from reading and re-implementing ideas (copyright protects expression, not
  ideas, in most jurisdictions);
- guarantee that a deployment restriction is enforceable in every country;
- automatically detect unlicensed deployment;
- override GitHub's Terms of Service, Community Guidelines, or DMCA process;
- convert public visibility into a technical protection measure.

**The honest position:** PASVL is a *legal and social* framework, not a technical one. Its
strength is clarity, record-keeping, and the willingness of the author to enforce. Its limits
are the limits of copyright, contract, and platform policy.

## 2. GitHub's Terms of Service and public repositories

When you make a repository public on GitHub, you grant GitHub a license to host, display, and
distribute it, and you grant **other GitHub users** certain rights under GitHub's Terms of
Service — principally the right to view and to fork the repository within GitHub.

This creates two important consequences:

### 2.1 Viewing and forking are unavoidable

PASVL therefore **expressly permits** viewing and forking (Article 3), so that the license and
the platform are not in conflict. A license that purported to forbid forking on GitHub would
create a contradiction that the platform, not the author, would resolve.

### 2.2 Forking is not deploying

A fork on GitHub is a copy of a repository inside GitHub's system. It is not a deployment.
PASVL treats forks as permitted study artifacts (Article 3.3) and separately prohibits using a
fork to deploy outside a LOSDA (Article 13.4). The two propositions are consistent.

The Author should read GitHub's current Terms of Service, Acceptable Use Policies, and DMCA
policy before adopting PASVL. This document summarizes them as of the framework's publication
date and does not replace them.

## 3. Repository mechanics that matter legally

| Mechanic | Legal significance | PASVL approach |
|---|---|---|
| `LICENSE` file | The license text GitHub displays | Contains PASVL in full |
| GitHub license detection | GitHub matches known licenses against its list | PASVL will show as "View license" or "Unknown" — this is expected; PASVL is not OSI-approved and does not claim to be |
| `NOTICE` file | Additional terms and attribution | Required by PASVL Appendix B |
| `README.md` badge | Communication to users | Use the official PASVL badges in `assets/` |
| Forks | Copies under platform terms | Permitted; deployment prohibited without a LOSDA |
| Releases (binaries) | Distribution of executable form | Requires a LOSDA Class D, or an express release permission |
| GitHub Actions artifacts | Built binaries | Same as releases |
| GitHub Pages | Hosted content | Hosting documentation is not deployment of software; hosting a running instance is |
| Packages (GHCR, npm, PyPI) | Distribution | A published package is still governed by PASVL; a LOSDA is required to deploy it |
| Copilot / code search | Indexing and suggestion | GitHub's own terms govern ingestion; PASVL Article 14 governs a user's deliberate ML use |
| Dependabot, code scanning | Automated analysis | Consistent with the audit right; not deployment |

## 4. What a deployer might try, and why it fails

| Attempted workaround | Why it does not work |
|---|---|
| "I cloned it, so I own this copy" | Cloning is permitted; deployment is not. Owning a copy is not owning a license. |
| "I forked it and changed the license" | You cannot relicense someone else's code (Article 4.4). The fork remains bound. |
| "I'll deploy from a fork" | Forks are for study and contribution. Deploying from one is a Violation (13.4). |
| "It's an internal tool, not a product" | Internal production use is a Deployment. Class I exists for it. |
| "Only my team uses it" | Seats count as users. Internal use still needs a LOSDA unless within Evaluation Use. |
| "I put it in a Docker image" | Containerization does not change the license. Distribution or hosting still requires a LOSDA. |
| "I used an AI to rewrite it" | Model laundering is prohibited (13.11, 14.4). |
| "The author hasn't complained" | Non-enforcement is not permission (§5.2). |
| "There was no click-through" | The license applies by the act of use; the repository carries the notice. |
| "The repo says MIT in the README" | The LICENSE file and NOTICE govern; report the discrepancy to the Author. |

## 5. Taking something down: the realistic routes

Where a deployment is unlicensed, the Author's realistic escalation path is:

1. **Contact the deployer.** Most unlicensed deployments are careless, not malicious, and are
   resolved by a letter and a payment.
2. **Use the framework.** Issue an NNC under `legal/enforcement-policy.md`, offer a cure
   period, and — where appropriate — offer a retroactive LOSDA to regularize the use.
3. **Platform reports.** For hosted code that infringes: a DMCA notice to the host, if the
   material is genuinely infringing and the requirements are met. For GitHub specifically, the
   DMCA Takedown Policy and the Copyright Claims Process apply. A license-violation report that
   is not a copyright claim may be handled under GitHub's other policies instead.
4. **Package registries.** npm, PyPI, NuGet, Maven Central, and app stores have their own
   complaint processes. Each requires the complainant to identify the rightsholder and the
   infringing material.
5. **Legal action.** Infringement claims, breach-of-license claims, or both, depending on the
   jurisdiction. Note the important split: in some jurisdictions a license breach sounds in
   contract; in others it is treated as infringement because the license condition delimits the
   scope of the grant.

**Reality check:** DMCA is a United States process. Deployers outside the United States, and
hosts outside the United States, are governed by local copyright law. PASVL does not promise a
fast takedown. It promises a documented, defensible record.

## 6. The GitHub license-detection problem

GitHub's license picker lists only OSI-approved and a small set of other licenses. PASVL is
not on that list. Consequences:

- The repository sidebar will typically show **"View license"** or **"Unknown license"**
  rather than a badge with the PASVL name.
- Package manifests that validate against an SPDX list will not accept `PASVL-1.0`. Use
  `LicenseRef-PASVL-1.0` where the manifest supports custom references, and a comment
  otherwise (Appendix B.3).
- Some tools will warn or fail on an unrecognized license. That warning is expected and is not
  a defect.

**Do not attempt to smuggle PASVL in under a known identifier.** Do not set a manifest to
`MIT` or `Apache-2.0` to silence a warning. Misrepresenting the license is itself a Violation
(Article 4.3) and destroys the credibility of the framework.

## 7. What adopters should do to make the framework work

1. Put the full license in `LICENSE`.
2. Put the NOTICE in `NOTICE` and repeat the essential terms in the README, in plain language.
3. Add license headers to source files (Appendix B.1) and enforce them in CI.
4. Add a `CONTRIBUTING.md` that requires DCO sign-off and states the inbound license.
5. Add `SECURITY.md` with a private reporting channel.
6. Publish a clear "How to get a LOSDA" section with response targets.
7. Register the Work in `registry/works.json` so the public can find its licensing status.
8. Keep the Registry honest: when a LOSDA is granted, record it; when it ends, record that too.

## 8. What the framework should never claim publicly

Authors who adopt PASVL must never claim that:

- the software is "unusable without permission" in a technical sense;
- the license "prevents copying";
- the license is "approved" or "certified" by any authority;
- the license is open source, free software, or OSI-approved;
- a LOSDA is "legally required worldwide" without qualification;
- the framework guarantees compliance or enforcement.

Overclaiming is a governance offense under the framework's own marketing rules
(`governance/CHARTER.md`, Section 7) because it damages the credibility of every author who
relies on the framework.

## 9. Related reading

- [`hierarchy-and-interpretation.md`](hierarchy-and-interpretation.md)
- [`../docs/faq.md`](../docs/faq.md)
- [`../governance/CHARTER.md`](../governance/CHARTER.md)
- GitHub Terms of Service: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- GitHub DMCA Takedown Policy: https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy
- Open Source Definition: https://opensource.org/osd

---

*Last reviewed: 2026-01-01. Platform terms change; re-review annually.*
