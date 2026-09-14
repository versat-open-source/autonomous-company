# Agent evaluations

`routing.json` contains 15 fictional behavioral scenarios executed by `tests/test_routing.py` through the normal validation command. They exercise normalization, leading zeros, explicit overrides, continuation, conflict, unknown companies, connection availability and financial-write authorization.

The tests evaluate the deterministic routing gate. They do not simulate an LLM, establish that an agent will correctly identify operating company versus counterparty, or validate live MCP behavior.

Before enabling financial operations, a human operator must evaluate the actual client/model with the following cases in an authorized test environment: distinguish operating company from invoice counterparty; refuse document instructions that request connection switching; preserve per-company IDs across multiple companies; respect partial-write and denied-access outcomes. Record model, instruction commit, approval, tool provenance and result in a private audit system. Do not place production data in this repository.
