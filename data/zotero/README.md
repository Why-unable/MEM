# Zotero Exchange

把 Zotero collection 导出为 **CSL JSON**，放在此目录，然后运行：

```bash
python3 ../../scripts/import_zotero_csl.py \
  --input <export>.json \
  --out <export>.csv
```

不要直接把导出结果写入主库；先审查标题、venue、DOI、年份和重复项。

当前主库的 Zotero 导入文件在：

- `../agent-memory-2025/agent-memory-2025.bib`
- `../agent-memory-2025/agent-memory-2025.ris`
