# Deployer Compliance Checklist

Print this. Work through it before every launch, and review it annually.

---

## Pre-deployment

### License discovery

- [ ] I have read the work's `LICENSE` and `NOTICE` in full.
- [ ] I know the license version that applies (PASVL-1.0).
- [ ] I know the Mode (S or U).
- [ ] I know whether the Ethics Policy is incorporated.
- [ ] I know who the issuer is and how to contact them.
- [ ] I know whether the work is dual-licensed.
- [ ] I have checked the dependency tree for incompatible licenses.

### Classification

- [ ] I have classified the deployment (I, S, H, D, M, A, G, P, R, X, or C).
- [ ] I have checked it against the examples in `docs/deployment-scopes.md`.
- [ ] I have confirmed that it is not within a no-LOSDA exception (Articles 3, 7, 8, 9).
- [ ] I have identified every Affiliate that will deploy.
- [ ] I have identified every contractor or agency that will deploy on my behalf.

### Application

- [ ] The application is complete, specific, and signed.
- [ ] Scale includes 24 months of headroom.
- [ ] The field of use describes the actual product, not a euphemism.
- [ ] Data and security sections are accurate.
- [ ] The compliance declarations are true.

### Permission

- [ ] I have a signed LOSDA.
- [ ] The Registry shows the LOSDA as `active`.
- [ ] The record hash on the letter matches the Registry.
- [ ] The scope covers the territory, field of use, and scale I need.
- [ ] The term covers my intended deployment period, with renewal time built in.
- [ ] I have stored the signed letter where my legal and audit teams can find it.

---

## Technical compliance

### Notices

- [ ] The `LICENSE` file is retained in the source tree I deploy.
- [ ] The `NOTICE` file is retained.
- [ ] Copyright headers are not removed from any file.
- [ ] Shipped artifacts include the license and notice files.
- [ ] Container images carry the correct license label.

### Attribution

- [ ] A "Third-party licenses" or "Credits" page exists in the product.
- [ ] It names the work, the author, and the license.
- [ ] It links to the canonical repository.
- [ ] It links to or reproduces the license text.
- [ ] Users can reach it within two clicks from the main interface.

### Scope controls

- [ ] A one-page record of the permitted scope exists and is current.
- [ ] Product launches are checked against the field of use.
- [ ] Territory controls exist (if the LOSDA limits territory).
- [ ] Scale monitoring exists and alerts before the limit is reached.
- [ ] New Affiliates trigger an amendment request.

### Security

- [ ] The issuer's security contact is in the incident runbook.
- [ ] The 72-hour incident notification (C6) is implemented.
- [ ] Sub-processors are disclosed where required (C13).
- [ ] The deployment's own security measures are documented.

### Data protection

- [ ] A DPIA or equivalent has been completed if personal data is processed.
- [ ] A DPA is in place where required.
- [ ] Retention and minimization are implemented.
- [ ] Cross-border transfers have a lawful basis.

---

## Operational compliance

- [ ] The Registry contact details are current (C7).
- [ ] The licensing mailbox is monitored.
- [ ] Records sufficient to demonstrate compliance are retained for 3 years (C8).
- [ ] The renewal date is in the calendar at 90/60/30 days.
- [ ] The LOSDA ID is recorded in the software inventory or SBOM.
- [ ] The LOSDA ID is included in any internal compliance register.
- [ ] Annual scale reporting is scheduled (C4, where applicable).
- [ ] Annual compliance attestation is scheduled (C15, where applicable).

---

## Change triggers: re-check the license if…

- [ ] You launch a new product.
- [ ] You enter a new country.
- [ ] You exceed a scale threshold.
- [ ] You acquire or merge with another company.
- [ ] You change hosting region.
- [ ] You begin distributing binaries.
- [ ] You begin offering a hosted service.
- [ ] You start training a model.
- [ ] You rebrand.
- [ ] The author releases a new major version.
- [ ] The author changes the license for future versions.
- [ ] Your LOSDA is amended, suspended, or expires.

---

## Incident response: unlicensed deployment discovered

- [ ] Stop the unlicensed deployment or reduce it to Evaluation Use immediately.
- [ ] Notify your legal team.
- [ ] Apply for a retroactive LOSDA with a regularization fee.
- [ ] Preserve records: deployment start date, scale, and what was processed.
- [ ] Do not conceal; concealment turns a curable breach into a non-curable one.
- [ ] Record the lesson in your license-review process.

---

## Incident response: Notice of Non-Compliance received

- [ ] Acknowledge receipt within 5 business days.
- [ ] Read the notice in full, including the cure requirements.
- [ ] Cure what can be cured immediately.
- [ ] Request an extension if needed (up to 30 days on reasonable grounds).
- [ ] Gather evidence if the facts are disputed.
- [ ] Reply in writing by the deadline.
- [ ] Escalate to legal if the matter is not resolved within the cure period.
- [ ] Consider an appeal within 20 business days of any final decision.

---

## Annual review

- [ ] All LOSDAs reviewed and renewed as needed.
- [ ] Scope records updated.
- [ ] Attribution pages checked for accuracy.
- [ ] Dependency licenses re-scanned.
- [ ] Incident runbook contacts updated.
- [ ] Training for engineering on license obligations.
- [ ] Report to management on compliance status.

---

*Based on PASVL-1.0 and the LOSDA specification §10. Version 1.0.*
