# Deployment Scopes: 40 Worked Examples

"Deployment" is the central concept of the framework. This document removes ambiguity by
working through real situations.

**Reminder:** the definition is in PASVL §1.7. If an example here seems to conflict with the
licence text, the licence wins.

---

## A. Reading, learning, and inspecting (no LOSDA)

| # | Situation | Deployment? | Why |
|---|---|---|---|
| 1 | Reading the source on GitHub | No | Article 3.1 |
| 2 | Cloning to your laptop to explore | No | Article 3.3 |
| 3 | Running a static analysis tool over the code | No | Article 3.2 |
| 4 | Writing a blog post quoting a function | No | Article 3.5 |
| 5 | Using it as a teaching example in a lecture | No | Article 3.4, 7.2 |
| 6 | Forking to open a pull request | No | Article 3.6 |
| 7 | Keeping a copy in an archive for provenance | No | Article 3.3 |
| 8 | Reproducing a bug in a private container | No, if within Evaluation Use | §6.3 |
| 9 | Comparing its behaviour with a competitor | No, if Evaluation Use | §6.3 |
| 10 | Reporting a vulnerability | No | Article 8 |

## B. Private evaluation (no LOSDA if within limits)

| # | Situation | Deployment? | Why |
|---|---|---|---|
| 11 | A developer runs it locally to evaluate it | No, under 30 days and Mode S | §6.3 |
| 12 | A team runs a proof of concept for three weeks, no real data | No, if private and non-production | §6.3 |
| 13 | A team runs the same POC for four months | Yes | Exceeds §6.3(e) |
| 14 | A proof of concept with real customer data | Yes | §6.3(b) fails |
| 15 | A demo on a public URL for investors | Yes | Serves persons other than the deployer |
| 16 | Running it in CI to test a pull request | No | Verification, not production use |

## C. Internal use (Class I)

| # | Situation | Deployment? | Why |
|---|---|---|---|
| 17 | Deployed on the company intranet for staff | Yes — I | Operational use by real users |
| 18 | A scheduled batch job using it every night | Yes — I | Operational use |
| 19 | Installed on every employee's laptop as a tool | Yes — I | Operational use; seats count |
| 20 | Used by a single contractor on a client project | Yes — I or S | Contractor is an agent; scope must cover it |
| 21 | Used by an Affiliate in another country | Yes — I or E | Affiliates need to be named |
| 22 | A test environment with production-shaped data | Yes — I | Non-production but operational; treat it as deployment |

## D. Customer-facing and hosted (Class S or H)

| # | Situation | Deployment? | Why |
|---|---|---|---|
| 23 | Embedded in your commercial desktop app | Yes — S or D | Distribution |
| 24 | Backend component of your SaaS | Yes — H | Hosted service |
| 25 | A public API powered by the work | Yes — H | Hosted service |
| 26 | A demo site that anyone can use | Yes — H | Serves third parties |
| 27 | A free community instance you run | Yes — H, often Class P or O | Free is not unlicensed |
| 28 | Providing the work to customers as a managed instance | Yes — H | Hosted service |
| 29 | White-labelling it for a client | Yes — H or D + Service Bureau permission | §13.5 |
| 30 | Reselling capacity on your instance | Yes — H + explicit resale permission | Service Bureau Use |

## E. Distribution and embedded (Class D)

| # | Situation | Deployment? | Why |
|---|---|---|---|
| 31 | Shipping a compiled binary with an installer | Yes — D | Distribution of executable form |
| 32 | Flashing it onto hardware you sell | Yes — D | Deployment into a device |
| 33 | Publishing an npm package that bundles it | Yes — D | Distribution |
| 34 | A Docker image on a public registry that runs it | Yes — D and/or H | Distribution and possibly hosting |
| 35 | An internal Docker image | Yes — I | Operational use |
| 36 | A GitHub Release with binaries | Yes — D | Distribution of executable form |

## F. Machine learning (Class M)

| # | Situation | Deployment? | Why |
|---|---|---|---|
| 37 | Training a code model on the repository | Yes — M | Article 14.1 |
| 38 | Using it as evaluation data for a benchmark | Yes — M, unless Article 7 research | Article 14.2 |
| 39 | Non-commercial research training, model not deployed | No | Article 14.2(a) |
| 40 | Fine-tuning a model and selling the model | Yes — M | Article 14.1, 14.6 |

---

## G. Edge cases, honestly answered

### G.1 "I run it on my own machine to do my job"

If you are an employee using it for your employer's work, that is internal deployment by the
employer. It needs a Class I LOSDA unless it falls within Evaluation Use.

### G.2 "It's a development dependency"

A build-time dependency that is only executed during compilation is not deployed in production.
But if the build produces artefacts distributed to users, the distribution question applies to
those artefacts.

### G.3 "We host it for one customer, privately"

That is a Hosted Service for that customer. Class H or I depending on whether the customer is
outside your organisation.

### G.4 "We run it for disaster response for a month"

Article 9.1 permits emergency use without a prior LOSDA for up to 90 days with notification
within 14 days.

### G.5 "We forked it and run our fork"

The fork is a study artefact. Running it is deployment (Class S, I, or H as appropriate), and
§13.4 prohibits using a fork to evade a LOSDA.

### G.6 "We don't run it; our customers do"

If you distribute it, you need Class D. If your customers then run it, they need their own
LOSDA unless your Class D grant extends to them — which requires an express term, because
sublicensing is otherwise prohibited.

### G.7 "We run a modified version privately"

Allowed within a LOSDA that permits modifications. Removing notices or introducing malicious
code is prohibited in all cases.

### G.8 "We use it in a hackathon demo for 48 hours"

Within Evaluation Use if private and Mode S. If the demo is public and serves users, it is
deployment; ask the author for a Class X extension, which is quick and usually free.

### G.9 "We use it in a non-profit's public website"

Non-profit status does not make a public service non-commercial. Class P or O may apply, often
at no fee.

### G.10 "We use it to test our own product's compatibility"

Private, non-production testing is verification, not deployment. Publishing compatibility
results is commentary.

---

## H. Decision tree

```
Is it running, serving, or distributed to someone other than you for a real purpose?
│
├─ No ──► Is it reading, studying, auditing, forking, quoting, or teaching?
│         ├─ Yes ──► No LOSDA needed (Article 3 / 7 / 8)
│         └─ No  ──► Private evaluation? ──► Under 30 days and Mode S? ──► No LOSDA
│                                            Otherwise ──► LOSDA needed
│
└─ Yes ─► Is anyone outside your organisation involved?
          ├─ No  ──► Class I LOSDA
          └─ Yes ─► Is the work distributed in executable form?
                    ├─ Yes ──► Class D (plus I or H if you also operate it)
                    └─ No  ─► Are you serving it over a network to third parties?
                              ├─ Yes ──► Class H
                              └─ No  ──► Class S
```

---

## I. How to describe your deployment in an application

Weak: "We will use it in our platform."

Strong:

> "We will embed the scheduler as a backend component of Acme Cloud, our multi-tenant SaaS
> product, serving approximately 4,000 business users in the EU and UK. We will not modify the
> core scheduling algorithm. We will expose its output through our own API. We will process
> customer job metadata, which includes personal data of end users. Hosting is in AWS
> eu-west-1 and eu-central-1. We expect to grow to 12,000 users within 24 months and are
> requesting headroom accordingly."

A specific description gets a fast, favourable decision. A vague one gets questions — and the
clock stops.
