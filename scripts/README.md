# Scripts

| 脚本 | 用途 |
|---|---|
| `bootstrap_scheme_a.sh` | 克隆 Research Nexus、Scholar Literature Maps、OpenAlex MCP 到 `.tools/` |
| `validate_mem.py` | 检查论文与边数据的必填字段、重复 ID、未知节点 |
| `build_research_map.py` | 生成 Obsidian 论文笔记、主题页、Canvas、research-map.md/json/csv |
| `export_zotero_formats.py` | 从 papers.json 生成 BibTeX / RIS |
| `import_zotero_csl.py` | 把 Zotero CSL JSON 转成人工审查 CSV |

## Typical sequence

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
```
