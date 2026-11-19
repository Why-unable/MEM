---
id: "memagent"
type: "paper"
title: "MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "training"
authors:
  - "Hongli Yu"
  - "Tinghong Chen"
  - "Jiangtao Feng"
  - "Jiangjie Chen"
  - "Weinan Dai"
  - "Qiying Yu"
  - "Ya-Qin Zhang"
  - "Wei-Ying Ma"
  - "Jingjing Liu"
  - "Mingxuan Wang"
  - "Hao Zhou"
doi: "10.48550/arXiv.2507.02259"
arxiv: "2507.02259"
openreview: "https://openreview.net/forum?id=k5nIOvYGCL"
pdf: "https://openreview.net/pdf?id=k5nIOvYGCL"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/training"
  - "tier/Top-ICLR"
  - "priority/core"
---
# MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent

> **一句话定位**：用 multi-conv RL 训练 memory agent 压缩长上下文，代表“记忆策略可学习”路线。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-Ying Ma, Jingjing Liu, Mingxuan Wang, Hao Zhou
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=k5nIOvYGCL)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=k5nIOvYGCL)

## 摘要

Despite improvements by length extrapolation, efficient attention and memory modules, handling infinitely long documents without performance degradation during extrapolation remains the ultimate challenge in long-text processing. To solve this problem, We introduce a novel agent workflow, \method, which processes text in segments and updates memory through an overwrite strategy, addressing the challenge of long-context task through enhanced memory management. We further extend the DAPO algorithm to directly optimize memory ability in an end-to-end fashion, facilitating training via independent-context multi-conversation generation. Experimental results demonstrate that MemAgent has superb long-context capabilities, being able to extrapolate from an 8K context to a 3.5M QA task with a performance loss of less than 10\% and achieving over 95\% on the 512K NIAH test.

## 在研究地图中的位置

- **类别**：记忆策略与训练
- **角色**：用 multi-conv RL 训练 memory agent 压缩长上下文，代表“记忆策略可学习”路线。
- **优先级**：核心

## 关系

- related → [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]]：RL memory agent 的两条实现路线
- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：记忆结构 → RL memory agent
- related ← [[10_Papers/learnshare|Learning to Share: Selective Memory for Efficient Parallel Agentic Systems]]：并行记忆共享 vs 长上下文压缩

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
