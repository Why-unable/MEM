---
id: "umem"
type: "paper"
title: "UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "training"
authors:
  - "Yongshi Ye"
  - "Hui Jiang"
  - "Feihu Jiang"
  - "Tian Lan"
  - "Yichao Du"
  - "Biao Fu"
  - "Xiaodong Shi"
  - "Qianghuai Jia"
  - "Longyue Wang"
  - "Weihua Luo"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=BoiXvrwtdi"
pdf: "https://openreview.net/pdf?id=BoiXvrwtdi"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/training"
  - "tier/CCF-A"
  - "priority/core"
---
# UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory

> **一句话定位**：统一记忆抽取与管理，强调跨任务、跨场景的泛化记忆能力。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Yongshi Ye, Hui Jiang, Feihu Jiang, Tian Lan, Yichao Du, Biao Fu, Xiaodong Shi, Qianghuai Jia, Longyue Wang, Weihua Luo
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=BoiXvrwtdi)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=BoiXvrwtdi)

## 摘要

Self-evolving memory serves as the trainable parameters for Large Language Models (LLMs)-based agents, where extraction (distilling insights from experience) and management (updating the memory bank) must be tightly coordinated.
Existing methods predominantly optimize memory management while treating memory extraction as a static process, resulting in poor generalization, where agents accumulate instance-specific noise rather than robust memories.
To address this, we propose Unified Memory Extraction and Management (UMEM), a self-evolving agent framework that jointly optimizes a LLM to simultaneously extract and manage memories.
To mitigate overfitting to specific instances, we introduce Semantic Neighborhood Modeling and optimize the model with a neighborhood-level marginal utility reward via GRPO.
This approach ensures memory generalizability by evaluating memory utility across clusters of semantically related queries.
Extensive experiments across five benchmarks demonstrate that UMEM significantly outperforms highly competitive baselines, achieving up to 11.49 points improvement in multi-turn interactive tasks. Furthermore, UMEM maintains a stable improvement trend during continuous evolution.

## 在研究地图中的位置

- **类别**：记忆策略与训练
- **角色**：统一记忆抽取与管理，强调跨任务、跨场景的泛化记忆能力。
- **优先级**：核心

## 关系

- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：动态组织 → 统一抽取与管理
- related ← [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]]：记忆管理与统一管理
- related ← [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]]：自动设计 vs 统一抽取

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
