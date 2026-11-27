---
id: "memgas"
type: "paper"
title: "From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "architecture"
authors:
  - "Derong Xu"
  - "Yi Wen"
  - "Pengyue Jia"
  - "Yingyi Zhang"
  - "Wenlin Zhang"
  - "Yichao Wang"
  - "Huifeng Guo"
  - "Ruiming Tang"
  - "Xiangyu Zhao"
  - "Enhong Chen"
  - "Tong Xu"
doi: null
arxiv: "2505.19549"
openreview: "https://openreview.net/forum?id=i2yIvZARnG"
pdf: "https://openreview.net/pdf?id=i2yIvZARnG"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents

> **一句话定位**：多粒度记忆关联与选择，缓解长对话中检索粒度不匹配的问题。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Derong Xu, Yi Wen, Pengyue Jia, Yingyi Zhang, Wenlin Zhang, Yichao Wang, Huifeng Guo, Ruiming Tang, Xiangyu Zhao, Enhong Chen, Tong Xu
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=i2yIvZARnG)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=i2yIvZARnG)

## 摘要

Large Language Models (LLMs) have recently been widely adopted in conversational agents. However, the increasingly long interactions between users and agents accumulate extensive dialogue records, making it difficult for LLMs with limited context windows to maintain a coherent long-term dialogue memory and deliver personalized responses. While retrieval-augmented memory systems have emerged to address this issue, existing methods often depend on single-granularity memory segmentation and retrieval. This approach falls short in capturing deep memory connections, leading to partial retrieval of useful information or substantial noise, resulting in suboptimal performance. To tackle these limits, we propose MemGAS, a framework that enhances memory consolidation by constructing multi-granularity association, adaptive selection, and retrieval. MemGAS is based on multi-granularity memory units and employs Gaussian Mixture Models to cluster and associate new memories with historical ones. An entropy-based router adaptively selects optimal granularity by evaluating query relevance distributions and balancing information completeness and noise. Retrieved memories are further refined via LLM-based filtering. Experiments on four long-term memory benchmarks demonstrate that MemGAS outperforms state-of-the-art methods on both question answer and retrieval tasks, achieving superior performance across different query types and top-K settings\footnote{https://github.com/Applied-Machine-Learning-Lab/ICLR2026\_MemGAS}.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：多粒度记忆关联与选择，缓解长对话中检索粒度不匹配的问题。
- **优先级**：支撑/扩展

## 关系

- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：记忆组织 → 多粒度关联
- extends ← [[10_Papers/secom|On Memory Construction and Retrieval for Personalized Conversational Agents]]：segment 级记忆 → 多粒度记忆
- related ← [[10_Papers/hipporag2|From RAG to Memory: Non-Parametric Continual Learning for Large Language Models]]：图检索与多粒度记忆的对照
- related ← [[10_Papers/evermemos|EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning]]：语义整合 + scene-guided retrieval
- related ← [[10_Papers/nemori|What Deserves Memory: Adaptive Memory Distillation for LLM Agents]]：自适应记忆蒸馏 vs 多粒度记忆
- related ← [[10_Papers/vikingmem|VikingMem: A Memory Base Management System for Stateful LLM-Based Applications]]：事件/实体 + 时间压缩 vs 多粒度记忆

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
