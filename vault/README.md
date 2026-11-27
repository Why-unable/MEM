# MEM Research Vault

这是 MEM 的独立 Obsidian Vault，当前对应 `Agent Memory 2025+` 研究案例。

## 入口

- [[90_System/Dashboard]]
- [[20_Topics/Agent Memory 2025+]]
- [[20_Topics/Mainline Overview]]
- [[10_Papers/evidence/INDEX|Per-Paper Evidence Index]]
- [[40_Maps/Agent Memory 2025+ Baseline Timeline|Baseline Timeline]]
- [[40_Maps/Agent Memory 2025+ Synthesis|Research Synthesis]]
- [[40_Maps/Agent Memory 2025+.canvas|Research Canvas]]

## 目录

```text
00_Inbox/                 未整理的论文、问题、链接
10_Papers/                生成型论文笔记
10_Papers/evidence/       逐篇 evidence 卡（人工维护）
20_Topics/                主题页与主线综合
30_Ideas/                 研究想法与问题
40_Maps/                  Canvas、研究综合、baseline 时间轴
90_System/                Dashboard、Zotero bridge、系统说明
Templates/                笔记模板
```

## 当前状态

- 52 篇正式发表论文
- 86 条概念关系
- 52/52 evidence-checked
- 52 条 baseline timeline 记录
- 0 verified

## 多机规则

- 不要提交 `.obsidian/workspace*.json`。
- 论文笔记由 `make build` 生成；人工内容只写在“可扩展笔记”区域。
- evidence 卡一篇一个文件，适合不同机器并行补写。
- baseline timeline 和 CSV 是生成物，源文件为 `data/agent-memory-2025/baseline-timeline.json`。
- 开工前运行 `make check`；部署细节见 `docs/multi-machine-playbook.md`。
