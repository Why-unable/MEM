# Zotero × Obsidian 接入说明


## 本机检测结果（2026-11-19）

- Obsidian 已安装。
- 检测到多个既有 vault，包括 `$HOME/Documents/Obsidian Vault`。
- MEM 已固定使用独立 vault：`$MEM_ROOT/vault`。
- 该 vault 已注册到 Obsidian，Dashboard 已打开。
- Zotero 已安装，数据目录为 `$HOME/Zotero`。
- 当前 Zotero 库检测到 **0 items / 0 collections**，本地 API 未启用。
- 因此当前最优路径是：先把 `agent-memory-2025.bib` 导入 Zotero，再决定是否迁移到既有 vault。

## 当前状态

MEM 已经生成了可直接导入 Zotero 的文件：

- `data/agent-memory-2025/agent-memory-2025.bib`
- `data/agent-memory-2025/agent-memory-2025.ris`
- `data/agent-memory-2025/papers.csv`

## 推荐做法

### 1. 在 Zotero 中建立 collection

建议命名：

```text
MEM / Agent Memory 2025+
```

### 2. 导入 BibTeX 或 RIS

Zotero → File → Import → 选择：

```text
MEM/data/agent-memory-2025/agent-memory-2025.bib
```

或：

```text
MEM/data/agent-memory-2025/agent-memory-2025.ris
```

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
- 如果 Zotero 条目与正式 proceedings 冲突，以官方页面为准。
