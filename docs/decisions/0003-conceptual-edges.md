# ADR-0003: Map Edges Are Conceptual by Default

- Status: accepted
- Date: 2026-11-19
- Owners: MEM
- Related: `data/agent-memory-2025/edges.json`

## Context

The current map was built from titles, abstracts, and venue records. It does not yet contain a complete citation graph.

## Decision

Edges in `edges.json` are conceptual relationships:

- `extends`
- `related`
- `contrasts`
- `applies`
- `evaluates`
- `evaluated-by`
- `risk`
- `inspired-by`

They must not be presented as verified citation edges unless explicitly labeled.

## Consequences

- The map is useful for research synthesis without overstating bibliometric evidence.
- A later citation graph can coexist as a separate artifact.

## Alternatives

- Delay the map until citation extraction is complete: rejected; conceptual maps are useful earlier.
