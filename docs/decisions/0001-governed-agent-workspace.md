# ADR-0001 — Govern the agent workspace with private local routing

- Status: Accepted
- Date: 2026-09-12

## Context

The initial workspace has an upstream skill, instructions and local company mappings. It needs a public repository without operational company data, plus a governed lifecycle. It does not implement a running software service.

## Decision

Use Harness 0.2.0, base + agent templates, finance domain and high operational criticality. Publish the applicable source artifacts with explicit owner authorization; pin their exact commit and digests. Preserve company data solely in ignored local JSON. Use a deterministic local routing gate and fictional offline evals while documenting the limits of instruction enforcement.

Translate project instructions into canonical English, retaining imported third-party skill content under the Language Standard's imported-artifact exception. Provide Portuguese and Spanish community entry points. Do not assign a new distribution license to imported material.

Initialize `main` with only `.gitignore` as a repository seed; submit the complete material bootstrap as a PR. The seed exists only to enable a normal reviewable branch lifecycle. Enable required checks, CODEOWNERS review and protected `main` before merging material changes.

## Consequences

New users must configure their own local companies and client connections. The public project can validate without private corporate access. Hosted execution, live model evals, ERP access and financial audit retention remain explicit operational responsibilities rather than implied readiness.

A second independent reviewer with write access may be needed before the bootstrap PR can merge; the author cannot approve their own PR. Do not weaken the review requirement to bypass that gate.
