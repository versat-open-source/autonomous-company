---
change: agent-template-migration
requirements: [REQ-001, REQ-002, REQ-003]
adrs: [ADR-0002]
validation:
  - Run bash scripts/validate/run.sh and git diff --check.
  - Verify every imported Harness snapshot against its source Git blob at the pinned revision.
  - Verify the imported Skill remains byte-identical and review workflow authorization and recovery cases.
  - Check local references and report native agent loading and live MCP execution as unverified.
---

# Design

Classify `skills/README.md` as obsolete integration guidance, `agents/operator.md` as consumer role guidance, and `workflows/versat-operation.md` as an operational flow. Remove the first, convert the role into native TOML, and expand the flow under its named directory. Preserve role purpose, authority, memory and ownership boundaries. Do not add model overrides or tool access configuration.

Refresh the existing applicable Harness snapshots from the exact source commit, resolve the new `core/agent-artifacts.md`, and retain the matching agent/workflow authoring templates for traceable format references. VERSION remains 0.2.0; provenance additionally records the Unreleased revision status, previous pin and this migration. The source update also includes the intervening Git/Shortcut guidance and SDD template updates. They do not introduce a Story for this work.

Document the project-specific architecture, inventory, supported runtime prerequisites and explicit workflow loading. The observed Codex CLI version is evidence of the environment only; TOML parsing does not prove native agent loading. Runtime verification remains an operational prerequisite. Supervised callers can explicitly follow the same instructions; no automatic runner is introduced.

Extend consumer validation to check artifact paths, TOML/frontmatter contracts, bound local workflow dependencies, source Git blob hashes and required documentation. Keep semantic authorization/recovery review distinct from structural checks. Exercise invalid names, missing dependencies and legacy paths with temporary fixtures, alongside existing routing evals. Ignore deleted paths when scanning public candidates so normal migrations validate before staging, but keep every existing tracked or untracked candidate subject to the privacy scan.

Alternative: keep documentation-only root directories. Rejected because it preserves the ambiguity the user asked to remove. Alternative: label the target as a new release. Rejected because the source is Unreleased. Apply an explicit revision exception instead.

Deliver through a PR; do not merge or archive without review and validation. Roll back through a reviewed revert that restores the previous pin and artifact paths together. Preserve local mappings; repository rollback never reverses ERP transactions.
