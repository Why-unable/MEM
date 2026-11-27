---
id: "hipporag2"
type: "paper"
title: "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models"
year: "2025"
venue: "ICML 2025"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Bernal Jiménez Gutiérrez"
  - "Yiheng Shu"
  - "Weijian Qi"
  - "Sizhe Zhou"
  - "Yu Su"
doi: null
arxiv: "2502.14802"
openreview: "https://proceedings.mlr.press/v267/gutierrez25a.html"
pdf: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/core"
---
# From RAG to Memory: Non-Parametric Continual Learning for Large Language Models

> **一句话定位**：用 Personalized PageRank + passage integration 统一事实、sense-making 和 associative memory 的图增强 RAG。

## 元数据

- **Venue**：ICML 2025（CCF-A）
- **年份**：2025
- **作者**：Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, Yu Su
- **PDF**：[打开 PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.mlr.press/v267/gutierrez25a.html)

## 摘要

Our ability to continuously acquire, organize, and leverage knowledge is a key feature of human intelligence that AI systems must approximate to unlock their full potential. Given the challenges in continual learning with large language models (LLMs), retrieval-augmented generation (RAG) has become the dominant way to introduce new information. However, its reliance on vector retrieval hinders its ability to mimic the dynamic and interconnected nature of human long-term memory. Recent RAG approaches augment vector embeddings with various structures like knowledge graphs to address some of these gaps, namely sense-making and associativity. However, their performance on more basic factual memory tasks drops considerably below standard RAG. We address this unintended deterioration and propose HippoRAG 2, a framework that outperforms standard RAG comprehensively on factual, sense-making, and associative memory tasks. HippoRAG 2 builds upon the Personalized PageRank algorithm used in HippoRAG and enhances it with deeper passage integration and more effective online use of an LLM. This combination pushes this RAG system closer to the effectiveness of human long-term memory, achieving a 7% improvement in associative memory tasks over the state-of-the-art embedding model while also exhibiting superior factual knowledge and sense-making memory capabilities. This work paves the way for non-parametric continual learning for LLMs. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：用 Personalized PageRank + passage integration 统一事实、sense-making 和 associative memory 的图增强 RAG。
- **优先级**：核心

## 关系

- related → [[10_Papers/magma|MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents]]：图增强 RAG vs 多关系 agent memory
- related → [[10_Papers/reconstructed|Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents]]：图检索基线 vs 主动重构
- related → [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]]：图检索与多粒度记忆的对照

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
