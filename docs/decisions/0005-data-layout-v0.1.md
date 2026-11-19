# ADR-0005: v0.1 Uses Single-File JSON

- Status: accepted
- Date: 2026-11-19
- Owners: MEM
- Related: `data/agent-memory-2025/papers.json`

## Context

The first research case needs a simple, inspectable data source. A single JSON file is easy to validate and build.

## Decision

v0.1 stores papers and edges in:

```text
data/agent-memory-2025/papers.json
data/agent-memory-2025/edges.json
```

## Consequences

- Simple to build and inspect.
- Multi-machine edits to different papers can create merge conflicts.
- Once collaboration begins, migrate to per-paper YAML under `data/papers/` and generated indexes.

## Migration trigger

Migrate when any of the following occurs:

- More than one machine edits papers concurrently.
- More than 50 papers are added.
- Merge conflicts occur in `papers.json`.
- Paper notes become the preferred source of truth.
