---
id: "rememberrefine"
type: "paper"
title: "Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution"
year: "2026"
venue: "ACL Findings 2026"
venue_tier: "ACL-Findings"
category: "procedural"
authors:
  - "Zouying Cao"
  - "Jiaji Deng"
  - "Li Yu"
  - "Weikang Zhou"
  - "Zhaoyang Liu"
  - "Bolin Ding"
  - "Hai Zhao"
doi: "10.48550/arXiv.2512.10696"
arxiv: "2512.10696"
openreview: "https://openreview.net/forum?id=Aosii0xMAw"
pdf: "https://aclanthology.org/2026.findings-acl.829.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/procedural"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution

> **一句话定位**：经验驱动的程序性记忆，让 agent 从历史经验中提炼可复用技能。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Zouying Cao, Jiaji Deng, Li Yu, Weikang Zhou, Zhaoyang Liu, Bolin Ding, Hai Zhao
- **PDF**：[打开 PDF](https://aclanthology.org/2026.findings-acl.829.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=Aosii0xMAw)

## 摘要

Procedural memory enables large language model (LLM) agents to internalize ”how-to” knowledge and thus reduce redundant trial-and-error. However, existing frameworks predominantly suffer from a ”passive accumulation” paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose ReMe (Remember Me, Refine Me), a comprehensive framework for experience-driven agent evolution. ReMe manages the memory lifecycle via three mechanisms: 1) multi-faceted distillation, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) context-adaptive reuse, which tailors historical insights to new contexts through scenario-aware indexing; and 3) utility-based refinement, which automatically adds validated memories and prunes outdated ones to maintain a compact, high-quality experience pool. Experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, indicating that self-evolving memory provides a computation-efficient path for lifelong learning.

## 在研究地图中的位置

- **类别**：程序性记忆
- **角色**：经验驱动的程序性记忆，让 agent 从历史经验中提炼可复用技能。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]]：程序性记忆 vs 元进化
- related ← [[10_Papers/reasoningbank|ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory]]：程序性记忆与经验蒸馏

## 我的阅读问题

1. 它把记忆的哪个环节作为核心：写入、组织、检索、整合、遗忘，还是评测？
2. 它和 [[20_Topics/Agent Memory 2025+]] 中的哪条研究线索最接近？
3. 它的实验能否迁移到我的研究问题？需要哪些数据或基线？

## 可扩展笔记

- 关键方法：
- 关键实验：
- 局限：
- 可复用点：
- 与 Zotero 条目：
