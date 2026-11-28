# AI Usage and Provenance

## Purpose

记录 AI 在检索、摘要、关系生成、地图构建和写作中的参与，避免把模型推断误当原文事实。

## Current record

| Date | Agent | Scope | Human verification | Notes |
|---|---|---|---|---|
| 2026-11-19 | Codex | 检索策略、论文元数据整理、概念地图、Obsidian 笔记、系统文档 | partial | 关键 venue 与 PDF 链接已核验；实验数字尚未逐篇复核 |
| 2026-11-27 | Codex | 52 篇论文的时间化 baseline、数据集和效果整理 | partial | 复用已完成 evidence 卡片；数字仍需逐项回 PDF/表格复核，跨论文不可直接横比 |
| 2026-11-27 | Codex | 多机部署、README/ROADMAP/STATUS、CI 与文档一致性检查 | partial | 文档与生成链路已校验；仓库状态、Zotero 与关键实验数字仍需人工确认 |
| 2026-11-27 | Codex | 硕士开题方向、写作规范、研究设计与模板 | partial | 基于 MEM evidence 与 baseline 整理；需结合学校模板、导师意见和算力做最终确认 |

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

2026-11-28　撰写并修订方向 B 开题正文，整理 52 篇更新相关证据与对照边界。详见 [研究日志](research-log/2026-11-28-direction-b-evidence-proposal.md)。

2026-11-28　围绕可追溯事实记忆更新重写开题正文，细化两项研究工作的对照与指标。详见 [研究日志](research-log/2026-11-28-direction-b-evidence-proposal.md)。

2026-11-28　调整开题正文为独立文稿，规范术语、文内引文与参考文献。详见 [研究日志](research-log/2026-11-28-direction-b-evidence-proposal.md)。

2026-11-28　精简开题背景与研究综述，复核更新时机的原始文献，重写技术路线和公开基准评测方案。详见 [研究日志](research-log/2026-11-28-direction-b-evidence-proposal.md)。
