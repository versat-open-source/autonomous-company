# Agent project architecture

## Artifact map and inventory

All paths below are relative to the project root. The maintainer is `@elviszoz`; business authorization and live execution belong to the human operator. Apply the [Agent Artifact Standard](../../.versat/standards/core/agent-artifacts.md).

| Artifact | Path | Purpose and consumer |
|---|---|---|
| Shared guidance | `AGENTS.md` | Routing, authority and lifecycle instructions for every project session |
| Reusable capability | `.agents/skills/versat-mcp/SKILL.md` | Imported ERP Skill 1.2.47; used by the operator and operation workflow |
| Codex execution role | `.codex/agents/operator.toml` | Supervised ERP operator; selected by a compatible Codex client |
| Operational composition | `workflows/versat-operation/workflow.md` | Orders company selection, gating, Skill execution, verification and recovery |
| Local control | `scripts/resolve_company.py` | Offline routing gate invoked before ERP calls; not an MCP client |
| Behavioral evidence | `evals/routing.json` and `tests/` | Fictional routing scenarios and structural validation regressions |

The original Skill remains unchanged and in its upstream language. Project-specific instructions stay in `AGENTS.md`, the role, workflow and gate; imported upgrades require provenance updates, evals and review. See [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

There are no root consumer `skills/` or `agents/` directories. Harness Plugin exports use a different packaging contract. `.github/workflows/` remains the GitHub Actions CI adapter; `.versat/sdd/` remains the development lifecycle. This workspace has no deployed application source or service.

## Source adoption

The migration pins Harness commit `9260d3a04f658b6eeec86a8dc88563d2051cb09d` (VERSION 0.2.0, Unreleased changes). The installed 0.2.0 Plugin package is unchanged. [ADR-0002](../decisions/0002-consumer-agent-layout.md) records the user-requested exception to release-only adoption. `.versat/bootstrap.json` records the previous pin, migration and all exact source hashes.

## Execution and runtime requirements

Native role selection requires a Codex release supporting standalone `.codex/agents/<name>.toml` with `name`, `description` and `developer_instructions`. The local environment reports `codex-cli 0.154.0-alpha.6.2`. This observation does not certify discovery: native agent loading and a live delegated invocation have not been tested. No model, sandbox, tool or reasoning override is introduced by the role.

Before claiming runtime readiness, verify that the deployment's Codex client exposes `operator` with the expected instructions and that a supervised, non-financial invocation loads the correct artifacts and stops on missing company configuration. Do not use an actual write to test discovery. Until that check passes, native adapter readiness remains unverified.

The executor explicitly reads `workflows/versat-operation/workflow.md`, resolves `.agents/skills/versat-mcp/SKILL.md` and checks the configured MCP tools before execution. A supervised caller may explicitly read the same guidance without claiming native role discovery. Workflow Markdown has no automatic scheduling or execution. There is no durable state, concurrency control, transactional pipeline or automatic retry implementation.

## Data, authorization and recovery

Only ignored `versat-companies.local.json` maps companies to actual configured connections; credentials remain in the client/service. Company context stays in the current conversation and every operation uses its own route and IDs. Read the resolved [security](../../.versat/standards/core/security.md), [AI](../../.versat/standards/core/ai.md) and [finance](../../.versat/standards/domains/finance.md) policies and [operations runbook](../operations.md) for approvals, audit evidence, retention and incident ownership.

The [workflow](../../workflows/versat-operation/workflow.md) defines complete, skipped, blocked and partial results, zero automatic retries and same-company verification before resumption. Duplicate prevention depends on inspecting ERP state and following the imported Skill; the repository supplies no idempotency service. Repository rollback restores code and instructions only.

## Validation

Run `bash scripts/validate/run.sh`. Consumer checks cover TOML/frontmatter, naming and canonical paths, workflow sections and local dependency resolution, source integrity, SDD, privacy and critical offline routing evals. Human review covers workflow meaning and authority preservation. Static checks do not verify native client discovery, live connections, model behavior or financial execution; see [readiness](../readiness.md).
