# Security review

This review applies the standard for a future public repository even though the intended GitHub repository is private.

| Source or candidate material | Repository decision |
| --- | --- |
| Local MCP adapter and focused workflow tests | Included as a repository-local adaptation with no vendored PentestGPT source. |
| Generic workflow handbook, SOP, governance, policy example, and templates | Included after replacing engagement-specific information with reusable placeholders. |
| Synthetic `example.com` state example | Included; it has no real target traffic, account, credential, payload, or finding. |
| Original prompt, tool-use guidance, allowlist, inventory, deployment notes, memory, platform report template | Excluded. |
| Complete OWASP WSTG copy and same-product-line-reuse source material | Excluded. |
| Reports, evidence, session data, captures, Burp traffic, target notes, and temporary files | Excluded and ignored. |
| PentestGPT upstream source, virtual environments, keys, credentials, logs, and binaries | Excluded. |

## Review outcome

- The included implementation has no hard-coded target, organization, school, local machine path, IP, domain other than `example.com`, API, table, field, cookie, token, account, report number, or personal identity.
- The final staged-file scan must be rerun immediately before commit without printing matched secret values.
