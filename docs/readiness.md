# Repository readiness

Bootstrap date: 2026-09-12. Owner: `versat-open-source`; maintainer: `@elviszoz`.

## Local governance

Identity, Standards snapshots, exact commit provenance, base + agent composition and SDD are present. Local validation passed on Python 3.12.14: formatting/lint, five unit-test groups including 15 fictional routing scenarios, project/SDD schemas, exact Standards resolution and snapshot integrity, local-data exclusion and a scan of public candidate files. All 23 imported Harness artifacts were verified against their Git blob hashes in the pinned upstream commit.

The installed Harness 0.2.0 validation entry point failed because its compatibility manifest contains `./skills` where the validator expects `./skills/`. The package was not modified to hide this failure. The project uses its own consumer validator for schemas, resolution, digests, privacy and SDD traceability; a passing consumer check does not turn the installed package check into a pass.

## Repository controls

Public repository creation, bootstrap PR, protected `main`, required `validate` check, CODEOWNERS review, secret scanning, push protection and private vulnerability reporting: pending remote setup and verification.

## Operational gates

Live MCP connectivity and LLM behavioral evals are unverified. No ERP call was made by the bootstrap. Production write readiness requires the operational owner to approve audit retention and recovery objectives and verify the actual model/client/ERP workflow. There is no deployed service or unattended execution.

No project-wide distribution license is selected. An independent eligible CODEOWNERS reviewer is needed to approve the bootstrap PR; the PR author cannot self-approve. These gaps must not be represented as verified compliance.
