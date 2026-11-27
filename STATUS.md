# MEM Status

> 更新时间：2026-11-27
> 当前阶段：`v0.2.2 — 51 篇逐篇证据层完成`
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
| 逐篇证据层 | 完成 | 51/51 evidence-checked；0 queued；0 verified（尚未人工复核） |
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
全文证据卡：51
```

## 本轮正在进行

- 完成 51/51 的逐篇 evidence 文件
- A–G 七条主线均有综合页
- 所有 evidence 文件至少完成 method / results / limitations / RQ 映射
- 校准正式 DOI、Zotero 与主库计数

## 下一步

1. 建立 `CLAIMS.md`，把七条主线结论转成 claim–evidence–confidence。
2. 选择 RQ1 并设计统一实验协议。
3. 对 51 张 evidence 做 `verified` 抽查（页码、数字、引用）。
4. 回填 15 篇新增论文的 `EXPERIMENT_LANDSCAPE.md` 矩阵。
5. 在第二台机器开始写入前，把 `papers.json` / `edges.json` 迁移为 per-paper 文件。

## 阻塞项

- A-Mem、G-Memory 的正式 NeurIPS 2025 camera-ready 尚未复核。
- Zotero 有书目但无 PDF 附件；全文目前保存在被 Git 忽略的 `data/agent-memory-2025/pdfs/`。
- `CLAIMS.md` 尚未建立。
- 51 张 evidence 尚未做 `verified` 人工抽查。
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
