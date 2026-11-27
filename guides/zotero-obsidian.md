# Zotero × Obsidian 接入说明


## 本机检测结果（2026-11-27）

- Obsidian 已安装。
- 检测到多个既有 vault，包括 `$HOME/Documents/Obsidian Vault`。
- MEM 已固定使用独立 vault：`$MEM_ROOT/vault`。
- 该 vault 已注册到 Obsidian，Dashboard 已打开。
- Zotero 已安装，数据目录为 `$HOME/Zotero`。
- 当前 Zotero 库已导入 **52 条书目 + 52 条 importer notes**，分 4 个 collection。
- PDF 附件为 **0**；本地 API 未启用。
- 实际导入状态以 `data/zotero/IMPORT_STATUS.md` 为准。

## 当前状态

MEM 已经生成主库与增量导入文件：

- `data/agent-memory-2025/agent-memory-2025.bib`
- `data/agent-memory-2025/agent-memory-2025.ris`
- `data/agent-memory-2025/agent-memory-2025-batch2.bib`
- `data/agent-memory-2025/agent-memory-2025-batch3.bib`
- `data/agent-memory-2025/agent-memory-2025-batch4.bib`
- `data/agent-memory-2025/papers.csv`

## 推荐做法

### 1. 在 Zotero 中建立 collection

建议最终命名：

```text
MEM / Agent Memory 2025+
```

当前实际使用的是 `agent-memory-2025` 主 collection 和三个 staging batch。

### 2. 导入 BibTeX 或 RIS

Zotero → File → Import。

新机器恢复时：

1. 先导入初始 `agent-memory-2025.bib` / `.ris`。
2. 再只导入缺失的 batch2 / batch3 / batch4 文件。
3. 不要重复导入完整主库，避免 duplicate items。
4. 导入后核对 52 条书目。

### 3. 下载/关联 PDF

优先把官方 PDF 放入 Zotero 附件。论文笔记中的 `PDF` 链接可以作为回退。

### 4. 从 Zotero 导出 CSL JSON

Zotero collection → 右键 → Export Collection → Format: CSL JSON。

把文件放到：

```text
MEM/data/zotero/
```

### 5. 运行导入脚本

```bash
python3 scripts/import_zotero_csl.py \
  --input data/zotero/<export>.json \
  --out data/zotero/<export>.csv
```

脚本只做中间转换，不会自动覆盖 `papers.json`。这是有意的：论文库应该经过人工确认。

## 未来可接入

- Zotero 本地 API：`http://127.0.0.1:23119/api/users/0`
- Zotero Better BibTeX citation key
- PDF 全文抽取
- Obsidian 中的 Zotero item key 双向链接

## 注意事项

- Zotero 是书目事实源；MEM 是研究理解和关系层。
- 不要把 Zotero 的自动抓取元数据直接当作已核验的 venue 信息。
- 不要把 `zotero.sqlite`、`storage/` 或第三方 PDF 提交到 Git。
- Zotero collection 尚未合并，item key 尚未回填。
- 如果 Zotero 条目与正式 proceedings 冲突，以官方页面为准。
