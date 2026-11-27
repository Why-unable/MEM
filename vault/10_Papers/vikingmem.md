---
id: "vikingmem"
type: "paper"
title: "VikingMem: A Memory Base Management System for Stateful LLM-Based Applications"
year: "2026"
venue: "PVLDB 2026"
venue_tier: "CCF-A"
category: "system"
authors:
  - "Jiajie Fu"
  - "Junwen Chen"
  - "Mengzhao Wang"
  - "Aoxiang He"
  - "Maojia Sheng"
  - "Xiangyu Ke"
  - "Yifan Zhu"
  - "Yunjun Gao"
doi: "10.14778/3827998.3828037"
arxiv: "2605.29640"
openreview: "https://doi.org/10.14778/3827998.3828037"
pdf: "https://arxiv.org/pdf/2605.29640"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-A"
  - "priority/core"
---
# VikingMem: A Memory Base Management System for Stateful LLM-Based Applications

> **一句话定位**：在 VikingDB 上实现 Memory Base 管理系统：事件/实体抽象、选择性抽取、状态演化、时间压缩与多向量重排。

## 元数据

- **Venue**：PVLDB 2026（CCF-A）
- **年份**：2026
- **作者**：Jiajie Fu, Junwen Chen, Mengzhao Wang, Aoxiang He, Maojia Sheng, Xiangyu Ke, Yifan Zhu, Yunjun Gao
- **PDF**：[打开 PDF](https://arxiv.org/pdf/2605.29640)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.14778/3827998.3828037)

## 摘要

Large Language Models have revolutionized interactive applications, however, their finite context windows pose a critical data management challenge for maintaining stateful, long-term interactions. Existing memory approaches, however, often rely on simplistic extraction that leads to incomplete memories or use rigid, single-use memory extract prompts tailored for one use case like Chatbots. Consequently, they lack generalizability and perform poorly on diverse downstream tasks. To bridge this gap, we introduce the Memory Base, a novel data management paradigm to manage the persistent state of long-term interactions. It is characterized by three core principles: selective extraction of high-value memories from raw information streams; inherent statefulness and evolution, where memory content is progressively summarized, corrected, and temporally weighted to prioritize recent interactions; and a generalizable abstraction paradigm designed for robust transferability across diverse applications, including education, recommendation, and agent memory. Building on this foundation, we present VikingMem, an end-to-end Memory Base Management System implemented on the VikingDB vector engine. VikingMem materializes this paradigm through interconnected event and entity abstractions. It features event-centric memory extraction to selectively handle complex information streams, while entities are dynamically updated by events to achieve stateful evolution. Using temporal compression via a topic-wise timeline and time-weighted recall, the system can progressively produce high-level summary memories, prioritize recent items, while compressing and fading older ones. Retrieval is further optimized through multi-vector-based reranking. Extensive evaluations on long-term memory benchmarks demonstrate that VikingMem achieves state-of-the-art performance, outperforming baselines by up to 30% in memory retrieval effectiveness while maintaining low latency essential for interactive applications.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：在 VikingDB 上实现 Memory Base 管理系统：事件/实体抽象、选择性抽取、状态演化、时间压缩与多向量重排。
- **优先级**：核心

## 关系

- extends → [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：生产级记忆流水线 → Memory Base 管理系统
- related → [[10_Papers/memoryos|Memory OS of AI Agent]]：Memory Base vs 分层 memory OS
- related → [[10_Papers/evermemos|EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning]]：Memory Base vs 自组织 memory OS
- related → [[10_Papers/hippocampus|Hippocampus: An Efficient and Scalable Memory Module for Agentic AI]]：VikingDB 向量引擎 vs 压缩检索模块
- related → [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]]：事件/实体 + 时间压缩 vs 多粒度记忆

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
