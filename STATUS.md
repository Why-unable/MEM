# MEM Status

> 更新时间：2026-11-27
> 当前阶段：`v0.2.1 — 主线 A 证据层已启动`
> 当前研究主题：`Agent Memory 2025+`

## 当前完成度

| 模块 | 状态 | 说明 |
|---|---|---|
| MEM 目录与原则 | 完成 | `README.md`、`SYSTEM.md`、`AGENTS.md` |
| 方案 A 工具 | 完成 | Research Nexus、Scholar Literature Maps、OpenAlex MCP 已克隆到 `.tools/` |
| 论文数据库 | 完成 | 51 篇正式发表论文；2026-11-27 分两批增补 15 篇 |
| 概念地图 | 完成 | 81 条概念关系 |
| Obsidian Vault | 完成 | 已注册并打开 `$MEM_ROOT/vault` |
| Obsidian Canvas | 完成 | `vault/40_Maps/Agent Memory 2025+.canvas` |
| 研究综合 | 完成 | `maps/agent-memory-2025/SYNTHESIS.md` |
| Zotero 导入文件 | 完成 | BibTeX / RIS 已生成 |
| Zotero 实际导入 | 完成 | 51 篇书目 + 51 条 importer notes；3 个 collection；无 PDF 附件 |
| 多机协作规范 | 完成 | `CONTRIBUTING.md`、schemas、CI、数据政策 |
| 主线分析层 | 完成 | 七条主线综合页；50/51 全文扫描（ReasoningBank 用摘要/实验地图） |
| 逐篇证据层 | 进行中 | 51 个 evidence 入口；18 张 evidence-checked；33 个 queued |
| 自动增量检索 | 未开始 | 计划 v0.3 |
| 实验/数据集登记 | 未开始 | 进入实验阶段后再建 |

## 当前研究状态

```text
论文：51
关系：81
CCF-A：26
Top-ICLR：12
ACL Findings：7
Top-COLM：3
Top-MLSys：1
CCF-B：2
全文证据卡：6
```

## 本轮正在进行

- 完成 A–G 七条主线的全文扫描与综合
- 建立 `vault/20_Topics/Mainline Overview.md` 总入口
- 为 AgeMem 建立页码级证据卡
- 校准正式 DOI、Zotero 与主库计数

## 下一步

1. 选择 RQ1 作为当前主研究问题。
2. 把 B–G 的核心论文各补 1–2 张页码级证据卡。
3. 用正式 camera-ready 复核 A-Mem / G-Memory。
4. 把主线 A 综合整理为 `CLAIMS.md` 的 claim-evidence 表。
5. 设计 RQ1 最小实验：full context / RAG / A-Mem-like / MAGMA-like / MRAgent-like。
6. 在第二台机器开始写入前，把 `papers.json` / `edges.json` 迁移为 per-paper 文件。

## 阻塞项

- A-Mem、G-Memory 的正式 NeurIPS 2025 camera-ready 尚未复核。
- Zotero 有书目但无 PDF 附件；全文目前保存在被 Git 忽略的 `data/agent-memory-2025/pdfs/`。
- `CLAIMS.md` 尚未建立。
- 新增 15 篇大多未补全文证据卡。
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
