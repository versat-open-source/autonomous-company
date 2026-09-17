# Agent Artifact Standard

## Scope and responsibilities

These rules apply when a consumer project defines Skills, custom agents or operational workflows, regardless of its profile. Projects without these artifacts are not required to create empty directories. Plugin packaging is a separate contract.

| Artifact | Project path | Responsibility |
|---|---|---|
| Skill | `.agents/skills/<skill-name>/SKILL.md` | Reusable capability with instructions and optional supporting resources |
| Codex custom agent | `.codex/agents/<agent-name>.toml` | Execution role, instructions and supported runtime configuration |
| Versat workflow | `workflows/<workflow-name>/workflow.md` | Ordered composition of named Skills to achieve an operational outcome |
| Shared project guidance | `AGENTS.md` | Instructions that apply to work in the repository or a subtree |

Paths are relative to the project root. Artifact names MUST use English lowercase hyphen-case. `SKILL.md` MUST retain its uppercase spelling for discovery; `workflow.md` MUST use lowercase. Each artifact MUST remain versioned with the project. Do not create duplicate sources merely to satisfy different directory conventions.

These artifacts MAY implement business operations or support development. They are not a replacement for the source layout of a separately deployed application: runtime code and resources MUST follow that application's declared architecture.

## Skills

- Each project Skill MUST have a `SKILL.md` with frontmatter containing `name` and `description`; `name` MUST match its directory name.
- A Skill MUST define when to use it, its inputs, observable result and failure conditions. Scripts, references and assets MAY accompany it in the same directory.
- A Skill MUST locate applicable policy through the project's resolved Standards rather than duplicate policy text.
- Installed Plugin Skills MAY be referenced as dependencies without copying them into the project. The project MUST identify their Plugin and exact version reference.

## Codex custom agents

- Each custom agent MUST use a TOML file with non-empty `name`, `description` and `developer_instructions`; `name` MUST match the filename stem.
- Supported Codex settings MAY specify model, reasoning effort, sandbox or tool configuration. Authors MUST verify compatibility with the target Codex release and document runtime requirements.
- `AGENTS.md` and arbitrary `agents/*.md` files MUST NOT be presented as native custom-agent registrations.
- `.codex/agents/` is the Codex adapter. Another executor MUST document its adapter mapping and any departure from the project convention in an ADR; it MUST NOT claim Codex discovery for unsupported paths.

## Versat workflows

Each `workflow.md` MUST define the following information. The [authoring template](../../project-templates/artifacts/workflow.md) provides headings; equivalent organization is allowed.

1. **Purpose and ownership:** the business outcome, accountable owner and boundaries of the operation.
2. **Trigger, inputs and preconditions:** when it runs, required data and what must already be configured.
3. **Executor and dependencies:** who or what follows the document; local Skill paths or installed Plugin Skill identifiers with exact version references; required connectors and access. Use project-root-relative paths for local dependencies.
4. **Steps and decisions:** ordered Skill calls, input/output handoffs, branch conditions and stop conditions. References MUST identify actual capabilities before the workflow is marked ready; descriptive aliases alone are insufficient.
5. **Authorization:** which actions require approval under resolved Standards, who grants it and what happens when it is absent.
6. **Results and evidence:** success criteria, partial or skipped outcomes, identifiers and operational records needed to verify completion.
7. **Failure and recovery:** retries, duplicate prevention, partial completion, resumption and escalation.

A workflow SHOULD delegate reusable operations to Skills and keep sequencing and handoffs in the workflow. It MUST reference applicable Standards rather than redefine policy or give itself additional permissions. Changes to steps, capability bindings or authorization boundaries MUST use the governed SDD process.

`workflow.md` is a Versat authoring convention. It is not automatically discovered or executed by Codex. The caller or a Skill MUST explicitly load the selected workflow, or a separately implemented executor MUST define its loading behavior. A document alone does not provide scheduling, durable state, transactional execution, retries or access to external services. Projects MUST document which of these guarantees their executor actually implements.

## Packaging and lifecycle boundaries

The Harness Plugin retains root `skills/` for installable capabilities and root `agents/` for reusable role guidance. Its package structure MUST NOT be copied as the default consumer layout. Plugin role guidance requires explicit loading or adapter conversion; its presence does not register a Codex agent.

The Harness's `sdd/workflows/` contains internal development lifecycle procedures. The consumer `workflows/` convention above describes operational flows that compose Skills; it does not relocate or replace the SDD process. GitHub Actions under `.github/workflows/` retain their own execution contract.

## Adoption and migration

New agent and hybrid projects MUST use the composed template layout. Existing consumers MUST adopt it through a reviewed migration pinned to an exact Harness release. Classify existing root artifacts before moving them: Plugin exports and application source may legitimately remain in their current locations. Convert role Markdown to valid agent TOML when appropriate; update dependency references and validate discovery and behavior. Renaming a file alone is not a verified migration.

## External format references

- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [Codex project guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

These references describe executor formats; Versat policy remains in the versioned Standards resolved by the project.
