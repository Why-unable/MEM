---
id: "tiermem"
type: "paper"
title: "TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory"
year: "2026"
venue: "COLM 2026"
venue_tier: "Top-COLM"
category: "consolidation"
authors:
  - "Qiming Zhu"
  - "Shunian Chen"
  - "Rui Yu"
  - "Zhehao Wu"
  - "Benyou Wang"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=svKCa4itcd"
pdf: "https://openreview.net/pdf?id=svKCa4itcd"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/consolidation"
  - "tier/Top-COLM"
  - "priority/supporting"
---
# TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory

> **一句话定位**：在压缩记忆与原始证据之间做分层权衡，面向长时程 agent memory。

## 元数据

- **Venue**：COLM 2026（Top-COLM）
- **年份**：2026
- **作者**：Qiming Zhu, Shunian Chen, Rui Yu, Zhehao Wu, Benyou Wang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=svKCa4itcd)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=svKCa4itcd)

## 摘要

Long-horizon agents must preserve past experience before knowing what future queries will require. Compact memory makes growing histories efficient to reuse by distilling experience into reusable abstractions, while raw history preserves fine-grained evidence for faithful grounding. Because future queries require different levels of detail, the appropriate memory granularity cannot be reliably fixed when memory is written. We therefore argue that memory granularity should be determined when the future information need becomes known. We introduce \textbf{TierMem}, a provenance-linked two-tier memory framework that allocates memory granularity according to evidence sufficiency. TierMem retrieves compact memory by default, uses a learned router to identify when finer-grained evidence is required, and follows provenance links to recover relevant raw evidence. Recovered evidence can be consolidated into compact memory for future reuse. Across two long-horizon memory benchmarks, TierMem recovers much of the quality enabled by raw evidence while substantially reducing inference cost. Further analyses show that provenance improves evidence recovery and that consolidation progressively increases the share of queries served by compact memory.

## 在研究地图中的位置

- **类别**：记忆整合
- **角色**：在压缩记忆与原始证据之间做分层权衡，面向长时程 agent memory。
- **优先级**：支撑/扩展

## 关系

- evaluates → [[10_Papers/persistbench|PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?]]：压缩记忆的遗忘边界
- extends ← [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：记忆压缩与证据保留
- extends ← [[10_Papers/timem|TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents]]：时间层次 → 压缩/证据分层

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
