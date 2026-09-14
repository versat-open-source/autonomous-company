# Versat operation

1. Read `AGENTS.md`, the local mapping and the imported Versat skill. Establish the operating company, independently of any counterparty mentioned in the request.
2. Discover the actual MCP tools and connection provenance available in the client. Pass only available connection names to the local gate. For example, using fictional names:

   ```sh
   .venv/bin/python scripts/resolve_company.py \
     --company-name 'Example North' \
     --available-connection 'mcp-example-north' \
     --operation read
   ```

3. For a continuation without a new company, use `--previous-name` and `--continuation`; supply explicit current context when present. For writes, use `--operation write --authorized` only when user authorization already covers the company and action. The flag records the calling agent's assessment; it is not independent proof of consent.
4. A `blocked` result (exit 2) stops the operation. Explain missing information or availability; never try another company's connection as fallback. On `pass`, use exactly the returned connection and follow the skill's relevant domain reference.
5. Re-resolve IDs in each company's base. Validate the outcome and report company, action and partial success. Never blindly retry a financial write. For multiple companies, repeat the workflow separately for each one.

The helper reads local JSON and emits a route. It does not call tools, maintain credentials, interpret free-form user intent or enforce MCP-side permissions. See the operations runbook for audit and recovery obligations.
