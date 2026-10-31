# For Educators and Researchers

Teaching and research are the framework's strongest commitments. PASVL grants a broad,
no-permission-needed envelope for both, and provides no-fee classes when you step beyond it.

---

## 1. What you can do without asking

### 1.1 Teaching

Under Article 3.4 and Article 7.2 you may:

- read, display, and discuss the source in lectures and tutorials;
- reproduce excerpts in slides, handouts, and textbooks, with attribution;
- assign students to read, analyze, and critique the code;
- have students build and run the software **in the teaching environment** for coursework;
- use the work as the basis of exercises and exams.

You may **not**:

- run a service for students that functions outside the teaching environment (for example, the
  university's official course-management system) without a Class A LOSDA;
- deploy the software in the institution's production infrastructure;
- offer the software to the public as part of a course platform.

### 1.2 Research

Under Article 7.1 you may:

- execute the work in a controlled research environment;
- modify it for research purposes;
- publish results, comparisons, and benchmarks, with attribution;
- use it in a testbed for a research project, provided it does not provide a service to persons
  outside the research team and is not used to improve a commercial product.

You may **not**:

- run a production research service serving external users (Class R);
- train a commercial model on it (Class M);
- deploy it in clinical, safety-critical, or regulated settings without the applicable review.

## 2. When to apply for a LOSDA

| Situation | Class | Fee |
|---|---|---|
| Course uses the software in labs | No LOSDA (Article 7.2) | — |
| University runs it as a shared service for students | A | None |
| Research testbed with external participants | R | None |
| Research project exceeding Article 7 limits | R | None |
| Clinical or regulated research use | R + ethics review | None |
| Teaching material published as a book | No LOSDA for the text; attribute | — |
| A spin-out company deploys it | S or H | Author's fees |

Applications for Classes A and R are **free** and reviewed in about 10 business days. Class R
requires an ethics statement and a data-handling plan.

## 3. Citing the work

When you publish, cite the work **and** the license. Suggested formats:

**Paper**

> Author, A. (2026). *Work Name* (Version 1.4) [Computer software]. Licensed under PASVL-1.0.
> https://github.com/example/work

**In-text**

> We used Work Name v1.4 (Author, 2026), licensed under the Public Availability with
> Source-Code Visibility License v1.0; deployment was permitted under LOSDA-BSDC-2026-000123.

Include the LOSDA ID when you publish results from a licensed deployment. It helps reviewers
verify that the use was authorized, and it makes the framework visible in the literature.

## 4. Ethics review

Where a deployment involves human participants, personal data, or a high-risk domain (health,
justice, employment, education, migration), obtain your institution's ethics approval as you
would for any research. If the work incorporates the Ethics Policy, the review must also address
the prohibited uses in `legal/ethics-policy.md`.

## 5. Students who want to deploy what they built

A student project that uses a PASVL work is generally within the teaching exception **while it
remains coursework**. The moment it becomes a real product — a startup, a public app, a service
for others — it is a deployment and needs a LOSDA.

Advise students to:

1. check the license before they build a company on it;
2. apply early; academic spin-out terms are often available;
3. keep the attribution in their product;
4. not assume "it was free for my coursework" means "it is free for my startup."

## 6. Publishing modified versions

You may publish a modification (a patch, a fork, a research variant) with attribution and under
the same license. Publishing does not grant deployment rights to anyone, including you. See
`legal/compatibility.md` before you combine the work with code under another license.

## 7. Institutional deployment

If your institution wants to run the work as part of its own operations — a scheduling system,
a repository mirror, a learning platform, a research cluster service — apply for a Class A
LOSDA. It is free. The application takes about ten minutes and protects both the institution and
the author.

## 8. Libraries, archives, and preservation

Librarians and archivists may:

- archive the source for preservation;
- mirror it for access;
- index and describe it in catalogs;
- provide access to students and researchers on institutional terminals.

Preservation and access are within Article 3. Running a public service from the archived copy is
not.

## 9. Open educational resources

If you want to publish a course based on the work under an open license, you may do so for your
own material. You cannot relicense the work itself, and you must carry its attribution and
license notice into your materials.

## 10. A teaching note

PASVL is a useful case study in itself: it shows students that "public" and "open" are not the
same thing, that licenses are engineering artifacts, and that a permission framework can be
designed deliberately rather than inherited by accident. Several universities use the framework's
documents in software-engineering ethics and licensing modules. You are welcome to do the same,
with attribution.

## 11. Support

- Class A and R applications: use [`../templates/LOSDA-REQUEST.md`](../templates/LOSDA-REQUEST.md)
  and mark "Academic".
- Questions: see `GOVERNANCE.md` contact details.
- Translation help for non-English institutions: see [`../translations/`](../translations/).
