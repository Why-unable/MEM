---
id: "ema"
type: "paper"
title: "EMA: An Episodic Memory Agent for Efficient and Selective Memory"
year: "2026"
venue: "ACL Findings 2026"
venue_tier: "ACL-Findings"
category: "episodic"
authors:
  - "Hongyi Lan"
  - "Jiaqi Song"
  - "Zhengjia Zhong"
  - "Hui Li"
  - "Hong Liu"
  - "Xianming Lin"
  - "Rongrong Ji"
doi: "10.18653/v1/2026.findings-acl.250"
arxiv: null
openreview: "https://openreview.net/forum?id=ZoBJWPoH9a"
pdf: "https://aclanthology.org/2026.findings-acl.250.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/episodic"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# EMA: An Episodic Memory Agent for Efficient and Selective Memory

> **一句话定位**：把对话抽象为 episodic memory unit 并做选择性记忆，降低长对话冗余。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Hongyi Lan, Jiaqi Song, Zhengjia Zhong, Hui Li, Hong Liu, Xianming Lin, Rongrong Ji
- **PDF**：[打开 PDF](https://aclanthology.org/2026.findings-acl.250.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=ZoBJWPoH9a)

## 摘要

Large Language Models (LLMs) demonstrate strong generation and reasoning abilities, but they still face challenges in long-term memory retention and multi-turn conversational consistency. Existing memory-augmented methods often incorporate full dialog histories without filtering, resulting in information redundancy and inference latency. Inspired by the episodic memory mechanism in human cognition, we abstract conversational context into Episodic Memory Units (EMUs). We then propose a comprehensive framework, Episodic Memory Agent (EMA), along with a filtering decision module called MemDecider. Specifically, EMA organizes and retrieves EMUs to support response generation, while MemDecider filters information to reduce noise and improve overall performance. Experiments on two widely-used benchmarks show that EMA maintains competitive performance, and integrating MemDecider into other methods reduces their token consumption by an average of 11.48% while effectively improving the overall performance. Code is available at https://github.com/Hongyi4221/EMA.

## 在研究地图中的位置

- **类别**：情景记忆
- **角色**：把对话抽象为 episodic memory unit 并做选择性记忆，降低长对话冗余。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/recmem|RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents]]：选择性记忆 → 复现式整合
- extends ← [[10_Papers/remem|REMem: Reasoning with Episodic Memory in Language Agent]]：事件级记忆 → 选择性 episodic unit
- related ← [[10_Papers/lightwm|LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents]]：小模型工作记忆 vs 事件记忆

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
