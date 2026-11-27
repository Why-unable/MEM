# MEM Data Model

## 1. Paper

Current source of truth:

```text
data/<topic>/papers.json
```

Required fields:

| Field | Type | Description |
|---|---|---|
| `id` | string | Stable lowercase slug |
| `title` | string | Canonical title |
| `year` | integer | 2025 or 2026 |
| `venue` | string | Venue with track |
| `venue_short` | string | Display venue |
| `venue_tier` | enum | CCF-A / Top-ICLR / Top-COLM / Top-MLSys / ACL-Findings / CCF-B |
| `category` | enum | architecture / training / system / episodic / consolidation / personalization / multimodal / procedural / multiagent / evaluation / safety / application / survey |
| `priority` | integer | 1 core, 2 supporting |
| `role_zh` | string | One-sentence role in map |
| `authors` | string[] | Authors |
| `abstract` | string | Official abstract |
| `openreview_url` | string | Official record |
| `pdf_url` | string | Official PDF |
| `status` | enum | published / accepted / excluded |
| `collected_at` | date | Retrieval date |

Optional fields:

- `DOI`
- `arXiv`
- `DBLP`
- `S2CorpusId`
- `keywords`
- `verified_by`
- `confidence`
- `notes`

## 2. Edge

Source of truth:

```text
data/<topic>/edges.json
```

```json
{
  "from": "amem",
  "to": "gmemory",
  "type": "extends",
  "label": "单 agent 记忆 → 多 agent 层次记忆"
}
```

Allowed types:

- `extends`
- `related`
- `contrasts`
- `applies`
- `evaluates`
- `evaluated-by`
- `risk`
- `inspired-by`

## 3. Topic

Topic note:

```text
vault/20_Topics/<Topic Name>.md
```

Frontmatter:

```yaml
type: topic
topic: Agent Memory 2025+
paper_count: 52
updated: 2026-11-27
tags:
  - topic
  - agent-memory
```

## 4. Idea

Idea note:

```text
vault/30_Ideas/<Idea>.md
```

Frontmatter:

```yaml
type: idea
status: seed
created: 2026-11-19
tags:
  - idea
  - agent-memory
```

## 5. Paper Note

Generated paper note:

```text
vault/10_Papers/<paper-id>.md
```

Sections:

- one-line positioning
- metadata
- official abstract
- role in map
- relations
- reading questions
- extensible notes

The “可扩展笔记” section is the preferred place for manual additions.

## 6. Baseline Timeline

Source of truth:

```text
data/<topic>/baseline-timeline.json
```

This is a curated, cross-paper evidence layer. It is not a universal ranking. Each row should contain:

| Field | Description |
|---|---|
| `date` | Formal publication month |
| `paper_id` | Foreign key to `papers.json` |
| `short` | Display name |
| `tagline` | 2–6 字 core-mechanism label |
| `type` | method / benchmark / attack / survey |
| `lane` | utility / efficiency / safety / benchmark / survey |
| `datasets` | Benchmarks or datasets used |
| `headline` | Primary reported result |
| `comparison` | Strongest baseline or comparable change |
| `delta_pct` | Optional sortable relative-improvement proxy |
| `baseline_shift` | How the baseline set / evaluation changed |
| `note` | Caveat or reading warning |

Generated outputs:

```text
data/<topic>/baseline-timeline.csv
vault/40_Maps/<Topic> Baseline Timeline.md
```

Do not hand-edit the generated CSV or Obsidian note.

## 6.1 Venue Audit

Generated from `papers.json`:

```text
data/<topic>/VENUE_AUDIT.md
```

The audit groups all papers by `venue_tier` and records official-record / PDF links. Run:

```bash
make venue-audit
```

## 7. Map

Generated files:

```text
maps/<topic>/research-map.md
maps/<topic>/research-map.json
maps/<topic>/research-map.canvas
maps/<topic>/papers.csv
```

Do not hand-edit generated map files without updating the builder.

## 8. IDs

Use stable, readable IDs:

```text
amem
gmemory
memoryr1
longmemeval
persistbench
```

Do not use sequential numbers alone.

## 9. Migration

Current version uses single-file JSON. The next data-layout migration should move to:

```text
data/papers/<id>.yaml
data/relations/<id>.yaml
data/index/papers.generated.json
data/index/graph.generated.json
```

Migration trigger is documented in `docs/decisions/0005-data-layout-v0.1.md`.
