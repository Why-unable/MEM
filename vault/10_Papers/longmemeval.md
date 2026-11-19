---
id: "longmemeval"
type: "paper"
title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
year: "2025"
venue: "ICLR 2025"
venue_tier: "Top-ICLR"
category: "evaluation"
authors:
  - "Di Wu"
  - "Hongwei Wang"
  - "Wenhao Yu"
  - "Yuwei Zhang"
  - "Kai-Wei Chang"
  - "Dong Yu"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=pZiyCaVuti"
pdf: "https://openreview.net/pdf?id=pZiyCaVuti"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/Top-ICLR"
  - "priority/core"
---
# LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

> **一句话定位**：长期交互记忆基准，已成为记忆系统评测的重要参照。

## 元数据

- **Venue**：ICLR 2025（Top-ICLR）
- **年份**：2025
- **作者**：Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=pZiyCaVuti)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=pZiyCaVuti)

## 摘要

Recent large language model (LLM)-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses. However, their long-term memory capabilities in sustained interactions remain underexplored. We introduce LongMemEval, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, LongMemEval presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions. We then present a unified framework that breaks down the long-term memory design into three stages: indexing, retrieval, and reading. Built upon key experimental insights, we propose several memory design optimizations including session decomposition for value granularity, fact-augmented key expansion for indexing, and time-aware query expansion for refining the search scope. Extensive experiments show that these optimizations greatly improve both memory recall and downstream question answering on LongMemEval. Overall, our study provides valuable resources and guidance for advancing the long-term memory capabilities of LLM-based chat assistants, paving the way toward more personalized and reliable conversational AI. Our benchmark and code are publicly available at https://github.com/xiaowu0162/LongMemEval.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：长期交互记忆基准，已成为记忆系统评测的重要参照。
- **优先级**：核心

## 关系

- related → [[10_Papers/membench|MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents]]：长期交互 → 综合记忆评测
- extends → [[10_Papers/beyondmillion|Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs]]：长期交互 → 百万 token 压力测试
- extends → [[10_Papers/interdependent|Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks]]：单会话评测 → 多 session 任务
- extends → [[10_Papers/persistbench|PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?]]：记忆保留 → 何时遗忘
- evaluated-by → [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：A-Mem 类系统的长期记忆评测参照
- related ← [[10_Papers/evoking|Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval]]：个性化检索 → 长期交互评测

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
