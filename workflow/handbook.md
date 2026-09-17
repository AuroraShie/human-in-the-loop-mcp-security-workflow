# Authorized security workflow handbook

## Purpose

This handbook describes a Human-in-the-loop workflow for authorized Web/API security analysis. It is a process artifact for the local MCP adapter, not a target-testing playbook.

## Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Human operator | Confirms authorization, performs target-side work, decides to stop, replays results, confirms impact | Keeps high-risk decisions and actions under human control |
| Host LLM | Reads persisted state, organizes information, proposes the next bounded step | Does not treat a suggestion as authorization or a tool lead as a finding |
| MCP workflow layer | Persists state and enforces selected stage and result gates | Does not contact targets or execute security tools |
| Security tools | Produce observations or leads | Their output is Candidate evidence, not a final conclusion |

## Workflow record

Each session has an authorization statement, scope, asset record, interface map, one hypothesis, validation records, and a stop or closure outcome. The session data is persisted locally as JSON and must be treated as sensitive operational data, even though it is excluded from this repository.

## Evidence discipline

Record concise, redacted summaries instead of raw credentials, traffic, or personal data. Preserve only what is necessary to explain a conclusion or a stop. Do not move real session data, captures, reports, or target notes into the showcase repository.

## Candidate and Confirmed

A Candidate is a tool or observation lead that still needs human review. A Confirmed result requires a manual replay and a concrete impact description. This distinction prevents a scanner label or an LLM suggestion from becoming a final security conclusion by itself.
