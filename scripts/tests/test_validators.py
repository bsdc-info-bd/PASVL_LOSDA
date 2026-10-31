"""Tests for the framework's validators.

Run with:
    python3 -m pytest scripts/tests -q
or, without pytest:
    python3 scripts/tests/test_validators.py

Licensed under PASVL-1.0. Source is public. Deployment requires a LOSDA.
SPDX-License-Identifier: LicenseRef-PASVL-1.0
"""

from __future__ import annotations

import copy
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import json  # noqa: E402

from hash_record import record_hash  # noqa: E402
from validate_losda import validate_record  # noqa: E402
from validate_registry import merkle_root  # noqa: E402


def sample() -> dict:
    """A valid Class H record used as the base for mutation tests."""
    return {
        "losda_id": "LOSDA-ACME-2026-000001",
        "version": "LOSDA-1.0",
        "license_version": "1.0",
        "class": "H",
        "work": {
            "name": "Acme Scheduler",
            "repo_url": "https://github.com/acmelabs/scheduler",
        },
        "issuer": {
            "legal_name": "Acme Labs Ltd",
            "issuer_code": "ACME",
            "capacity": "author",
            "country": "Bangladesh",
        },
        "licensee": {
            "legal_name": "Example Corp",
            "entity_type": "company",
            "country": "United Kingdom",
            "anonymised": False,
        },
        "scope": {
            "deployment_types": ["hosted_service"],
            "territory": ["Worldwide"],
            "field_of_use": "Managed workflow product for business customers.",
            "scale": {"end_users": 1000, "unlimited": False},
        },
        "conditions": {"codes": ["C1", "C3"], "bespoke": []},
        "fees": {"payable": True, "amount": 1000, "currency": "USD", "basis": "annual"},
        "term": {
            "start": "2026-11-01",
            "end": "2027-10-31",
            "perpetual": False,
            "reliance_period_days": 180,
        },
        "effective_date": "2026-11-01",
        "status": "pending",
        "status_history": [],
        "signature": {"method": "qualified_e_signature", "signatory": "A. Person"},
        "registry": {
            "record_hash": "a" * 64,
            "recorded_at": "2026-10-30T00:00:00Z",
        },
    }


class TestLosdaValidation(unittest.TestCase):
    def test_valid_record_passes(self) -> None:
        report = validate_record(sample())
        self.assertTrue(report.ok, report.errors)

    def test_bad_identifier_rejected(self) -> None:
        record = sample()
        record["losda_id"] = "LOSDA-acme-1-1"
        self.assertFalse(validate_record(record).ok)

    def test_missing_id_rejected(self) -> None:
        record = sample()
        del record["losda_id"]
        self.assertFalse(validate_record(record).ok)

    def test_unknown_class_rejected(self) -> None:
        record = sample()
        record["class"] = "Z"
        self.assertFalse(validate_record(record).ok)

    def test_unsigned_is_void(self) -> None:
        record = sample()
        record["signature"] = {"method": "none"}
        report = validate_record(record)
        self.assertFalse(report.ok)
        self.assertTrue(any("unsigned" in e for e in report.errors))

    def test_steward_continuity_requires_bsdc(self) -> None:
        record = sample()
        record["issuer"]["capacity"] = "steward_continuity"
        report = validate_record(record)
        self.assertFalse(report.ok)

    def test_perpetual_with_end_date_rejected(self) -> None:
        record = sample()
        record["term"]["perpetual"] = True
        self.assertFalse(validate_record(record).ok)

    def test_missing_end_date_rejected(self) -> None:
        record = sample()
        record["term"].pop("end")
        self.assertFalse(validate_record(record).ok)

    def test_end_before_start_rejected(self) -> None:
        record = sample()
        record["term"]["end"] = "2025-01-01"
        self.assertFalse(validate_record(record).ok)

    def test_bad_condition_code_rejected(self) -> None:
        record = sample()
        record["conditions"]["codes"] = ["C99"]
        self.assertFalse(validate_record(record).ok)

    def test_placeholder_hash_warns(self) -> None:
        record = sample()
        record["registry"]["record_hash"] = "0" * 64
        report = validate_record(record)
        self.assertTrue(report.ok)
        self.assertTrue(any("placeholder" in w for w in report.warnings))

    def test_active_with_past_end_date_rejected(self) -> None:
        record = sample()
        record["status"] = "active"
        record["term"]["start"] = "2020-01-01"
        record["term"]["end"] = "2021-01-01"
        record["effective_date"] = "2020-01-01"
        self.assertFalse(validate_record(record).ok)

    def test_missing_field_of_use_warns_for_class_m(self) -> None:
        record = sample()
        record["class"] = "M"
        record["scope"]["field_of_use"] = ""
        report = validate_record(record)
        self.assertFalse(report.ok)

    def test_anonymised_needs_display_name(self) -> None:
        record = sample()
        record["licensee"]["anonymised"] = True
        self.assertFalse(validate_record(record).ok)


class TestHashing(unittest.TestCase):
    def test_hash_is_deterministic(self) -> None:
        record = sample()
        self.assertEqual(record_hash(record), record_hash(copy.deepcopy(record)))

    def test_hash_ignores_key_order(self) -> None:
        record = sample()
        reordered = {k: record[k] for k in reversed(list(record))}
        self.assertEqual(record_hash(record), record_hash(reordered))

    def test_hash_changes_on_content_change(self) -> None:
        record = sample()
        before = record_hash(record)
        record["scope"]["field_of_use"] = "Something else entirely."
        self.assertNotEqual(before, record_hash(record))

    def test_hash_excludes_itself(self) -> None:
        record = sample()
        first = record_hash(record)
        record["registry"]["record_hash"] = "b" * 64
        self.assertEqual(first, record_hash(record))

    def test_merkle_root_empty(self) -> None:
        self.assertEqual(len(merkle_root([])), 64)

    def test_merkle_root_stable(self) -> None:
        hashes = ["a" * 64, "b" * 64, "c" * 64]
        self.assertEqual(merkle_root(hashes), merkle_root(list(reversed(hashes))))

    def test_merkle_root_changes(self) -> None:
        hashes = ["a" * 64, "b" * 64]
        self.assertNotEqual(merkle_root(hashes), merkle_root(["a" * 64, "c" * 64]))


class TestRepositoryFiles(unittest.TestCase):
    def test_example_record_parses(self) -> None:
        payload = json.loads((ROOT / "examples" / "losda-record.json").read_text())
        self.assertIn("losda_id", payload)

    def test_registry_parses(self) -> None:
        payload = json.loads((ROOT / "registry" / "losda-registry.json").read_text())
        self.assertIn("records", payload)

    def test_schemas_parse(self) -> None:
        for name in ("losda-v1.schema.json", "registry-v1.schema.json"):
            json.loads((ROOT / "schemas" / name).read_text())

    def test_licence_mentions_key_articles(self) -> None:
        text = (ROOT / "LICENSE").read_text()
        for needle in (
            "ARTICLE 3 — THE VISIBILITY GRANT",
            "ARTICLE 5 — RESERVED RIGHTS",
            "ARTICLE 10 — THE LETTER OF SOFTWARE DEPLOYMENT APPROVAL",
            "APPENDIX A",
        ):
            self.assertIn(needle, text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
