---
id: "learnshare"
type: "paper"
title: "Learning to Share: Selective Memory for Efficient Parallel Agentic Systems"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "multiagent"
authors:
  - "Joseph Fioresi"
  - "Parth Parag Kulkarni"
  - "Ashmal Vayani"
  - "Song Wang"
  - "Mubarak Shah"
doi: "10.48550/arXiv.2602.05965"
arxiv: "2602.05965"
openreview: "https://openreview.net/forum?id=cCFyY2LmF5"
pdf: "https://openreview.net/pdf?id=cCFyY2LmF5"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/multiagent"
  - "tier/CCF-A"
  - "priority/supporting"
---
# Learning to Share: Selective Memory for Efficient Parallel Agentic Systems

> **一句话定位**：并行多 agent 系统中的选择性共享记忆，平衡效率与协作收益。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Joseph Fioresi, Parth Parag Kulkarni, Ashmal Vayani, Song Wang, Mubarak Shah
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=cCFyY2LmF5)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=cCFyY2LmF5)

## 摘要

Agentic systems solve complex tasks by coordinating multiple agents that iteratively reason, invoke tools, and exchange intermediate results. To improve robustness and solution quality, recent approaches deploy multiple agent teams running in parallel to explore diverse reasoning trajectories. However, parallel execution comes at a significant computational cost: when different teams independently reason about similar sub-problems or execute analogous steps, they repeatedly perform substantial overlapping computation. To address these limitations, in this paper, we propose Learning to Share (LTS), a learned shared-memory mechanism for parallel agentic frameworks that enables selective cross-team information reuse while controlling context growth. LTS introduces a global memory bank accessible to all teams and a lightweight controller that decides whether intermediate agent steps should be added to memory or not. The controller is trained using stepwise reinforcement learning with usage-aware credit assignment, allowing it to identify information that is globally useful across parallel executions. Experiments on the AssistantBench and GAIA benchmarks show that LTS significantly reduces overall runtime while matching or improving task performance compared to memory-free parallel baselines, demonstrating that learned memory admission is an effective strategy for improving the efficiency of parallel agentic systems.

## 在研究地图中的位置

- **类别**：多智能体记忆
- **角色**：并行多 agent 系统中的选择性共享记忆，平衡效率与协作收益。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/memagent|MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent]]：并行记忆共享 vs 长上下文压缩
- extends ← [[10_Papers/gmemory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]]：团队记忆 → 选择性共享记忆

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
