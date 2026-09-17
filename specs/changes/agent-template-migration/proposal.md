---
change: agent-template-migration
status: implemented
owner: versat-open-source
summary: Adopt the requested consumer agent layout and explicit operational workflow contract.
risk: medium
---

# Proposal

The user requested adoption of the new Harness agent definitions: keep project Skills under `.agents/skills/`, convert root role guidance to `.codex/agents/`, and structure operational workflows according to the new Standard. The root `skills/` currently contains only explanatory documentation; `agents/operator.md` is role guidance, not application code or a Plugin export.

Target the exact Harness revision `9260d3a04f658b6eeec86a8dc88563d2051cb09d`, whose VERSION is still 0.2.0 and whose changes are explicitly Unreleased. The installed 0.2.0 package does not contain this layout. The upstream layout PR #5 was verified merged; this user-requested revision adoption does not assert that a new release exists. ADR-0002 records the exception to release-only adoption. No Shortcut Story was supplied; do not invent one.

Scope covers the source snapshots and provenance, role conversion, workflow contract, documentation, consumer validation and a reviewable PR. ERP transactions, credentials, company mappings, installed Plugin updates, and live agent execution are outside this migration. Preserve the imported Skill byte for byte and preserve the routing gate's behavior.

Acceptance is a single canonical layout, explicit dependency and recovery contracts, passing offline validation and truthful records of outstanding runtime, review and merge checks.
