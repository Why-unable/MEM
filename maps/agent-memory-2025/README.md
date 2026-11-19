# Agent Memory 2025+ Map

## Outputs

- `research-map.md` — Mermaid 全景图 + 论文清单 + 关系边
- `research-map.json` — 机器可读节点/边
- `research-map.canvas` — 可导入 Obsidian 的 Canvas
- `papers.csv` — 表格视图
- `SYNTHESIS.md` — 研究综合、争议、空白与阅读路径
- `vault/40_Maps/Agent Memory 2025+ Synthesis.md` — Obsidian 内可打开的综合副本

## Stats

- 36 papers
- 47 conceptual edges
- 17 CCF-A
- 8 ICLR
- 6 ACL Findings
- 3 COLM
- 1 MLSys
- 1 ECAI

## Rebuild

```bash
python3 scripts/validate_mem.py \
  --papers data/agent-memory-2025/papers.json \
  --edges data/agent-memory-2025/edges.json

python3 scripts/build_research_map.py \
  --papers data/agent-memory-2025/papers.json \
  --edges data/agent-memory-2025/edges.json \
  --vault vault \
  --out maps/agent-memory-2025 \
  --topic 'Agent Memory 2025+'
```
