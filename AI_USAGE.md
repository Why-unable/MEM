# AI Usage and Provenance

## Purpose

记录 AI 在检索、摘要、关系生成、地图构建和写作中的参与，避免把模型推断误当原文事实。

## Current record

| Date | Agent | Scope | Human verification | Notes |
|---|---|---|---|---|
| 2026-11-19 | Codex | 检索策略、论文元数据整理、概念地图、Obsidian 笔记、系统文档 | partial | 关键 venue 与 PDF 链接已核验；实验数字尚未逐篇复核 |
| 2026-11-27 | Codex | 52 篇论文的时间化 baseline、数据集和效果整理 | partial | 复用已完成 evidence 卡片；数字仍需逐项回 PDF/表格复核，跨论文不可直接横比 |
| 2026-11-27 | Codex | 多机部署、README/ROADMAP/STATUS、CI 与文档一致性检查 | partial | 文档与生成链路已校验；仓库状态、Zotero 与关键实验数字仍需人工确认 |

## Tools used

- OpenReview API
- Semantic Scholar `paper/search/match`
- ACL Anthology official PDFs
- AAAI OJS
- Crossref / OpenAlex (supplementary; rate-limited)

## Rules

1. 模型不能作为 DOI、venue、作者、引用的唯一来源。
2. 模型总结必须与官方 PDF/摘要核对。
3. 论文笔记中的“模型推断”应标明。
4. 地图关系边默认是概念关系，不是引文事实。
5. 生成后必须运行 `make check`。

## What AI did not verify

- 每篇论文的完整实验设置
- 数据集与指标细节
- 所有数字与表格
- 所有引用上下文

## Future records

每次大规模 AI 辅助研究需要新增一行，并链接研究日志。
