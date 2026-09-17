# Agent Profile

Agent projects MUST define roles, instructions, Skills, tools, permissions, memory boundaries, evals, observability and human approval points. Instructions and tools MUST be versioned alongside the agent.

Project artifacts MUST follow the [Agent Artifact Standard](../core/agent-artifacts.md). The architecture MUST distinguish reusable capabilities, executor-specific roles and operational workflow composition, and identify the executor responsible for each workflow. Declaring a workflow does not establish that its dependencies or integrations are ready.
