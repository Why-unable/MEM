---
id: "mplus"
type: "paper"
title: "M+: Extending MemoryLLM with Scalable Long-Term Memory"
year: "2025"
venue: "ICML 2025"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Yu Wang"
  - "Dmitry Krotov"
  - "Yuanzhe Hu"
  - "Yifan Gao"
  - "Wangchunshu Zhou"
  - "Julian McAuley"
  - "Dan Gutfreund"
  - "Rogerio Feris"
  - "Zexue He"
doi: "10.48550/arXiv.2502.00592"
arxiv: "2502.00592"
openreview: "https://openreview.net/forum?id=OcqbkROe8J"
pdf: "https://openreview.net/pdf?id=OcqbkROe8J"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/supporting"
---
# M+: Extending MemoryLLM with Scalable Long-Term Memory

> **一句话定位**：扩展 MemoryLLM 的可扩展长期参数记忆，连接参数化记忆与外部记忆。

## 元数据

- **Venue**：ICML 2025（CCF-A）
- **年份**：2025
- **作者**：Yu Wang, Dmitry Krotov, Yuanzhe Hu, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, Zexue He
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=OcqbkROe8J)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=OcqbkROe8J)

## 摘要

Equipping large language models (LLMs) with latent-space memory has attracted increasing attention as they can extend the context window of existing language models. However, retaining information from the distant past remains a challenge. For example, MemoryLLM (Wang et al., 2024a), as a representative work with latent-space memory, compresses past information into hidden states across all layers, forming a memory pool of 1B parameters. While effective for sequence lengths up to 16k tokens, it struggles to retain knowledge beyond 20k tokens. In this work, we address this limitation by introducing M+, a memory-augmented model based on MemoryLLM that significantly enhances long-term information retention. M+ integrates a long-term memory mechanism with a co-trained retriever, dynamically retrieving relevant information during text generation. We evaluate M+ on diverse benchmarks, including long-context understanding and knowledge retention tasks. Experimental results show that M+ significantly outperforms MemoryLLM and recent strong baselines, extending knowledge retention from under 20k to over 160k tokens with similar GPU memory overhead.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：扩展 MemoryLLM 的可扩展长期参数记忆，连接参数化记忆与外部记忆。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/reconstructed|Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents]]：参数化记忆 vs 图重构记忆

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
