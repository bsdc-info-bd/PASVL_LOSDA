# Adoption Checklist for Authors

Work through this list before you announce that your project uses PASVL-1.0. Most enforcement
problems begin with an adoption that was rushed.

## 1. Before you publish

- [ ] You own, or have authority to license, **all** of the code you are publishing.
- [ ] Every contributor has signed off under the DCO or a written inbound license.
- [ ] Third-party components are compatible with PASVL (see `legal/compatibility.md`).
- [ ] No component is under GPL, AGPL, or another license incompatible with PASVL.
- [ ] No component is under an exclusive grant to someone else.
- [ ] You have checked whether your employer, university, or funder has rights in the work.
- [ ] Your funding agreement does not require an open license.
- [ ] You have decided your Mode (S or U).
- [ ] You have decided whether to incorporate the Ethics Policy.
- [ ] You have decided your LOSDA classes and fees (which may be "none").

## 2. Files to add

- [ ] `LICENSE` — the full PASVL-1.0 text, unmodified.
- [ ] `NOTICE` — filled from `templates/NOTICE-TEMPLATE`.
- [ ] `README.md` — a plain-language "Can I use this?" section with a link to the LOSDA process.
- [ ] `CONTRIBUTING.md` — DCO, inbound license statement, review process.
- [ ] `CODE_OF_CONDUCT.md` — adopted from the framework or an equivalent.
- [ ] `SECURITY.md` — private reporting channel.
- [ ] `THIRD-PARTY-NOTICES.md` — component licenses.
- [ ] `TRADEMARK.md` — or a link to the framework's policy.
- [ ] `LICENSING.md` — classes, fees, response targets, contact.

## 3. Source and build hygiene

- [ ] License header on every source file (see `templates/LICENSE-HEADER.txt`).
- [ ] Header check in CI (see `scripts/check_license_headers.py`).
- [ ] `SPDX-License-Identifier: LicenseRef-PASVL-1.0` in file headers.
- [ ] Package manifest points to `LICENSE` rather than to a false SPDX identifier.
- [ ] Container images carry `org.opencontainers.image.licenses=LicenseRef-PASVL-1.0`.
- [ ] Release artifacts include the `LICENSE` and `NOTICE`.

## 4. Display and communication

- [ ] README badge from `assets/` displayed.
- [ ] A short "Deployment requires a LOSDA" statement near the download instructions.
- [ ] The repository's "About" description does not say "open source".
- [ ] The website does not say "free to use" if deployment requires permission.
- [ ] A pricing or licensing page exists, even if every fee is zero.
- [ ] The licensing contact is monitored.

## 5. Registry

- [ ] The work is added to `registry/works.json` (or your own register) with its repository URL.
- [ ] You have an issuer code, if you intend to issue LOSDAs.
- [ ] You have read `governance/REGISTRY-POLICY.md`.
- [ ] You know where LOSDAs will be recorded, and who will record them.

## 6. Operations

- [ ] You have a template response for licensing requests.
- [ ] You have a target of 20 business days for standard classes.
- [ ] You have a process for refusals (reasoned, appealable).
- [ ] You have a process for violations (see `legal/enforcement-policy.md`).
- [ ] You have decided whether to offer a retroactive LOSDA for accidental deployment.
- [ ] You have documented how a licensee verifies its status.

## 7. Governance

- [ ] You have read the transparency requirements and will report annually.
- [ ] You have decided who signs LOSDAs, and how signatures are secured.
- [ ] You have a backup signatory and a key-revocation plan.
- [ ] You have a succession plan for your own project (who issues if you disappear).

## 8. Legal review

- [ ] You have read `legal/plain-language.md` and `legal/platform-reality.md`.
- [ ] You have read `legal/jurisdiction-matrix.md` and know your main markets.
- [ ] For high-value commercial works, you have taken local legal advice.
- [ ] You understand that PASVL is not OSI-approved and will not claim otherwise.

## 9. Announcement

- [ ] The announcement explains the model honestly.
- [ ] The announcement links to the license, the LOSDA process, and the FAQ.
- [ ] The announcement invites questions, and you have an answer for the obvious ones.
- [ ] Existing users are told what changes and given a transition period if they were previously
  on another license.

## 10. After launch

- [ ] Review the README again after 30 days against actual user questions.
- [ ] Publish a first licensing decision (even a refusal) to show the process works.
- [ ] Join the annual transparency reporting cycle.
