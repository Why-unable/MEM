---
id: "hippocampus"
type: "paper"
title: "Hippocampus: An Efficient and Scalable Memory Module for Agentic AI"
year: "2026"
venue: "MLSys 2026"
venue_tier: "Top-MLSys"
category: "system"
authors:
  - "Yi Li"
  - "Lianjie Cao"
  - "Faraz Ahmed"
  - "Puneet Sharma"
  - "Bingzhe Li"
doi: "10.48550/arXiv.2602.13594"
arxiv: "2602.13594"
openreview: "https://openreview.net/forum?id=0sUYZh9D4a"
pdf: "https://openreview.net/pdf?id=0sUYZh9D4a"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/Top-MLSys"
  - "priority/supporting"
---
# Hippocampus: An Efficient and Scalable Memory Module for Agentic AI

> **一句话定位**：面向 agentic AI 的高效、可扩展记忆模块，偏系统实现与部署效率。

## 元数据

- **Venue**：MLSys 2026（Top-MLSys）
- **年份**：2026
- **作者**：Yi Li, Lianjie Cao, Faraz Ahmed, Puneet Sharma, Bingzhe Li
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=0sUYZh9D4a)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=0sUYZh9D4a)

## 摘要

Agentic AI systems require persistent memory to store user-specific histories beyond the limited context window of LLMs. Existing memory systems rely on the dense vector databases, knowledge-graph traversal, or hybrids, which incur high retrieval latency and poor storage scalability.
We introduce HIPPOCAMPUS, an agentic memory management system that uses compact binary signatures for semantic search and lossless token-ID streams for exact content reconstruction. Its core is a Dynamic Wavelet Matrix (DWM) that compresses and co-indexes
both streams to support ultra-fast search in the compressed domain, thus avoiding costly dense-vector or graph computations. For a fixed tokenizer vocabulary, the storage footprint of this design grows linearly with memory size, making it suitable for long-horizon agentic deployments. Empirically, across LoCoMo and LongMemEval, HIPPOCAMPUS achieves end-to-end retrieval latency that is comparable to or lower than the evaluated agentic memory baselines, with 1.1X–31.5X speedups over the evaluated baselines, and reduces per-query token footprint by 1.1X–14.5X, while maintaining competitive task accuracy.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：面向 agentic AI 的高效、可扩展记忆模块，偏系统实现与部署效率。
- **优先级**：支撑/扩展

## 关系

- extends ← [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：长期记忆系统 → 高效记忆模块
- related ← [[10_Papers/lightmem|LightMem: Lightweight and Efficient Memory-Augmented Generation]]：高效记忆模块的不同系统路线
- related ← [[10_Papers/vikingmem|VikingMem: A Memory Base Management System for Stateful LLM-Based Applications]]：VikingDB 向量引擎 vs 压缩检索模块

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
