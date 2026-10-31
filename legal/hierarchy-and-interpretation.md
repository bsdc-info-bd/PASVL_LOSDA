# Hierarchy, Precedence, and Interpretation

This document explains how the instruments of the framework fit together and how they must be
read when they appear to conflict.

## 1. The precedence ladder

From strongest to weakest:

```
1. Mandatory law of the applicable jurisdiction
2. The signed LOSDA record (for that licensee, that Work, that term)
3. PASVL-1.0 (the license text)
4. The Author's NOTICE file
5. Repository documentation
6. Marketing material, badges, and summaries
```

### 1.1 Why mandatory law is first

No license can exclude rights that the law grants and does not allow to be waived. Examples
include, depending on the jurisdiction: consumer guarantees, statutory rights to decompile for
interoperability, exhaustion of distribution rights, fair use or fair dealing, and certain
moral rights. PASVL acknowledges this expressly in §28.7 and is drafted to continue working
even where part of it cannot take effect.

### 1.2 Why the LOSDA outranks the license for its licensee

The LOSDA is the Author's specific permission. A general rule yields to a specific grant. But
this cuts only one way: **a LOSDA can add permission; it cannot subtract rights that PASVL
grants to everyone.** A LOSDA that purports to forbid reading, auditing, or quoting the source
is ineffective to that extent, because those rights are granted by PASVL to the public and
cannot be withdrawn by an individual instrument.

### 1.3 Why the NOTICE outranks documentation

The NOTICE is the Author's formal statement to users. README files are documentation and are
frequently stale. Where a README says "MIT licensed" but the LICENSE and NOTICE say PASVL, the
LICENSE and NOTICE govern, and the Author should correct the README.

## 2. Interpretation rules

### 2.1 Purposive reading

The framework exists for two purposes that must both be preserved:

1. **Transparency** — the source is visible, auditable, teachable, and forkable by anyone.
2. **Permission-gated deployment** — running the software in the real world requires a grant.

Any interpretation that destroys either purpose is wrong. Reading a clause so broadly that it
forbids study breaks purpose 1. Reading it so narrowly that anyone may deploy breaks purpose 2.

### 2.2 No implied grants

There is no implied license, no license by estoppel, and no license by tolerated practice.
Silence, inaction, delay, or a friendly reply on a chat platform is not permission (PASVL
§5.2). Permission exists when it is written, signed, and registered (PASVL §10.4).

### 2.3 No implied conditions either

Correspondingly, conditions must also be express. A deployer is not in breach for failing to
comply with a practice that appears only in a tutorial or a blog post. Only the License, the
NOTICE, the LOSDA, and binding governance documents create obligations.

### 2.4 Contra proferentem, carefully

Ambiguity in a LOSDA is read against expansion of the licensee's scope, because the Author
reserved the right to decide the scope (PASVL §10.5, §28.2). Ambiguity in the License is read
to preserve the public visibility grant, because that grant is the framework's core promise to
society. Both rules point the same direction: **toward the public's right to see, and away
from unearned permission to run.**

### 2.5 Definitions control

Where a term is defined in PASVL Article 1, that definition applies throughout the framework
unless a document expressly says otherwise. A document that uses "deployment" loosely cannot
thereby enlarge the scope of a LOSDA.

### 2.6 Ejusdem generis and noscitur a sociis

Lists in the License are read in light of their class. "Hosting, serving, exposing over a
network, embedding, flashing" are all examples of putting software into operational use; the
list is not a closed catalog of every possible way to operate software, and a novel method of
operational use falls within **Deployment** if it serves the same function.

### 2.7 Expressio unius

A LOSDA that grants "deployment in the European Union for a customer-support product" does not
grant deployment in the United Kingdom, and does not grant deployment for a billing product.

### 2.8 Severability and the blue-pencil rule

If a provision is unenforceable, it is narrowed to the minimum extent necessary, not deleted
wholesale. If narrowing is impossible, the clause falls away and the rest of the License stands
(PASVL §25.1). The framework is designed so that the collapse of the deployment restriction in
one jurisdiction does not collapse the visibility grant anywhere.

### 2.9 Language

English is authoritative. Translations are aids. Where a translation is designated
authoritative for a jurisdiction by notice of the Steward, that designation must be published
in `translations/` with the date and scope of the designation (PASVL §28.4).

### 2.10 Headings and examples

Headings, tables, examples, and diagrams are aids. They do not create rights or obligations.
Where an example conflicts with text, the text prevails.

## 3. Relationship between the License and the LOSDA

| Question | Answered by |
|---|---|
| May I read the source? | License, Article 3 — always yes |
| May I fork it? | License, Article 3 — always yes |
| May I modify it privately? | License, Articles 3 and 6 — yes, for study and evaluation |
| May I run it in production? | LOSDA |
| May I run it for 30 days privately? | License, §6.3 |
| May I offer it as SaaS? | LOSDA, Class H |
| May I ship it in a device? | LOSDA, Class D |
| May I train a model on it? | LOSDA, Class M |
| What conditions apply to my deployment? | My LOSDA, plus the License |
| What happens if I breach? | Enforcement Policy + License Article 18 |
| Who decides disputes? | License Article 24 |

## 4. The three common misreadings

### 4.1 "Public repository means public license"

No. A public repository is a publication. Publication is not a license. PASVL is the license,
and it grants visibility, not deployment.

### 4.2 "The framework is just a proprietary license"

No. It is materially different from a proprietary end-user license in five ways: (a) the source
is public; (b) auditing and teaching are expressly permitted; (c) a broad set of no-fee
permissions exists for research, education, government, and public interest (Article 7,
Article 9); (d) revocation requires cause, notice, hearing, and a 180-day wind-down (Articles 18
and 19); and (e) the license cannot be tightened retroactively against releases you already
received (§19.5, §26.3).

### 4.3 "The framework is open source with extra steps"

No, and the framework forbids saying so (PASVL §28.5). It fails the Open Source Definition's
requirement that a license not restrict fields of use or require separate permission to
deploy. It is deliberately, honestly source-available.

## 5. Interpretation of gaps

Where the framework is silent, the following defaults apply, in order:

1. The purpose of the framework (Section 2.1 above).
2. The practice of the Steward, published in the Registry or a governance document.
3. The law governing the instrument (PASVL §24.1).
4. A written interpretation issued by the License Council, published in `governance/`.

Interpretations are prospective unless the Council states otherwise, and must be published
within thirty days of adoption.

## 6. Conflicts between documents: worked examples

| Conflict | Resolution |
|---|---|
| README says "MIT"; LICENSE and NOTICE say PASVL | PASVL governs; README must be fixed |
| LOSDA says "unlimited users"; Registry record says "500 users" | LOSDA letter and Registry must agree; pending correction, the narrower record limits reliance (§12.1) |
| NOTICE says "Mode U"; README says "try it free" | Mode U governs; no evaluation execution is permitted |
| Vendor tells you "it's fine, just deploy" | Not permission; only a signed, registered LOSDA is (§10.4) |
| Translation says deployment is allowed without a LOSDA; English says otherwise | English governs (§28.4) |

## 7. Amendment of this document

This document is interpretive guidance. It may be updated by the Steward with a `CHANGELOG.md`
entry. It cannot change the License; only the Amendment Process can do that.
