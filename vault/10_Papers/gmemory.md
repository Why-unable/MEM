---
id: "gmemory"
type: "paper"
title: "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems"
year: "2025"
venue: "NeurIPS 2025"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Guibin Zhang"
  - "Muxin Fu"
  - "Kun Wang"
  - "Guancheng Wan"
  - "Miao Yu"
  - "Shuicheng YAN"
doi: "10.48550/arXiv.2506.07398"
arxiv: "2506.07398"
openreview: "https://openreview.net/forum?id=mmIAp3cVS0"
pdf: "https://openreview.net/pdf?id=mmIAp3cVS0"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/core"
---
# G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems

> **一句话定位**：把多智能体协作轨迹组织成层次记忆，连接个体记忆与团队记忆。

## 元数据

- **Venue**：NeurIPS 2025（CCF-A）
- **年份**：2025
- **作者**：Guibin Zhang, Muxin Fu, Kun Wang, Guancheng Wan, Miao Yu, Shuicheng YAN
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=mmIAp3cVS0)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=mmIAp3cVS0)

## 摘要

Large language model (LLM)-powered multi-agent systems (MAS) have demonstrated cognitive and execution capabilities that far exceed those of single LLM agents, yet their capacity for self-evolution remains hampered by underdeveloped memory architectures. Upon close inspection, we are alarmed to discover that prevailing MAS memory mechanisms (1) are overly simplistic, completely disregarding the nuanced inter-agent collaboration trajectories, and (2) lack cross-trial and agent-specific customization, in stark contrast to the expressive memory developed for single agents. To bridge this gap, we introduce G-Memory, a hierarchical, agentic memory system for MAS inspired by organizational memory theory, which manages the lengthy MAS interaction via a three-tier graph hierarchy: insight, query, and interaction graphs. Upon receiving a new user query, G-Memory performs bi-directional memory traversal to retrieve both \textit{high-level, generalizable insights} that enable the system to leverage cross-trial knowledge, and \textit{fine-grained, condensed interaction trajectories} that compactly encode prior collaboration experiences. Upon task execution, the entire hierarchy evolves by assimilating new collaborative trajectories, nurturing the progressive evolution of agent teams. Extensive experiments across five benchmarks, three LLM backbones, and three popular MAS frameworks demonstrate that G-Memory improves success rates in embodied action and accuracy in knowledge QA by up to $20.89\\%$ and $10.12\\%$, respectively, without any modifications to the original frameworks.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：把多智能体协作轨迹组织成层次记忆，连接个体记忆与团队记忆。
- **优先级**：核心

## 关系

- extends → [[10_Papers/learnshare|Learning to Share: Selective Memory for Efficient Parallel Agentic Systems]]：团队记忆 → 选择性共享记忆
- related → [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]]：多 agent 记忆 → 记忆系统进化
- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：单 agent 记忆 → 多 agent 层次记忆

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
