# Scripts

## Core

| 脚本 | 用途 | 生成物 |
|---|---|---|
| `bootstrap_scheme_a.sh` | 克隆 Research Nexus、Scholar Literature Maps、OpenAlex MCP 到 `.tools/` | `.tools/*`（ignored） |
| `validate_mem.py` | 检查论文与边数据的必填字段、重复 ID、未知节点 | — |
| `build_research_map.py` | 生成 Obsidian 论文笔记、主题页、Canvas、research-map.md/json/csv | `vault/10_Papers/*.md`、`maps/<topic>/*` |
| `export_zotero_formats.py` | 从 `papers.json` 生成 BibTeX / RIS | `agent-memory-2025.bib/.ris` |
| `import_zotero_csl.py` | 把 Zotero CSL JSON 转成人工审查 CSV | 指定 CSV |
| `build_evidence_index.py` | 建立逐篇 evidence 索引 | `vault/10_Papers/evidence/INDEX.md` |
| `build_baseline_timeline.py` | 从 curated JSON 生成时间化 baseline CSV + Obsidian 笔记 | `baseline-timeline.csv`、`vault/40_Maps/... Baseline Timeline.md` |
| `build_venue_audit.py` | 从 `papers.json` 生成 venue 分层审计 | `data/<topic>/VENUE_AUDIT.md` |
| `check_docs.py` | 检查 README / STATUS / ROADMAP / Dashboard / evidence / timeline / venue audit 是否一致 | — |

## Recommended

```bash
make check
```

`make check` runs:

```text
schemas
validate
build
export
evidence-index
baseline-timeline
venue-audit
docs-check
git diff --check
```

## Typical Sequence

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

python3 scripts/export_zotero_formats.py \
  --papers data/agent-memory-2025/papers.json \
  --out-dir data/agent-memory-2025 \
  --stem agent-memory-2025

python3 scripts/build_evidence_index.py
python3 scripts/build_baseline_timeline.py
python3 scripts/build_venue_audit.py
python3 scripts/check_docs.py
```

## Rules

- Do not edit generated outputs by hand.
- If a generator changes, update its tests/checks and `CHANGELOG.md`.
- Multi-machine conflict rules are in `docs/multi-machine-playbook.md`.
