# Autonomous Company

[Português](docs/README.pt-BR.md) · [Español](docs/README.es.md)

A governed agent workspace for company-specific Versat ERP operations. It combines project instructions, the imported Versat MCP skill, private local routing and offline validation. It does not deploy a service, configure MCP credentials or execute financial transactions by itself.

Owner: **versat-open-source**. Repository maintainer: **@elviszoz**. Profile: **agent / finance**, high operational criticality. Governance: Versat AI Harness revision **9260d3a** (VERSION **0.2.0**, Unreleased changes), pinned by full commit and content digest in `.versat/`. See [the adoption decision](docs/decisions/0002-consumer-agent-layout.md).

## Setup

Use Python **3.12.14** (see `.python-version`):

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
cp versat-companies.example.json versat-companies.local.json
```

Replace the placeholders in the local JSON with your operating companies and the exact names of MCP connections already configured in your agent client. Keep tokens in the client's secret configuration. The local JSON is ignored by Git and must never be force-added.

Open the workspace in a client that reads `AGENTS.md` and discovers `.agents/skills/`. Before using ERP tools, follow [the operation workflow](workflows/versat-operation/workflow.md). Ambiguous context, missing mappings, unavailable connections and unauthorized writes block execution.

Project Skills live in `.agents/skills/`; the supervised operator is defined in `.codex/agents/operator.toml`. Workflows use `workflows/<name>/workflow.md` and must be explicitly loaded. Native operator loading requires a compatible Codex client and separate verification; no workflow scheduler is installed. See [agent architecture and runtime requirements](docs/architecture/agent-project.md).

## Validation and contributions

```sh
bash scripts/validate/run.sh
```

This command checks formatting, lint, unit tests, 15 offline routing scenarios, artifact structure and dependency bindings, project and SDD schemas, Standards resolution and integrity, and private-data exclusions. CI uses the same command without production credentials. Offline tests do not certify native agent discovery, model behavior or live ERP connectivity.

Use [Versat SDD](.versat/sdd/process.md) for material changes; require a PR, CODEOWNERS review and a passing `validate` check. Update fixed dependencies and Harness versions through reviewable PRs. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Design and operations

- [Current architecture](docs/architecture/overview.md) and [ADR-0001](docs/decisions/0001-governed-agent-workspace.md).
- [Product scope](specs/product/overview.md) and [requirements](specs/product/requirements.md).
- [Operations and recovery](docs/operations.md), [security reporting](SECURITY.md) and [readiness](docs/readiness.md).
- [Artifact migration](specs/changes/agent-template-migration/proposal.md) and [bootstrap history](specs/changes/project-bootstrap/proposal.md).

Public availability is not a software license grant. No project-wide distribution license has been selected; see [third-party provenance](THIRD_PARTY_NOTICES.md) before redistribution.
