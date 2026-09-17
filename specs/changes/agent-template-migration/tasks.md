---
change: agent-template-migration
tasks:
  - id: TASK-001
    description: Record the exact target and refresh applicable snapshots and provenance.
    requirements: [REQ-003]
    status: completed
  - id: TASK-002
    description: Convert the operator, reorganize the workflow and update living documentation.
    requirements: [REQ-001, REQ-002]
    status: completed
  - id: TASK-003
    description: Validate the artifacts, preserved routing behavior and source integrity.
    requirements: [REQ-001, REQ-002, REQ-003]
    status: completed
  - id: TASK-004
    description: Submit the migration for review and record CI and runtime verification limits.
    requirements: [REQ-003]
    status: in-progress
---

# Tasks and evidence

Local implementation and verification completed on 2026-09-17. `bash scripts/validate/run.sh` passed with Python 3.12.9: formatting/lint, 14 tests including 15 routing scenarios, artifact structure/dependency checks, schemas, Standards, provenance and privacy exclusions. CI retains Python 3.12.14. `git diff --check` and local Markdown links passed. All 26 source snapshots were compared with the pinned upstream Git objects; all eight imported Skill files and the routing gate are unchanged.

Workflow review covered out-of-scope requests, ambiguous company, absent authorization, missing connection, complete results, uncertain writes and partial recovery. The workflow binds the actual imported Skill and stops before any speculative retry or cross-company fallback. This is document inspection, not a live model evaluation.

Upstream layout PR #5 was verified merged. No new Harness release is claimed. Consumer PR submission and CI are in progress. Native custom-agent loading and live MCP behavior remain unverified; no ERP call was made. Consumer review, merge and archival remain pending.
