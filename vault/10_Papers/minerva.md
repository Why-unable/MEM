---
id: "minerva"
type: "paper"
title: "Minerva: A Programmable Memory Test Benchmark for Language Models"
year: "2025"
venue: "ICML 2025"
venue_tier: "CCF-A"
category: "evaluation"
authors:
  - "Menglin Xia"
  - "Victor Rühle"
  - "Saravan Rajmohan"
  - "Reza Shokri"
doi: "10.48550/arXiv.2502.03358"
arxiv: "2502.03358"
openreview: "https://openreview.net/forum?id=ib9drlZllP"
pdf: "https://openreview.net/pdf?id=ib9drlZllP"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/CCF-A"
  - "priority/supporting"
---
# Minerva: A Programmable Memory Test Benchmark for Language Models

> **一句话定位**：可编程记忆测试基准，把记忆能力拆成可组合的测试程序。

## 元数据

- **Venue**：ICML 2025（CCF-A）
- **年份**：2025
- **作者**：Menglin Xia, Victor Rühle, Saravan Rajmohan, Reza Shokri
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=ib9drlZllP)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=ib9drlZllP)

## 摘要

How effectively can LLM-based AI assistants utilize their memory (context) to perform various tasks? Traditional data benchmarks, which are often manually crafted, suffer from several limitations: they are static, susceptible to overfitting, difficult to interpret, and lack actionable insights--failing to pinpoint the specific capabilities a model lacks when it does not pass a test. In this paper, we present a framework for automatically generating a comprehensive set of tests to evaluate models' abilities to use their memory effectively. Our framework extends the range of capability tests beyond the commonly explored (passkey, key-value, needle in the haystack) search, a dominant focus in the literature. Specifically, we evaluate models on atomic tasks such as searching, recalling, editing, matching, comparing information in context memory, performing basic operations when inputs are structured into distinct blocks, and maintaining state while operating on memory, simulating real-world data. Additionally, we design composite tests to investigate the models' ability to perform more complex, integrated tasks. Our benchmark enables an interpretable, detailed assessment of memory capabilities of LLMs.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：可编程记忆测试基准，把记忆能力拆成可组合的测试程序。
- **优先级**：支撑/扩展

## 关系

- related ← [[10_Papers/membench|MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents]]：综合评测 vs 可编程测试

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
