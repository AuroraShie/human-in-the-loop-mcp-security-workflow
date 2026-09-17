# Security review

This review applies the standard for a future Public repository even though the intended GitHub repository is Private.

| Source or candidate path | Risk category | Repository decision |
| --- | --- | --- |
| `tools/PentestGPT/integrations/pentestgpt_mcp.py` | Local adaptation; dependency imports; workflow strings | Included with repository-local paths and a dependency-unavailable fallback for offline workflow use. No credential value was found in the reviewed copy. |
| `tools/PentestGPT/tests/test_mcp_workflow.py` | Synthetic test records; authorization-like parameter names | Included after package-import adjustment. No credential value was found. |
| `tools/PentestGPT/.env` | Environment configuration and possible secrets | Excluded. |
| `tools/PentestGPT/mcp-sessions/` | Session data | Excluded and ignored. |
| `reports/`, `evidence/`, `temp/`, Burp data | Real targets, traffic, findings, and evidence | Excluded and ignored. |
| `tools/PentestGPT/pentestgpt_agent/`, `pentestgpt_legacy/`, upstream tests and docs | Third-party source | Excluded; referenced only through attribution and separate-install instructions. |
| Tool binaries, virtual environments, keys, credentials, logs | Secrets, third-party artifacts, or local machine state | Excluded and ignored. |

## Review outcome

- The committed example session is fictional and uses `example.com` only.
- No real vulnerability, target, account, token, cookie, request, response, session, or absolute local path is intentionally committed.
- The final staged-file scan must be rerun immediately before commit without printing matched secret values.
