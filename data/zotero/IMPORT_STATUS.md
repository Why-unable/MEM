# Zotero Import Status

- Date: 2026-11-27
- Zotero installed: yes
- Zotero data dir: `$HOME/Zotero`
- Local API: not enabled
- Library at last read-only check: **52 bibliographic items + 52 importer notes**
- PDF attachments: **0**
- Collections:
  - `agent-memory-2025`：36 篇（原始主库）
  - `agent-memory-2025-batch2`：8 篇（2026-11-27 Batch 1）
  - `agent-memory-2025-batch3`：7 篇（2026-11-27 Batch 2）
  - `agent-memory-2025-batch4`：1 篇（VikingMem）
- Import files:
  - `$MEM_ROOT/data/agent-memory-2025/agent-memory-2025.bib`（初始 36 篇）
  - `$MEM_ROOT/data/agent-memory-2025/agent-memory-2025-batch2.bib`
  - `$MEM_ROOT/data/agent-memory-2025/agent-memory-2025-batch3.bib`
  - `$MEM_ROOT/data/agent-memory-2025/agent-memory-2025-batch4.bib`
- Zotero import confirmed: **yes**
- No direct writes to `zotero.sqlite` were performed.

## Notes

- 注意：Zotero 运行时，最新变更可能还在 `zotero.sqlite-wal`；只复制主数据库会看到旧状态。
- 本次通过 Zotero 的 File → Import 导入 Batch 2 / Batch 3 / Batch 4，每个批次创建一个 staging collection。
- 目前没有把四个 collection 合并；条目本身已经全部存在于 My Library。
- 后续可以在 Zotero 中把 batch2 / batch3 / batch4 的条目拖入 `agent-memory-2025`，再删除 staging collection；删除 collection 不会删除条目。

## Recommended collection

```text
MEM / Agent Memory 2025+
```

当前实际使用：

```text
agent-memory-2025
agent-memory-2025-batch2
agent-memory-2025-batch3
agent-memory-2025-batch4
```
