---
change: project-bootstrap
status: accepted
owner: versat-open-source
summary: Establish a public, governed agent repository with private local company routing.
risk: high
---

# Proposal

The current workspace contains ERP instructions and local company mappings but has no Git history, CI or project governance. The user authorized local Git initialization, a public repository in `versat-open-source`, and publication of the applicable Harness artifacts on 2026-09-12.

Compose the Harness 0.2.0 base and agent profiles, preserve existing routing and the imported skill, and create a reviewable bootstrap PR. Financial tool access makes operational criticality high even though this change performs no ERP operations.

Scope includes versioned Standards, SDD, local routing checks, fictional evals, documentation, CI and repository protection. Building an autonomous financial service, configuring MCP credentials, transacting in ERP and selecting a distribution license are out of scope.

Acceptance: local validation passes, private mappings are excluded from all commits, and repository readiness accurately distinguishes verified controls from review and live-execution gaps.
