#!/usr/bin/env python3
"""Compute and verify the canonical record hash of a LOSDA record.

Canonical form (LOSDA specification section 6):
  * JSON with keys sorted lexicographically
  * UTF-8 encoding
  * no insignificant whitespace (separators are ',' and ':')
  * arrays kept in declared order
  * timestamps in RFC 3339 with 'Z'
  * the hash field itself excluded from the digest

Usage:
    python3 scripts/hash_record.py examples/losda-record.json
    python3 scripts/hash_record.py examples/losda-record.json --verify
    python3 scripts/hash_record.py examples/losda-record.json --canonical

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
from typing import Any


def canonical_bytes(record: dict[str, Any], drop_hash: bool = True) -> bytes:
    """Return the canonical byte form that is hashed.

    The record hash is excluded so that a record can carry its own digest without a
    chicken-and-egg problem. Everything else is included, including status_history.
    """
    clone = json.loads(json.dumps(record))  # deep copy through JSON

    if drop_hash:
        registry = clone.get("registry")
        if isinstance(registry, dict):
            registry.pop("record_hash", None)
            registry.pop("verification_url", None)

    return json.dumps(
        clone,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")


def record_hash(record: dict[str, Any], drop_hash: bool = True) -> str:
    return hashlib.sha256(canonical_bytes(record, drop_hash=drop_hash)).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compute or verify a LOSDA record hash.")
    parser.add_argument("path", type=pathlib.Path)
    parser.add_argument("--verify", action="store_true", help="compare against the stored hash")
    parser.add_argument("--canonical", action="store_true", help="print the canonical JSON")
    parser.add_argument(
        "--include-hash",
        action="store_true",
        help="include the stored hash in the digest (rarely useful)",
    )
    args = parser.parse_args(argv)

    if not args.path.exists():
        print(f"error: {args.path} not found", file=sys.stderr)
        return 2

    record = json.loads(args.path.read_text(encoding="utf-8"))
    if not isinstance(record, dict):
        print("error: top-level JSON must be an object", file=sys.stderr)
        return 2

    if args.canonical:
        print(canonical_bytes(record, drop_hash=not args.include_hash).decode("utf-8"))
        return 0

    digest = record_hash(record, drop_hash=not args.include_hash)

    if args.verify:
        stored = (record.get("registry") or {}).get("record_hash")
        print(f"computed: {digest}")
        print(f"stored:   {stored}")
        if stored == digest:
            print("MATCH — the record is unaltered")
            return 0
        if stored and set(str(stored)) == {"0"}:
            print("MISMATCH — the stored hash is a placeholder, not a real digest")
            return 1
        print("MISMATCH — the record has been altered since it was recorded")
        return 1

    print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
