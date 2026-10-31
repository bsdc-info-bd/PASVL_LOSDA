# Anti-Patterns

Twenty-five ways to use this framework badly. Each one has been observed or is predictable, and
each one damages the credibility of every author who adopts the license honestly.

---

## Author anti-patterns

### 1. The stale README
Your README says MIT. Your LICENSE says PASVL. A deployer relies on the README and you enforce
against them. **This is the worst anti-pattern.** Readers trust the README more than the
LICENSE. Fix every mention, in every repository, in every package, at once.

### 2. The invisible license
PASVL in a `LICENSE` file, but no NOTICE, no header, no README statement. Users will assume it is
permissive. **Fix:** make deployment-permission unmistakable at every entry point.

### 3. The bait-and-switch
"MIT forever!" — then a sudden relicensing of existing releases. You cannot do this, and if you
try, you will lose the community and possibly the code. **Fix:** forward-only relicensing with
consent and grandfathering.

### 4. The surprise fee
A fee appears only after someone has deployed. **Fix:** publish the schedule, including "free"
for the classes you price at zero.

### 5. The black hole
Applications go unanswered for months. Silence is indistinguishable from refusal, and it pushes
people to deploy without permission. **Fix:** acknowledge in 3 days, decide in 20 for standard
classes.

### 6. The arbitrary refusal
"We don't like your company." **Fix:** use one of the ten grounds, state it, and offer an appeal.
Discriminatory refusal is prohibited.

### 7. The unrecorded grant
"I said yes on Twitter." **Fix:** sign a letter and record it. A permission that cannot be
verified is not a permission.

### 8. The moving goalposts
Scale limits, territories, and conditions change every renewal in ways not disclosed in advance.
**Fix:** publish the standard terms, and hold them for the term.

### 9. The one-person registry
One person holds the signing key, the registry, and the enforcement authority, with no backup.
**Fix:** deputy signatories, key rotation, and a succession plan.

### 10. The vendetta
Enforcement used against a critic, a competitor, or a former employee. **Fix:** enforcement is for
the license, reviewed by a second person, and appealable.

### 11. Overclaiming
"The most secure license in the world." "Nobody can use this without our permission." Both are
false — evaluation, academic, and public-interest rights exist, and enforcement is not absolute.
**Fix:** describe the license as source-available, permission-gated deployment.

### 12. Gating security patches
Charging for a fix to a vulnerability. **Fix:** never. It is indefensible and it is a
reputational disaster.

### 13. The license laundry
Putting PASVL code into an MIT project and calling the result MIT. **Fix:** keep the licenses
separate and the notices visible.

### 14. The empty no-fee class
Advertising an academic class that is refused in practice. **Fix:** if you publish a no-fee
class, honor it.

---

## Deployer anti-patterns

### 15. "It's on GitHub, so it's free"
The most common violation in the ecosystem. **Fix:** read the LICENSE before you build a business
on it.

### 16. Deploy first, license later
Launching and hoping. **Fix:** apply before launch; the process is faster than your release cycle.

### 17. Scope creep by inattention
A new product, a new country, a new subsidiary — and no amendment. **Fix:** make the LOSDA part
of the product-launch checklist.

### 18. The shell company shuffle
Splitting entities to stay under a scale limit. **Fix:** do not. It is a Violation under §11.6
and §13.1, and it is fraud-adjacent.

### 19. The silent acquisition
Buying a company that held a LOSDA and assuming the permission transferred. **Fix:** notify
within 30 days and obtain approval.

### 20. The attribution burial
A credits page three clicks deep, in 6pt grey text, no links. **Fix:** make attribution
genuinely accessible; condition C2 requires "reasonably accessible".

### 21. The model laundering
"An AI rewrote it, so it's a new work." **Fix:** it is not, and §13.11 and §14.4 prohibit it.

### 22. Ignoring an NNC
The fastest way to escalate from a conversation to a court case. **Fix:** acknowledge within 5
business days, even if you dispute the facts.

### 23. Concealment
Deleting the deployment, rewriting history, and denying it. **Fix:** self-report. Concealment
removes the cure right (PASVL §18.4).

---

## Community anti-patterns

### 24. Calling it open source
Repeated, casually, in issues, blog posts, and conference talks. It is not. **Fix:** say
source-available, and explain the trade honestly.

### 25. Refusing to engage with criticism
"Just fork it." Forking is allowed, but dismissal is not an argument. **Fix:** answer the hard
questions in the FAQ, and change the framework when the criticism is right.

---

## The meta-anti-pattern

**Adopting the framework without believing in it.** If you want an open license, use one. If you
want a proprietary license, use one. This framework only works if the author genuinely believes
that visibility should be universal and that deployment should be deliberate. Half-belief
produces the worst of both worlds: an unenforceable restriction and an untrustworthy promise.
