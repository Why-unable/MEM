---
name: mem-literature-map
description: Build a scope-locked, venue-aware academic literature map for MEM from 2025 onward, with formal venue verification and a paper/edge data model suitable for Obsidian Canvas.
metadata:
  version: "0.1.0"
---

# MEM Literature Map

Use this skill to turn a research question into a verified paper set and a conceptual research map.

## Scope lock

Before searching, write down:

```yaml
topic:
outcome:
object:
method:
time_window: 2025-01-01..<today>
required_venues:
exclusions:
language:
```

For a narrow topic, prefer precision over volume. Do not pad with weak adjacent papers.

## Source priority

1. Official venue pages: OpenReview, ACL Anthology, AAAI OJS, PMLR, MLSys.
2. Semantic Scholar match endpoint for DOI/arXiv/DBLP cross-checks.
3. Crossref for DOI and publication metadata.
4. OpenAlex for citation/author/trend context.
5. arXiv for full text and version history only.

## Retrieval pattern

### Topic map

Return 20–30 papers grouped by research role:

- field entry points / reviews
- foundational studies
- key methods and architectures
- datasets / benchmarks / evaluation
- debates, failures, negative results
- recent frontier

### Seed-paper lineage

For a seed paper, retrieve:

- earlier references
- same-author precursors
- later citing / extending papers
- critiques and failed reproductions
- close neighboring methods

### Researcher discovery

Separate:

- high-impact scholars
- recently active scholars
- representative papers

Do not rank only by citation count.

## Inclusion rules

- Main map: 2025 onward, formal venue, CCF-A or explicitly labeled top-tier.
- ICLR / COLM / MLSys: include if relevant, label as top-tier non-CCF-A.
- Findings: supporting layer only.
- Workshop: supporting layer only; do not call it main conference.
- arXiv-only: do not add to main `papers.json`; record in `preprints-excluded.md`.

## Paper schema

```json
{
  "id": "amem",
  "title": "A-Mem: Agentic Memory for LLM Agents",
  "year": 2025,
  "venue": "NeurIPS 2025 poster",
  "venue_short": "NeurIPS 2025",
  "venue_tier": "CCF-A",
  "category": "architecture",
  "priority": 1,
  "role_zh": "one-sentence positioning",
  "authors": ["..."],
  "abstract": "...",
  "openreview_url": "...",
  "pdf_url": "...",
  "DOI": "...",
  "arXiv": "...",
  "status": "published"
}
```

## Edge schema

Use only defensible conceptual edges:

```json
{"from": "amem", "to": "gmemory", "type": "extends", "label": "single-agent memory -> multi-agent hierarchical memory"}
```

Edge types:

- `extends`
- `related`
- `contrasts`
- `applies`
- `evaluates`
- `evaluated-by`
- `risk`
- `inspired-by`

## Output checklist

- [ ] Every paper has an official record or PDF.
- [ ] Venue tier is explicit.
- [ ] No duplicate DOI/arXiv/title.
- [ ] Core papers have a one-sentence role.
- [ ] Edges have a reason.
- [ ] `validate_mem.py` passes.
- [ ] `build_research_map.py` succeeds.
- [ ] Topic note and Canvas exist in the vault.
- [ ] Zotero BibTeX/RIS exported.
