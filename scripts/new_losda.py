#!/usr/bin/env python3
"""Scaffold a new LOSDA record and print the canonical hash.

This script does not issue a permission. It produces a draft JSON record that an issuer
fills in, signs, and records. Nothing here is valid until a human signs it and a registry
custodian records it.

Usage:
    python3 scripts/new_losda.py --issuer ACME --class H \\
        --work "Acme Scheduler" --repo https://github.com/acmelabs/scheduler \\
        --licensee "Cloudscale Systems Inc." --country "United States" \\
        --out drafts/cloudscale.json

    python3 scripts/new_losda.py --next-serial ACME --registry registry

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from hash_record import record_hash  # noqa: E402

CLASS_LABELS = {
    "S": "Standard Commercial",
    "E": "Enterprise / Portfolio",
    "I": "Internal Use",
    "H": "Hosted Service / SaaS",
    "D": "Distribution / OEM / Embedded",
    "A": "Academic / Non-Commercial",
    "G": "Government / Public Sector",
    "P": "Public Interest",
    "R": "Research",
    "X": "Evaluation Extension",
    "C": "Continuity",
    "M": "Machine Learning / AI Data",
    "O": "Open Deployment",
}

DEFAULT_TERMS = {
    "S": 365,
    "E": 1095,
    "I": 365,
    "H": 365,
    "D": 365,
    "A": 730,
    "G": 730,
    "P": 365,
    "R": 365,
    "X": 90,
    "C": 365,
    "M": 365,
    "O": None,  # standing public grant
}

DEFAULT_CONDITIONS = {
    "S": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
    "E": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C13", "C15"],
    "I": ["C1", "C2", "C3", "C4", "C5", "C7", "C9"],
    "H": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C13"],
    "D": ["C1", "C2", "C3", "C5", "C6", "C8", "C9", "C12"],
    "A": ["C1", "C2", "C3", "C7", "C9"],
    "G": ["C1", "C2", "C3", "C6", "C7", "C15"],
    "P": ["C1", "C2", "C3", "C7"],
    "R": ["C1", "C3", "C6", "C8", "C9", "C14"],
    "X": ["C1", "C3", "C7"],
    "C": ["C1", "C2", "C3", "C6", "C7", "C15"],
    "M": ["C1", "C3", "C5", "C7", "C8", "C9", "C10", "C11"],
    "O": ["C1", "C2", "C3", "C7"],
}

NO_FEE_CLASSES = {"A", "G", "P", "R", "X", "C"}


def next_serial(registry: pathlib.Path, issuer: str, year: int) -> int:
    """Return the next free serial for an issuer and year."""
    used: set[int] = set()
    registry_file = registry / "losda-registry.json"
    if registry_file.exists():
        payload = json.loads(registry_file.read_text(encoding="utf-8"))
        pattern = re.compile(rf"^LOSDA-{re.escape(issuer)}-{year}-(\d{{6}})$")
        for record in payload.get("records", []):
            match = pattern.match(str(record.get("losda_id", "")))
            if match:
                used.add(int(match.group(1)))
    return (max(used) + 1) if used else 1


def build_record(args: argparse.Namespace) -> dict:
    today = dt.date.today()
    if args.serial is not None:
        serial = args.serial
    else:
        serial = next_serial(args.registry, args.issuer, today.year)

    losda_id = f"LOSDA-{args.issuer}-{today.year}-{serial:06d}"

    days = DEFAULT_TERMS.get(args.klass) if args.days is None else args.days
    start = dt.date.fromisoformat(args.start) if args.start else today
    end = None if days is None else (start + dt.timedelta(days=days)).isoformat()

    payable = args.klass not in NO_FEE_CLASSES and args.fee is not None

    record = {
        "losda_id": losda_id,
        "version": "LOSDA-1.0",
        "license_version": "1.0",
        "class": args.klass,
        "class_label": CLASS_LABELS[args.klass],
        "work": {
            "name": args.work,
            "repo_url": args.repo,
            "commit": args.commit or "",
            "version_range": args.version_range or "",
            "notice_url": args.notice_url or "",
        },
        "issuer": {
            "legal_name": args.issuer_name or args.issuer,
            "issuer_code": args.issuer,
            "capacity": args.capacity,
            "country": args.issuer_country,
            "signatory": args.signatory or "",
            "contact": args.issuer_contact or "",
        },
        "licensee": {
            "legal_name": args.licensee,
            "display_name": args.display_name or args.licensee,
            "entity_type": args.entity_type,
            "registration_number": args.registration or "",
            "country": args.country,
            "anonymised": bool(args.anonymise),
            "affiliates_covered": [],
        },
        "scope": {
            "deployment_types": args.deployment_type,
            "territory": args.territory,
            "field_of_use": args.field_of_use or "TO BE COMPLETED",
            "scale": {
                "end_users": args.end_users,
                "seats": args.seats,
                "instances": args.instances,
                "devices": args.devices,
                "monthly_api_requests": args.api_requests,
                "revenue_threshold_usd": 0,
                "unlimited": bool(args.unlimited),
            },
            "excluded_uses": [],
            "sublicensing_permitted": False,
            "service_bureau_permitted": False,
            "modifications_permitted": True,
        },
        "conditions": {
            "codes": DEFAULT_CONDITIONS[args.klass],
            "bespoke": [],
            "ethics_policy_incorporated": bool(args.ethics),
        },
        "fees": {
            "payable": payable,
            "amount": args.fee if payable else 0,
            "currency": args.currency,
            "basis": "annual" if payable else "none",
            "confidential": bool(args.fee_confidential),
            "refund_policy": "",
        },
        "term": {
            "start": start.isoformat(),
            "end": end,
            "perpetual": end is None,
            "renewal": "by_application",
            "reliance_period_days": 180,
        },
        "effective_date": start.isoformat(),
        "status": "pending",
        "status_history": [],
        "signature": {
            "method": "none",
            "signatory": "",
            "date": None,
            "key_fingerprint": None,
        },
        "registry": {
            "record_hash": "0" * 64,
            "previous_hash": None,
            "recorded_at": dt.datetime.now(dt.timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z"),
            "recorded_by": "",
            "verification_url": (
                "https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/"
                f"registry/losda-registry.json#{losda_id}"
            ),
        },
        "confidential_annex": {"exists": False, "contents": []},
        "notes": (
            "DRAFT generated by scripts/new_losda.py. This is not a permission. "
            "It is void unless signed by an authorised issuer and recorded by a "
            "registry custodian. Complete field_of_use, set signature.method, "
            "and recompute the record_hash before recording."
        ),
    }

    record["registry"]["record_hash"] = record_hash(record)
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold a LOSDA record. Produces a draft, never a permission."
    )
    parser.add_argument("--issuer", required=False, help="issuer code, e.g. ACME")
    parser.add_argument("--issuer-name", help="issuer legal name")
    parser.add_argument("--issuer-country", default="Bangladesh")
    parser.add_argument("--issuer-contact", help="licensing contact email")
    parser.add_argument("--signatory", help="name and title of the signatory")
    parser.add_argument(
        "--capacity",
        default="author",
        choices=[
            "author",
            "co-author",
            "authorised_agent",
            "steward_continuity",
            "steward_extension",
        ],
    )
    parser.add_argument("--class", dest="klass", required=False, choices=sorted(CLASS_LABELS))
    parser.add_argument("--work", help="name of the licensed work")
    parser.add_argument("--repo", help="repository URL")
    parser.add_argument("--commit")
    parser.add_argument("--version-range")
    parser.add_argument("--notice-url")
    parser.add_argument("--licensee", help="licensee legal name")
    parser.add_argument("--display-name")
    parser.add_argument(
        "--entity-type",
        default="company",
        choices=[
            "natural_person",
            "company",
            "non_profit",
            "government",
            "university",
            "consortium",
            "other",
        ],
    )
    parser.add_argument("--registration")
    parser.add_argument("--country", help="licensee country")
    parser.add_argument("--anonymise", action="store_true")
    parser.add_argument(
        "--deployment-type",
        action="append",
        choices=[
            "internal",
            "customer_facing",
            "hosted_service",
            "embedded",
            "distributed_binary",
            "ml_training",
            "ml_evaluation",
            "research_testbed",
            "open_deployment",
        ],
        help="repeatable",
    )
    parser.add_argument("--territory", action="append", help="repeatable; defaults to Worldwide")
    parser.add_argument("--field-of-use")
    parser.add_argument("--end-users", type=int, default=0)
    parser.add_argument("--seats", type=int, default=0)
    parser.add_argument("--instances", type=int, default=0)
    parser.add_argument("--devices", type=int, default=0)
    parser.add_argument("--api-requests", type=int, default=0)
    parser.add_argument("--unlimited", action="store_true")
    parser.add_argument("--fee", type=float)
    parser.add_argument("--currency", default="USD")
    parser.add_argument("--fee-confidential", action="store_true")
    parser.add_argument("--ethics", action="store_true")
    parser.add_argument("--start", help="YYYY-MM-DD; defaults to today")
    parser.add_argument("--days", type=int, help="term length; defaults per class")
    parser.add_argument("--serial", type=int, help="override the serial number")
    parser.add_argument("--registry", type=pathlib.Path, default=pathlib.Path("registry"))
    parser.add_argument("--out", type=pathlib.Path, help="write the record to this file")
    parser.add_argument(
        "--next-serial",
        metavar="ISSUER",
        help="print the next free serial for an issuer and exit",
    )
    args = parser.parse_args(argv)

    if args.next_serial:
        serial = next_serial(args.registry, args.next_serial, dt.date.today().year)
        print(f"{serial:06d}")
        return 0

    missing = [
        flag
        for flag, value in (
            ("--issuer", args.issuer),
            ("--class", args.klass),
            ("--work", args.work),
            ("--repo", args.repo),
            ("--licensee", args.licensee),
            ("--country", args.country),
        )
        if not value
    ]
    if missing:
        print(f"error: missing required option(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    if not args.issuer.isupper():
        print("error: --issuer must be uppercase", file=sys.stderr)
        return 2

    args.deployment_type = args.deployment_type or ["internal"]
    args.territory = args.territory or ["Worldwide"]

    record = build_record(args)
    payload = json.dumps(record, indent=2, ensure_ascii=False) + "\n"

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
        print(f"draft written to {args.out}")
        print(f"losda_id:     {record['losda_id']}")
        print(f"record_hash:  {record['registry']['record_hash']}")
        print()
        print("NEXT STEPS")
        print("  1. Complete scope.field_of_use and any bespoke conditions.")
        print("  2. Set signature.method and signatory, then sign the record.")
        print("  3. Recompute the hash:  python3 scripts/hash_record.py <file>")
        print("  4. Set status to 'active' and effective_date correctly.")
        print("  5. Give the record to the Registry Custodian to record.")
        print("  A draft is not a permission. Deployment before recording is a violation.")
    else:
        print(payload)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
