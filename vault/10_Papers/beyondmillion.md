---
id: "beyondmillion"
type: "paper"
title: "Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "evaluation"
authors:
  - "Mohammad Tavakoli"
  - "Alireza Salemi"
  - "Carrie Ye"
  - "Mohamed Abdalla"
  - "Hamed Zamani"
  - "J Ross Mitchell"
doi: "10.48550/arXiv.2510.27246"
arxiv: "2510.27246"
openreview: "https://openreview.net/forum?id=y59hf5lrMn"
pdf: "https://openreview.net/pdf?id=y59hf5lrMn"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs

> **一句话定位**：百万 token 级长记忆评测与增强，扩展了长上下文记忆的压力测试。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Mohammad Tavakoli, Alireza Salemi, Carrie Ye, Mohamed Abdalla, Hamed Zamani, J Ross Mitchell
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=y59hf5lrMn)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=y59hf5lrMn)

## 摘要

Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is hampered by the existing benchmarks, which often lack narrative coherence, cover narrow domains, and only test simple recall-oriented tasks. This paper introduces a comprehensive solution to these challenges. First, we present a
novel framework for automatically generating long (up to 10M tokens), coherent, and topically diverse conversations, accompanied by probing questions targeting a wide range of memory abilities. From this, we construct BEAM, a new benchmark comprising 100 conversations and 2,000 validated questions. Second, to enhance model performance, we propose LIGHT–a framework inspired by human cognition that equips LLMs with three complementary memory systems: a long-term episodic memory, a short-term working memory, and a scratchpad for accumulating salient facts. Our experiments on BEAM reveal that even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen. In contrast, LIGHT consistently improves performance
across various models, achieving an average improvement of 3.5%–12.69% over the strongest baselines, depending on the backbone LLM. An ablation study further confirms the contribution of each memory component.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：百万 token 级长记忆评测与增强，扩展了长上下文记忆的压力测试。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/interdependent|Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks]]：规模压力 vs 任务依赖
- extends ← [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：长期交互 → 百万 token 压力测试

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
