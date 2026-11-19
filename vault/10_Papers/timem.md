---
id: "timem"
type: "paper"
title: "TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents"
year: "2026"
venue: "ACL Findings 2026"
venue_tier: "ACL-Findings"
category: "consolidation"
authors:
  - "Kai Li"
  - "Xuanqing Yu"
  - "Ziyi Ni"
  - "Yi Zeng"
  - "Yao Xu"
  - "Zheqing Zhang"
  - "Xin Li"
  - "Jitao Sang"
  - "Xiaogang Duan"
  - "Xuelei Wang"
  - "Chengbao Liu"
  - "Jie Tan"
doi: "10.48550/arXiv.2601.02845"
arxiv: "2601.02845"
openreview: "https://openreview.net/forum?id=40y8NAFkq0"
pdf: "https://aclanthology.org/2026.findings-acl.1091.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/consolidation"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents

> **一句话定位**：时间—层次记忆整合，面向长时程对话中的时序信息保持。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Kai Li, Xuanqing Yu, Ziyi Ni, Yi Zeng, Yao Xu, Zheqing Zhang, Xin Li, Jitao Sang, Xiaogang Duan, Xuelei Wang, Chengbao Liu, Jie Tan
- **PDF**：[打开 PDF](https://aclanthology.org/2026.findings-acl.1091.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=40y8NAFkq0)

## 摘要

Long-horizon conversational agents have to manage ever-growing interaction histories that quickly exceed the finite context windows of large language models (LLMs). Existing memory frameworks provide limited support for temporally structured information across hierarchical levels, often leading to fragmented memories and unstable long-horizon personalization. We present TiMem, a temporal–hierarchical memory framework that organizes conversations through a Temporal Memory Tree (TMT), enabling systematic memory consolidation from raw conversational observations to progressively abstracted persona representations. TiMem is characterized by three core properties: (1) temporal–hierarchical organization through TMT; (2) semantic-guided consolidation that enables memory integration across hierarchical levels without fine-tuning; and (3) complexity-aware memory recall that balances precision and efficiency across queries of varying complexity. Under a consistent evaluation setup, TiMem achieves state-of-the-art accuracy on both benchmarks, reaching 75.30% on LoCoMo and 76.88% on LongMemEval-S. It outperforms all evaluated baselines while reducing the recalled memory length by 52.20% on LoCoMo. Manifold analysis indicates clear persona separation on LoCoMo and reduced dispersion on LongMemEval-S. Overall, TiMem treats temporal continuity as a first-class organizing principle for long-horizon memory in conversational agents. The code is available at https://github.com/TiMEM-AI/timem.

## 在研究地图中的位置

- **类别**：记忆整合
- **角色**：时间—层次记忆整合，面向长时程对话中的时序信息保持。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/tiermem|TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory]]：时间层次 → 压缩/证据分层
- extends ← [[10_Papers/recmem|RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents]]：整合 → 时间层次整合

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
