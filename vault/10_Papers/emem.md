---
id: "emem"
type: "paper"
title: "E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Kaixiang Wang"
  - "Yidan Lin"
  - "Zihan Wang"
  - "Bunyod Suvonov"
  - "Zhaojiacheng Zhou"
  - "Yuxiang Zheng"
  - "Jiaxi Cao"
  - "Zhiheng Dong"
  - "Chentao Wu"
  - "Jiong Lou"
  - "Jie Li"
doi: null
arxiv: "2601.21714"
openreview: "https://proceedings.mlr.press/v306/wang26ee.html"
pdf: "https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26ee/wang26ee.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/supporting"
---
# E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory

> **一句话定位**：用多个 assistant agent 保留未压缩的情境上下文，由 master agent 协调局部推理和证据重构，避免记忆预处理造成去语境化。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Kaixiang Wang, Yidan Lin, Zihan Wang, Bunyod Suvonov, Zhaojiacheng Zhou, Yuxiang Zheng, Jiaxi Cao, Zhiheng Dong, Chentao Wu, Jiong Lou, Jie Li
- **PDF**：[打开 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26ee/wang26ee.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.mlr.press/v306/wang26ee.html)

## 摘要

The evolution of Large Language Model (LLM) agents towards System~2 reasoning, characterized by deliberative, high-precision problem-solving, requires maintaining rigorous logical integrity over extended horizons. However, prevalent memory preprocessing paradigms suffer from destructive de-contextualization. By compressing complex sequential dependencies into pre-defined structures (e.g., embeddings or graphs), these methods sever the contextual integrity essential for deep reasoning. To address this, we propose E-mem, a framework shifting from Memory Preprocessing to Episodic Context Reconstruction. Inspired by biological engrams, E-mem employs a heterogeneous hierarchical architecture where multiple assistant agents maintain uncompressed memory contexts, while a central master agent orchestrates global planning. Unlike passive retrieval, our mechanism empowers assistants to locally reason within activated segments, extracting context-aware evidence before aggregation. Evaluations on the LoCoMo benchmark demonstrate that E-mem achieves over 54\% F1, surpassing the state-of-the-art GAM by 7.75\%, while reducing token cost by over 70\%.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：用多个 assistant agent 保留未压缩的情境上下文，由 master agent 协调局部推理和证据重构，避免记忆预处理造成去语境化。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/reconstructed|Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents]]：episodic context reconstruction vs active reconstruction
- related → [[10_Papers/gam|GAM: Hierarchical Graph-based Agentic Memory for LLM Agents]]：E-mem 在 LoCoMo 上以 GAM 为强基线

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
