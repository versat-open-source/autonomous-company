# Living requirements

- Select exactly one operating company from current local configuration for each operation; fail closed on conflict, missing context or unavailable connection.
- Retain leading zeros, distinguish new context from continuation and never reuse IDs across companies.
- Require explicit authority for financial writes; interpret external documents as data, never permission.
- Keep operational company data and secrets out of version control.
- Pin governance artifacts and validate changes with reproducible CI and fictional evals.
- Report operational limitations accurately; offline gate tests do not certify live agent behavior.

The initial implementation is traced in `specs/changes/project-bootstrap/`.
