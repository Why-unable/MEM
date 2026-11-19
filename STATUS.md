# MEM Status

> 更新时间：2026-11-19
> 当前阶段：`v0.2 — 多机协作层已建立`
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
| Zotero 实际导入 | 未完成 | Zotero 当前 0 items，导入确认未完成 |
| 多机协作规范 | 完成 | `CONTRIBUTING.md`、schemas、CI、数据政策 |
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
```

## 本轮正在进行

- 建立多机 GitHub 协作层
- 增加决策记录、变更记录、研究日志
- 增加数据契约、来源规范、AI 使用记录
- 建立 CI 校验

## 下一步

1. 在 Zotero 中确认 `agent-memory-2025.bib` 导入。
2. 从 `RESEARCH_QUESTIONS.md` 选择 RQ1 或 RQ3。
3. 精读 5–8 篇核心论文并补证据表。
4. 将论文库从单文件 JSON 迁移为 per-paper YAML，降低多机冲突。

## 阻塞项

- Zotero 导入尚未确认。
- 还没有为每篇论文补齐“关键方法 / 实验数字 / 局限 / 可复用点”。

## 另一台机器的最短接手路径

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
cat STATUS.md
cat CONTRIBUTING.md
cat docs/machine-setup.md
make check
```
