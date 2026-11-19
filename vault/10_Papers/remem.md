---
id: "remem"
type: "paper"
title: "REMem: Reasoning with Episodic Memory in Language Agent"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "episodic"
authors:
  - "Yiheng Shu"
  - "Saisri Padmaja Jonnalagedda"
  - "Xiang Gao"
  - "Bernal Jiménez Gutiérrez"
  - "Weijian Qi"
  - "Kamalika Das"
  - "Huan Sun"
  - "Yu Su"
doi: "10.48550/arXiv.2602.13530"
arxiv: "2602.13530"
openreview: "https://openreview.net/forum?id=fugnQxbvMm"
pdf: "https://openreview.net/pdf?id=fugnQxbvMm"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/episodic"
  - "tier/Top-ICLR"
  - "priority/core"
---
# REMem: Reasoning with Episodic Memory in Language Agent

> **一句话定位**：把 episodic memory 与推理过程结合，强调事件级经验的复用。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Yiheng Shu, Saisri Padmaja Jonnalagedda, Xiang Gao, Bernal Jiménez Gutiérrez, Weijian Qi, Kamalika Das, Huan Sun, Yu Su
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=fugnQxbvMm)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=fugnQxbvMm)

## 摘要

Humans excel at remembering concrete experiences along spatiotemporal contexts and performing reasoning across those events, i.e., the capacity for episodic memory. In contrast, memory in language agents remains mainly semantic, and current agents are not yet capable of effectively recollecting and reasoning over interaction histories. We identify and formalize the core challenges of episodic recollection and reasoning from this gap, and observe that existing work often overlooks episodicity, lacks explicit event modeling, or overemphasizes simple retrieval rather than complex reasoning. We present REMem, a two-phase framework for constructing and reasoning with episodic memory: 1) Offline indexing, where REMem converts experiences into a hybrid memory graph that flexibly links time-aware gists and facts. 2) Online inference, where REMem employs an agentic retriever with carefully curated tools for iterative retrieval over the memory graph. Comprehensive evaluation across four episodic memory benchmarks shows that REMem substantially outperforms state-of-the-art memory systems such as Mem0 and HippoRAG 2, showing 3.4% and 13.4% absolute improvements on episodic recollection and reasoning tasks, respectively. Moreover, REMem also demonstrates more robust refusal behavior for unanswerable questions.

## 在研究地图中的位置

- **类别**：情景记忆
- **角色**：把 episodic memory 与推理过程结合，强调事件级经验的复用。
- **优先级**：核心

## 关系

- extends → [[10_Papers/ema|EMA: An Episodic Memory Agent for Efficient and Selective Memory]]：事件级记忆 → 选择性 episodic unit
- extends → [[10_Papers/multimodal|Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory]]：文本事件 → 多模态经验
- extends ← [[10_Papers/humanepisodic|Human-inspired Episodic Memory for Infinite Context LLMs]]：类人 episodic memory → 推理中的事件记忆

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
