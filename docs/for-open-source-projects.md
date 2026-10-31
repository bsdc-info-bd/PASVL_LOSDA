# For Open-Source Projects

Many projects arrive at PASVL after years under a permissive license. This guide is about
migrating responsibly — and about when not to migrate at all.

---

## 1. The hard truth first

If your project has already been released under MIT, Apache-2.0, BSD, or another permissive
license, **you cannot revoke that license for the versions already released.** Those versions
remain available under their original terms forever. What you can do is license **future
versions** under PASVL.

That is legitimate, and many projects do it, but it requires honesty:

- Do not pretend the old versions are gone.
- Do not claim that "the project is no longer open source" — say "future versions are
  source-available under PASVL."
- Expect a fork of your last open version to continue. That is not betrayal; it is how open
  source works.

## 2. Can you even do it?

You need the agreement of the copyright holders — in practice, all contributors whose code
remains in the project. Check:

| Situation | Can you relicense future versions? |
|---|---|
| You are the sole copyright holder | ✅ Yes |
| You have a CLA assigning rights to you or a foundation | ✅ Yes, per the CLA |
| You have DCO sign-offs only | ✅ For your own code; ⚠️ for others' code, the DCO grants a license to the project but does not transfer ownership — relicensing a combined work is legally risky |
| Contributors hold copyright and there is no CLA | ⚠️ You need permission from each, or you must remove their code |
| Your project is under a foundation's stewardship | ✅ Only with the foundation's approval |

**If you have any doubt, do not relicense.** Get legal advice. A defective relicensing
poisons the project for everyone.

## 3. What your contributors agreed to

The DCO (Developer Certificate of Origin 1.1) certifies that the contributor has the right to
submit the code under the project's existing license. It does **not** grant a right to change
that license. Unless you have a CLA with a relicensing right, you must ask.

### 3.1 Asking contributors

A good request looks like this:

> We are proposing to license version 5.0 and later under PASVL-1.0. Versions up to 4.x will
> remain available under Apache-2.0 permanently. PASVL keeps the source public and requires a
> free, recorded permission for deployment. We are asking for your consent to relicense your
> contributions in future versions. You can decline, and we will keep your code under
> Apache-2.0 in a separate module.

Record every consent. Silence is not consent.

## 4. The migration options

| Option | What happens | Best for |
|---|---|---|
| **A. Forward-only relicensing** | Old versions stay open; new versions are PASVL | Projects with a CLA or a single owner |
| **B. Dual licensing** | Public PASVL + commercial license for large deployers | Commercial open-core projects |
| **C. Split license** | Core under PASVL; SDK and client libraries under Apache-2.0 | Platforms that want wide client adoption |
| **D. Stay open** | Keep Apache-2.0/MIT; monetize support or hosting | Projects whose value is in operations |
| **E. Open core** | Open core; PASVL for a commercial module | Vendors with a proprietary product |

Option **C** is often the best compromise: a permissive SDK makes adoption easy, while the
server component is permission-gated.

## 5. The migration checklist

- [ ] Identify every copyright holder.
- [ ] Review CLAs and DCO records.
- [ ] Decide the scope of the change: which directories, which versions.
- [ ] Contact contributors and record consents.
- [ ] Check dependencies for incompatible licenses.
- [ ] Check funder and employer obligations.
- [ ] Decide whether to keep the old license for a `legacy/` branch.
- [ ] Update `LICENSE`, `NOTICE`, `README`, and package manifests.
- [ ] Update source headers.
- [ ] Update the website and any marketplace listing.
- [ ] Announce with a clear explanation and a FAQ.
- [ ] Open a discussion and answer objections honestly.
- [ ] Set a transition date for any existing commercial users.
- [ ] Publish the first version under the new license.
- [ ] Register the work and start the LOSDA process.

## 6. The announcement

A good announcement answers, in this order:

1. **What is changing** — "From version 5.0, future releases will be licensed under PASVL-1.0."
2. **What is not changing** — "Versions up to 4.x remain under Apache-2.0 forever."
3. **Why** — "The project needs sustainable funding; deployment permission is the part of the
   value we can charge for, while keeping the code public."
4. **What you can still do** — reading, auditing, forking, contributing, teaching, research.
5. **What now needs permission** — production deployment, hosted services, embedded distribution.
6. **How to get permission** — the process, the classes, the fees, the response time.
7. **What happens to existing users** — the transition period and any grandfathering.
8. **Where to ask questions** — a discussion thread, and a named person.

A bad announcement is a surprise. A good one is a conversation you started.

## 7. Managing the reaction

Expect:

- **"This is a rug-pull."** Answer with the forward-only commitment and the grandfathered
  versions.
- **"This isn't open source."** Agree. Say "source-available" and explain the trade.
- **"We'll fork it."** That is allowed and expected. Compete on quality, not on resentment.
- **"Our company policy forbids this."** Offer a no-fee class or a permissive SDK.
- **"You're betraying the community."** Engage, do not lecture. Publish the numbers if you can:
  how much the project costs, and how the license funds it.

## 8. Keeping the project healthy

1. **Keep the client libraries permissive.** Adoption suffers when integration is gated.
2. **Never gate security patches.** Anyone affected should get the fix.
3. **Keep a free tier.** Small teams should not need a lawyer.
4. **Publish the fee schedule.** No private pricing games.
5. **Answer licensing requests quickly.** Slow licensing is indistinguishable from refusal.
6. **Do not tighten retroactively.** Every future change that restricts rights must be
   prospective.
7. **Preserve the community.** The people who contribute under PASVL must feel that their work
   is valued and that the terms are stable.

## 9. What not to do

- Do not relicense contributions without consent.
- Do not claim old versions are withdrawn.
- Do not describe the project as open source in your README, your package metadata, or your
  conference talks.
- Do not use the license as a weapon against a competitor; use it as a permission system.
- Do not make the free tiers so narrow that they are a marketing lie.

## 10. Is this still open source? A fair answer

No. It is source-available. It grants more than a proprietary license (reading, auditing,
forking, teaching, contributing) and less than an open-source license (free deployment). It is
honest about the difference, and that honesty is the point.

If your community's core value is "anyone may run this for any purpose," PASVL is the wrong
license and you should not adopt it. If your community's core value is "the code is public and
the project is sustainable," PASVL is a defensible answer.
