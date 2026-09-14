# Operations and recovery

There is no deployed workload or unattended execution. Availability, latency and capacity telemetry are the responsibility of the chosen agent client and Versat MCP service. Repository checks cover local instruction and helper changes only.

## Data and access

The public repository contains source, standards and fictional fixtures. Real company identifiers and connection names are confidential local configuration. ERP financial records and tokens must remain in the authorized ERP/client environment. Do not add raw business payloads to logs, tests, issues or PRs.

Keep the local mapping only for the lifetime of the installation, restrict access to the operator account and remove it on retirement. Remove client credentials separately. Preserve required financial audit records in the organization's approved system; the owner must approve retention and deletion periods before production writes. This repository does not invent a statutory retention period.

## Approval and evidence

Before a financial write, verify explicit user authority for the company and action. An explicit current instruction can provide that authority. Record the actor, timestamp, model, instruction commit, logical action, selected company, tool provenance, approval and outcome in a private audit system without tokens or full sensitive payloads.

Unknown company, unavailable connection or denied access: stop and report to the operator. Partial financial write: preserve returned record identity privately, inspect the same company's record and follow the skill's recovery flow. Never switch company or retry blindly. Escalate incidents to the human operator and repository maintainer through private channels.

## Recovery and retirement

Before enabling production writes, the operational owner must define approved recovery-time and recovery-point objectives for the actual client/ERP deployment and complete live behavioral evals. These are not yet established here.

Revert defective code or instructions through a PR, preserving local mappings. A repository revert does not undo ERP transactions; corrections require an explicitly authorized business operation in the affected company. No background retry or scheduled operation is installed by this project.
