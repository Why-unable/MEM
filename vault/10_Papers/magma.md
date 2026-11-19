---
id: "magma"
type: "paper"
title: "MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Dongming Jiang"
  - "Yi Li"
  - "Guanpeng Li"
  - "Bingzhe Li"
doi: "10.48550/arXiv.2601.03236"
arxiv: "2601.03236"
openreview: "https://openreview.net/forum?id=ktbwLLO9nX"
pdf: "https://aclanthology.org/2026.acl-long.1709.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/core"
---
# MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents

> **一句话定位**：用多图结构组织实体、事件和时间关系，强调可解释、可检索的 agent 记忆。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Dongming Jiang, Yi Li, Guanpeng Li, Bingzhe Li
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.1709.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=ktbwLLO9nX)

## 摘要

Memory-Augmented Generation (MAG) extends large language models with external memory to support long-context reasoning, but existing approaches largely rely on semantic similarity over monolithic memory stores, entangling temporal, causal, and entity information. This design limits interpretability and alignment between query intent and retrieved evidence, leading to suboptimal reasoning accuracy. In this paper, we propose MAGMA, a multi-graph agentic memory architecture that represents each memory item across orthogonal semantic, temporal, causal, and entity graphs. MAGMA formulates retrieval as policy-guided traversal over these relational views, enabling query-adaptive selection and structured context construction. By decoupling memory representation from retrieval logic, MAGMA provides transparent reasoning paths and fine-grained control over retrieval. Experiments on LoCoMo and LongMemEval demonstrate that MAGMA consistently outperforms state-of-the-art agentic memory systems in long-horizon reasoning task.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：用多图结构组织实体、事件和时间关系，强调可解释、可检索的 agent 记忆。
- **优先级**：核心

## 关系

- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：动态记忆组织 → 多图结构

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
