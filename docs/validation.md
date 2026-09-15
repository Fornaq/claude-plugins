# Validation record

Package version: **1.0.0**. Checked **September 15, 2026** with **Claude Code 2.1.259**.

## Passed

- Marketplace validation with `claude plugin validate . --strict`.
- Plugin validation with `claude plugin validate ./plugins/lazy-schedule --strict`.
- Distribution file allowlist, relative marketplace source, and remote MCP configuration checks.
- Marketplace registration and plugin installation using an isolated temporary Claude configuration. The installed plugin reported version 1.0.0, enabled status, and the expected HTTP MCP endpoint.
- A second isolated installation directly from the public `Fornaq/claude-plugins` GitHub marketplace loaded all three skills and the remote MCP connection.
- GitHub Actions validation passed for the initial release: https://github.com/Fornaq/claude-plugins/actions/runs/35035739096.
- The published release ZIP's GitHub SHA-256 digest matched the local package checksum.
- Public MCP health returned success.
- OAuth protected-resource and authorization-server discovery returned the expected resource, issuer, dynamic client registration endpoint, and S256 PKCE support.
- An unauthenticated MCP initialize request was rejected with HTTP 401 and a protected-resource metadata challenge.

## Still requires an account session

- OAuth sign-in and consent in the target Claude host.
- Authenticated task/goal reads and writes, progress publication, and revocation checks in [acceptance.md](acceptance.md).
- Directory submission and review by Anthropic.

These checks validate packaging, installation, and unauthenticated endpoint behavior. They do not establish that authenticated workflows or host-specific behavior have passed.
