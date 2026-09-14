---
change: project-bootstrap
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: [ADR-0001]
validation:
  - Run bash scripts/validate/run.sh.
  - Inspect Git tracked content and ignored local configuration before push.
  - Inspect GitHub checks and branch protection after creating the PR.
---

# Design

Use the base and agent template modules with project identity in `.versat/project.yaml`. Copy only applicable Standards, schema and lifecycle artifacts; record exact hashes and commit provenance. Permission to publish those private-source artifacts was explicitly granted by the user.

Keep the imported Versat skill intact and extend project instructions in English. A small local Python gate resolves explicit operating-company context, continuation, connection availability and write authorization. It never calls an MCP or executes text from the mapping. The calling agent must still follow the skill's domain contracts and verify identity before using tools.

Use Python 3.12.14 and exact development dependencies. CI uses fictional fixtures and no ERP secrets. The gate's behavior is deterministic; it does not prove that a language model will interpret every request correctly.

Publish a minimal seed commit to establish `main`, then submit the complete bootstrap on `bootstrap/project-bootstrap`. Require PR review and validation before merging. Rollback uses a revert PR; preserve local mappings and keep external transaction recovery outside repository rollback.

See ADR-0001 and the operating runbook for data, approval, observability and recovery boundaries. Use the README for setup and the readiness record for checks that could not be verified.
