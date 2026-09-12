---
change: project-bootstrap
tasks:
  - id: TASK-001
    description: Pin identity, Standards and template provenance while preserving local data.
    requirements: [REQ-001, REQ-002]
    status: completed
  - id: TASK-002
    description: Implement routing gate, validation and fictional evaluations.
    requirements: [REQ-001, REQ-003]
    status: completed
  - id: TASK-003
    description: Document architecture, operations, translations and ownership.
    requirements: [REQ-004]
    status: completed
  - id: TASK-004
    description: Publish seed and bootstrap PR with CI and branch protection evidence.
    requirements: [REQ-004]
    status: in-progress
---

# Tasks

- [x] TASK-001 — Versioned identity and private configuration.
- [x] TASK-002 — Routing gate, validators and evaluations.
- [x] TASK-003 — Documentation and ownership.
- [ ] TASK-004 — GitHub publication and readiness evidence.

## Validation evidence

Local validation passed on Python 3.12.14: Ruff formatting/lint, five unit-test groups including 15 routing scenarios, schema validation, Standards resolution, snapshot integrity and local-data scanning. The installed Harness validator reports a compatibility manifest path mismatch (`./skills` versus `./skills/`); this remains a separate upstream-package validation gap. Remote readiness evidence is pending.
