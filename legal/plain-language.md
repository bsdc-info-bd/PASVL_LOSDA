# PASVL-1.0 in Plain Language

> **This page is a human-readable summary. It is not the license and it has no legal force.**
> The binding text is [`LICENSE`](../LICENSE). If this page and the license disagree, the
> license wins. Nothing here grants you any right.

---

## The one-paragraph version

You may read, study, audit, copy, fork, cite, teach, quote, and contribute to this software for
free, forever, without asking anyone. You may **not run it as a real deployment** until the
author gives you a **Letter of Software Deployment Approval (LOSDA)** — a short, numbered,
signed, publicly recorded permission that says who may deploy, where, how much, for how long,
and under what conditions. Reading is free. Running is licensed.

---

## What you can do without asking

| You want to… | Can you? | Notes |
|---|---|---|
| Read the source code | ✅ Yes | Free, forever, any purpose |
| Study how it works | ✅ Yes | Free, forever |
| Security-audit it | ✅ Yes | Report bugs responsibly (Article 8) |
| Fork or clone it | ✅ Yes | Keep the notices |
| Quote it in a paper or a blog | ✅ Yes | Attribute it |
| Teach with it | ✅ Yes | Don't run a class service on it |
| Learn from it and write your own thing | ✅ Yes | But don't launder a copy (4.5) |
| Submit a pull request | ✅ Yes | You keep your copyright |
| Build it privately to see if it works | ✅ Yes | 30 days per year, private, non-production |
| Run it for your own private evaluation | ✅ Yes | See above |
| Run it in production | ❌ Not yet | You need a LOSDA |
| Offer it as a service to others | ❌ Not yet | You need a LOSDA |
| Ship it inside your product | ❌ Not yet | You need a LOSDA |
| Use it to train an AI model | ❌ Not yet | You need a Class M LOSDA |
| Sell it, sublicense it, rebrand it as yours | ❌ No | Never, without written permission |
| Call it "open source" | ❌ No | It is source-available, not open source |

---

## What a LOSDA is, in one picture

```
   You                    The Author                The Registry
    │                         │                         │
    │ 1. Apply ──────────────►│                         │
    │                         │ 2. Review               │
    │                         │ 3. Decide               │
    │                         │ 4. Sign ───────────────►│ 5. Record
    │◄──────── 6. Receive ────│                         │
    │                                                   │
    │ 7. Deploy, within the scope written on the letter │
    │                                                   │
    │ 8. Anyone can check your status at the Registry ──│
```

A LOSDA is **10 fields long**, not a contract negotiation:

1. A number, like `LOSDA-BSDC-2026-000123`
2. Who issued it
3. Who it is for
4. What software, at which version
5. What kind of deployment (SaaS, internal, embedded, research…)
6. Where (territory)
7. How much (users, servers, devices)
8. How long (term)
9. What conditions (attribution, reporting…)
10. A registry link anyone can verify

---

## What the author promises you

- The source **stays public**. No bait-and-switch.
- The rights you have today **stay** for the versions you received (§19.5).
- **No implied permission** and **no surprise revocation** — revoking a LOSDA needs grounds,
  notice, a hearing, and a 180-day wind-down (Articles 18–19).
- If you deploy legally, you get **notice and a cure period** before anything happens.
- New, stricter license terms **cannot take back** rights already granted to you.

## What the author does not promise you

- That the software works. It is provided **as is**, with **no warranty** (Article 21).
- That you can deploy it without permission. You cannot.
- That you can use the name or logo. You cannot (Article 17).
- That this page is legal advice. It is not.

---

## The five things that get people into trouble

1. **"It's on GitHub, so it's free."** Not here. Public visibility ≠ public license to deploy.
2. **"I only copied a little."** A Substantial Portion is still covered (§1.35, §4.5).
3. **"I'm just running it for my startup's internal tool."** That is Internal Use — you need a
   Class I LOSDA.
4. **"My AI will rewrite it from scratch."** That is model laundering (§13.11, §14.4).
5. **"I got permission on Twitter."** Permission exists only if it is in the Registry (§10.4).

---

## Frequently misunderstood words

| Term | What it actually means here |
|---|---|
| **Source-available** | You can see the code; that is not the same as being allowed to use it |
| **Deployment** | Running it for real — not reading, not studying, not building privately |
| **Evaluation Use** | 30 private, non-production days per year, with limits |
| **Commercial** | Anything meant to make money, save money, or win advantage |
| **Affiliate** | Companies under the same control — permission does not leak between them by accident |
| **Substantial Portion** | Any part that matters to what the software does |
| **Reliance Period** | The 180 days you get to migrate if a permission ends |
| **NNC** | Notice of Non-Compliance — the formal "you are breaking the rules" letter, with a cure clock |

---

## If you are worried about this license

That is healthy. Read:

- [`docs/faq.md`](../docs/faq.md) — the questions everyone asks first
- [`legal/platform-reality.md`](platform-reality.md) — what GitHub's terms do and do not permit
- [`legal/plain-language.md#honest-limits`](#honest-limits) — the section below
- [`docs/for-deployers.md`](../docs/for-deployers.md) — how to get permission smoothly

### Honest limits

This framework is new. It is **not** a license approved by the Open Source Initiative, and the
community must never describe it as open source. Whether a court will enforce a deployment
restriction to the full extent intended depends on the jurisdiction, on how the work is
distributed, and on how clearly the restriction is communicated. Some rights cannot be
contracted away — including statutory consumer rights, certain interoperability rights, and
non-waivable moral rights. The framework is designed to **fail softly**: if a deployment
restriction is unenforceable somewhere, the visibility grant and the attribution duties still
stand, and the author retains every right the law gives them.

If you need certainty for a high-stakes commercial deployment, get the LOSDA in writing and get
your own lawyer to read it. That is not suspicion of the framework; that is how serious
licensing works.

---

*Machine-readable identifier: `LicenseRef-PASVL-1.0`. Not an OSI-approved license.*
