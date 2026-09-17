# Authorization and stop policy

This policy describes the intended operating boundary for the local MCP adapter. It is guidance, not a complete runtime enforcement layer.

## Authorization

- Create a session only after the operator supplies an exact scope, an authorization basis, an allowed target kind, and an explicit confirmation.
- Record endpoints only after the related asset is both confirmed and in scope.
- Target-side browsing, requests, scans, and validation are manual operator actions. The adapter does not perform them.

## Stage gates

- Map at least five key endpoints before selecting a hypothesis.
- Select one hypothesis per session.
- Record no more than one baseline and one supplemental comparison for that hypothesis.
- Treat scanner output as a Candidate until it is manually replayed.
- Mark a result Confirmed only when the caller supplies both a manual-replay flag and a concrete impact statement.

## Stop behavior

- Stop when the operator records non-owned sensitive data, service instability, or a boundary stop.
- A stopped session accepts no further active workflow records.
- Preserve only the minimum redacted summary needed for a recap.
