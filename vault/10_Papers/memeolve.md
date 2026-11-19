---
id: "memeolve"
type: "paper"
title: "MemEvolve: Meta-Evolution of Agent Memory Systems"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "training"
authors:
  - "Guibin Zhang"
  - "Haotian Ren"
  - "Chong Zhan"
  - "Junhao Wang"
  - "He Zhu"
  - "Wangchunshu Zhou"
  - "Shuicheng YAN"
doi: "10.48550/arXiv.2512.18746"
arxiv: "2512.18746"
openreview: "https://openreview.net/forum?id=qpkG0eKx4v"
pdf: "https://openreview.net/pdf?id=qpkG0eKx4v"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/training"
  - "tier/CCF-A"
  - "priority/core"
---
# MemEvolve: Meta-Evolution of Agent Memory Systems

> **一句话定位**：用元进化自动设计记忆系统的结构与策略，代表“记忆系统自动设计”方向。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Guibin Zhang, Haotian Ren, Chong Zhan, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng YAN
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=qpkG0eKx4v)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=qpkG0eKx4v)

## 摘要

Self-evolving memory systems are rapidly reshaping the evolutionary paradigm of large language model (LLM)-based agents. Prior work has predominantly relied on manually engineered memory architectures to store trajectories, distill experience, and synthesize reusable tools, enabling agents to evolve on the fly within environment interactions. However, this paradigm is fundamentally constrained by the \textit{staticity} of the memory system itself: while memory facilitates agent-level evolving, the underlying memory architecture cannot be meta-adapted to diverse task contexts. To address this gap, we propose MemEvolve, a meta-evolutionary framework that jointly evolves agents’ experiential knowledge and their memory architecture, allowing agent systems not only to accumulate experience but also to progressively refine how they learn from it. To ground MemEvolve in prior work and promote openness in future self-evolving systems, we introduce EvolveLab, a unified memory codebase that distills twelve representative memory systems into a modular design space (\textit{encode}, \textit{store}, \textit{retrieve}, \textit{manage}), providing a standardized implementation substrate and a fair experimental arena. Extensive evaluations on four challenging agentic benchmarks show that MemEvolve delivers (i) substantial performance gains, improving frameworks such as SmolAgent and Flash-Searcher by up to $17.06\%$, and (ii) strong cross-task and cross-LLM generalization, yielding memory architectures that transfer effectively across diverse benchmarks and backbones.

## 在研究地图中的位置

- **类别**：记忆策略与训练
- **角色**：用元进化自动设计记忆系统的结构与策略，代表“记忆系统自动设计”方向。
- **优先级**：核心

## 关系

- related → [[10_Papers/umem|UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory]]：自动设计 vs 统一抽取
- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：手工设计 → 元进化
- related ← [[10_Papers/gmemory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]]：多 agent 记忆 → 记忆系统进化
- extends ← [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]]：记忆策略学习 → 记忆系统进化
- related ← [[10_Papers/rememberrefine|Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution]]：程序性记忆 vs 元进化

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
