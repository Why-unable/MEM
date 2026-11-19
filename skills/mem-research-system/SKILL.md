---
name: mem-research-system
description: "Operate the MEM personal paper research system: discover and verify papers, maintain the local Obsidian research vault, update paper/edge JSON, rebuild research maps and Canvas, and export Zotero-compatible metadata."
metadata:
  version: "0.1.0"
---

# MEM Research System

Use this skill when the user wants to add, verify, organize, map, or review academic papers in the `MEM` workspace.

## Locate MEM

Find the workspace root containing:

- `SYSTEM.md`
- `README.md`
- `data/`
- `vault/`
- `scripts/build_research_map.py`

Do not assume the current working directory is MEM. Resolve the path first.

## Read before acting

Read:

1. `SYSTEM.md`
2. `config/mem.config.json`
3. `config/venues.yaml`
4. For a new topic: `skills/mem-literature-map/SKILL.md`
5. For an existing topic: `data/<topic>/queries.md` and `maps/<topic>/research-map.md`

## Workflow

### 1. Lock the scope

State the research object, time window, required venues, exclusions, and output mode.

### 2. Discover

Use Scholar Literature Maps as the retrieval workflow. Prefer:

- field-standard English query terms
- core seed papers first
- controlled adjacent expansion
- reviews, foundational papers, methods, benchmarks, contradictions, recent frontier

### 3. Verify

For every candidate, verify:

- exact title
- authors
- year
- venue
- official record or PDF
- DOI / arXiv / OpenReview / ACL Anthology / AAAI / PMLR ID

Do not use model memory as the only source for venue or DOI.

### 4. Write data

Add verified papers to:

```text
data/<topic>/papers.json
```

Add conceptual edges to:

```text
data/<topic>/edges.json
```

Use stable lowercase paper IDs such as `amem`, `gmemory`, `longmemeval`.

### 5. Validate

```bash
python3 scripts/validate_mem.py \
  --papers data/<topic>/papers.json \
  --edges data/<topic>/edges.json
```

Fix errors before building.

### 6. Build

```bash
python3 scripts/build_research_map.py \
  --papers data/<topic>/papers.json \
  --edges data/<topic>/edges.json \
  --vault vault \
  --out maps/<topic> \
  --topic '<Topic Name>'
```

This writes:

- `vault/10_Papers/*.md`
- `vault/20_Topics/<Topic Name>.md`
- `vault/40_Maps/<Topic Name>.canvas`
- `maps/<topic>/research-map.md`
- `maps/<topic>/research-map.json`
- `maps/<topic>/research-map.canvas`
- `maps/<topic>/papers.csv`

### 7. Export Zotero formats

```bash
python3 scripts/export_zotero_formats.py \
  --papers data/<topic>/papers.json \
  --out-dir data/<topic> \
  --stem <topic>
```

### 8. Review in Obsidian

Open the topic note and Canvas. Ask the user to review:

- missing key papers
- wrong categories
- weak or speculative edges
- papers that should be core vs supporting
- claims that require PDF-level checking

## Rules

- Main map: published papers only.
- CCF-A first; ICLR/COLM/MLSys allowed with explicit labels.
- Findings and workshops are supporting nodes unless explicitly requested otherwise.
- arXiv-only papers go to `preprints-excluded.md`.
- Edges are conceptual unless explicitly documented as citation edges.
- Never overwrite the user's Obsidian notes without a preview/diff when the task is an update.
- Keep the original user idea text in `30_Ideas`; do not rewrite it in place.

## Current topic

`Agent Memory 2025+` is the first working example. Use it as the reference implementation.
