# Governance

Who decides, how they decide, and how to challenge what they decide.

The PASVL/LOSDA framework is a public legal infrastructure. Infrastructure needs institutions
that outlive any single maintainer. This directory contains the constitution, the policies, and
the procedures of those institutions.

## 1. The bodies

| Body | Role | Document |
|---|---|---|
| **The Steward** — Bangladesh Software Development Community (BSD C) | Publisher, registrar, custodian of the marks | [`CHARTER.md`](CHARTER.md) |
| **The License Council** | Final governance body; approves amendments; appoints officers | [`LICENSE-COUNCIL.md`](LICENSE-COUNCIL.md) |
| **The Registry Custodian** | Operates the LOSDA Registry and Enforcement Register | [`REGISTRY-CUSTODIAN.md`](REGISTRY-CUSTODIAN.md) |
| **The Appeals Panel** | Hears appeals from licensing and enforcement decisions | [`APPEALS.md`](APPEALS.md) |
| **The Ethics Review Board** | Advises on prohibited and high-risk uses | [`ETHICS-REVIEW-BOARD.md`](ETHICS-REVIEW-BOARD.md) |
| **The Authors' Assembly** | All authors who adopt the framework; elects Council members | [`ELECTIONS.md`](ELECTIONS.md) |

## 2. The policies

| Policy | Covers |
|---|---|
| [`AMENDMENT-PROCESS.md`](AMENDMENT-PROCESS.md) | How the License and LOSDA specification may be changed |
| [`REGISTRY-POLICY.md`](REGISTRY-POLICY.md) | What is recorded, by whom, and how it is corrected |
| [`CONFLICT-OF-INTEREST.md`](CONFLICT-OF-INTEREST.md) | Declarations and recusals |
| [`DISSOLUTION-AND-SUCCESSION.md`](DISSOLUTION-AND-SUCCESSION.md) | What happens if the Steward ceases to exist |
| [`TRANSPARENCY-REPORT-TEMPLATE.md`](TRANSPARENCY-REPORT-TEMPLATE.md) | The annual public report |

## 3. Separation of powers

```
        ┌─────────────────────────────┐
        │  Authors' Assembly          │  elects
        │  (all adopters)             │─────────┐
        └─────────────────────────────┘         │
                     ▲                          ▼
                     │              ┌──────────────────────┐
        reports      │              │   License Council    │
                     │              │  (policy, amendment) │
                     │              └──────────┬───────────┘
                     │                         │ appoints
        ┌────────────┴───────────┐   ┌─────────▼──────────┐
        │   Appeals Panel        │   │ Registry Custodian │
        │  (hears challenges)    │   │  (operates data)   │
        └────────────▲───────────┘   └─────────┬──────────┘
                     │                         │
                     │ appeals                 │ records
        ┌────────────┴───────────┐   ┌─────────▼──────────┐
        │  Authors (issuance,    │   │  LOSDA Registry    │
        │  revocation)           │   │  Enforcement Reg.  │
        └────────────────────────┘   └────────────────────┘
```

The author decides about their own work. The Council decides about the framework. The Registry
records what happened. The Appeals Panel checks that both stayed inside the rules. No single
body holds all four powers.

## 4. Principles of governance

1. **Rule of the published text.** No decision binds anyone unless it is grounded in a
   published instrument.
2. **Public by default.** Deliberations, votes, and decisions are published, subject only to
   the privacy policy.
3. **Reasoned decisions.** Every decision states its grounds.
4. **No self-dealing.** Officers may not decide matters in which they have an interest.
5. **Time limits.** Every process has a deadline, and a failure to decide has a stated
   consequence.
6. **Appealability.** Almost everything can be challenged once.
7. **Succession.** Every role has a named deputy and a documented handover.

## 5. Meetings and records

- The Council meets at least quarterly; minutes are published within 15 days.
- Votes are recorded by name, except where the privacy policy requires anonymization.
- All framework documents are versioned in this repository. If it is not in the repository, it
  is not a rule.

## 6. Contact

See [`../GOVERNANCE.md#contact`](../GOVERNANCE.md) for the current officers and contact routes.

## 7. Amending governance documents

Governance documents are amended by the License Council under
[`AMENDMENT-PROCESS.md`](AMENDMENT-PROCESS.md), Section 6. Amendments to the License itself
follow the stricter process in Section 3 of that document.
