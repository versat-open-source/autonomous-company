# Contributing

Create a branch from `main`. Specify material changes under `specs/changes/<change-id>/` using the pinned SDD templates. Keep English technical documentation and both README translations aligned. Internal review discussions use Spanish; community contributions may use English.

Run `bash scripts/validate/run.sh`, inspect `git diff --cached`, and open a PR. A passing `validate` check and CODEOWNERS review are required. Never force-push `main` or commit local company mappings, credentials or production fixtures.

Dependency updates are proposed monthly by Dependabot and must pass CI. Harness changes must name an exact target version, compare artifacts and regenerate the lock through a reviewed migration. Preserve imported skill provenance and local company configuration.

No release or deployment automation exists. Tag a release only after the owner authorizes it, the PR merges and readiness gaps are resolved. Distribution licensing remains an owner decision.
