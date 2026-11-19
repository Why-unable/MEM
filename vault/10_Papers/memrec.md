---
id: "memrec"
type: "paper"
title: "MemRec: Collaborative Memory-Augmented Agentic Recommender System"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "application"
authors:
  - "Weixin Chen"
  - "Yuhan Zhao"
  - "Jingyuan Huang"
  - "Zihe Ye"
  - "Mingxuan Ju"
  - "Tong Zhao"
  - "Neil Shah"
  - "Li Chen"
  - "Yongfeng Zhang"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=FaMcfd14pg"
pdf: "https://aclanthology.org/2026.acl-long.2061.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/application"
  - "tier/CCF-A"
  - "priority/supporting"
---
# MemRec: Collaborative Memory-Augmented Agentic Recommender System

> **一句话定位**：把协作记忆增强用于 agentic recommender system。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Weixin Chen, Yuhan Zhao, Jingyuan Huang, Zihe Ye, Mingxuan Ju, Tong Zhao, Neil Shah, Li Chen, Yongfeng Zhang
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.2061.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=FaMcfd14pg)

## 摘要

The evolution of recommender systems has shifted from traditional collaborative filtering to LLM-based agentic systems, which rely on semantic user and item memories to make predictions. However, existing agents maintain these memories in isolation. This overlooks crucial collaborative signals, such as user-item co-engagements and peer relationships across the community, which significantly limits their ability to uncover hidden preferences and accurately infer user needs, particularly for data-sparse users. To bridge this gap, we introduce collaborative memory, a paradigm that connects isolated semantics to enable the sharing of relational insights. Yet, naively utilizing collaborative memory causes severe context overload and introduces noise to downstream LLMs, alongside prohibitive computational costs. To resolve this, we propose MemRec, a framework that architecturally decouples memory management from reasoning. MemRec introduces a dedicated, lightweight language model LM_Mem to efficiently manage and synthesize a dynamic collaborative memory graph in the background. It provides only distilled, high-signal contexts to a downstream, heavyweight large language model (LLM_Rec) for the final recommendation. Extensive experiments on four benchmarks demonstrate that MemRec achieves state-of-the-art performance. Code: https://github.com/rutgerswiselab/memrecHomepage: https://memrec.weixinchen.com

## 在研究地图中的位置

- **类别**：应用
- **角色**：把协作记忆增强用于 agentic recommender system。
- **优先级**：支撑/扩展

## 关系

- applies → [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：长期记忆用于推荐

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
