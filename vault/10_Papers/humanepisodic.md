---
id: "humanepisodic"
type: "paper"
title: "Human-inspired Episodic Memory for Infinite Context LLMs"
year: "2025"
venue: "ICLR 2025"
venue_tier: "Top-ICLR"
category: "episodic"
authors:
  - "Zafeirios Fountas"
  - "Martin Benfeghoul"
  - "Adnan Oomerjee"
  - "Fenia Christopoulou"
  - "Gerasimos Lampouras"
  - "Haitham Bou Ammar"
  - "Jun Wang"
doi: null
arxiv: "2407.09450"
openreview: "https://openreview.net/forum?id=BI2int5SAC"
pdf: "https://openreview.net/pdf?id=BI2int5SAC"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/episodic"
  - "tier/Top-ICLR"
  - "priority/core"
---
# Human-inspired Episodic Memory for Infinite Context LLMs

> **一句话定位**：用类人 episodic memory 扩展无限上下文，是 2025 年记忆架构的重要基础工作。

## 元数据

- **Venue**：ICLR 2025（Top-ICLR）
- **年份**：2025
- **作者**：Zafeirios Fountas, Martin Benfeghoul, Adnan Oomerjee, Fenia Christopoulou, Gerasimos Lampouras, Haitham Bou Ammar, Jun Wang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=BI2int5SAC)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=BI2int5SAC)

## 摘要

Large language models (LLMs) have shown remarkable capabilities, but still struggle with processing extensive contexts, limiting their ability to maintain coherence and accuracy over long sequences. In contrast, the human brain excels at organising and retrieving episodic experiences across vast temporal scales, spanning a lifetime. In this work, we introduce EM-LLM, a novel approach that integrates key aspects of human episodic memory and event cognition into LLMs with no fine-tuning, enabling them to handle practically infinite context lengths while maintaining computational efficiency. EM-LLM organises sequences of tokens into coherent episodic events using a combination of Bayesian surprise and graph-theoretic boundary refinement in an online fashion. When needed, these events are retrieved through a two-stage memory process, combining similarity-based and temporally contiguous retrieval for efficient, human-inspired access to relevant information. Experiments on the LongBench and $\infty$-Bench benchmarks demonstrate EM-LLM's superior performance, consistently outperforming the state-of-the-art retrieval model InfLLM across various baseline LLMs. In addition, EM-LLM outperforms its popular counterpart, RAG, in a wide range of tasks, while requiring similar resources. Notably, EM-LLM's performance even surpasses full-context models in most tasks, while successfully performing retrieval across 10 million tokens -- a scale computationally infeasible for such models. Finally, our analysis reveals strong correlations between EM-LLM's event segmentation and human-perceived events, suggesting parallels between this artificial system and its biological counterpart, thereby offering a novel computational framework for exploring human memory mechanisms.

## 在研究地图中的位置

- **类别**：情景记忆
- **角色**：用类人 episodic memory 扩展无限上下文，是 2025 年记忆架构的重要基础工作。
- **优先级**：核心

## 关系

- extends → [[10_Papers/remem|REMem: Reasoning with Episodic Memory in Language Agent]]：类人 episodic memory → 推理中的事件记忆
- extends → [[10_Papers/artem|ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory]]：无限上下文 → 时空 episodic memory
- related ← [[10_Papers/artem|ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory]]：时空事件记忆与类人机制

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
