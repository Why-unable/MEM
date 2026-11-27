---
id: "nemori"
type: "paper"
title: "What Deserves Memory: Adaptive Memory Distillation for LLM Agents"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "consolidation"
authors:
  - "Wenquan Ma"
  - "Jiayan Nan"
  - "Wenlong Wu"
doi: "10.18653/v1/2026.acl-long.1607"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2026.acl-long.1607"
pdf: "https://aclanthology.org/2026.acl-long.1607.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/consolidation"
  - "tier/CCF-A"
  - "priority/supporting"
---
# What Deserves Memory: Adaptive Memory Distillation for LLM Agents

> **一句话定位**：把“什么值得记住”转化为可预测性/预测误差驱动的自适应蒸馏（Nemori），避免重要性分数等启发式规则。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Wenquan Ma, Jiayan Nan, Wenlong Wu
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.1607.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2026.acl-long.1607)

## 摘要

Memory systems for LLM agents struggle to determine what information deserves retention. Existing approaches rely on predefined heuristics such as importance scores, emotional tags, or factual templates, encoding designer intuition rather than learning from the data itself. Inspired by cognitive ideas, we propose Nemori , an adaptive memory distillation framework that casts the assessment of the experience’s future utility as a matter of predictability. Specifically, Nemori comprises two cascading modules: Episodic Memory Integration transforms raw interactions into coherent narratives, and Semantic Knowledge Distillation extracts insights via prediction error. Centering on distillation, the framework remains agnostic to downstream management. Extensive experiments confirm that Nemori achieves strong performance, efficiency, and storage reduction. Our work suggests that observing the intrinsic properties of interaction sequences offers a viable, data-driven alternative to heuristic-based memory design.

## 在研究地图中的位置

- **类别**：记忆整合
- **角色**：把“什么值得记住”转化为可预测性/预测误差驱动的自适应蒸馏（Nemori），避免重要性分数等启发式规则。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]]：自适应记忆蒸馏 vs 多粒度记忆
- related → [[10_Papers/recmem|RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents]]：预测误差驱动整合 vs recurrence-based consolidation

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
