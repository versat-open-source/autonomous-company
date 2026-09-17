# Versat Spec Driven Development

## Lifecycle

```text
Intent -> Proposal -> Requirements -> Design -> Tasks
       -> Implementation -> Validation -> Pull Request
       -> Merge -> Archive -> Living Specification
```

## Invariants

- Every change has a stable identifier in lowercase hyphen-case.
- Proposal explains why, scope, exclusions and expected impact.
- Requirements are observable and include acceptance scenarios.
- Design resolves architecture, data, security, operations and migration concerns that are actually relevant.
- Tasks trace to requirements and have verifiable completion.
- Implementation does not begin while a material unresolved decision blocks safe execution.
- Validation covers tests, evals and deterministic compliance applicable to the profile.
- Archive happens only after implementation and living specifications agree.

## Proportionality

Small, low-risk changes may use concise documents. High-criticality or irreversible changes require deeper alternatives, rollout, rollback, observability and approval analysis. Proportionality changes depth, not traceability.

## Workflow terminology

The procedures in `sdd/workflows/` implement this development lifecycle. Consumer operational workflows compose Skills under the [Agent Artifact Standard](../standards/core/agent-artifacts.md); their definitions and changes pass through SDD but do not replace it. A workflow document describes execution and dependencies, not an automatically installed runtime.

## Directory convention

```text
specs/
├── product/
│   ├── overview.md
│   └── requirements.md
├── changes/
│   └── <change-id>/
│       ├── proposal.md
│       ├── requirements.md
│       ├── design.md
│       └── tasks.md
└── archive/
    └── <change-id>/
```
