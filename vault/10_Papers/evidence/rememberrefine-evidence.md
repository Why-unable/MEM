---
type: evidence
paper_id: "rememberrefine"
title: "Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "E"
tags:
  - evidence
  - mainline-e
---

# Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Zouying Cao, Jiaji Deng, Li Yu, Weikang Zhou, Zhaoyang Liu, Bolin Ding, Hai Zhao
- **DOI**：10.48550/arXiv.2512.10696
- **arXiv**：2512.10696
- **PDF**：https://aclanthology.org/2026.findings-acl.829.pdf
- **正式记录**：https://openreview.net/forum?id=Aosii0xMAw
- **主库角色**：经验驱动的程序性记忆，让 agent 从历史经验中提炼可复用技能。

## 官方摘要

Procedural memory enables large language model (LLM) agents to internalize ”how-to” knowledge and thus reduce redundant trial-and-error. However, existing frameworks predominantly suffer from a ”passive accumulation” paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose ReMe (Remember Me, Refine Me), a comprehensive framework for experience-driven agent evolution. ReMe manages the memory lifecycle via three mechanisms: 1) multi-faceted distillation, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) context-adaptive reuse, which tailors historical insights to new contexts through scenario-aware indexing; and 3) utility-based refinement, which automatically adds validated memories and prunes outdated ones to maintain a compact, high-quality experience pool. Experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, indicating that self-evolving memory provides a computation-efficient path for lifelong learning.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 E 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://aclanthology.org/2026.findings-acl.829.pdf
- 正式记录：https://openreview.net/forum?id=Aosii0xMAw
