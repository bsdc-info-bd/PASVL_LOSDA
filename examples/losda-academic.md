# Example LOSDA — Class A (Academic) and Class R (Research)

> Worked example, fictitious names. Shows the two free classes and why they are short.

---

## Part 1 — Class A, institutional deployment

**LOSDA ID:** `LOSDA-UNIDHAKA-2026-000012`
**Status on issue:** ACTIVE
**Verification URL:** `…/losda-registry.json#LOSDA-UNIDHAKA-2026-000012`

### Parties

| Role | Value |
|---|---|
| Issuer | OpenLedger Foundation (issuer code `OPENLEDGER`), authorized agent named in the NOTICE |
| Licensee | University of Dhaka, Department of Computer Science and Engineering |
| Country | Bangladesh |
| Public display name | University of Dhaka — CSE |
| Contact | head.cse@du.example |
| Compliance officer | Dr N. Rahman, Associate Professor |

### The work

| Field | Value |
|---|---|
| Work | OpenLedger Core |
| Repository | https://github.com/openledger/core |
| Version | 2.4.x |

### Scope

| Field | Value |
|---|---|
| Class | **A** — Academic / Non-Commercial |
| Deployment type | Internal — institutional teaching infrastructure |
| Territory | Bangladesh |
| Field of use | Hosting course laboratory exercises for enrolled students in CSE 3xx and 4xx courses. Not for administrative systems, not for research publications' experiments, not for any income-generating activity. |
| Scale | 1,200 student accounts; 3 instances |
| Modifications | Allowed for teaching materials; changes must not be published as an official release |

### Term and fee

| Field | Value |
|---|---|
| Effective | 2026-11-15 |
| End | 2028-11-14 (two years) |
| Fee | **None** |

### Conditions

| Code | Applied |
|---|---|
| C1 notices preserved | Yes |
| C2 attribution in the lab portal | Yes |
| C3 territory and field | Yes |
| C7 registry contact | Yes |
| C9 no hostile IP assertions | Yes |

### Bespoke conditions

1. The Licensee must not use the deployment to provide services to persons outside the enrolled
   student body or the department's teaching staff.
2. Student coursework built on the Work must carry the attribution in its submission headers.
3. The Licensee must notify the Issuer before using the deployment for any research purpose, so
   that a Class R LOSDA can be considered.

### Why so short?

Because the risk is low, the fee is zero, and university legal offices need documents they can
read in five minutes. Class A is deliberately minimal.

---

## Part 2 — Class R, research testbed

**LOSDA ID:** `LOSDA-UNIDHAKA-2026-000013`
**Status on issue:** ACTIVE

### Parties (Class R)

| Role | Value |
|---|---|
| Issuer | OpenLedger Foundation (`OPENLEDGER`) |
| Licensee | University of Dhaka — CSE, Distributed Systems Research Group |
| Country | Bangladesh |
| Contact | dsrg@du.example |

### Scope (Class R)

| Field | Value |
|---|---|
| Class | **R** — Research |
| Deployment type | Research testbed serving external research participants |
| Territory | Worldwide (participants only; hosting in Bangladesh) |
| Field of use | The "LatencyLab" study measuring consensus latency across participating institutions. Participants interact only through a research interface; no commercial service is offered. |
| Scale | 300 participants; 1 instance |
| Fee | **None** |

### Ethics statement (required for Class R)

> The study has been approved by the University of Dhaka Institutional Review Board (ref
> DU-IRB-2026-118). Participants receive an information sheet and give informed consent.
> Telemetry collected is limited to latency measurements and a pseudonymous participant ID. No
> personal data is published. Results are reported in aggregate.

### Data handling plan (required for Class R)

| Item | Detail |
|---|---|
| Categories of data | Latency measurements; pseudonymous participant identifiers |
| Lawful basis | Consent |
| Retention | 24 months from study close |
| Storage | Encrypted, access-controlled, hosted in Bangladesh |
| Publication | Aggregate only; no re-identification by combination |

### Conditions (Class R)

| Code | Applied | Notes |
|---|---|---|
| C1 notices | Yes | |
| C3 territory and field | Yes | |
| C6 security incident | Yes | Within 72 hours |
| C8 records | Yes | |
| C9 no hostile IP | Yes | |
| C14 ethics policy | Yes | Prohibited uses apply |

### Bespoke conditions (Class R)

1. The testbed must not be advertised as a production service.
2. The Licensee must publish the study results, including negative results, within 18 months.
3. If the study pivots to commercial application, the Licensee must apply for a Class S or H
   LOSDA before continuing.

---

## What these examples demonstrate

| Principle | Demonstration |
|---|---|
| No-fee classes are real | Both are zero-fee and issued in days, not weeks |
| Risk-appropriate length | Class A is half a page of terms; Class R adds only the ethics and data sections |
| Research is protected but bounded | The testbed is allowed; commercial spin-out requires a new class |
| Attribution survives | Students and participants see the author's name |
| The framework is usable by public institutions | No procurement nightmare, no cost, no legal escalation |
