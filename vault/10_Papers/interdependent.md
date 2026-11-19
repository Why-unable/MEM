---
id: "interdependent"
type: "paper"
title: "Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "evaluation"
authors:
  - "Zexue He"
  - "Yu Wang"
  - "Churan Zhi"
  - "Yuanzhe Hu"
  - "Tzu-Ping Chen"
  - "Lang Yin"
  - "Ze Chen"
  - "Tong Arthur Wu"
  - "Siru Ouyang"
  - "Zihan Wang"
  - "Jiaxin Pei"
  - "Julian McAuley"
  - "Yejin Choi"
  - "Alex Pentland"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=JHYmxqS9Jv"
pdf: "https://openreview.net/pdf?id=JHYmxqS9Jv"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/CCF-A"
  - "priority/core"
---
# Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks

> **一句话定位**：多 session 相互依赖任务中的 agent memory 基准，贴近真实长期任务。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Zexue He, Yu Wang, Churan Zhi, Yuanzhe Hu, Tzu-Ping Chen, Lang Yin, Ze Chen, Tong Arthur Wu, Siru Ouyang, Zihan Wang, Jiaxin Pei, Julian McAuley, Yejin Choi, Alex Pentland
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=JHYmxqS9Jv)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=JHYmxqS9Jv)

## 摘要

Existing evaluations of agents with memory typically assess **memorization** and **action** in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment, and subsequently rely on that memory to solve future tasks. To capture this setting, we introduce MemoryArena, a unified evaluation gym for benchmarking agent memory in multi-session Memory-Agent-Environment loops. The benchmark consists of human-crafted agentic tasks with explicitly interdependent subtasks, where agents must learn from earlier actions and feedback by distilling experiences into memory, and subsequently use that memory to guide later actions to solve the overall task. MEMORYARENA supports evaluation across web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning, and reveals that agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting, exposing a gap in current evaluations for agents with memory.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：多 session 相互依赖任务中的 agent memory 基准，贴近真实长期任务。
- **优先级**：核心

## 关系

- extends ← [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：单会话评测 → 多 session 任务
- related ← [[10_Papers/beyondmillion|Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs]]：规模压力 vs 任务依赖

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
