# ADR-0002: Main Map Contains Published Papers Only

- Status: accepted
- Date: 2026-11-19
- Owners: MEM
- Related: `data/agent-memory-2025/queries.md`

## Context

The agent-memory literature contains many high-visibility arXiv preprints. Treating preprints as formally published would weaken venue audits and reproducibility.

## Decision

The main map contains papers with a verified formal venue record. ICLR, COLM, MLSys, ACL Findings, and CCF-B venues are included only with explicit tier labels.

arXiv-only work is recorded in `preprints-excluded.md` and excluded from the main map.

## Consequences

- The main map is conservative and auditable.
- Some influential systems may be absent until their formal publication is verified.
- Future updates must verify new proceedings rather than relying on memory.

## Alternatives

- Include all arXiv: rejected due to venue-quality ambiguity.
- Exclude all non-CCF-A: rejected because it would remove highly relevant ICLR/COLM work.
