# Language Standard

## Required language by artifact

| Artifact | Required language |
|---|---|
| GitHub organization names | English |
| Repository names | English |
| Directories | English |
| Structural files | English |
| Classes, functions, methods and variables | English |
| APIs and endpoints | English |
| DTOs, schemas and contracts | English |
| Events | English |
| New database tables and columns | English |
| Code comments | English |
| Technical READMEs | English |
| ADRs and architecture documentation | English |
| Skills reusable across systems | English |
| `AGENTS.md` files and agent instructions | English |
| SDD technical specifications and business rules | English |
| Internal Finance, HR, Customer Success, Sales and other business playbooks | Spanish |
| Internal issues and pull requests | Spanish |
| Discussions between collaborators | Spanish |
| Slack, meetings and other corporate communication | Spanish |
| Product user interfaces | Canonical English, with Portuguese and Spanish translations |
| Community-facing documentation | Canonical English, with Portuguese and Spanish translations |

## Translation requirements

For product user interfaces and community-facing documentation, English MUST be the canonical source. Portuguese and Spanish translations MUST be provided and kept aligned with the canonical English content.

## Exceptions

- Widely accepted technical terms MAY remain in English in Spanish content when translation reduces precision.
- Generated or imported third-party artifacts MAY retain their original language when modification is unsafe.
- Existing database objects MAY retain their current names when renaming them would introduce compatibility or migration risk.
- Any project-wide exception MUST be documented in an ADR.
