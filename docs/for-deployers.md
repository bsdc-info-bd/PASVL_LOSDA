# For Deployers

You found software you want to run. Under PASVL, running it in production requires a **Letter of
Software Deployment Approval (LOSDA)**. This guide gets you from "I found this" to "I am
compliant" without drama.

---

## 1. First: what kind of use do you have?

| Your situation | Do you need a LOSDA? | Where to look |
|---|---|---|
| Reading the code to understand it | ❌ No | Article 3 |
| Security-auditing it | ❌ No | Article 8 |
| Forking it to propose a fix | ❌ No | Article 3.3, Article 12 |
| Classroom use | ❌ No, within limits | Article 7 |
| Academic research, non-commercial | ❌ No, within limits | Article 7 |
| Private evaluation, under 30 days | ❌ No | §6.3 (Mode S only) |
| Internal tool used by your staff | ✅ Yes — Class I | LOSDA spec §6.3 |
| Customer-facing product | ✅ Yes — Class S or H | LOSDA spec §6.1, §6.4 |
| SaaS you resell | ✅ Yes — Class H | LOSDA spec §6.4 |
| Embedded in a device or installer | ✅ Yes — Class D | LOSDA spec §6.5 |
| Training an AI model | ✅ Yes — Class M | PASVL Article 14 |
| Government service | ✅ Usually free — Class G | LOSDA spec §6.7 |
| Emergency or public-interest use | ✅ Usually free and expedited — Class P | PASVL Article 9 |

When in doubt: **ask before you deploy.** Asking is free. Deploying unlicensed is not.

## 2. The application, in plain terms

You will be asked for ten things:

1. **Who you are** — legal entity, country, registration number.
2. **What you want to run** — the work and the version.
3. **How you will run it** — internal, hosted, embedded, ML.
4. **Where** — territory.
5. **What for** — a specific description of your product.
6. **How big** — users, seats, instances, devices.
7. **How long** — your intended term.
8. **What you will change** — modifications, if any.
9. **Data and security** — whether you process personal data, and how you handle incidents.
10. **Declarations** — that you are authorised, not sanctioned, and will comply.

Use [`../templates/LOSDA-REQUEST.md`](../templates/LOSDA-REQUEST.md). A complete application gets
a decision in about **20 business days** for standard classes.

## 3. What happens next

```
You apply ──► Acknowledgement (3 days) ──► Triage (5 days) ──► Review (10 days)
         ──► Decision (10 days) ──► Letter signed ──► Registry recorded (2 days)
         ──► You receive a LOSDA ID and a verification URL
```

You may **not** deploy until the Registry shows the LOSDA as `active`. A letter that is not in
the Registry is not a permission.

## 4. What your LOSDA will contain

- your name and entity details;
- the work and version;
- the class and deployment type;
- the territory and field of use;
- the scale limits;
- your conditions (attribution, reporting, security);
- the fees and term;
- a registry hash and verification URL.

Read it. Check the scope matches your plan. If you need more, ask for an amendment before you
launch, not after.

## 5. Common mistakes by deployers

1. **"We only use it internally."** Internal use is still deployment. Class I exists for it.
2. **"We're not selling it, so it's non-commercial."** Saving money or gaining advantage is
   commercial. Read §1.4.
3. **"We'll get the licence after launch."** That is a Violation from launch. Ask first; it is
   usually quick.
4. **"Our contractor will deploy it for us."** Contractors are agents; you remain liable, and
   the scope must cover them.
5. **"We bought the company that had a LOSDA."** Transfers require approval. Notify within 30
   days.
6. **"We scaled to 10x users."** Scale limits are limits. Request an amendment.
7. **"We trained a model on it because it was public."** That requires Class M.
8. **"We removed the attribution because our design team objected."** That is a breach of C1.

## 6. What compliance looks like day to day

| Obligation | Practical action |
|---|---|
| C1 notices preserved | Keep the `LICENSE` and `NOTICE` in your source and in shipped artefacts |
| C2 attribution to users | Add an "Open source and third-party licences" page to your product |
| C3 scope | Keep a one-page record of your permitted scope; check new products against it |
| C4 scale reporting | Automate a quarterly count of users or instances |
| C5 no sublicensing | Tell your resellers they cannot pass on rights |
| C6 security incidents | Add the issuer to your incident notification list |
| C7 registry contact | Keep a monitored licensing mailbox |
| C8 records | Retain evidence for three years |
| C9 no hostile IP claims | Notify your legal team of the defensive-only patent clause |

Use [`checklist-deployer-compliance.md`](checklist-deployer-compliance.md) for the full list.

## 7. If something goes wrong

### You deployed without a LOSDA

1. Stop, or scope down to Evaluation Use immediately.
2. Apply for a LOSDA, and tell the issuer you have been deploying.
3. Ask for a retroactive LOSDA with a regularisation fee.
4. Most authors will regularise rather than litigate. Concealment is what turns a mistake into a
   dispute.

### You received a Notice of Non-Compliance

1. Read it fully before replying.
2. Do not ignore it — the cure clock is running.
3. Cure what you can immediately.
4. Ask for an extension if you need one; the policy allows up to 30 additional days.
5. If the facts are wrong, say so with evidence.
6. You have the right to appeal a final decision.

### Your LOSDA was suspended or revoked

1. Check the Registry: the status is authoritative.
2. Read the decision and the grounds (PASVL §18.7 lists all permitted grounds).
3. If a Reliance Period applies, you have 180 days to migrate — use them.
4. File an appeal within 20 business days if you disagree.

## 8. Procurement and legal review

If your organisation requires a legal review, give your lawyers:

- the licence text (`LICENSE`);
- the plain-language summary (`legal/plain-language.md`);
- the platform reality note (`legal/platform-reality.md`);
- the risk register (`legal/risk-register.md`);
- your LOSDA;
- the jurisdiction matrix (`legal/jurisdiction-matrix.md`).

Expect questions about enforceability, warranty, and indemnity. The framework's answers are:
enforceability varies by jurisdiction; there is **no warranty**; indemnity is available only
where a paid LOSDA says so.

## 9. Questions to ask an author before you apply

1. What classes do you offer and what do they cost?
2. What is your response time?
3. Will you offer a retroactive licence if we discover a past deployment?
4. What are your scale thresholds?
5. Do you incorporate the Ethics Policy?
6. Who signs, and what is your backup if you are unavailable?
7. Do you offer support, and on what terms?

## 10. Next

- [`../templates/LOSDA-REQUEST.md`](../templates/LOSDA-REQUEST.md)
- [`checklist-deployer-compliance.md`](checklist-deployer-compliance.md)
- [`deployment-scopes.md`](deployment-scopes.md)
- [`faq.md`](faq.md)
