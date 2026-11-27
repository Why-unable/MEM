# Agent Memory 2025+ Map

## Outputs

- `research-map.md` — Mermaid 全景图 + 论文清单 + 关系边
- `research-map.json` — 机器可读节点/边
- `research-map.canvas` — Obsidian Canvas 副本
- `papers.csv` — 表格视图
- `SYNTHESIS.md` — 研究综合、争议、空白与阅读路径
- `EXPERIMENT_LANDSCAPE.md` — 数据集、任务与 baseline 家族全景
- `vault/40_Maps/Agent Memory 2025+ Synthesis.md` — Obsidian 内综合副本
- `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md` — 时间化效果、数据集与 baseline 变化

## Stats

- 52 papers
- 86 conceptual edges
- 27 CCF-A
- 12 Top-ICLR
- 7 ACL Findings
- 3 Top-COLM
- 1 Top-MLSys
- 2 CCF-B

## Rebuild

```bash
make check
```

Or run the pieces separately:

```bash
make validate
make build
make export
make evidence-index
make baseline-timeline
make venue-audit
make docs-check
```

Direct map rebuild:

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

## Notes

- 关系边是概念关系，不等于逐条引文边。
- 生成文件不要手工编辑；先改 `papers.json` / `edges.json`，再运行 `make check`。
- `EXPERIMENT_LANDSCAPE.md` 的实验矩阵仍需持续回填；baseline timeline 已覆盖 52 篇的精选主结果。
