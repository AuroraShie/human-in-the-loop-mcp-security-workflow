# Workflow governance

## Approval boundary

The operator owns authorization and action-level approval. Creating a session requires an explicit authorization confirmation, but that value is supplied by the caller and is not independently verified by the adapter.

## Tool boundary

Security tools are manually operated outside the MCP adapter. Their evidence may be summarized into the session but does not directly change a result to Confirmed. Tool policy is documented here and in an example policy file; it is not completely runtime-enforced.

## Verification boundary

The workflow separates candidate leads from confirmed outcomes. A Confirmed record requires both a caller-supplied manual-replay flag and a concrete impact statement. This is a process gate, not a replacement for human judgment.

## Stop boundary

The session must stop after uncertain or out-of-scope boundaries. The runtime also forces a stopped state for sensitive non-owned data, service instability, or an explicit forced-stop conclusion. A stopped session does not accept further active workflow records.

## Data handling

Use redacted summaries. Keep raw traffic, credentials, session files, reports, captures, and target-specific notes outside this repository. JSON persistence is local and has limited concurrency guarantees.
