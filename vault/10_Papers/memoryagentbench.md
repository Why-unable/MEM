---
id: "memoryagentbench"
type: "paper"
title: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "evaluation"
authors:
  - "Yuanzhe Hu"
  - "Yu Wang"
  - "Julian McAuley"
doi: null
arxiv: "2507.05257"
openreview: "https://proceedings.iclr.cc/paper_files/paper/2026/hash/fd1eff9dd295df50a41f2521942fa31d-Abstract-Conference.html"
pdf: "https://proceedings.iclr.cc/paper_files/paper/2026/file/fd1eff9dd295df50a41f2521942fa31d-Paper-Conference.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions

> **一句话定位**：把长期记忆评测改造成增量多轮交互，覆盖检索、测试时学习、长程理解和选择性遗忘四项能力。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Yuanzhe Hu, Yu Wang, Julian McAuley
- **PDF**：[打开 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/fd1eff9dd295df50a41f2521942fa31d-Paper-Conference.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fd1eff9dd295df50a41f2521942fa31d-Abstract-Conference.html)

## 摘要

Recent benchmarks for Large Language Model (LLM) agents primarily focus on evaluating reasoning, planning, and execution capabilities, while another critical component-memory, encompassing how agents memorize, update, and retrieve long-term information-is under-evaluated due to the lack of benchmarks. We term agents with memory mechanisms as memory agents. In this paper, based on classic theories from memory science and cognitive science, we identify four core competencies essential for memory agents: accurate retrieval, test-time learning, long-range understanding, and selective forgetting. Existing benchmarks either rely on limited context lengths or are tailored for static, long-context settings like book-based QA, which do not reflect the interactive, multi-turn nature of memory agents that incrementally accumulate information. Moreover, no existing benchmarks cover all four competencies. We introduce MemoryAgentBench, a new benchmark specifically designed for memory agents. Our benchmark transforms existing long-context datasets and incorporates newly constructed datasets into a multi-turn format, effectively simulating the incremental information processing characteristic of memory agents. By carefully selecting and curating datasets, our benchmark provides comprehensive coverage of the four core memory competencies outlined above, thereby offering a systematic and challenging testbed for assessing memory quality. We evaluate a diverse set of memory agents, ranging from simple context-based and retrieval-augmented generation (RAG) systems to advanced agents with external memory modules and tool integration. Empirical results reveal that current methods fall short of mastering all four competencies, underscoring the need for further research into comprehensive memory mechanisms for LLM agents.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：把长期记忆评测改造成增量多轮交互，覆盖检索、测试时学习、长程理解和选择性遗忘四项能力。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：静态长期记忆评测 → 增量多轮能力评测
- related → [[10_Papers/membench|MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents]]：综合记忆评测的不同维度
- related → [[10_Papers/persistbench|PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?]]：选择性遗忘与遗忘边界评测
- related ← [[10_Papers/memorybench|MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems]]：持续学习与增量多轮记忆的不同评测维度

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
