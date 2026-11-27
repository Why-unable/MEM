---
id: "evermemos"
type: "paper"
title: "EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "system"
authors:
  - "Chuanrui Hu"
  - "Xingze Gao"
  - "Zuyi Zhou"
  - "Dannong Xu"
  - "Yi Bai"
  - "Xintong Li"
  - "Hui Zhang"
  - "Tong Li"
  - "Chong Zhang"
  - "Lidong Bing"
  - "Yafeng Deng"
doi: "10.18653/v1/2026.acl-long.2125"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2026.acl-long.2125"
pdf: "https://aclanthology.org/2026.acl-long.2125.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-A"
  - "priority/supporting"
---
# EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning

> **一句话定位**：用 engram-inspired 生命周期组织记忆：Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Chuanrui Hu, Xingze Gao, Zuyi Zhou, Dannong Xu, Yi Bai, Xintong Li, Hui Zhang, Tong Li, Chong Zhang, Lidong Bing, Yafeng Deng
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.2125.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2026.acl-long.2125)

## 摘要

Large Language Models (LLMs) are increasingly deployed as long-term interactive agents, yet their limited context windows make it difficult to sustain coherent behavior over extended interactions. Existing memory systems for LLMs often store isolated records and retrieve fragments, limiting their ability to consolidate evolving experience and resolve conflicts. We introduce EverMemOS, a self-organizing memory operating system that implements an engram-inspired lifecycle for computational memory. First, Episodic Trace Formation converts dialogue streams into MemCells that capture episodic traces, atomic facts, and time-bounded foresight. Second, Semantic Consolidation organizes MemCells into thematic MemScenes, distilling stable semantic structures and updating user profiles. Finally, Reconstructive Recollection performs MemScene-guided agentic retrieval to compose the necessary and sufficient context for downstream reasoning. Experiments on LoCoMo, LongMemEval, and PersonaMem-v2 show that EverMemOS significantly outperforms state-of-the-art methods on memory-augmented reasoning tasks.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：用 engram-inspired 生命周期组织记忆：Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/memoryos|Memory OS of AI Agent]]：分层 memory OS → 自组织 memory OS
- related → [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]]：语义整合 + scene-guided retrieval
- related ← [[10_Papers/vikingmem|VikingMem: A Memory Base Management System for Stateful LLM-Based Applications]]：Memory Base vs 自组织 memory OS

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
