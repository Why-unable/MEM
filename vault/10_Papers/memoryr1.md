---
id: "memoryr1"
type: "paper"
title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "training"
authors:
  - "Sikuan Yan"
  - "Xiufeng Yang"
  - "Zuchao Huang"
  - "Ercong Nie"
  - "Zifeng Ding"
  - "Zonggen Li"
  - "Xiaowen Ma"
  - "Jinhe Bi"
  - "Kristian Kersting"
  - "Jeff Z. Pan"
  - "Hinrich Schütze"
  - "Volker Tresp"
  - "Yunpu Ma"
doi: "10.48550/arXiv.2508.19828"
arxiv: "2508.19828"
openreview: "https://openreview.net/forum?id=inJIfKNFuE"
pdf: "https://aclanthology.org/2026.acl-long.583.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/training"
  - "tier/CCF-A"
  - "priority/core"
---
# Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning

> **一句话定位**：用强化学习训练记忆管理与使用策略，把记忆操作从 prompt 工程推进为可学习策略。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe Bi, Kristian Kersting, Jeff Z. Pan, Hinrich Schütze, Volker Tresp, Yunpu Ma
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.583.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=inJIfKNFuE)

## 摘要

Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLMs with an external memory bank, yet most existing pipelines are static and heuristic-driven, lacking a learned mechanism for deciding what to store, update, or retrieve. We present Memory-R1, a reinforcement learning (RL) framework that equips LLMs with the ability to actively manage and utilize external memory through two specialized agents: a Memory Manager that learns structured operations, including ADD, UPDATE, DELETE, and NOOP; and an Answer Agent that pre-selects and reasons over relevant entries. Both agents are fine-tuned with outcome-driven RL (PPO and GRPO), enabling adaptive memory management with minimal supervision. With only 152 training QA pairs, Memory-R1 outperforms strong baselines and generalizes across diverse question types, three benchmarks (LoCoMo, MSC, LongMemEval), and multiple model scales (3B–14B).

## 在研究地图中的位置

- **类别**：记忆策略与训练
- **角色**：用强化学习训练记忆管理与使用策略，把记忆操作从 prompt 工程推进为可学习策略。
- **优先级**：核心

## 关系

- extends → [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]]：记忆策略学习 → 记忆系统进化
- related → [[10_Papers/umem|UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory]]：记忆管理与统一管理
- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：记忆结构 → 可学习记忆策略
- related ← [[10_Papers/memagent|MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent]]：RL memory agent 的两条实现路线
- evaluated-by ← [[10_Papers/persistbench|PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?]]：记忆管理与遗忘边界

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
