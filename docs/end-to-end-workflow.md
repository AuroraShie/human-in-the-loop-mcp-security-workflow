# End-to-end workflow

This document describes the intended handoff between the human operator, host LLM, MCP workflow layer, and security tools. It does not authorize any target-side action by itself.

## 1. Authorization

The operator defines the exact permitted scope and authorization basis. The MCP layer rejects creation when explicit authorization confirmation is absent. The LLM can organize the scope statement but does not decide whether authorization is valid.

## 2. Scope and asset confirmation

The operator confirms an asset is in scope and records ownership evidence. The runtime requires a confirmed in-scope asset before interface records can be added.

## 3. Endpoint mapping

The operator maps key interfaces from approved, normal use or other permitted observation. The LLM may help organize the map. The runtime changes to hypothesis selection only after five endpoints have been recorded.

## 4. Hypothesis selection

The operator and LLM narrow the mapped evidence to one safety-bounded hypothesis. The MCP layer accepts one hypothesis per session so that validation history stays attributable to a single direction.

## 5. Controlled validation

The human performs the real target-side action. The workflow records a baseline, one controlled change, and an observed result. At most one supplemental comparison is accepted, and only after an insufficient or suspected first result.

## 6. Result recording

Security-tool output is recorded as Candidate. A Confirmed conclusion requires human manual replay and a concrete impact statement supplied by the caller. These gates make the state explicit; they do not independently verify the caller's statement.

## 7. Stop, report, and closure

The operator stops on an out-of-scope or uncertain boundary, and the runtime stops when sensitive non-owned data, service instability, or a forced-stop conclusion is recorded. The remaining work is a minimum redacted recap and closure, not expanded testing.
