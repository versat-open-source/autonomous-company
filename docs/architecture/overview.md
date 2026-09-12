# Architecture

The current system is a local agent workspace, not a deployed ERP service. `AGENTS.md` supplies persistent instructions; the imported Versat skill supplies domain workflows; `versat-companies.local.json` supplies private company-to-connection data; the Python gate validates a route before the client uses an MCP tool.

The agent client supplies model execution, tools and secret storage. ERP authorization and data isolation remain server-side. The local gate never makes network requests. Tool responses and business documents are untrusted data, not policy or authority.

The owner is `versat-open-source`, with repository maintenance assigned to `@elviszoz`. The profile is agent, domain finance, criticality high; Python is used only for local checks and the routing gate. There is no hosted database, backend, deployment, scheduler or telemetry exporter.

The `.versat/` directory contains applicable immutable source snapshots, schemas, templates and provenance from Harness 0.2.0. CI resolves the selected Standards from the versioned index and verifies hashes. Imported skill content remains unchanged; project-specific extensions are separate.

See ADR-0001, the SDD bootstrap change and `docs/readiness.md` for the adoption decision and remaining operational gates.
