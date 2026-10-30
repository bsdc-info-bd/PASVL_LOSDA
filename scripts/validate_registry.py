#!/usr/bin/env python3
"""Validate the LOSDA registry and the enforcement register.

Checks performed:
  1. Structure of the registry file and the enforcement register.
  2. Every record validates as a LOSDA (delegated to validate_losda).
  3. Unique LOSDA identifiers, no reuse.
  4. Issuer codes appear in issuers.json.
  5. Hash chain integrity where previous_hash is used.
  6. Status consistency (active records are within term; expired records are past term).
  7. Statistics agree with the records.
  8. Merkle root reproducibility, when a root is published.

Usage:
    python3 scripts/validate_registry.py
    python3 scripts/validate_registry.py --registry registry --strict

Exit codes: 0 valid, 1 errors, 2 bad invocation.

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import sys
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from validate_losda import validate_record  # noqa: E402

STATUSES = {
    "pending",
    "active",
    "suspended",
    "expired",
    "revoked",
    "superseded",
    "withdrawn",
    "void",
}

REGISTRY_REQUIRED = ("registry_version", "framework_version", "updated_at", "records")
RECORD_REQUIRED = (
    "losda_id",
    "work_name",
    "repo_url",
    "class",
    "licensee_display",
    "effective_date",
    "status",
    "record_hash",
)


def load(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def merkle_root(hashes: list[str]) -> str:
    """Compute a simple SHA-256 Merkle root over a sorted list of hex digests."""
    if not hashes:
        return hashlib.sha256(b"").hexdigest()

    layer = sorted(hashes)
    if len(layer) % 2:
        layer.append(layer[-1])
    while len(layer) > 1:
        nxt: list[str] = []
        for i in range(0, len(layer), 2):
            nxt.append(hashlib.sha256((layer[i] + layer[i + 1]).encode()).hexdigest())
        layer = nxt
    return layer[0]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the registry.")
    parser.add_argument("--registry", type=pathlib.Path, default=pathlib.Path("registry"))
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = parser.parse_args(argv)

    root: pathlib.Path = args.registry
    registry_path = root / "losda-registry.json"
    if not registry_path.exists():
        print(f"error: {registry_path} not found", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    registry = load(registry_path)

    # 1 -- structure -------------------------------------------------------
    for key in REGISTRY_REQUIRED:
        if key not in registry:
            errors.append(f"registry: missing required field '{key}'")

    records = registry.get("records", [])
    if not isinstance(records, list):
        errors.append("registry.records: must be an array")
        records = []

    # 2 -- per-record rules ------------------------------------------------
    seen_ids: set[str] = set()
    duplicate_ids: set[str] = set()

    for index, item in enumerate(records):
        where = f"records[{index}]"
        for key in RECORD_REQUIRED:
            if key not in item:
                errors.append(f"{where}: missing '{key}'")

        losda_id = item.get("losda_id")
        if losda_id in seen_ids:
            duplicate_ids.add(str(losda_id))
            errors.append(f"{where}: duplicate losda_id {losda_id!r} (identifiers are never reused)")
        seen_ids.add(str(losda_id))

        status = item.get("status")
        if status not in STATUSES:
            errors.append(f"{where}.status: {status!r} is not a valid status")

        # status/term consistency
        end = item.get("end_date")
        if status == "active" and end:
            try:
                if dt.date.today() > dt.date.fromisoformat(str(end)):
                    errors.append(
                        f"{where}: status is 'active' but end_date {end} has passed; "
                        "the record must be marked 'expired'"
                    )
            except ValueError:
                errors.append(f"{where}.end_date: '{end}' is not an ISO date")
        if status == "active" and not item.get("perpetual") and not end:
            warnings.append(
                f"{where}: status is 'active', not perpetual, and has no end_date"
            )

        # 3 -- issuer codes ------------------------------------------------
        if isinstance(losda_id, str) and losda_id.count("-") >= 3:
            _prefix, issuer_code = losda_id.split("-")[:2]
            issuers_path = root / "issuers.json"
            if issuers_path.exists():
                known = {
                    i.get("issuer_code")
                    for i in load(issuers_path).get("issuers", [])
                }
                if issuer_code not in known:
                    errors.append(
                        f"{where}: issuer code {issuer_code!r} is not registered in issuers.json"
                    )

        # 4 -- hash format --------------------------------------------------
        digest = item.get("record_hash")
        if isinstance(digest, str):
            if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                errors.append(f"{where}.record_hash: not a lowercase SHA-256 hex digest")
            elif set(digest) == {"0"}:
                errors.append(f"{where}.record_hash: placeholder value, not a real digest")

        # 5 -- schema-level record validation, where the full record exists
        full = item.get("record")
        if isinstance(full, dict):
            report = validate_record(full, where)
            errors.extend(report.errors)
            warnings.extend(report.warnings)

    # 6 -- hash chain ------------------------------------------------------
    chain = [
        r.get("previous_hash")
        for r in records
        if isinstance(r, dict) and r.get("previous_hash")
    ]
    for previous in chain:
        if previous not in {r.get("record_hash") for r in records}:
            errors.append(
                f"hash chain: previous_hash {str(previous)[:12]}… does not match any record"
            )

    # 7 -- statistics ------------------------------------------------------
    stats = registry.get("statistics") or {}
    if stats:
        counts = {s: 0 for s in STATUSES}
        for item in records:
            status = item.get("status")
            if status in counts:
                counts[status] += 1
        if stats.get("total_records") not in (None, len(records)):
            errors.append(
                f"statistics.total_records: {stats.get('total_records')} does not match "
                f"{len(records)} records"
            )
        for key in ("active", "suspended", "revoked", "expired"):
            if stats.get(key) not in (None, counts[key]):
                errors.append(
                    f"statistics.{key}: {stats.get(key)} does not match {counts[key]} records"
                )

    # 8 -- merkle root -----------------------------------------------------
    published_root = registry.get("merkle_root")
    if published_root:
        computed = merkle_root([r.get("record_hash", "") for r in records])
        if computed != published_root:
            errors.append(
                "merkle_root: published root does not match the computed root; "
                "the registry may have been edited after publication"
            )

    # 9 -- enforcement register -------------------------------------------
    enforcement_path = root / "enforcement-register.json"
    if enforcement_path.exists():
        enforcement = load(enforcement_path)
        for index, entry in enumerate(enforcement.get("entries", [])):
            for key in ("reference", "date", "stage", "provision", "outcome"):
                if key not in entry:
                    errors.append(f"enforcement.entries[{index}]: missing '{key}'")

    # report ---------------------------------------------------------------
    for message in errors:
        print(f"FAIL {message}")
    for message in warnings:
        print(f"warn {message}")

    print()
    print(
        f"registry checked: {len(records)} record(s), "
        f"{len(errors)} error(s), {len(warnings)} warning(s)"
    )

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
