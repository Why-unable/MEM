---
type: system
updated: 2026-11-19
tags:
  - zotero
  - system
---

# Zotero Bridge

## 当前可用导入文件

- `MEM/data/agent-memory-2025/agent-memory-2025.bib`
- `MEM/data/agent-memory-2025/agent-memory-2025.ris`

推荐在 Zotero 中建立 collection：

```text
MEM / Agent Memory 2025+
```

## 导入后

1. 在论文笔记的“与 Zotero 条目”处填写 citation key 或 item key。
2. 把 Zotero collection 导出为 CSL JSON。
3. 放到 `MEM/data/zotero/`。
4. 运行：

```bash
python3 scripts/import_zotero_csl.py \
  --input data/zotero/<export>.json \
  --out data/zotero/<export>.csv
```

## 原则

- Zotero 是书目和附件事实源。
- MEM 是理解、关系和研究问题层。
- 不用 Zotero 自动元数据替代正式 venue 核验。
