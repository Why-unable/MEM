# Agent Memory 2025+ Dataset

## Files

| 文件 | 用途 |
|---|---|
| `papers.json` | 主论文库，36 篇 |
| `edges.json` | 概念关系，47 条 |
| `queries.md` | 检索协议与来源 |
| `preprints-excluded.md` | 未进入主地图的高相关预印本 |
| `agent-memory-2025.bib` | Zotero BibTeX 导入 |
| `agent-memory-2025.ris` | Zotero RIS 导入 |

## Paper record schema

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

## Edge schema

```json
{"from": "amem", "to": "gmemory", "type": "extends", "label": "单 agent 记忆 → 多 agent 层次记忆"}
```
