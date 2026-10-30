# Jurisdiction Matrix

**Version:** 1.0 · **Status:** Informational, not legal advice

Licences are drafted internationally but interpreted locally. This document records what the
framework's drafters understand about key jurisdictions and, just as importantly, records what
is unknown. It is maintained so that authors and deployers can see the assumptions behind the
drafting.

## 1. How to read this document

- **Enforceability of deployment restriction**: whether a condition limiting deployment is
  likely to be treated as a condition of the copyright licence (infringement if breached) or as
  a contractual promise (breach if broken).
- **Moral rights**: whether the author has rights that cannot be waived.
- **Interoperability / reverse engineering**: statutory rights that cannot be excluded.
- **Unknown**: the question has not been tested.

No entry in this table is a legal opinion. Every entry should be verified by local counsel
before it is relied on in a dispute.

## 2. Matrix

| Jurisdiction | Deployment restriction | Contract basis | Moral rights | Interoperability carve-out | Overall confidence |
|---|---|---|---|---|---|
| **Bangladesh** (home jurisdiction) | Likely enforceable as a contractual condition; copyright remedies available | Contract Act 1872; Copyright Act 2000 | Yes — attribution and integrity | Limited | Medium |
| **India** | Enforceable; courts have treated licence conditions seriously | Indian Contract Act; Copyright Act 1957 | Yes | Limited | Medium |
| **United States** | Likely enforceable; licence conditions delimiting scope are usually treated as copyright conditions | State contract law; Copyright Act | Limited (VARA for visual art) | Fair use; §1201(f) interoperability | Medium–High |
| **United Kingdom** | Enforceable as a licence condition; damages and injunction available | Contract; CDPA 1988 | Yes — attribution, integrity; not waivable | Limited | Medium–High |
| **European Union** | Enforceable, subject to consumer and competition rules; software directive allows decompilation for interoperability | National contract law; InfoSoc Directive; Software Directive 2009/24/EC | Varies by member state | Decompilation for interoperability | Medium |
| **Germany** | Enforceable; careful drafting of AGB (standard terms) required | BGB §§305 ff. | Strong moral rights | §69d UrhG decompilation | Medium |
| **France** | Enforceable, but moral rights are strong and partially unwaivable | Code de la propriété intellectuelle | Strong | Limited | Medium |
| **Japan** | Enforceable as a licence condition | Civil Code; Copyright Act | Attribution, integrity | Program analysis for interoperability | Medium |
| **South Korea** | Enforceable | Civil Act; Copyright Act | Attribution, integrity | Interoperability exception | Medium |
| **China** | Enforceable in principle; enforcement practice varies | Civil Code; Copyright Law | Yes | Limited | Low–Medium |
| **Brazil** | Enforceable | Civil Code; Software Law 9.609/98 | Yes | Limited | Medium |
| **Canada** | Enforceable | Provincial contract law; Copyright Act | Yes | Interoperability exception in some contexts | Medium |
| **Australia** | Enforceable | Contract; Copyright Act 1968 | Yes | Reverse engineering for interoperability (limited) | Medium |
| **Nigeria** | Enforceable in principle; case law limited | Contract; Copyright Act | Yes | Limited | Low |
| **UAE** | Enforceable; Federal Decree-Law No. 38 of 2021 on copyright | Contract; civil code | Yes | Limited | Low–Medium |
| **Saudi Arabia** | Enforceable in principle | Contract; copyright regulations | Yes | Limited | Low |
| **Singapore** | Enforceable | Contract; Copyright Act 2021 | Yes | Limited | Medium–High |

## 3. Cross-cutting issues

### 3.1 Standard-form terms

In the EU, Germany, France, and several other civil-law jurisdictions, terms presented on a
take-it-or-leave-it basis are subject to fairness review. Clauses that are surprising,
disproportionate, or unclear may be struck down. The framework mitigates this by:

- publishing the terms prominently and in plain language;
- keeping the core restriction simple and central to the bargain;
- providing a wind-down period;
- avoiding penalties and forfeitures;
- providing an appeals process.

### 3.2 Consumer rules

A consumer deploying software for personal use may have rights that cannot be waived. PASVL does
not require consumers to obtain a LOSDA for personal, private, non-commercial use within
Evaluation Use, and it preserves statutory consumer rights expressly (§21.6). Where a consumer
is entitled by law to use software for personal purposes, that law prevails over the licence.

### 3.3 Competition law

A refusal to license, an exclusive grant, or a discriminatory licensing practice could raise
competition-law issues in some markets, particularly where the Work is a de facto standard or
where the Author has market power. The framework mitigates by:

- non-exclusivity by default (§10.6);
- published, non-discriminatory classes and fees;
- an appeal process;
- a prohibition on discriminatory refusal (Ethics Policy, Section 5).

Authors with substantial market power should obtain competition-law advice before adopting an
exclusive or highly restrictive licensing model.

### 3.4 Exhaustion and first sale

Where a physical device containing the Work is sold, the rights holder's distribution right may
be exhausted, depending on the jurisdiction. A LOSDA cannot override statutory exhaustion of
distribution rights in a lawfully sold copy. The framework's restrictions focus on the right to
run and serve, not on the right to resell a lawfully purchased device.

### 3.5 Moral rights

In jurisdictions with strong moral rights (France being the clearest example), an author may not
be able to waive attribution or integrity rights. The framework preserves attribution in all
cases, which keeps it compatible with moral-rights regimes. A licensee may add attribution but
may not remove it.

### 3.6 Jurisdictional drafting choice

PASVL chooses Bangladesh law by default (§24.1). An Author may choose another governing law in
the NOTICE, and a LOSDA may choose another venue. This flexibility is deliberate: an author in
Germany, or a deployer in Brazil, should not be forced into a forum that makes enforcement
impossible. The choice must be exercised in the NOTICE before deployment, not retroactively.

## 4. Questions the framework cannot answer

1. Whether a particular deployment architecture creates a derivative work.
2. Whether a model trained on the Work is a derivative work in a given jurisdiction.
3. Whether a mirror on a platform outside the author's jurisdiction can be removed.
4. Whether a contractual deployment restriction binds a party that never assented.
5. Whether a non-compete-style term is enforceable in a given market.

These are genuinely unsettled. The framework is drafted to be defensible, not omniscient.

## 5. Contributing to this document

Corrections and additions are welcome through an RFC. A contribution must be:

- sourced to legislation or case law (with a citation);
- clearly marked as informational;
- reviewed by at least one contributor with jurisdiction experience.

## 6. Review

Reviewed annually by the License Council. The next review is due 2027-01-01.
