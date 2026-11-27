---
id: "persistbench"
type: "paper"
title: "PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "evaluation"
authors:
  - "Sidharth Pulipaka"
  - "Oliver Chen"
  - "Manas Sharma"
  - "Taaha Saleem Bajwa"
  - "Vyas Raina"
  - "Ivaxi Sheth"
doi: "10.48550/arXiv.2602.01146"
arxiv: "2602.01146"
openreview: "https://openreview.net/forum?id=Z7Rhzk13NT"
pdf: "https://openreview.net/pdf?id=Z7Rhzk13NT"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/CCF-A"
  - "priority/core"
---
# PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?

> **一句话定位**：评测“何时应该遗忘”，把记忆持久化边界变成显式研究对象。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Sidharth Pulipaka, Oliver Chen, Manas Sharma, Taaha Saleem Bajwa, Vyas Raina, Ivaxi Sheth
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=Z7Rhzk13NT)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=Z7Rhzk13NT)

## 摘要

Conversational assistants are increasingly integrating long-term memory with large language models (LLMs). This persistence of memories, e.g., the user is vegetarian, can enhance personalization in future conversations. However, the same persistence can also introduce safety risks that have been largely overlooked. Hence, we introduce \textbf{PersistBench} to measure the extent of these safety risks. We identify two long-term memory-specific risks: \textit{cross-domain leakage}, where LLMs inappropriately inject context from the long-term memories; and \textit{memory-induced sycophancy}, where stored long-term memories insidiously reinforce user biases. We evaluate 18 frontier and open-source LLMs on our benchmark. Our results reveal a surprisingly high failure rate across these LLMs - a median failure rate of $53\%$ on cross-domain samples and $97\%$ on sycophancy samples. To address this, our benchmark encourages the development of more robust and safer long-term memory usage in frontier conversational systems.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：评测“何时应该遗忘”，把记忆持久化边界变成显式研究对象。
- **优先级**：核心

## 关系

- evaluated-by → [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]]：记忆管理与遗忘边界
- evaluates ← [[10_Papers/tiermem|TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory]]：压缩记忆的遗忘边界
- extends ← [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：记忆保留 → 何时遗忘
- related ← [[10_Papers/memoryagentbench|Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions]]：选择性遗忘与遗忘边界评测
- related ← [[10_Papers/agemem|Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents]]：可学习 discard 动作与遗忘边界评测

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
