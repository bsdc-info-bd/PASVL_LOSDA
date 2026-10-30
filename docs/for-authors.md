# For Authors

You wrote something good. You want it to be visible, auditable, and trustworthy. You also want
to be able to make a living from it, and you want to decide who runs it in the real world.

PASVL is built for exactly that combination. This guide tells you what you get, what you give
up, and how to do it properly.

---

## 1. What PASVL gives you

| Benefit | How |
|---|---|
| Public visibility without surrender | Article 3 grants reading, auditing, forking, teaching, and quoting to everyone |
| A real permission process | LOSDA: numbered, signed, recorded, verifiable |
| Commercial control | You decide classes, fees, territory, scale, and term |
| Credibility | The source can be audited by anyone, including your customers |
| A no-fee public-good channel | Academic, government, research, and public-interest classes |
| Protection against predatory relicensing | Nothing you grant can be taken back (§19.5) |
| A defence against "it's public so it's free" | Clear, repeated notices plus a registry |

## 2. What you give up

- **The "open source" label.** You cannot call it open source, and some of the community will
  not use it for that reason.
- **Some adoption.** Companies with strict procurement rules may not use PASVL works without a
  legal review. That is the cost of control.
- **Administration.** You must answer licensing requests, keep a register, and enforce
  occasionally.
- **The moral high ground of pure permissiveness.** You will be asked, "why not MIT?" Have an
  honest answer ready.

## 3. The honest answer to "why not MIT?"

> "Because I want the code to be public and the deployment to be deliberate. MIT gives away the
> right to run it commercially without asking. I want readers, auditors, and students to have
> everything they need, and I want organisations that build a business on it to talk to me
> first. That is a fair trade, and it is transparent."

If that is not your position — if you want maximum adoption above all — use MIT or Apache-2.0.
The framework does not want reluctant adopters.

## 4. Adoption in nine steps

1. **Check your rights.** Read `templates/ADOPTION-CHECKLIST.md`.
2. **Add the files.** `LICENSE`, `NOTICE`, `README` section, `CONTRIBUTING`, `SECURITY`,
   `THIRD-PARTY-NOTICES`, `TRADEMARK`.
3. **Add headers.** Use `templates/LICENSE-HEADER.txt`; enforce in CI.
4. **Choose your Mode.** Mode S (30 days evaluation allowed) or Mode U (no execution at all
   without permission).
5. **Define your classes and fees.** You can set every fee to zero and still keep the process.
6. **Register the work.** Add it to `registry/works.json` or your own register.
7. **Publish the process.** Say how to request a LOSDA, and your response target.
8. **Announce honestly.** Source-available, permission-gated deployment, not open source.
9. **Operate it.** Answer requests, record decisions, publish an annual note.

## 5. Deciding your terms

### 5.1 Mode

| Mode | Meaning | Choose when |
|---|---|---|
| **S** | Evaluation Use is permitted for 30 private, non-production days per year | You want people to be able to try it |
| **U** | No execution at all without a LOSDA | You want strict control, or the work is dangerous when misused |

### 5.2 Fee policy

| Policy | Effect |
|---|---|
| All zero | Maximum goodwill; you still keep control of scope and term |
| Free for small, paid for large | Common and defensible; publish the threshold |
| Paid for hosted service only | Matches the value: running a service is where money is made |
| Paid for embedded distribution | Matches hardware and OEM economics |

Whatever you choose, publish it. Surprise fees are the fastest way to lose the community.

### 5.3 Classes to offer

Most authors should offer: **S** (commercial), **I** (internal), **H** (hosted), **D** (embedded),
**A** (academic), **P** (public interest), **X** (evaluation extension). Add **E**, **G**, **R**,
**M**, **C**, **O** as needed.

## 6. Writing a good NOTICE

Your NOTICE is the first thing a deployer reads. Make it short and unambiguous:

```
Work:        Acme Scheduler
Author:      Acme Labs Ltd, https://acme.example, licensing@acme.example
License:     PASVL-1.0 — https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/LICENSE
Deployment:  Requires a LOSDA. Apply at https://acme.example/licensing
Mode:        S — 30 days private evaluation permitted
No-fee:      Academic, government, public interest, research
Issuing:     Author
Ethics:      Incorporated
```

## 7. Handling requests

| Situation | Do this |
|---|---|
| A student asks to use it in a class project | Point at Article 7 teaching exception; no LOSDA needed |
| A startup asks to use it internally | Class I, usually cheap or free below a revenue threshold |
| A company asks to build a SaaS | Class H; ask about scale and sub-processors |
| A company asks to embed it in hardware | Class D; ask about volumes and support window |
| A company asks for "unlimited everything forever" | Allowed for a price; make the price explicit |
| Someone deployed without asking | Stage 0 courtesy message, then offer a retroactive LOSDA |
| A competitor asks | You may refuse if the use is outside your offer; state a reason and offer an appeal |

**Respond even when you refuse.** Silence creates enemies and weakens the framework.

## 8. Enforcement, realistically

Most breaches are careless, not malicious. The framework's process starts with a friendly
message, gives a cure period, and only escalates if ignored. Plan for roughly one or two
conversations per year for a mid-sized project; far fewer for a small one.

You will need:

- a template NNC (`templates/NOTICE-OF-NON-COMPLIANCE.md`);
- a decision about whether to offer retroactive licences;
- a line in your budget for occasional legal advice;
- patience.

## 9. Common mistakes

1. Leaving a stale README that says MIT. **This is the single most damaging mistake.** It
   undermines enforcement and is unfair to users.
2. Publishing without checking employer or funder rights.
3. Setting fees but never publishing them.
4. Refusing without reasons.
5. Never recording LOSDAs, so no one can verify.
6. Overclaiming ("nobody can use this without paying") when the licence grants evaluation and
   academic rights.

## 10. When PASVL is the wrong choice

Use a different licence if:

- you want maximum adoption and do not care about commercial licensing;
- your funder requires OSI-approved open source;
- your project is a standard that needs universal, unconditional implementation rights;
- you cannot commit to answering licensing requests;
- your main goal is to prevent any commercial use at all (use a non-commercial licence, which is
  a different instrument with different trade-offs).

## 11. Next steps

- [`quickstart.md`](quickstart.md) — the 30-minute adoption
- [`../templates/ADOPTION-CHECKLIST.md`](../templates/ADOPTION-CHECKLIST.md)
- [`for-open-source-projects.md`](for-open-source-projects.md) — if you are migrating an existing
  project
- [`../legal/compatibility.md`](../legal/compatibility.md) — before you add dependencies
