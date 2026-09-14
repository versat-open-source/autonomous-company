"""Validate the consumer project; print JSON evidence and fail on violations."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]


def read_yaml(path: str) -> dict:
    return yaml.safe_load((ROOT / path).read_text())


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate() -> list[dict[str, str]]:
    project = read_yaml(".versat/project.yaml")
    lock = read_yaml(".versat/standards.lock")
    for data, schema in ((project, "project"), (lock, "standards")):
        jsonschema.validate(data, read_yaml(f".versat/schemas/{schema}.schema.yaml"))
    require(sys.version_info[:2] == (3, 12), "Python 3.12 is required")
    info = project["project"]
    index = read_yaml(".versat/standards/index.yaml")
    selected = index["core"]["always"] + index["profiles"][info["profile"]]
    selected += index["domains"][info["domain"]] + index["criticality"][info["criticality"]]
    for technology in project["technologies"]:
        selected += index["technologies"][technology]
    selected = set(selected)
    require(selected == {item["path"] for item in lock["standards"]}, "Standards resolution drift")
    require(len(lock["standards"]) == len(selected), "Duplicate Standards entries")
    for item in lock["standards"]:
        content = (ROOT / ".versat/standards" / item["path"]).read_bytes()
        require(item["digest"] == "sha256:" + hashlib.sha256(content).hexdigest(), "Digest drift")
        require(item["version"] == lock["harness"]["version"], "Standards version drift")
    provenance = json.loads((ROOT / ".versat/bootstrap.json").read_text())
    require(lock["harness"]["commit"] == provenance["harness_commit"], "Commit drift")
    require(lock["harness"]["version"] == provenance["harness_version"], "Harness version drift")
    require(bool(re.fullmatch(r"[0-9a-f]{40}", lock["harness"]["commit"])), "Unpinned commit")
    for item in provenance["artifacts"]:
        content = (ROOT / item["path"]).read_bytes()
        require(hashlib.sha256(content).hexdigest() == item["sha256"], "Snapshot drift")
    profile = read_yaml(".versat/project-templates/agent/structure.yaml")
    for directory in profile["directories"]:
        require((ROOT / directory).is_dir(), f"Missing profile directory: {directory}")
    for name in (
        "AGENTS.md",
        "README.md",
        "docs/README.pt-BR.md",
        "docs/README.es.md",
        "docs/architecture/overview.md",
        "docs/decisions/0001-governed-agent-workspace.md",
        "docs/operations.md",
        "docs/readiness.md",
        ".github/CODEOWNERS",
        ".github/workflows/validate.yml",
        "specs/product/overview.md",
        "specs/product/requirements.md",
    ):
        require((ROOT / name).is_file() and (ROOT / name).stat().st_size > 0, f"Missing: {name}")
    for change in (ROOT / "specs/changes").iterdir():
        if not change.is_dir():
            continue
        metadata = {}
        for name in ("proposal", "requirements", "design", "tasks"):
            text = (change / f"{name}.md").read_text()
            require(text.startswith("---\n"), f"Missing SDD metadata: {name}")
            data = yaml.safe_load(text.split("---", 2)[1])
            jsonschema.validate(data, read_yaml(f".versat/sdd/schemas/{name}.schema.yaml"))
            require(data["change"] == change.name, "SDD identifier mismatch")
            metadata[name] = data
        requirements = {r["id"] for r in metadata["requirements"]["requirements"]}
        require(len(requirements) == len(metadata["requirements"]["requirements"]), "Duplicate REQ")
        tasks = metadata["tasks"]["tasks"]
        require(len({t["id"] for t in tasks}) == len(tasks), "Duplicate TASK")
        traced = {r for task in tasks for r in task["requirements"]}
        require(requirements == traced, "SDD task coverage drift")
        require(
            set(metadata["design"]["requirements"]) == requirements, "SDD design coverage drift"
        )
    tracked = set(filter(None, git("ls-files", "-z").split("\0")))
    require("versat-companies.local.json" not in tracked, "Private mapping is tracked")
    require(
        not any(p.startswith(".venv/") or p.endswith(".DS_Store") for p in tracked),
        "Local artifacts are tracked",
    )
    ignored = git("check-ignore", "--no-index", "versat-companies.local.json").strip()
    require(ignored == "versat-companies.local.json", "Private mapping is not ignored")
    candidates = set(
        filter(
            None, git("ls-files", "--cached", "--others", "--exclude-standard", "-z").split("\0")
        )
    )
    forbidden = []
    local = ROOT / "versat-companies.local.json"
    if local.exists():
        for company in json.loads(local.read_text())["companies"]:
            forbidden.extend(company[k] for k in ("name", "document", "mcp_connection"))
            forbidden.append("".join(c for c in company["document"] if c.isalnum()))
    secret_pattern = re.compile(
        r"(?:gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |EC )?PRIVATE KEY)"
    )
    for path in candidates:
        text = (ROOT / path).read_text(errors="replace")
        require(
            not any(value and value in text for value in forbidden),
            f"Private company value in public candidate: {path}",
        )
        require(not secret_pattern.search(text), f"Possible credential in: {path}")
    return [
        {"check": "schemas_standards_provenance_sdd", "status": "pass"},
        {"check": "private_file_exclusion_and_secret_patterns", "status": "pass"},
        {
            "check": "local_company_values_scan",
            "status": "pass" if local.exists() else "unable-to-verify",
            "detail": "Local-only values are intentionally absent in CI"
            if not local.exists()
            else "No local company values found in public candidate files",
        },
        {
            "check": "live_mcp_and_model_behavior",
            "status": "unable-to-verify",
            "detail": "Offline gate evals do not invoke an LLM or an ERP connection",
        },
    ]


if __name__ == "__main__":
    try:
        print(json.dumps({"status": "pass", "checks": validate()}, indent=2))
    except Exception as error:
        print(json.dumps({"status": "fail", "error": str(error)}))
        sys.exit(1)
