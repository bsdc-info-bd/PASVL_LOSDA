# Requests for Comments (RFCs)

This is where the framework changes. Every substantive change to the license, the LOSDA
specification, the schemas, or the governance goes through an RFC — including changes proposed by
the Steward.

## 1. Why RFCs

A license that can be edited by whoever holds the repository is a promise, not a license. A
license that can never be edited is a fossil. The RFC process is the narrow path between them:
public, reasoned, time-limited, and recorded.

## 2. RFC lifecycle

```
Draft ──► Triage ──► Public comment ──► Decision ──► Published ──► Post-implementation review
 (you)    (Council    (30 or 45 days)     (vote)      (changelog)        (12 months later,
          + sponsor)                                                     major changes only)
```

| Stage | Owner | Duration |
|---|---|---|
| Draft | Anyone | No limit |
| Triage | License Council | 10 business days |
| Public comment | Community | 30 days (minor) or 45 days (major) |
| Decision | License Council (+ Assembly for major) | 10 business days |
| Publication | Steward | 5 business days |
| Review | Council | 12 months after a major change |

## 3. How to submit

1. Copy [`0000-template.md`](0000-template.md) to `NNNN-short-title.md`, where `NNNN` is the next
   free number.
2. Fill in every section. An RFC with a "Problem statement" of "it would be better" will be
   returned.
3. Open a pull request that adds the file.
4. Announce it in the discussions.

## 4. Numbering

- `0000` is reserved for the template.
- Open RFCs are numbered in the order they are opened.
- An RFC that is withdrawn keeps its number.
- A superseded RFC is marked `Superseded by NNNN` in its header.

## 5. Files

| RFC | Title | Status |
|---|---|---|
| [`0000-template.md`](0000-template.md) | Template | — |
| [`0001-publish-pasvl-1.0.md`](0001-publish-pasvl-1.0.md) | Publish PASVL-1.0 and LOSDA-1.0 | Accepted |
| [`0002-registry-hash-chain.md`](0002-registry-hash-chain.md) | Add the hash chain and monthly Merkle root | Accepted |

## 6. Decision rules

| Class | Approval |
|---|---|
| Editorial | Steward, with changelog |
| Clarifying | Steward, 14-day notice |
| Minor | Simple majority of the Council |
| Major | Two-thirds of the whole Council + Assembly ratification |
| Emergency | Immediate Council action, 7-day notice, later ratification |

## 7. What an RFC must contain

1. Problem statement.
2. Proposed text (a diff, not a description).
3. Rationale.
4. Effects on authors, licensees, contributors, the registry, and existing LOSDAs.
5. Compatibility and migration.
6. Alternatives considered.
7. Legal review notes.
8. Who it hurts, and how that is justified.

**Section 8 is mandatory.** Every change has costs. An RFC that does not name them is not ready.

## 8. Rejection

An RFC may be rejected for:

- a problem that does not exist;
- a fix that costs more than the problem;
- a change that withdraws a right already granted;
- a change that makes the license describable as open source when it is not;
- insufficient engagement during the comment period;
- a conflict with the framework's mission in `governance/CHARTER.md` §4.

Rejection must be reasoned, and the reasons are published.

## 9. Withdrawal

The author may withdraw an RFC at any time. The number stays in the index, marked `Withdrawn`.

## 10. After acceptance

The Steward:

1. publishes the new version;
2. updates `CHANGELOG.md`;
3. updates the schema, if relevant;
4. publishes a migration note;
5. announces the change to registered adopters;
6. reviews the effects after 12 months (major changes only).
