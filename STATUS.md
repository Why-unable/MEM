# MEM Status

> 更新时间：2026-11-26
> 当前阶段：`v0.2.1 — 主线 A 证据层已启动`
> 当前研究主题：`Agent Memory 2025+`

## 当前完成度

| 模块 | 状态 | 说明 |
|---|---|---|
| MEM 目录与原则 | 完成 | `README.md`、`SYSTEM.md`、`AGENTS.md` |
| 方案 A 工具 | 完成 | Research Nexus、Scholar Literature Maps、OpenAlex MCP 已克隆到 `.tools/` |
| 论文数据库 | 完成 | 36 篇正式发表论文 |
| 概念地图 | 完成 | 47 条概念关系 |
| Obsidian Vault | 完成 | 已注册并打开 `$MEM_ROOT/vault` |
| Obsidian Canvas | 完成 | `vault/40_Maps/Agent Memory 2025+.canvas` |
| 研究综合 | 完成 | `maps/agent-memory-2025/SYNTHESIS.md` |
| Zotero 导入文件 | 完成 | BibTeX / RIS 已生成 |
| Zotero 实际导入 | 完成 | 36 条书目 + 36 条 importer notes；collection `agent-memory-2025`；无 PDF 附件 |
| 多机协作规范 | 完成 | `CONTRIBUTING.md`、schemas、CI、数据政策 |
| 主线 A 证据层 | 进行中 | 5 篇全文证据卡 + 比较矩阵 v0；其余论文尚未精读 |
| 自动增量检索 | 未开始 | 计划 v0.3 |
| 实验/数据集登记 | 未开始 | 进入实验阶段后再建 |

## 当前研究状态

```text
论文：36
关系：47
CCF-A：17
Top-ICLR：8
ACL Findings：6
Top-COLM：3
Top-MLSys：1
CCF-B：1
全文证据卡：5
```

## 本轮正在进行

- 主线 A：A-Mem、G-Memory、MAGMA、MemGAS、MRAgent 全文精读
- 建立 `vault/10_Papers/evidence/` 证据卡层
- 把主线 A 的发现重写为 RQ1 的可检验假设
- 校准正式 DOI 与 Zotero 实际状态

## 下一步

1. 选择 RQ1 作为当前主研究问题。
2. 用正式 camera-ready 复核 A-Mem / G-Memory。
3. 把主线 A 综合整理为 `CLAIMS.md` 的 claim-evidence 表。
4. 设计 RQ1 最小实验：full context / RAG / A-Mem-like / MAGMA-like / MRAgent-like。
5. 在第二台机器开始写入前，把 `papers.json` / `edges.json` 迁移为 per-paper 文件。

## 阻塞项

- A-Mem、G-Memory 的正式 NeurIPS 2025 camera-ready 尚未复核。
- Zotero 有书目但无 PDF 附件；全文目前保存在被 Git 忽略的 `data/agent-memory-2025/pdfs/`。
- `CLAIMS.md` 尚未建立。
- 单文件 JSON 在多机同时编辑时仍可能冲突。

## 另一台机器的最短接手路径

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
cat STATUS.md
cat CONTRIBUTING.md
cat docs/machine-setup.md
make check
```
