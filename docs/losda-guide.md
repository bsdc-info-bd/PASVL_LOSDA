# The LOSDA Guide

A practical walkthrough of the permission process, written for the person who has to do it.

---

## 1. What you are asking for

You are asking for a **specific, time-limited, scoped permission to run software**. You are not
asking for a copy (you can already read it). You are not asking for ownership. You are asking to
be allowed to operate it in the real world.

Understanding that distinction makes the application easy.

---

## 2. The five-minute application

You need:

1. **Your legal identity** — company name as registered, or your own legal name.
2. **The work and version** — the repository and the release you will run.
3. **What you will do with it** — one clear paragraph.
4. **Scale** — real numbers, with 24 months of headroom.
5. **Where and for how long** — territory and intended term.

Everything else is detail.

---

## 3. Choosing a class

| If you are… | Ask for | Typical fee |
|---|---|---|
| Using it internally | **I** | Free to low |
| Building a product | **S** | Author's standard |
| Running a service | **H** | Author's standard, often usage-based |
| Shipping hardware or binaries | **D** | Often per-device |
| A university teaching or researching | **A** or **R** | Free |
| A public body | **G** | Free |
| Responding to a disaster | **P** | Free, expedited |
| Trying before buying | **X** | Free, ≤90 days |
| Rescuing an essential service | **C** | Free, requires evidence |
| Training a model | **M** | Negotiated |
| You are the public | **O** | Only if the author offers it |

If you are unsure, ask for **X** first. It buys time and shows good faith.

---

## 4. Writing a good application

### 4.1 The field of use

Weak:

> We will use it in our software products.

Strong:

> We will use the library as the queue component of Acme Workflow, our B2B workflow product. It
> will run inside our multi-tenant backend and will not be exposed directly to customers. We will
> not modify the queuing algorithm, but we will add adapters for our own storage layer.

### 4.2 Scale

Give a number, a unit, and a growth assumption:

> 1,200 named users today; projected 4,000 within 24 months; requesting 5,000.

### 4.3 Data and security

> The component processes job metadata including end-user identifiers. We host in AWS
> eu-central-1. We have a 24/7 incident process and will notify the issuer within 72 hours of a
> material incident.

### 4.4 Modifications

Say clearly whether you will change the code. Unexplained modifications are the most common
reason an application is returned.

---

## 5. What the issuer does

| Step | What happens | Time |
|---|---|---|
| Acknowledgment | You get a reference number | 3 business days |
| Triage | Class, completeness, sanctions screening | 5 business days |
| Review | Identity, use case, scale, risk | 10 business days |
| Decision | Approve, approve with conditions, or refuse | 10 business days |
| Issue | Letter generated and signed | 3 business days |
| Record | Registry entry and hash | 2 business days |
| Delivery | You receive the letter and verification URL | 1 business day |

If the issuer asks a question, answer it fully — the clock stops while they wait.

---

## 6. Reading your LOSDA

Check these fields carefully:

| Field | Why it matters |
|---|---|
| **Work and version range** | A permission for v1 does not cover v2 if the LOSDA fixes a version |
| **Class** | Determines the default conditions |
| **Territory** | Serving a user outside the territory is a breach |
| **Field of use** | A new product is a new field of use |
| **Scale** | Exceeding it is a breach |
| **Term** | Expiry is a hard stop |
| **Conditions** | C1–C16, plus any bespoke conditions |
| **Reliance Period** | Your migration window if the permission ends |
| **Record hash** | Must match the Registry |

If anything is unclear, ask **before** you deploy. Ambiguity does not excuse a breach.

---

## 7. Verifying a LOSDA

1. Open the Verification URL on the letter.
2. Confirm the status is `active`.
3. Confirm the record hash matches the letter.
4. Confirm the scope matches what you are doing.
5. If the status is `suspended`, `revoked`, or `expired`, stop and contact the issuer.

A screenshot of a letter is not verification. The Registry is the source of truth.

---

## 8. Amending

You need an amendment when you:

- exceed scale by more than the permitted headroom;
- launch a new product in a new field of use;
- expand to a new territory;
- add an Affiliate;
- change hosting to a new country;
- start distributing binaries;
- acquire another company that uses the work.

Use [`../templates/LOSDA-AMENDMENT.md`](../templates/LOSDA-AMENDMENT.md). Amendments that expand
your rights need the issuer's signature; amendments that restrict them need yours too.

---

## 9. Renewal

- Apply **30 days before expiry**.
- If you miss the date, ask for a continuity bridge; most issuers will grant one if there was no
  breach during the gap.
- Set a calendar reminder at 90 days, 60 days, and 30 days.

---

## 10. If you are refused

1. Read the ground.
2. Fix it if you can — narrower scope, different class, extra identity evidence.
3. Ask what would make a future application succeed (the refusal notice must say).
4. Appeal within 20 business days if you think the decision is wrong.
5. Consider a different work. The ecosystem does not owe you this one.

---

## 11. Keeping compliance cheap

| Practice | Effect |
|---|---|
| Record your scope on one page | Everyone knows the boundary |
| Automate scale reporting | No quarterly scramble |
| Put the issuer in your incident runbook | C6 compliance without thinking |
| Add a third-party licenses page | C1/C2 compliance by default |
| Review the LOSDA at each product launch | No accidental scope creep |
| Keep the signed letter in your contract system | Audit-ready |

---

## 12. Template emails

**Initial request**

> Subject: LOSDA request — [Work] — [Your company]
>
> Hello,
>
> We would like to deploy [Work] version [x.y] as [describe use] in [territory], serving
> approximately [N] users. We have attached the completed application form.
>
> Could you confirm receipt and the expected decision date? We are planning to launch on [date]
> and would like to allow time for any questions.
>
> Best regards,
> [Name], [Role], [Company]

**Follow-up after 15 business days**

> Subject: Re: LOSDA request — [Work] — [reference]
>
> Hello,
>
> Following up on our application of [date] (reference [x]). We have not yet received a decision
> and wanted to check whether you need any further information from us.
>
> We are still planning to launch on [date]. If a decision is not possible before then, could you
> let us know whether a Class X evaluation extension is available in the meantime?
>
> Best regards,
> [Name]

**Discovering a past unlicensed deployment**

> Subject: Retroactive LOSDA request — [Work] — [Company]
>
> Hello,
>
> During a license review we discovered that we have been running [Work] in [context] since
> [date]. We believe this was outside the license and we want to correct it.
>
> We have [describe immediate action] and would like to apply for a retroactive LOSDA covering the
> period since [date]. We are happy to pay a regularization fee.
>
> We apologize for the oversight and would like to put the relationship on a proper footing.
>
> Best regards,
> [Name]
