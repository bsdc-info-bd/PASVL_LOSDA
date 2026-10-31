# Frequently Asked Questions

Honest answers to the questions people actually ask, including the uncomfortable ones.

---

## The basics

### 1. What is PASVL?

A license that makes source code public and readable by everyone, while reserving the right to
**deploy** it to the author, who grants that right individually through a **Letter of Software
Deployment Approval (LOSDA)**.

### 2. Is this open source?

No. It is **source-available**. Under the Open Source Definition, a license must not restrict
fields of use or require separate permission to run the software. PASVL does both. Saying it is
open source is a misrepresentation and is prohibited by the license itself (§28.5).

### 3. Is it free software?

No, for the same reason. You are free to read and study it, but not to run it for any purpose
without permission.

### 4. Can I still call it "source available"?

Yes — that is the correct term.

### 5. What is a LOSDA?

A short, numbered, signed, publicly recorded permission. It says who may deploy, what they may
deploy, where, how much, for how long, and under what conditions. See
[`../legal/losda-specification.md`](../legal/losda-specification.md).

### 6. Why not just use a proprietary license?

Because with a proprietary license, you cannot read the code, cannot audit it, cannot fork it,
cannot teach with it, and cannot fix it yourself. PASVL keeps all of that and only gates
deployment.

### 7. Why not MIT or Apache-2.0?

Because those licenses give away the right to deploy commercially without asking. If you want
maximum adoption and do not need to fund the project from deployment, use them.

---

## Using the software

### 8. Can I read the source?

Yes. Always. Any purpose.

### 9. Can I fork it?

Yes. Keep the notices, and do not deploy from the fork without permission.

### 10. Can I use it in my class?

Yes, within Article 7. You may not run a course-wide service without a Class A LOSDA.

### 11. Can I use it in my research?

Yes, in a controlled research setting under Article 7. If you need a shared testbed, apply for
Class R, which is free.

### 12. Can I run it on my laptop to see if it works?

Yes, for up to 30 private, non-production days per year in Mode S. That is Evaluation Use.

### 13. Can I run it for my company's internal tool?

Not without a Class I LOSDA. Internal use is deployment.

### 14. Can I run it for my own small business?

Yes, with a LOSDA. Many authors price small businesses at zero, but the permission still exists.

### 15. Can I sell a product built on it?

With a LOSDA, yes. Without one, no.

### 16. Can I offer it as a SaaS?

With a Class H LOSDA, yes.

### 17. Can I ship it inside a device?

With a Class D LOSDA, yes.

### 18. Can I use it to train an AI model?

Only with a Class M LOSDA, or within the narrow research exception in Article 14.2.

### 19. Can I quote it in my book?

Yes, with attribution. Quoting source for commentary is permitted under Article 3.5.

### 20. Can I translate it?

Yes. A translation is a derivative work; it must keep the license and attribution, and deploying
the translation requires a LOSDA.

### 21. Can I use it in a hackathon?

Private and non-production: yes, within Evaluation Use. Public and serving real users: ask for a
free Class X extension — authors usually say yes.

### 22. Can I use it for disaster response?

Yes. Article 9.1 permits emergency use for up to 90 days with notice.

### 23. Can I use it for a non-profit?

Yes, usually free under Class P or A — but "non-profit" does not mean "no permission."

### 24. What if I only use it during the build, not at runtime?

A build-time tool that is not distributed or served is not deployed. If it produces artifacts
you distribute, the distribution question applies.

### 25. What if my users run it, not me?

If you distribute it, you need Class D. Your users need their own permission unless your LOSDA
expressly extends to them.

---

## The permission process

### 26. How do I get a LOSDA?

Fill in [`../templates/LOSDA-REQUEST.md`](../templates/LOSDA-REQUEST.md), send it to the address
in the work's `NOTICE`, and wait for a decision. Standard classes target 20 business days.

### 27. Does it cost money?

It depends on the author. Many offer free classes for academia, government, public interest, and
small organizations. Fees are published.

### 28. When can I start deploying?

Only when the Registry shows your LOSDA as `active`. A signed letter is not enough on its own.

### 29. What if the author never replies?

Silence is not permission. Escalate to the Steward if the author is unresponsive and the
deployment supports an essential service (Continuity LOSDA, Article 9.2).

### 30. Can the author refuse me?

Yes, but only on the ten grounds in the LOSDA specification, and with reasons. Refusal on
protected grounds is prohibited. Refusals are appealable.

### 31. Can the author revoke my permission?

Only for cause: breach, fraud, serious harm, non-payment, a legal requirement, or persistent
misconduct. With notice, a hearing, and (usually) a 180-day wind-down.

### 32. What if the author is acquired or disappears?

The successor must assume the author's obligations (§25.4). If the author disappears, a
Continuity LOSDA is available for essential services.

### 33. Is my LOSDA transferable?

Only with the author's written approval, recorded in the Registry. In M&A, negotiate an
assignment right up front.

### 34. Can I sublicense?

Only if the LOSDA expressly says so. "We'll let our customers use it" is sublicensing.

---

## Enforcement and disputes

### 35. What happens if I deploy without permission?

You are in breach. The author will usually start with a friendly message, then a formal notice
with a cure period. You can usually regularize with a retroactive LOSDA.

### 36. Will I be sued immediately?

No. The Enforcement Policy requires cure before escalation, and proportionality. Only serious,
deliberate, or concealed breaches escalate quickly.

### 37. What if I made an honest mistake?

Cure within 30 days of notice, and a first-time good-faith non-commercial breach results in
automatic reinstatement (§18.12).

### 38. How does the author detect violations?

Public sources, reports, and voluntary disclosure. Some works include a deployment gate.
Surveillance of private systems is not a detection method.

### 39. Can I appeal?

Yes — refusals, suspensions, revocations, and sanctions are all appealable once, within 20
business days, free of charge.

### 40. Is the enforcement register public?

Yes, from Stage 2 upwards, redacted for personal data.

---

## Legal and practical objections

### 41. Is this enforceable?

It depends on the jurisdiction, how clearly the restriction is communicated, and how the work is
distributed. In many jurisdictions a condition limiting the scope of a copyright license is
enforceable as a condition; in others it is a contractual promise. The license is drafted to
survive partial unenforceability: the visibility grant and attribution duties remain even if the
deployment restriction fails in one place. See
[`../legal/jurisdiction-matrix.md`](../legal/jurisdiction-matrix.md).

### 42. Doesn't public availability imply permission?

No. Publication is not a license. The license is the license.

### 43. What about GitHub's terms — doesn't forking give me rights?

GitHub's terms let you view and fork public repositories within the platform. They do not grant
a deployment license, and PASVL expressly permits forking so there is no conflict. See
[`../legal/platform-reality.md`](../legal/platform-reality.md).

### 44. Can't I just clone it and run it anyway?

Technically, yes — as with any license. Legally, that is the breach. PASVL's contribution is to
make the rules clear and the permission routine, so that most people comply because it is easy
and fair, not because they are forced to.

### 45. Isn't this just a proprietary license with extra steps?

It is materially different: the source is public, auditing and teaching are expressly permitted,
there are broad no-fee classes, revocation requires cause and a wind-down, and rights cannot be
tightened retroactively. But yes, it reserves deployment — that is its purpose.

### 46. Won't this kill adoption?

It will reduce adoption among organizations that cannot accept a gated deployment. It may
increase adoption among organizations that want to audit their suppliers and are willing to pay
for a clear permission. Whether that trade is right depends on the project.

### 47. What about the "Open Source Definition"? Isn't gating deployment ethically wrong?

Some in the community believe all software should be freely runnable. That is a legitimate
position. PASVL is for authors who disagree, and who want to publish anyway. The framework does
not claim the moral high ground of open source; it claims honesty about its terms.

### 48. Is a deployment gate (technical enforcement) required?

No. Gates are optional. Many authors rely on the law and on goodwill. Gates must be disclosed,
must be disableable for accessibility and testing, and must not be circumvented
(PASVL §13.7).

### 49. What about privacy?

The Registry publishes limited, minimized data; anonymized listing is available; the privacy
policy sets retention limits. See [`../legal/privacy-policy.md`](../legal/privacy-policy.md).

### 50. What about sanctions and export control?

Compliance is required (Article 22). Issuers screen applicants. See
[`../legal/sanctions-and-export.md`](../legal/sanctions-and-export.md).

---

## For authors

### 51. How do I adopt it?

Follow [`quickstart.md`](quickstart.md) and
[`../templates/ADOPTION-CHECKLIST.md`](../templates/ADOPTION-CHECKLIST.md).

### 52. Do I have to charge?

No. You can set every fee to zero and still keep the permission process, the registry, and the
control.

### 53. Do I have to run a registry?

For your own works, a JSON file in your repository in the documented format is enough. The public
Registry is for works that want to be discoverable and verifiable globally.

### 54. Can I change the license later?

For future versions, yes. You cannot withdraw rights already granted for published versions
(§19.5), and a major restriction requires the Amendment Process if you are using the framework's
stewardship.

### 55. What if a contributor refuses to agree?

Then their code cannot be relicensed. Keep it under the old license in a separate module, or
remove it.

### 56. What happens if I stop maintaining the project?

Existing LOSDAs remain valid for their term. Publish a succession plan so your users can get a
Continuity LOSDA if you disappear.

### 57. Can I use the BSDC name or logo?

Only as permitted by [`../TRADEMARK.md`](../TRADEMARK.md). Nominative use is fine; endorsement is
not.

---

## Meta

### 58. Who wrote this?

The Bangladesh Software Development Community (BSD C) stewards the framework. The license was
drafted for international use, with Bangladesh as the default governing law, and is published
openly for review and amendment.

### 59. Can I suggest changes?

Yes. Open an RFC in [`../rfcs/`](../rfcs/). Major changes require a 45-day comment period and a
two-thirds vote.

### 60. Is this legal advice?

No. Nothing in this repository is legal advice. If you are deploying commercially at scale, get
your own lawyer.

### 61. What if I think the whole idea is wrong?

Say so publicly, with reasons — that is exactly the kind of criticism the framework should
survive. If your objection is that all software should be freely deployable, the framework
respectfully disagrees, and it will not pretend otherwise.

### 62. Where do I start?

- Author: [`for-authors.md`](for-authors.md)
- Deployer: [`for-deployers.md`](for-deployers.md)
- Contributor: [`for-contributors.md`](for-contributors.md)
- Skeptic: [`why-this-exists.md`](why-this-exists.md) and
  [`../legal/plain-language.md`](../legal/plain-language.md)
