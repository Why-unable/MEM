# MEM Status

> 更新时间：2026-11-27
> 当前阶段：`v0.2.4 — 多机研究协作与证据运营`
> 当前研究主题：`Agent Memory 2025+`
> 当前研究分支：`research/agent-memory-evidence`
> 稳定基线分支：`main`

## 当前完成度

| 模块 | 状态 | 说明 |
|---|---|---|
| MEM 目录与原则 | 完成 | `README.md`、`SYSTEM.md`、`AGENTS.md` |
| 方案 A 工具 | 完成 | Research Nexus、Scholar Literature Maps、OpenAlex MCP 可通过 bootstrap 重建 |
| 论文数据库 | 完成 | 52 篇正式发表论文；ID / venue / 关系已校验 |
| 概念地图 | 完成 | 86 条概念关系；Canvas 与 Markdown 地图已生成 |
| Obsidian Vault | 完成 | 独立 `vault/`，Dashboard、主题页、主线页、Canvas 均可进入 |
| 逐篇证据层 | 完成 | 52/52 `evidence-checked`；0 queued；0 verified |
| 个人路线总纲 | 完成 | `个人理解/路线分类.md` 覆盖 52/52，链接直达 evidence，带机制标签 |
| 主线分析层 | 完成 | A–G 七条主线综合页 |
| 研究综合 | 完成 | `maps/agent-memory-2025/SYNTHESIS.md` 已同步 |
| 实验/baseline 登记 | 完成 | `baseline-timeline.json`、CSV、Obsidian 时间轴；数据集与 baseline 变化已整理 |
| Venue 审计 | 完成 | `VENUE_AUDIT.md` 从主库自动生成 |
| Zotero 导入文件 | 完成 | BibTeX / RIS 已生成 |
| Zotero 实际导入 | 完成 | 52 书目 + 52 importer notes；4 个 collection；0 PDF 附件 |
| 多机协作规范 | 完成 | CONTRIBUTING、multi-machine playbook、schemas、CI、数据政策 |
| 自动化质量门禁 | 完成 | `make check` 含 docs-check、timeline、venue audit、evidence index |
| 自动增量检索 | 未开始 | 计划 v0.3 |

## 当前研究状态

```text
论文：52
关系：86
CCF-A：27
Top-ICLR：12
ACL-Findings：7
Top-COLM：3
Top-MLSys：1
CCF-B：2
全文证据卡：52
verified：0
```

## 最近完成

- 完成 52/52 逐篇 evidence。
- 完成 A–G 七条主线的全文扫描与综合页。
- VikingMem 进入主库并完成 evidence、关系和 Zotero 导入。
- 更新 `个人理解/路线分类.md`：所有论文引用直达 evidence，并附 2–6 字机制标签。
- 新增 baseline 时间轴：按正式发表月份、同月效果、数据集和 baseline 变化整理。
- 新增 `docs/multi-machine-playbook.md`、`scripts/check_docs.py`、`scripts/build_venue_audit.py`。
- 将研究分支、PR、生成物和文档一致性纳入 CI。

## 下一步

1. 建立 `CLAIMS.md`，把七条主线结论转成 claim–evidence–confidence。
2. 选择 RQ1，设计统一实验协议：固定 benchmark、metric、backbone、judge、retrieval budget。
3. 对 52 张 evidence 做 `verified` 抽查，优先 VikingMem、TiMem、RecMem、MRAgent、MAGMA。
4. 回填 16 篇新增论文到 `EXPERIMENT_LANDSCAPE.md` 的正式实验矩阵。
5. 把 `papers.json` / `edges.json` 迁移为 per-paper / per-edge 分片，降低多机冲突。
6. 在 Zotero 中回填 item key，并逐步链接 PDF 附件。

## 阻塞项

- 52 张 evidence 仍是 `evidence-checked`，未完成人工 `verified` 抽查。
- Zotero 有书目但无 PDF 附件；全文目前保存在被 Git 忽略的 `data/agent-memory-2025/pdfs/`。
- `CLAIMS.md` 尚未建立。
- 单文件 JSON 在多机同时编辑时仍可能冲突。
- 部分 2026 proceedings 页面与 camera-ready 版本仍需后续复核。

## 另一台机器的最短接手路径

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
git fetch origin
git switch research/agent-memory-evidence
cat STATUS.md
cat docs/multi-machine-playbook.md
cat CONTRIBUTING.md
make check
```

部署验收：

- `make check` 通过
- `papers.json`、`baseline-timeline.json`、CSV、Obsidian 时间轴均为 52 篇
- 52 个 evidence 文件均存在且状态为 `evidence-checked` 或 `verified`
- `vault/90_System/Dashboard.md` 与 `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md` 可打开
- Zotero 条目数为 52，且未把数据库或 PDF 放入 Git
