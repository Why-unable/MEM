---
id: "amem"
type: "paper"
title: "A-Mem: Agentic Memory for LLM Agents"
year: "2025"
venue: "NeurIPS 2025"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Wujiang Xu"
  - "Zujie Liang"
  - "Kai Mei"
  - "Hang Gao"
  - "Juntao Tan"
  - "Yongfeng Zhang"
doi: "10.48550/arXiv.2502.12110"
arxiv: "2502.12110"
openreview: "https://openreview.net/forum?id=FiM0M8gcct"
pdf: "https://openreview.net/pdf?id=FiM0M8gcct"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/core"
---
# A-Mem: Agentic Memory for LLM Agents

> **一句话定位**：提出动态组织、链接和演化的 agentic memory，是 2025 年后记忆结构设计的高频基线。

## 元数据

- **Venue**：NeurIPS 2025（CCF-A）
- **年份**：2025
- **作者**：Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=FiM0M8gcct)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=FiM0M8gcct)

## 摘要

While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems' fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution -- as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management.
Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The code is available at \url{https://anonymous.4open.science/r/AgenticMemory-76B4}.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：提出动态组织、链接和演化的 agentic memory，是 2025 年后记忆结构设计的高频基线。
- **优先级**：核心

## 关系

- extends → [[10_Papers/gmemory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]]：单 agent 记忆 → 多 agent 层次记忆
- extends → [[10_Papers/magma|MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents]]：动态记忆组织 → 多图结构
- extends → [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]]：记忆组织 → 多粒度关联
- extends → [[10_Papers/reconstructed|Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents]]：检索 → 重构
- extends → [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]]：记忆结构 → 可学习记忆策略
- extends → [[10_Papers/memagent|MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent]]：记忆结构 → RL memory agent
- extends → [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]]：手工设计 → 元进化
- extends → [[10_Papers/umem|UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory]]：动态组织 → 统一抽取与管理
- extends → [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：研究原型 → 生产级记忆流水线
- evaluated-by ← [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：A-Mem 类系统的长期记忆评测参照
- evaluated-by ← [[10_Papers/membench|MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents]]：agent memory 综合评测参照

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
