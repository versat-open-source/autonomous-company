# Product scope

Autonomous Company is currently a governed local agent workspace for user-directed Versat ERP operations across separately configured companies. Its users are authorized ERP operators. It provides routing instructions, a local gate, domain skill integration, governance and offline validation.

The workspace neither configures MCP servers nor implements unattended finance, business calculations, a backend or a hosted user interface. Future capabilities require SDD changes and updated operational readiness.

Its reusable ERP capability is `.agents/skills/versat-mcp/`; `.codex/agents/operator.toml` defines the supervised execution role; `workflows/versat-operation/workflow.md` composes the operational steps and must be explicitly loaded. Native role loading and live integrations require separate verification.
