# Versioning

Three things are versioned in this repository, and confusing them causes real problems.

## 1. The three version numbers

| Thing | Format | Example | Meaning |
|---|---|---|---|
| **License** | `PASVL-<major>.<minor>[.<patch>]` | `PASVL-1.0` | The legal text |
| **LOSDA specification** | `LOSDA-<major>.<minor>[.<patch>]` | `LOSDA-1.0` | The permission instrument's operating rules |
| **Schema** | `losda-v<major>.schema.json` | `losda-v1.schema.json` | The machine-readable record format |
| **Templates** | `<NAME>-<major>.<minor>` | `LOSDA-TEMPLATE-1.0` | The forms |
| **Registry** | SemVer + date | `2026.10.0` | The dataset |

## 2. What each number means

### 2.1 Major

A major change **may alter rights**. Examples:

- adding or removing a permission;
- changing the deployment model;
- changing the revocation grounds;
- changing the governing law;
- changing the required fields of a LOSDA.

A major license change applies only to **new releases** and **new LOSDAs** (§26.3). Existing
grants are unaffected unless the licensee opts in.

### 2.2 Minor

A minor change **adds** something without altering existing rights:

- a new no-fee class;
- a clarification that resolves an ambiguity in favor of the licensee;
- a new process with a longer deadline;
- a new optional condition code.

### 2.3 Patch

Editorial only: typos, links, examples, formatting. No change in meaning.

## 3. Which version applies to me?

```
Read the work's NOTICE
        │
        ├─ States a license version? ──► That version governs your use of that release
        │
        └─ Silent? ──► The version published when your copy of the release was made
```

A LOSDA states its own version. Its terms govern that licensee for that permission.

## 4. The compatibility promise

Within a major version:

1. Rights will not be reduced.
2. Required LOSDA fields will not be added (only optional ones).
3. The schema will remain backward compatible.
4. Existing records will remain valid.

Across a major version:

1. A migration note will be published.
2. A schema converter will be provided where the record format changes.
3. Existing LOSDAs remain valid for their term.
4. Licensees may opt into the new version.

## 5. How to pin a version

**In a NOTICE**

```
License: PASVL-1.0
```

**In a source header**

```
SPDX-License-Identifier: LicenseRef-PASVL-1.0
```

**In a LOSDA**

```
license_version: "1.0"
losda_version: "1.0"
```

**In a Registry record**

```json
{ "version": "LOSDA-1.0", "license_version": "PASVL-1.0" }
```

## 6. Deprecation

1. A version is deprecated when a successor is published.
2. Deprecated versions remain valid for existing works and LOSDAs.
3. Security-related corrections may be backported to a deprecated version.
4. "Deprecated" does not mean "invalid" and does not withdraw any grant.

## 7. Release cadence

| Document | Review | Typical change |
|---|---|---|
| License | Annual, or on a Major RFC | Patch most years; Major rarely |
| LOSDA specification | Annual | Minor |
| Schema | With the specification | Additive |
| Templates | As needed | Editorial |
| Registry | Continuous | Data |

## 8. Registry versioning

The Registry is a dataset, not a license. Its releases are tagged:

```
registry-2026.10.0
```

The tag is signed. Every monthly release publishes a Merkle root of all records. A verifier can
reconstruct the chain and detect any retrospective edit.

## 9. What never changes retrospectively

- The rights of the public in a released version.
- The validity of a recorded LOSDA for its stated term.
- The record of an enforcement action (it may be annotated, never deleted).
- A signature's meaning: a document signed under 1.0 remains a 1.0 document.

## 10. Reporting a versioning problem

If you believe a change has altered rights without a major version bump, raise it with the
Appeals Panel under `governance/APPEALS.md` as a procedural challenge. This is a serious
allegation and will be investigated promptly.
