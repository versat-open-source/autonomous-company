# Security

Do not report credentials, company records or exploitable details in public issues. Use the repository's private vulnerability reporting channel when enabled, or contact the repository maintainer privately.

Private routing configuration stays on the operator's machine; authentication belongs to the configured MCP client and its secret store. The workspace is not an authorization boundary: each MCP connection must enforce its own company and user permissions.

Local validation checks known local company values and common credential signatures. GitHub secret scanning and push protection complement these checks. None of these scans proves that arbitrary text is safe to publish; review staged content before submission.
