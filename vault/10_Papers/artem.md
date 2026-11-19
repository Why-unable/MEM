---
id: "artem"
type: "paper"
title: "ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory"
year: "2026"
venue: "AAAI 2026"
venue_tier: "CCF-A"
category: "episodic"
authors:
  - "Cassandra Hui-Ming Tan"
  - "Budhitama Subagdja"
  - "Ah-Hwee Tan"
doi: "10.1609/aaai.v40i30.39773"
arxiv: null
openreview: "https://openreview.net/forum?id=fwbNOrflIy"
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39773/43734"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/episodic"
  - "tier/CCF-A"
  - "priority/supporting"
---
# ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory

> **一句话定位**：时空 episodic memory，关注事件顺序、时间依赖和长期空间经验。

## 元数据

- **Venue**：AAAI 2026（CCF-A）
- **年份**：2026
- **作者**：Cassandra Hui-Ming Tan, Budhitama Subagdja, Ah-Hwee Tan
- **PDF**：[打开 PDF](https://ojs.aaai.org/index.php/AAAI/article/download/39773/43734)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=fwbNOrflIy)

## 摘要

Current large language models (LLMs) exhibit significant deficiencies in episodic memory tasks including encoding, storing, and retrieving specific information from temporally dependent events over a long period of time. Recent approaches to handle memory tasks in LLMs, such as in-context learning, retrieval-augmented generation (RAG), and fine-tuning, may resolve the long-term retention issues, but are still inadequate to handle tasks requiring chronological awareness of the stored information. We introduce Agentic Retrieval with Temporal-Episodic Memory (ARTEM), a hybrid LLM-based agent architecture integrating LLMs with a self-organizing neural network named Spatial-Temporal Episodic Memory (STEM), designed to handle episodic memory tasks. Our approach employs LLMs for event extraction from the inputs to represent temporal, spatial, entitative, and semantic information that may facilitate future retrieval, aside from generating outputs or direct responses. The extracted events can then be encoded vectorially and stored in a fast and stable manner in the episodic memory through an instance-based incremental learning in STEM. STEM supports precise episodes retrieval and helps reduce computational overhead in generating the appropriate responses by LLMs. Evaluation on standardized episodic memory benchmarks across four tasks—partial cue retrieval, epistemic uncertainty detection, recent event identification, and chronological recall—demonstrates superior performance of ARTEM compared to in-context learning, RAG, and fine-tuning in various popular LLMs.

## 在研究地图中的位置

- **类别**：情景记忆
- **角色**：时空 episodic memory，关注事件顺序、时间依赖和长期空间经验。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/humanepisodic|Human-inspired Episodic Memory for Infinite Context LLMs]]：时空事件记忆与类人机制
- extends ← [[10_Papers/humanepisodic|Human-inspired Episodic Memory for Infinite Context LLMs]]：无限上下文 → 时空 episodic memory

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
