# Amendment Process

**Version:** 1.0 · **Applies to:** the License, the LOSDA specification, the schemas, and all
governance documents.

A license that can be changed by its author at will is not a license; it is a promise. A license
that can never change is not a license either; it is a fossil. This process is the narrow path
between the two.

## 1. Classes of change

| Class | Examples | Process |
|---|---|---|
| **Editorial** | Typo, broken link, formatting, example correction | Steward action + changelog entry |
| **Clarifying** | Adds explanation without changing rights | Steward action + 14-day notice + changelog |
| **Minor** | Adds a permission, improves a process, fixes a gap that favors licensees | RFC + 30-day comment + Council majority |
| **Major** | Removes or restricts a permission, changes the deployment model, changes the registry | RFC + 45-day comment + two-thirds Council + Assembly ratification |
| **Emergency** | Required by law, court order, or an imminent security issue | Immediate Council action + 7-day notice + ratification at the next meeting |

**A change that reduces a licensee's existing rights is always Major**, even if it looks small.

## 2. Who may propose

Anyone: an author, a licensee, a contributor, a member of the public, an officer, or the Steward
itself. Proposals are opened as an RFC in [`../rfcs/`](../rfcs/) using
[`../rfcs/0000-template.md`](../rfcs/0000-template.md).

## 3. The RFC process

### Step 1 — Draft (anyone, no deadline)

The proposal must contain:

1. **Problem statement** — what is wrong or missing today, with examples.
2. **Proposed text** — the exact wording, as a diff against the current document.
3. **Rationale** — why this is the right fix.
4. **Effects** — on authors, licensees, contributors, the registry, and existing LOSDAs.
5. **Compatibility** — whether existing LOSDAs remain valid, and if not, how they are handled.
6. **Alternative approaches** — including doing nothing.
7. **Legal review** — any known jurisdictional issues.
8. **Migration** — what deployers must do, and by when.

### Step 2 — Triage (10 business days)

The License Council assigns a sponsor and a reviewer. Triage outcomes: accept for comment,
return for revision, or close with reasons.

### Step 3 — Public comment

| Class | Minimum comment period |
|---|---|
| Minor | 30 days |
| Major | 45 days |
| Emergency | 7 days (ex post) |

Comments are public. Anonymous comments are accepted but carry less weight. The sponsor must
publish a response to every substantive comment.

### Step 4 — Decision

| Class | Required approval |
|---|---|
| Minor | Simple majority of the Council |
| Major | Two-thirds of the whole Council, then ratification by the Authors' Assembly (simple majority of those voting, quorum 20% of adopters) |
| Emergency | Council decision immediately; ratification at the next meeting |

Votes are recorded by name. The decision, with reasons, is published within 10 business days.

### Step 5 — Publication

The change is published as:

1. a new version number (`PASVL-1.1`, `PASVL-2.0`, …);
2. an updated `CHANGELOG.md` entry with the effective date;
3. an updated schema, where relevant;
4. a migration note in `docs/migration-guide.md`;
5. an announcement in the repository and to registered adopters.

### Step 6 — Review

The Council reviews the effects of every Major change 12 months after it takes effect.

## 4. Veto and objection

Any of the following triggers a mandatory second review:

1. A petition of 20% of registered adopters.
2. A reasoned objection by the Appeals Panel on procedural grounds.
3. A legal opinion obtained by the Steward that the change creates a material legal risk.

The second review must conclude within 60 days. The change may be suspended during the review
if the Council so decides by simple majority.

## 5. Retroactivity

**Rights granted cannot be withdrawn.** A Major change applies only to:

1. versions of a Work released after the change's effective date; and
2. new LOSDAs issued after the effective date.

Existing LOSDAs continue under the version in force when they were issued, unless the licensee
opts into the new version in writing. Where an amendment is required by law, the Council must
state the legal basis and the affected terms.

## 6. Governance document amendments

Governance documents (this directory) are amended by the Council:

- Minor: simple majority.
- Structural (changes to bodies, elections, or separation of powers): two-thirds of the whole
  Council + 30-day comment.

Governance amendments cannot alter the License. If they conflict, the License prevails.

## 7. Schema changes

A schema change that breaks existing records is Major. A backward-compatible addition is Minor.
Every schema version must accept all records valid under the previous version, or provide a
documented migration.

## 8. Emergency changes

An emergency change requires:

1. a written statement of the emergency;
2. the minimum change necessary;
3. immediate publication;
4. a 7-day comment period and ratification at the next Council meeting;
5. automatic expiry after 180 days unless ratified by the full process.

## 9. Version numbering

| Change | License | LOSDA spec | Schema |
|---|---|---|---|
| Editorial | 1.0.1 | 1.0.1 | — |
| Clarifying | 1.0.x | 1.0.x | patch |
| Minor | 1.1.0 | 1.1.0 | minor |
| Major | 2.0.0 | 2.0.0 | major |

## 10. Record of amendments

Every amendment is recorded in [`../CHANGELOG.md`](../CHANGELOG.md) with:

- the RFC number;
- the class of change;
- the comment period dates;
- the vote;
- the effective date;
- the migration requirement, if any.

## 11. Process failures

If the Council fails to complete a decision within the stated deadline:

1. the RFC remains open;
2. the sponsor may escalate to the Appeals Panel for a procedural order;
3. the status quo continues — no change takes effect by default.

**Silence is not approval**, in amendments as in licensing.
