---
id: "agemem"
type: "paper"
title: "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "training"
authors:
  - "Yi Yu"
  - "Liuyi Yao"
  - "Yuexiang Xie"
  - "Qingquan Tan"
  - "Jiaqi Feng"
  - "Yaliang Li"
  - "Libing Wu"
doi: "10.18653/v1/2026.acl-long.981"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2026.acl-long.981"
pdf: "https://aclanthology.org/2026.acl-long.981.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/training"
  - "tier/CCF-A"
  - "priority/core"
---
# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

> **一句话定位**：把 long-term / short-term memory 操作统一成 agent policy 的 tool actions，并用三阶段 RL + step-wise GRPO 训练。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, Libing Wu
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.981.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2026.acl-long.981)

## 摘要

Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relying on heuristics or auxiliary controllers, which limits adaptability and end-to-end optimization. In this paper, we propose Agentic Memory (AgeMem), a unified framework that integrates LTM and STM management directly into the agent’s policy. AgeMem exposes memory operations as tool-based actions, enabling the LLM agent to autonomously decide what and when to store, retrieve, update, summarize, or discard information. To train such unified behaviors, we propose a three-stage progressive reinforcement learning strategy and design a step-wise GRPO to address sparse and discontinuous rewards induced by memory operations. Experiments on five long-horizon benchmarks demonstrate that AgeMem consistently outperforms strong memory-augmented baselines across multiple LLM backbones, achieving improved task performance, higher-quality long-term memory, and more efficient context usage.

## 在研究地图中的位置

- **类别**：记忆策略与训练
- **角色**：把 long-term / short-term memory 操作统一成 agent policy 的 tool actions，并用三阶段 RL + step-wise GRPO 训练。
- **优先级**：核心

## 关系

- extends → [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]]：分离的记忆操作 → 统一 LTM/STM 策略
- related → [[10_Papers/memagent|MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent]]：RL memory agent 的不同统一管理路线
- related → [[10_Papers/persistbench|PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?]]：可学习 discard 动作与遗忘边界评测

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
