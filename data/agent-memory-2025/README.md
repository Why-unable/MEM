# Agent Memory 2025+ Dataset

## Current State

- Papers: 52
- Conceptual edges: 86
- Evidence cards: 52/52 `evidence-checked`
- Baseline timeline rows: 52
- Formal publication only

## Files

| 文件 | 用途 |
|---|---|
| `papers.json` | 主论文库，52 篇 |
| `edges.json` | 概念关系，86 条 |
| `baseline-timeline.json` | 时间化效果、数据集、baseline 变化源数据，52 篇 |
| `baseline-timeline.csv` | `baseline-timeline.json` 的筛选/分析表 |
| `queries.md` | 检索协议与来源 |
| `preprints-excluded.md` | 未进入主地图的高相关预印本 |
| `COVERAGE_AUDIT.md` | 覆盖审计、增补批次与暂缓候选 |
| `VENUE_AUDIT.md` | 从 `papers.json` 自动生成的 venue 分层清单 |
| `agent-memory-2025.bib` | 初始 Zotero BibTeX 导入 |
| `agent-memory-2025.ris` | 初始 Zotero RIS 导入 |
| `agent-memory-2025-batch2.bib/.ris` | 2026-11-27 Batch 1 增量导入 |
| `agent-memory-2025-batch3.bib/.ris` | 2026-11-27 Batch 2 增量导入 |
| `agent-memory-2025-batch4.bib/.ris` | VikingMem 增量导入 |

## Source-of-truth Rules

- `papers.json` 和 `edges.json` 是论文与关系源数据。
- `baseline-timeline.json` 是时间化 baseline 的源数据；CSV 和 Obsidian 笔记必须由脚本生成。
- `VENUE_AUDIT.md` 必须由 `papers.json` 生成，不手工维护论文列表。
- 论文 evidence 位于 `vault/10_Papers/evidence/`，一篇论文一个文件。
- 个人路线总纲位于 `个人理解/路线分类.md`，需人工维护。
- 不提交 PDF、Zotero 数据库、私密导出或凭证。

## Paper Record Schema

```json
{
  "id": "amem",
  "title": "...",
  "year": 2025,
  "venue": "NeurIPS 2025 poster",
  "venue_short": "NeurIPS 2025",
  "venue_tier": "CCF-A",
  "category": "architecture",
  "priority": 1,
  "role_zh": "...",
  "authors": ["..."],
  "abstract": "...",
  "openreview_url": "...",
  "pdf_url": "...",
  "DOI": "...",
  "arXiv": "...",
  "status": "published"
}
```

## Edge Schema

```json
{"from": "amem", "to": "gmemory", "type": "extends", "label": "单 agent 记忆 → 多 agent 层次记忆"}
```

## Baseline Timeline Row

```json
{
  "date": "2026-08",
  "paper_id": "vikingmem",
  "short": "VikingMem",
  "tagline": "事件实体",
  "type": "method",
  "lane": "utility",
  "datasets": "LoCoMo；LongMemEval-S",
  "headline": "LoCoMo LLM-J 88.83/90.12；LongMemEval 66.36/75.80",
  "comparison": "GPT-4o-mini LoCoMo：88.83 vs Mirix 78.66",
  "delta_pct": 12.93,
  "baseline_shift": "...",
  "note": "..."
}
```

## Rebuild

```bash
make check
```

## Multi-Machine

- 不要多人同时编辑 `papers.json`、`edges.json` 或 `baseline-timeline.json`。
- 时间轴发生修改时运行 `make baseline-timeline`。
- 文档或数据发生修改时运行 `make docs-check`。
- 详细协作规则见 `docs/multi-machine-playbook.md`。
