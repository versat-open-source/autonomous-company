---
change: agent-template-migration
requirements:
  - id: REQ-001
    statement: Adopt canonical consumer artifact locations while preserving capabilities and authorization boundaries.
    acceptance:
      - Root skills and agents directories are absent; the imported versat-mcp Skill is unchanged.
      - The operator is valid TOML with matching name, description and developer_instructions.
      - Current instructions and documentation resolve the new operator and workflow paths.
  - id: REQ-002
    statement: Define an explicitly loaded, supervised Versat operation workflow.
    acceptance:
      - The workflow declares ownership, trigger, inputs, executor, actual Skill dependencies and ordered decisions.
      - Authorization, complete, skipped, blocked and partial outcomes, evidence and safe recovery are explicit.
      - No scheduling, automatic discovery, durable execution or live connectivity is claimed.
  - id: REQ-003
    statement: Preserve exact provenance and validate the migration with truthful evidence.
    acceptance:
      - Applicable snapshots match commit 9260d3a04f658b6eeec86a8dc88563d2051cb09d and their hashes.
      - Unreleased revision adoption is documented without inventing a release or Story.
      - Required checks, critical routing evals and artifact validation pass; runtime checks and PR state are reported separately.
---

# Requirements

Company routing, approval assessment and recovery stay governed by the local instructions, original Skill and resolved Standards. A structural migration does not authorize any financial operation.
