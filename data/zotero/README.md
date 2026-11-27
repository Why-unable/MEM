# Zotero Exchange

MEM 采用 **export-first** 流程：从 `papers.json` 生成 BibTeX / RIS，再通过 Zotero 的 File → Import 导入；不直接修改 `zotero.sqlite`。

## 当前状态

- Zotero: 52 bibliographic items + 52 importer notes
- PDF attachments: 0
- Collections:
  - `agent-memory-2025`：36 篇（初始主库）
  - `agent-memory-2025-batch2`：8 篇
  - `agent-memory-2025-batch3`：7 篇
  - `agent-memory-2025-batch4`：1 篇（VikingMem）
- 详细状态：`IMPORT_STATUS.md`

## 导入文件

主库与增量文件位于 `../agent-memory-2025/`：

- `agent-memory-2025.bib` / `.ris`
- `agent-memory-2025-batch2.bib` / `.ris`
- `agent-memory-2025-batch3.bib` / `.ris`
- `agent-memory-2025-batch4.bib` / `.ris`

## 新机器恢复

1. 先读 `IMPORT_STATUS.md`，不要盲目重复导入。
2. 打开 Zotero，确认/创建 `agent-memory-2025`。
3. 导入初始主库文件。
4. 只导入缺失的增量 batch。
5. 核对 52 条书目。
6. 后续再把 batch collection 合并到主 collection，并回填 item key。

## CSL JSON 交换

```bash
python3 ../../scripts/import_zotero_csl.py \
  --input <export>.json \
  --out <export>.csv
```

不要直接把导出结果写入主库；先审查标题、venue、DOI、年份和重复项。

## 禁止提交

- `zotero.sqlite`
- `fulltext.sqlite`
- `storage/`
- 第三方 PDF
- 私有导出、API key、cookie
