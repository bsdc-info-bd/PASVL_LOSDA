# RFC 0002 — Hash chain and monthly Merkle root for the registry

| Field | Value |
|---|---|
| RFC number | 0002 |
| Title | Hash chain and monthly Merkle root for the registry |
| Author(s) | Registry Custodian |
| Status | **Accepted** |
| Class | Minor (strengthens an existing process; changes no rights) |
| Created | 2025-10-01 |
| Sponsor | License Council |
| Comment period | 2025-10-10 to 2025-11-09 (30 days) |
| Decision date | 2025-11-20 |
| Effective | 2026-01-01 |

---

## 1. Summary

Make the registry tamper-evident by (a) storing a SHA-256 hash in every record, (b) chaining each
record to its predecessor, and (c) publishing a Merkle root of the whole registry every month.
Any retrospective edit becomes detectable by anyone, without trusting the Custodian.

## 2. Problem statement

An append-only registry is only trustworthy if append-only can be verified. A git history helps,
but a custodian with write access can rewrite history on a self-hosted mirror, and a third party
has no practical way to notice.

Concretely, without a digest:

- A revoked LOSDA could be quietly returned to `active`.
- A record could be deleted and the statistics adjusted.
- A correction could be made silently instead of as a new entry.
- A forged letter could be presented alongside an edited registry.

Third parties today must trust the Custodian. That is too much trust to ask for a permission
system whose entire purpose is verifiability.

## 3. Proposed text

Additions to `governance/REGISTRY-POLICY.md` §3.3 and §6:

- `registry.record_hash`: SHA-256 over the canonical JSON form of the record, excluding
  `registry.record_hash` and `registry.verification_url`.
- `registry.previous_hash`: the `record_hash` of the preceding record.
- `merkle_root`: a SHA-256 Merkle root over the sorted record hashes, published monthly by the
  5th, in `registry/losda-registry.json` and in a public announcement.
- `scripts/hash_record.py` for computation and verification.
- `scripts/validate_registry.py` rejects a published root that does not match the computed root.

Canonical form: JSON with sorted keys, UTF-8, `separators=(',', ':')`, arrays in declared order,
timestamps in RFC 3339 with `Z`.

## 4. Rationale

This is the cheapest available mechanism that converts "trust us" into "check for yourself":

1. **No infrastructure.** A hash is a hex string in a JSON file.
2. **No privacy cost.** Hashing reveals nothing.
3. **No new authority.** Verification is available to anyone with a text editor or the script.
4. **Detects the attacks that matter.** Retrospective edits, deletions, and silent corrections.
5. **Complements git.** Signed tags and a second mirror make rewriting history harder; the Merkle
   root makes it detectable even if the history is rewritten.

The monthly cadence is a compromise: daily roots would be more precise, but publication must be
sustainable by a volunteer steward.

## 5. Effects

| Party | Effect |
|---|---|
| Authors | No change |
| Licensees | Can verify their own record independently |
| Contributors | No change |
| The registry | Two fields per record, one monthly publication, one validation step in CI |
| Existing LOSDAs | None — fields are additive; existing records are hashed on first publication |
| The Steward | A recurring publication obligation, with a defined missed-publication consequence |

## 6. Compatibility and migration

- The schema change is additive; records without `previous_hash` remain valid.
- The first publication hashes every existing record and publishes a root.
- A record whose hash does not match after publication is treated as an incident, not a correction.

## 7. Alternatives considered

| Alternative | Why rejected |
|---|---|
| **Rely on git history** | A custodian can rewrite a self-hosted mirror; a third party may not notice |
| **Blockchain anchoring** | Disproportionate cost, environmental and governance baggage, and no real advantage over a published digest with an independent mirror |
| **Transparency log (Certificate Transparency style)** | Better long-term, but requires infrastructure and third-party log operators that do not yet exist for this framework. Revisit in a later RFC |
| **Digital signatures only** | Signing the registry daily is more operational work than a digest, and still depends on key custody |
| **Do nothing** | Fails the framework's core promise of verifiability |

## 8. Who this hurts

1. **The Custodian**, who now has a monthly obligation and a public failure mode if a root is
   missed. This is intentional: a verifiable registry is worth more than a convenient one.
2. **Authors who want to make a quiet correction.** Silent edits become detectable. Corrections
   must be made openly, which is the correct trade.
3. **Anyone relying on no downtime.** A hash mismatch freezes status changes until resolved.

## 9. Legal review

| Question | Answer |
|---|---|
| Does this change rights? | No. It strengthens evidence; it grants and removes nothing |
| Jurisdictions reviewed | Not jurisdiction-specific |
| Enforceability concerns | None; it is a record-keeping control |
| Advice obtained | None required |

## 10. Implementation plan

1. Add the fields to the schema. ✅
2. Publish `hash_record.py` and the canonical-form definition. ✅
3. Add validation in CI, including a root check. ✅
4. Publish the first root with the first non-empty registry. ☐
5. Publish monthly, and note missed publications in the transparency report. ☐

## 11. Open questions

1. Should the root be published more often than monthly once there are more than 1,000 records?
   Likely yes; revisit with data.
2. Should a second, independent party co-sign the root? Recommended once a partner is available.

## 12. Decision

| Field | Value |
|---|---|
| Outcome | **Accepted** |
| Vote | For: 6 · Against: 0 · Abstain: 1 |
| Reasons | Cheap, effective, privacy-preserving, and consistent with the framework's promise |
| Effective date | 2026-01-01 |
| Review date | 2027-01-01 |
