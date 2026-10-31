#!/usr/bin/env python3
"""Validate LOSDA records against the rules in the LOSDA specification.

Usage:
    python3 scripts/validate_losda.py registry/losda-registry.json
    python3 scripts/validate_losda.py examples/losda-record.json --single
    python3 scripts/validate_losda.py path/to/records/ --recursive

Exit codes:
    0  all records valid
    1  at least one error
    2  bad invocation

The validator is deliberately dependency-free. It checks the rules that make a LOSDA
legally effective (LOSDA specification section 7 and 8), not merely the JSON shape.

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
from typing import Any, Iterable

LOSDA_ID_RE = re.compile(r"^LOSDA-[A-Z0-9]{3,8}-\d{4}-\d{6}$")
HASH_RE = re.compile(r"^[a-f0-9]{64}$")

# PASVL section 10.14 -- the closed set of classes.
CLASSES = {"S", "E", "I", "H", "D", "A", "G", "P", "R", "X", "C", "M", "O"}

# LOSDA specification section 10 -- condition codes.
CONDITION_CODES = {f"C{i}" for i in range(1, 17)}

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

DEPLOYMENT_TYPES = {
    "internal",
    "customer_facing",
    "hosted_service",
    "embedded",
    "distributed_binary",
    "ml_training",
    "ml_evaluation",
    "research_testbed",
    "open_deployment",
}

CAPACITIES = {
    "author",
    "co-author",
    "authorised_agent",
    "steward_continuity",
    "steward_extension",
}

# PASVL Appendix A -- a LOSDA missing any of these is void ab initio.
REQUIRED_MINIMUM = (
    "losda_id",
    "work",
    "issuer",
    "licensee",
    "class",
    "term",
    "effective_date",
    "signature",
    "registry",
)


class Report:
    """Collects errors and warnings for one record."""

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def _parse_date(value: Any, field: str, report: Report) -> dt.date | None:
    if not isinstance(value, str):
        report.error(f"{field}: expected an ISO date string, got {type(value).__name__}")
        return None
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        report.error(f"{field}: '{value}' is not an ISO 8601 date (YYYY-MM-DD)")
        return None


def _require(mapping: dict, key: str, where: str, report: Report) -> Any:
    if key not in mapping or mapping[key] in (None, "", []):
        report.error(f"{where}.{key}: required field is missing or empty")
        return None
    return mapping[key]


def validate_record(record: dict, where: str = "record") -> Report:
    """Validate one LOSDA record. Returns a Report; caller decides what to do with it."""

    if not isinstance(record, dict):
        report = Report(where)
        report.error(f"{where}: a LOSDA record must be a JSON object")
        return report

    identifier = str(record.get("losda_id", where))
    report = Report(identifier)

    for field in REQUIRED_MINIMUM:
        if field not in record:
            report.error(f"{field}: required by PASVL Appendix A; a LOSDA without it is void")

    # -- identifier ---------------------------------------------------------
    losda_id = record.get("losda_id")
    if losda_id is not None:
        if not isinstance(losda_id, str) or not LOSDA_ID_RE.match(losda_id):
            report.error(
                "losda_id: must match LOSDA-<ISSUER>-<YYYY>-<NNNNNN>, "
                f"got {losda_id!r}"
            )

    # -- versions -----------------------------------------------------------
    if record.get("version") not in (None, "LOSDA-1.0"):
        report.warn(
            f"version: {record.get('version')!r} is not LOSDA-1.0; "
            "check that the specification for that version is published"
        )

    # -- class --------------------------------------------------------------
    klass = record.get("class")
    if klass is not None and klass not in CLASSES:
        report.error(f"class: {klass!r} is not one of {sorted(CLASSES)}")

    # -- work ---------------------------------------------------------------
    work = record.get("work")
    if isinstance(work, dict):
        _require(work, "name", "work", report)
        repo = _require(work, "repo_url", "work", report)
        if repo is not None and not str(repo).startswith(("http://", "https://")):
            report.error("work.repo_url: must be an http(s) URL")
    elif work is not None:
        report.error("work: must be an object")

    # -- issuer -------------------------------------------------------------
    issuer = record.get("issuer")
    if isinstance(issuer, dict):
        _require(issuer, "legal_name", "issuer", report)
        code = _require(issuer, "issuer_code", "issuer", report)
        if code is not None and not re.match(r"^[A-Z0-9]{3,8}$", str(code)):
            report.error("issuer.issuer_code: must be 3-8 uppercase alphanumeric characters")
        capacity = issuer.get("capacity")
        if capacity is not None and capacity not in CAPACITIES:
            report.error(f"issuer.capacity: {capacity!r} is not a recognised capacity")
        if capacity in {"steward_continuity", "steward_extension"}:
            if str(code) != "BSDC":
                report.error(
                    "issuer.issuer_code: only the Steward (BSDC) may issue continuity "
                    "or extension LOSDAs (PASVL sections 9.2 and 6.5)"
                )
    elif issuer is not None:
        report.error("issuer: must be an object")

    # -- licensee -----------------------------------------------------------
    licensee = record.get("licensee")
    if isinstance(licensee, dict):
        _require(licensee, "legal_name", "licensee", report)
        if licensee.get("anonymised") and not licensee.get("display_name"):
            report.error(
                "licensee.display_name: an anonymised listing still needs a display "
                "identifier (privacy policy section 4)"
            )
    elif licensee is not None:
        report.error("licensee: must be an object")

    # -- scope --------------------------------------------------------------
    scope = record.get("scope")
    if isinstance(scope, dict):
        types = scope.get("deployment_types")
        if not types:
            report.error("scope.deployment_types: at least one deployment type is required")
        else:
            for item in types:
                if item not in DEPLOYMENT_TYPES:
                    report.error(f"scope.deployment_types: {item!r} is not recognised")
        territory = scope.get("territory")
        if not territory:
            report.error("scope.territory: at least one territory is required ('Worldwide' is valid)")
        _require(scope, "field_of_use", "scope", report)
        if klass in {"H", "M"} and not scope.get("field_of_use"):
            report.error(f"scope.field_of_use: required for class {klass}")

        scale = scope.get("scale") or {}
        if isinstance(scale, dict) and not scale.get("unlimited"):
            bounded = any(
                isinstance(scale.get(k), int)
                for k in ("end_users", "seats", "instances", "devices", "monthly_api_requests")
            )
            if not bounded and klass in {"S", "H", "E", "I"}:
                report.warn(
                    "scope.scale: no numeric limit and 'unlimited' is false; "
                    "condition C4 may be unenforceable"
                )
        if klass == "D" and not (scale or {}).get("devices"):
            report.warn("scope.scale.devices: class D usually states a device or unit limit")

        if scope.get("service_bureau_permitted") and not scope.get("sublicensing_permitted"):
            report.warn(
                "scope: Service Bureau Use usually requires sublicensing to be permitted as well"
            )
    elif scope is not None:
        report.error("scope: must be an object")

    # -- conditions ---------------------------------------------------------
    conditions = record.get("conditions")
    if isinstance(conditions, dict):
        for code in conditions.get("codes", []) or []:
            if code not in CONDITION_CODES:
                report.error(f"conditions.codes: {code!r} is not a defined condition code (C1-C16)")

    # -- term ---------------------------------------------------------------
    term = record.get("term")
    start = end = None
    if isinstance(term, dict):
        start = _parse_date(term.get("start"), "term.start", report) if term.get("start") else None
        if term.get("end"):
            end = _parse_date(term.get("end"), "term.end", report)
        if term.get("perpetual") and term.get("end"):
            report.error("term: a LOSDA cannot be both perpetual and have an end date")
        if not term.get("perpetual") and not term.get("end"):
            report.error("term.end: required unless term.perpetual is true")
        if start and end and end < start:
            report.error("term: end date precedes the start date")
        reliance = term.get("reliance_period_days", 180)
        if not isinstance(reliance, int) or reliance < 0:
            report.error("term.reliance_period_days: must be a non-negative integer")
        elif reliance < 180:
            report.warn(
                "term.reliance_period_days: less than the 180-day default in PASVL section 19.2; "
                "confirm the licensee agreed in writing"
            )
    elif term is not None:
        report.error("term: must be an object")

    # -- effective date -----------------------------------------------------
    effective = None
    if record.get("effective_date"):
        effective = _parse_date(record["effective_date"], "effective_date", report)
    if start and effective and effective < start:
        report.warn("effective_date: earlier than term.start; confirm this is intended")

    # -- status -------------------------------------------------------------
    status = record.get("status")
    if status is None:
        report.error("status: required")
    elif status not in STATUSES:
        report.error(f"status: {status!r} is not one of {sorted(STATUSES)}")
    else:
        if status == "active":
            if end and dt.date.today() > end:
                report.error("status: 'active' but the term has ended; the status must be 'expired'")
            if effective and dt.date.today() < effective:
                report.warn("status: 'active' but the effective date is in the future")
        for entry in record.get("status_history", []) or []:
            if isinstance(entry, dict) and entry.get("to") not in STATUSES:
                report.error(f"status_history: {entry.get('to')!r} is not a valid status")

    # -- signature ----------------------------------------------------------
    signature = record.get("signature")
    if isinstance(signature, dict):
        method = _require(signature, "method", "signature", report)
        if method in {"none", None}:
            report.error("signature.method: an unsigned LOSDA is void (Appendix A, element A.17)")
        if method in {"pgp", "qualified_e_signature"} and not signature.get("key_fingerprint"):
            report.warn("signature.key_fingerprint: recommended for cryptographic signatures")
    elif signature is not None:
        report.error("signature: must be an object")

    # -- registry -----------------------------------------------------------
    registry = record.get("registry")
    if isinstance(registry, dict):
        _require(registry, "record_hash", "registry", report)
        _require(registry, "recorded_at", "registry", report)
        digest = registry.get("record_hash")
        if digest and not HASH_RE.match(str(digest)):
            report.error("registry.record_hash: must be 64 lowercase hexadecimal characters")
        elif digest and set(str(digest)) == {"0"}:
            report.warn(
                "registry.record_hash: all-zero placeholder; compute the real hash with "
                "scripts/hash_record.py before recording"
            )
        previous = registry.get("previous_hash")
        if previous is not None and not HASH_RE.match(str(previous)):
            report.error("registry.previous_hash: must be 64 lowercase hexadecimal characters or null")
    elif registry is not None:
        report.error("registry: must be an object")

    # -- fees ---------------------------------------------------------------
    fees = record.get("fees")
    if isinstance(fees, dict):
        if fees.get("payable") and fees.get("amount") in (None, 0) and fees.get("basis") != "negotiated":
            report.warn("fees: payable is true but no amount or negotiated basis is recorded")
        if fees.get("confidential") and not (record.get("confidential_annex") or {}).get("exists"):
            report.warn("fees.confidential: a confidential fee should be noted in confidential_annex")

    # -- class-specific advice ---------------------------------------------
    if klass == "M":
        if "C10" not in (conditions or {}).get("codes", []):
            report.warn("class M: condition C10 (model card and provenance) is strongly recommended")
        if "C11" not in (conditions or {}).get("codes", []):
            report.warn("class M: condition C11 (no output laundering) is strongly recommended")
    if klass == "D" and "C12" not in (conditions or {}).get("codes", []):
        report.warn("class D: condition C12 (security updates for distributed devices) is recommended")
    if klass == "H" and "C13" not in (conditions or {}).get("codes", []):
        report.warn("class H: condition C13 (sub-processor disclosure) is recommended")

    return report


def _iter_records(path: pathlib.Path, recursive: bool) -> Iterable[tuple[str, dict]]:
    """Yield (label, record) pairs from a file or directory."""

    if path.is_dir():
        pattern = "**/*.json" if recursive else "*.json"
        for file in sorted(path.glob(pattern)):
            yield from _iter_records(file, recursive=False)
        return

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        yield (str(path), {"__error__": str(exc)})
        return

    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        for index, item in enumerate(payload["records"]):
            yield (f"{path}#{index}", item)
    elif isinstance(payload, list):
        for index, item in enumerate(payload):
            yield (f"{path}#{index}", item)
    else:
        yield (str(path), payload)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate LOSDA records.")
    parser.add_argument("path", type=pathlib.Path, help="a JSON file or a directory")
    parser.add_argument(
        "--recursive", action="store_true", help="recurse into subdirectories"
    )
    parser.add_argument(
        "--single", action="store_true", help="treat the file as a single record, not a registry"
    )
    parser.add_argument("--quiet", action="store_true", help="only print failures and the summary")
    args = parser.parse_args(argv)

    if not args.path.exists():
        print(f"error: {args.path} does not exist", file=sys.stderr)
        return 2

    total = failed = warnings = 0

    if args.single and args.path.is_file():
        records: Iterable[tuple[str, dict]] = [(str(args.path), json.loads(args.path.read_text()))]
    else:
        records = _iter_records(args.path, args.recursive)

    for label, record in records:
        total += 1
        if isinstance(record, dict) and "__error__" in record:
            print(f"FAIL {label}: cannot parse JSON: {record['__error__']}")
            failed += 1
            continue
        report = validate_record(record, label)
        if report.ok:
            if not args.quiet:
                print(f"ok   {report.identifier}")
        else:
            failed += 1
            print(f"FAIL {report.identifier}")
            for message in report.errors:
                print(f"     error: {message}")
        for message in report.warnings:
            warnings += 1
            print(f"     warn:  {message}")

    print()
    print(f"{total} record(s) checked, {failed} invalid, {warnings} warning(s)")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
