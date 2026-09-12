"""Resolve an operating company locally; this module never calls ERP tools."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"name", "document_type", "document", "mcp_connection"}


def normalize(value: str) -> str:
    """Ignore punctuation, whitespace and case without dropping digits."""
    return "".join(c for c in value.casefold() if c.isalnum())


def validate_config(config: Any) -> list[dict[str, str]]:
    if not isinstance(config, dict) or set(config) != {"companies"}:
        raise ValueError("invalid_config")
    companies = config["companies"]
    if not isinstance(companies, list) or not companies:
        raise ValueError("invalid_config")
    for company in companies:
        if not isinstance(company, dict) or set(company) != FIELDS:
            raise ValueError("invalid_config")
        for value in company.values():
            if not isinstance(value, str) or not normalize(value):
                raise ValueError("invalid_config")
            if value.startswith("REPLACE_WITH_"):
                raise ValueError("unconfigured_example")
    for field in ("name", "document", "mcp_connection"):
        values = [normalize(c[field]) for c in companies]
        if len(values) != len(set(values)):
            raise ValueError("duplicate_mapping")
    return companies


def resolve(config: Any, request: dict[str, Any]) -> dict[str, Any]:
    """Gate routing, actual availability and explicit financial-write authority."""
    try:
        companies = validate_config(config)
        if request.get("operation", "read") not in {"read", "write"}:
            raise ValueError("invalid_operation")
        name, document = request.get("name"), request.get("document")
        explicit = name is not None or document is not None
        if not explicit:
            if request.get("continuation") is not True or not request.get("previous_name"):
                raise ValueError("company_required")
            name = request["previous_name"]
        matches = companies
        for field, value in (("name", name), ("document", document)):
            if value is not None:
                if not isinstance(value, str) or not normalize(value):
                    raise ValueError("invalid_context")
                matches = [c for c in matches if normalize(c[field]) == normalize(value)]
        if len(matches) != 1:
            raise ValueError("unresolved_or_conflicting_company")
        company = matches[0]
        available = request.get("available_connections", [])
        if not isinstance(available, list) or company["mcp_connection"] not in available:
            raise ValueError("connection_unavailable")
        if request.get("operation", "read") == "write" and request.get("authorized") is not True:
            raise ValueError("write_authorization_required")
        return {
            "status": "pass",
            "company": company["name"],
            "connection": company["mcp_connection"],
        }
    except ValueError as error:
        return {"status": "blocked", "reason": str(error)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "versat-companies.local.json")
    parser.add_argument("--company-name", dest="name")
    parser.add_argument("--document")
    parser.add_argument("--previous-name")
    parser.add_argument("--continuation", action="store_true")
    parser.add_argument("--available-connection", action="append", default=[])
    parser.add_argument("--operation", choices=["read", "write"], default="read")
    parser.add_argument("--authorized", action="store_true")
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text())
        request = vars(args)
        request["available_connections"] = request.pop("available_connection")
        result = resolve(config, request)
    except (OSError, UnicodeError, json.JSONDecodeError):
        result = {"status": "blocked", "reason": "missing_or_invalid_local_config"}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] == "pass" else 2


if __name__ == "__main__":
    sys.exit(main())
