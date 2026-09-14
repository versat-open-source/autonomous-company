# Repository readiness

Bootstrap date: 2026-09-12. Owner: `versat-open-source`; maintainer: `@elviszoz`.

## Local governance

Identity, Standards snapshots, exact commit provenance, base + agent composition and SDD are present. Local validation passed on Python 3.12.14: formatting/lint, five unit-test groups including 15 fictional routing scenarios, project/SDD schemas, exact Standards resolution and snapshot integrity, local-data exclusion and a scan of public candidate files. All 23 imported Harness artifacts were verified against their Git blob hashes in the pinned upstream commit.

The installed Harness 0.2.0 validation entry point failed because its compatibility manifest contains `./skills` where the validator expects `./skills/`. The package was not modified to hide this failure. The project uses its own consumer validator for schemas, resolution, digests, privacy and SDD traceability; a passing consumer check does not turn the installed package check into a pass.

## Repository controls

- Public repository: https://github.com/versat-open-source/autonomous-company.
- Bootstrap PR: https://github.com/versat-open-source/autonomous-company/pull/1. The full project is on `bootstrap/project-bootstrap`; `main` contains the seed `.gitignore` until review and merge.
- CI passed for bootstrap commit `fa22965`: [push run](https://github.com/versat-open-source/autonomous-company/actions/runs/34713957275) and [PR run](https://github.com/versat-open-source/autonomous-company/actions/runs/34713957336). The PR check list is authoritative for later evidence-only commits.
- `main` protection verified: required `validate` check with an up-to-date branch, one approving review, stale approval dismissal, CODEOWNERS review, conversation resolution and linear history; protections apply to administrators. Force pushes and branch deletion are disabled.
- CODEOWNERS is included in the bootstrap PR and becomes the base-branch ownership file after merge. No organization teams existed at bootstrap; the maintainer is the initial code owner.
- Secret scanning, secret push protection, vulnerability alerts and private vulnerability reporting were enabled and verified. Dependabot monthly update configuration is included in the PR and becomes active after merge.
- Both initial commits (70 file versions) were checked for local company names, identifiers and connection names. No matches were found; the real mapping was never committed. Public commits use the maintainer's GitHub noreply address.

## Operational gates

Live MCP connectivity and LLM behavioral evals are unverified. No ERP call was made by the bootstrap. Production write readiness requires the operational owner to approve audit retention and recovery objectives and verify the actual model/client/ERP workflow. There is no deployed service or unattended execution.

No project-wide distribution license is selected. An independent eligible CODEOWNERS reviewer is needed to approve the bootstrap PR; the PR author cannot self-approve. These gaps must not be represented as verified compliance.
