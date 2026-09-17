# ADR-0002 — Adopt the consumer agent artifact contract

- Status: Proposed; implementation requested by the user, PR review pending
- Date: 2026-09-17
- Refines: ADR-0001 artifact layout and Harness source pin

## Context

The initial template produced root `skills/` and `agents/`, while the installed project Skill already lived under `.agents/skills/`. Harness revision `9260d3a04f658b6eeec86a8dc88563d2051cb09d` separates consumer capabilities, native Codex roles and operational workflows. It remains Unreleased with VERSION 0.2.0 and a proposed upstream ADR-0012.

## Decision

Follow the user's explicit request to adopt these new definitions at that exact commit. This is a documented exception to release-only consumer migration, pending review; do not represent the revision as a published release or the installed Plugin as updated. Pin all applicable source snapshots consistently, including the new Agent Artifact Standard and the intervening Git/SDD guidance.

Keep `.agents/skills/versat-mcp/` unchanged. Remove the documentation-only root `skills/`. Convert the ERP operator to `.codex/agents/operator.toml` and remove root `agents/`. Move the operation into `workflows/versat-operation/workflow.md`, with explicit Skill binding, supervised loading and recovery semantics. Keep `.github/workflows/` for CI.

The role uses only the required name, description and developer_instructions fields. A Codex runtime supporting standalone custom-agent TOML is required for native selection. Record the observed client version and require actual loading verification before declaring the adapter operational. Static syntax validation and workflow documentation cannot establish ERP readiness.

## Consequences and rollback

Each artifact has one source and current references use it. The imported Skill and local gate retain their behavior. A workflow document adds no scheduler, transaction engine, automatic retry or credential provisioning. Human review and live integration remain separate gates.

Roll back the migration with a reviewed revert restoring the previous exact Harness commit and the previous role/workflow paths together. Preserve private local mappings. No remote ERP state is changed by this migration.
