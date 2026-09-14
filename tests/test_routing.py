"""Offline evaluations use fictional mappings and never invoke an MCP."""

import copy
import json
import unittest
from pathlib import Path

from scripts.resolve_company import normalize, resolve, validate_config

ROOT = Path(__file__).resolve().parents[1]


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.fixtures = json.loads((ROOT / "evals/routing.json").read_text())

    def test_behavioral_scenarios(self):
        for case in self.fixtures["cases"]:
            with self.subTest(case=case["id"]):
                result = resolve(self.fixtures["config"], case["request"])
                self.assertEqual(result, case["expected"])

    def test_rejects_duplicate_documents_and_connections(self):
        for field in ("document", "mcp_connection", "name"):
            with self.subTest(field=field):
                config = copy.deepcopy(self.fixtures["config"])
                config["companies"][1][field] = config["companies"][0][field]
                with self.assertRaisesRegex(ValueError, "duplicate_mapping"):
                    validate_config(config)

    def test_example_cannot_be_used_as_configuration(self):
        config = json.loads((ROOT / "versat-companies.example.json").read_text())
        with self.assertRaisesRegex(ValueError, "unconfigured_example"):
            validate_config(config)

    def test_malformed_configuration_fails_closed(self):
        for config in (None, [], {}, {"companies": []}, {"companies": [{}]}):
            self.assertEqual(resolve(config, {}), {"status": "blocked", "reason": "invalid_config"})

    def test_document_normalization_retains_leading_zeros(self):
        self.assertEqual(normalize("00.123-4"), "001234")
        self.assertNotEqual(normalize("00.123-4"), normalize("123-4"))


if __name__ == "__main__":
    unittest.main()
