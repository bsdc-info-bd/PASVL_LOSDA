# Scripts

Small, dependency-free tools that keep the framework honest. Everything here is standard-library
Python 3.9+; nothing needs installing.

## Tools

| Script | What it does |
|---|---|
| [`validate_losda.py`](validate_losda.py) | Validates a LOSDA record against the rules that make it legally effective |
| [`validate_registry.py`](validate_registry.py) | Validates the registry: identity, status, hash chain, statistics, Merkle root |
| [`hash_record.py`](hash_record.py) | Computes or verifies the canonical SHA-256 record hash |
| [`new_losda.py`](new_losda.py) | Scaffolds a draft record and prints its hash — it does not issue a permission |
| [`check_license_headers.py`](check_license_headers.py) | Fails CI when a source file lacks a PASVL license header |

## Quick start

```bash
# Validate an example record
python3 scripts/validate_losda.py examples/losda-record.json --single

# Validate the whole registry
python3 scripts/validate_registry.py

# Compute a record hash
python3 scripts/hash_record.py examples/losda-record.json

# Verify a stored hash
python3 scripts/hash_record.py examples/losda-record.json --verify

# Scaffold a draft Class H record
python3 scripts/new_losda.py \
  --issuer ACME --issuer-name "Acme Labs Ltd" --class H \
  --work "Acme Scheduler" --repo https://github.com/acmelabs/scheduler \
  --licensee "Example Corp" --country "United Kingdom" \
  --deployment-type hosted_service --field-of-use "Managed workflow product" \
  --end-users 50000 --fee 60000 \
  --out drafts/example.json

# Check license headers across the repository
python3 scripts/check_license_headers.py --path . --allow-missing README.md
```

## Tests

```bash
python3 -m pytest scripts/tests -q
# or, with no dependencies:
python3 scripts/tests/test_validators.py
```

## What the validators enforce

The validators implement the LOSDA specification, not merely the JSON shape. In particular they
enforce the rules that make an instrument **void** if broken:

1. The identifier format `LOSDA-<ISSUER>-<YYYY>-<NNNNNN>`.
2. Every element required by PASVL Appendix A.
3. A recognized class from PASVL §10.14.
4. A recognized capacity to issue, and the rule that only `BSDC` may issue Continuity or
   Extension LOSDAs.
5. A signature that is not `none`.
6. A term that is stated: an end date, or an express perpetual grant — never neither.
7. An end date that follows the start date.
8. Defined condition codes (C1–C16).
9. A registered issuer code.
10. Status consistency: an `active` record cannot be past its term.

They also warn about the things that make an instrument weak rather than void: placeholder
hashes, missing scale limits, missing class-specific conditions, and a reliance period below the
180-day default.

## The canonical hash

```
canonical = JSON(
    sort_keys    = True,
    ensure_ascii = False,
    separators   = (",", ":"),
    encoded as   = UTF-8,
)
digest = SHA-256(canonical)
```

The `registry.record_hash` and `registry.verification_url` fields are excluded from the digest so
that a record can carry its own hash. Everything else, including `status_history`, is included.
Any alteration to the record changes the hash, which is how a forged or edited letter is
detected.

## Design rules

1. **Standard library only.** A validator you cannot run is not a validator.
2. **Fail loudly.** An invalid instrument must produce a non-zero exit code.
3. **No network access.** These tools never call home, never phone a license server, and never
   collect telemetry. That would contradict the framework.
4. **No silent fixes**, except in `--fix` mode for license headers, which is explicit.

## Adding a script

1. Standard library only, or justify the dependency in a pull request.
2. Use `argparse`, with `--help` text a non-expert can read.
3. Exit `0` on success, `1` on a validation failure, `2` on bad invocation.
4. Add a test in [`tests/`](tests/).
5. Add the PASVL header (the CI will check).
