# Security Standard

- Apply least privilege to humans, agents, service accounts and tools.
- Secrets MUST use an approved secret manager and MUST NOT be committed.
- Untrusted input MUST be validated at trust boundaries.
- High-impact or irreversible actions MUST require explicit authorization and auditable execution.
- Dependencies and build provenance MUST be reviewable.
- Projects handling sensitive data MUST document classification, retention, access and deletion.
- Security controls that can be deterministic MUST be enforced by CI or platform policy.
