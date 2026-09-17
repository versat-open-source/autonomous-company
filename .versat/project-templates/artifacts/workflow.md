# Workflow name

Authoring template only. Replace placeholders before declaring this workflow ready.

## Purpose and ownership

- Outcome: describe the operational result.
- Owner: identify the accountable team or person.
- Scope: define what this workflow covers.

## Trigger, inputs and preconditions

Specify the trigger, required inputs, supported environment and readiness checks.

## Executor and dependencies

- Executor: identify the agent, supervised session or implemented runner that explicitly loads this document.
- Skills: list project-root-relative `.agents/skills/<skill-name>/SKILL.md` paths or installed Plugin identifiers and exact version references.
- Connectors: identify required services and access configuration.
- Execution guarantees: describe actual scheduling, state and retry support, or state that execution is manual.

## Steps and decisions

| Step | Skill | Inputs | Outputs and next decision |
|---|---|---|---|
| 1 | Exact dependency from the list above | Required input | Observable output, next step or stop condition |

Document handoffs between steps; do not leave capability names unbound.

## Authorization

Reference the project's resolved Standards. Identify approval points, approving roles, evidence and behavior when authorization is absent.

## Results and evidence

Define complete, skipped, blocked and partial outcomes, output identifiers and the records needed to verify each outcome.

## Failure and recovery

Describe duplicate prevention, retry limits, checkpoints, partial completion, resumption and escalation. State which guarantees require an implemented executor or external system.
