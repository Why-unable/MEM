---
id: "recmem"
type: "paper"
title: "RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents"
year: "2026"
venue: "ACL Findings 2026"
venue_tier: "ACL-Findings"
category: "consolidation"
authors:
  - "Zijie Dai"
  - "Shiyuan Deng"
  - "Sheng Guan"
  - "Yizhou Tian"
  - "Xin Yao"
  - "Xiao Yan"
  - "James Cheng"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=GIyUZ9ffAK"
pdf: "https://aclanthology.org/2026.findings-acl.1619.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/consolidation"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents

> **一句话定位**：基于复现/重复的记忆整合，减少对每条交互做 eager extraction 的开销。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Zijie Dai, Shiyuan Deng, Sheng Guan, Yizhou Tian, Xin Yao, Xiao Yan, James Cheng
- **PDF**：[打开 PDF](https://aclanthology.org/2026.findings-acl.1619.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=GIyUZ9ffAK)

## 摘要

Memory systems often organize user-agent interactions as retrievable external memory and are crucial for long-running agents by overcoming the limited context windows of LLMs. However, existing memory systems invoke LLMs to process every incoming interaction for memory extraction, and such an eager memory consolidation scheme leads to substantial token consumption. To tackle this problem, we propose RecMem by rethinking when memory consolidation should be conducted. RecMem stores incoming interactions in a subconscious memory layer and encode them using lightweight embedding models for retrieval. LLMs are only invoked to extract episodic and semantic memory when sustained recurrence are observed for semantically similar interactions. Such recurrence-based consolidation works because these interactions correspond to a semantic cluster with rich information and thus are worth extraction and summarization. To improve accuracy, RecMem also incorporates a semantic refinement mechanism that recovers the fine-grained facts omitted by memory extraction. Experiments show that RecMem reduces the memory construction token cost of three SOTA memory systems by up to 87% while exceeding their accuracy.

## 在研究地图中的位置

- **类别**：记忆整合
- **角色**：基于复现/重复的记忆整合，减少对每条交互做 eager extraction 的开销。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/timem|TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents]]：整合 → 时间层次整合
- related ← [[10_Papers/ema|EMA: An Episodic Memory Agent for Efficient and Selective Memory]]：选择性记忆 → 复现式整合

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
