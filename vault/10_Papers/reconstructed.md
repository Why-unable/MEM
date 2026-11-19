---
id: "reconstructed"
type: "paper"
title: "Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Shuo Ji"
  - "Yibo Li"
  - "Bryan Hooi"
doi: "10.48550/arXiv.2606.06036"
arxiv: "2606.06036"
openreview: "https://openreview.net/forum?id=xRVWftS3ES"
pdf: "https://openreview.net/pdf?id=xRVWftS3ES"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/core"
---
# Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents

> **一句话定位**：把记忆视为“重构”而不是“检索”，用图结构动态重建上下文。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Shuo Ji, Yibo Li, Bryan Hooi
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=xRVWftS3ES)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=xRVWftS3ES)

## 摘要

Despite recent progress, LLM agents still struggle with reasoning over long interaction histories. While current memory-augmented agents rely on a static ``retrieve-then-reason'' paradigm, this rigid pipeline design prevents them from dynamically adapting memory access to intermediate evidence discovered during inference. To bridge this gap, we propose MRAgent, a framework that combines an associative memory graph with an active reconstruction mechanism. We represent memory as a Cue–Tag–Content graph, where associative tags serve as semantic bridges connecting fine-grained cues to memory contents. Operating on this structure, our active reconstruction mechanism integrates LLM reasoning directly into memory access, allowing the agent to iteratively explore and prune retrieval paths based on accumulated evidence. This ensures that memory retrieval is dynamically adapted to the  reasoning context while avoiding combinatorial explosion caused by unconstrained expansion. Experiments on the LoCoMo benchmark  and LongMemEval benchmark  demonstrate significant improvements over strong baselines (up to $23\\%$), while substantially reducing retrieval cost, highlighting the effectiveness of active and associative reconstruction for long-horizon memory reasoning.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：把记忆视为“重构”而不是“检索”，用图结构动态重建上下文。
- **优先级**：核心

## 关系

- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：检索 → 重构
- related ← [[10_Papers/mplus|M+: Extending MemoryLLM with Scalable Long-Term Memory]]：参数化记忆 vs 图重构记忆

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
