---
change: project-bootstrap
requirements:
  - id: REQ-001
    statement: Preserve local company routing without publishing operational company data.
    acceptance:
      - The local mapping is ignored and no tracked artifact contains its names, documents or connection identifiers.
      - Missing, conflicting or unknown company context produces no permitted tool call.
  - id: REQ-002
    statement: Pin the applicable Harness Standards and identify the project.
    acceptance:
      - Agent, finance, Python and high-criticality resolution matches the lockfile and snapshot digests.
      - Source artifacts match Harness 0.2.0 commit 85194bf7fb6c708de6a0f29acabb90eaaa1d055f.
  - id: REQ-003
    statement: Provide reproducible validation and critical routing evaluations.
    acceptance:
      - Formatting, lint, schemas, integrity, privacy, unit tests and offline evals run through one command and CI.
      - A write without explicit authorization or an unavailable connection fails closed.
  - id: REQ-004
    statement: Publish a governed repository with truthful readiness evidence.
    acceptance:
      - A public repository exists under versat-open-source and bootstrap is submitted through a PR.
      - Required validation, CODEOWNERS review and force-push protection are configured.
      - English documentation has aligned Portuguese and Spanish entry points; live ERP gaps are explicit.
---

# Requirements

Users supply the intended operating company, separately from customer or supplier names in documents. Only the local mapping defines eligible companies. The workspace has no deployment or unattended scheduler.
