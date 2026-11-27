---
id: "storagetexperience"
type: "paper"
title: "From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms"
year: "2026"
venue: "ACL Findings 2026"
venue_tier: "ACL-Findings"
category: "survey"
authors:
  - "Jinghao Luo"
  - "Yuchen Tian"
  - "Chuxue Cao"
  - "Ziyang Luo"
  - "Hongzhan Lin"
  - "Kaixin Li"
  - "Chuyi Kong"
  - "Ruichao Yang"
  - "Jing Ma"
doi: "10.18653/v1/2026.findings-acl.2069"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2026.findings-acl.2069"
pdf: "https://aclanthology.org/2026.findings-acl.2069.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/survey"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms

> **一句话定位**：把 LLM agent memory 的演化概括为 Storage → Reflection → Experience 三阶段，并梳理长程一致性、动态环境和持续学习三条驱动线。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Jinghao Luo, Yuchen Tian, Chuxue Cao, Ziyang Luo, Hongzhan Lin, Kaixin Li, Chuyi Kong, Ruichao Yang, Jing Ma
- **PDF**：[打开 PDF](https://aclanthology.org/2026.findings-acl.2069.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2026.findings-acl.2069)

## 摘要

Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscillating between operating system engineering and cognitive science. This theoretical divide prevents a unified view of technological synthesis and a coherent evolutionary perspective. To bridge this gap, this survey proposes a novel evolutionary framework for LLM agent memory mechanisms, formalizing the development process into three stages: **Storage** (trajectory preservation), **Reflection** (trajectory refinement), and **Experience** (trajectory abstraction). We first formally define these three stages before analyzing the three core drivers of this evolution: the necessity for long-range consistency, the challenges in dynamic environments, and the ultimate goal of continual learning. Furthermore, we specifically explore two transformative mechanisms in the frontier Experience stage: proactive exploration and cross-trajectory abstraction. By synthesizing these disparate views, this work offers robust design principles and a clear roadmap for the development of next-generation LLM agents.

## 在研究地图中的位置

- **类别**：综述与框架
- **角色**：把 LLM agent memory 的演化概括为 Storage → Reflection → Experience 三阶段，并梳理长程一致性、动态环境和持续学习三条驱动线。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：综述框架：Storage → Reflection → Experience
- related → [[10_Papers/reasoningbank|ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory]]：Experience 阶段的跨轨迹抽象

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
