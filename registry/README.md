# The LOSDA Registry

The public, append-only record of who may deploy what.

## 1. Why it exists

A permission that cannot be verified is not a permission. The Registry lets anyone — a customer,
an auditor, a regulator, a competitor — confirm in seconds that a deployment is authorised, for
what scope, and until when.

## 2. Files

| File | Purpose |
|---|---|
| [`losda-registry.json`](losda-registry.json) | Every LOSDA and its current status |
| [`issuers.json`](issuers.json) | Registered issuer codes and their authority |
| [`works.json`](works.json) | Works that have adopted the framework |
| [`enforcement-register.json`](enforcement-register.json) | Enforcement actions from Stage 2 upwards |
| `keys/` | Public keys for verifying issuer signatures |

## 3. How to verify a LOSDA

1. Open `losda-registry.json`.
2. Find the record with the matching `losda_id`.
3. Check `status`. It must be `active`.
4. Check that `end_date` has not passed (or `perpetual` is true).
5. Check that the scope covers the deployment you are looking at.
6. Compare the `record_hash` with the hash printed on the signed letter.

If the status is `suspended`, `revoked`, `expired`, `superseded`, `withdrawn`, or `void`, the
permission is not currently valid. A `suspended` record may return to `active`; a `revoked` one
will not, except on reinstatement.

## 4. Status meanings

| Status | Meaning | Reliance |
|---|---|---|
| `pending` | Issued but not yet effective | Do not rely |
| `active` | Valid permission | Rely within scope |
| `suspended` | Temporarily withdrawn pending investigation | Do not rely |
| `expired` | Term ended | Do not rely |
| `revoked` | Withdrawn for cause | Do not rely |
| `superseded` | Replaced by an amendment | Rely on the successor |
| `withdrawn` | Surrendered by the licensee | Do not rely |
| `void` | Never valid, or fraudulent | Do not rely; report |

## 5. Rules for the registry

1. **Append-only.** Nothing is deleted. Corrections are new entries.
2. **Hashed.** Each record carries a SHA-256 hash of its canonical JSON form.
3. **Chained.** Records may reference the previous hash to detect insertion or reordering.
4. **Monthly Merkle root.** A digest of the whole registry is published by the 5th of each month.
5. **Signed releases.** Registry tags are signed.
6. **Reviewed writes.** Every write is reviewed by a second custodian.

Full policy: [`../governance/REGISTRY-POLICY.md`](../governance/REGISTRY-POLICY.md).

## 6. Privacy

The registry publishes the minimum needed to make a permission verifiable. It does not publish
fees, personal contact details, identity numbers, or confidential annex contents. A licensee may
request an anonymised listing.

See [`../legal/privacy-policy.md`](../legal/privacy-policy.md).

## 7. Running your own registry

An author who does not want to use the public registry may keep a registry in their own
repository, using the same JSON format and schema
([`../schemas/registry-v1.schema.json`](../schemas/registry-v1.schema.json)). If you do:

- publish the URL in your NOTICE;
- keep it append-only;
- sign the releases;
- follow the same status values.

Authors who want global verifiability should register with the Steward.

## 8. Correcting an error

Use the process in [`../governance/REGISTRY-POLICY.md`](../governance/REGISTRY-POLICY.md) §7. Do
not edit a record silently; a correction is a new entry.

## 9. Fraud

A forged LOSDA, an altered letter, or a false registry claim may be criminal. Report it with
[`../templates/VIOLATION-REPORT.md`](../templates/VIOLATION-REPORT.md). The Steward will publish
a fraud notice and, where appropriate, notify platforms and authorities.
