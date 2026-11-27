---
id: "memorybench"
type: "paper"
title: "MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "evaluation"
authors:
  - "Qingyao Ai"
  - "Yichen Tang"
  - "Changyue Wang"
  - "Jianming Long"
  - "Weihang Su"
  - "Yiqun Liu"
doi: null
arxiv: "2510.17281"
openreview: "https://proceedings.mlr.press/v306/ai26e.html"
pdf: "https://raw.githubusercontent.com/mlresearch/v306/main/assets/ai26e/ai26e.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/CCF-A"
  - "priority/supporting"
---
# MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems

> **一句话定位**：用用户反馈模拟框架评测 LLM 系统的持续学习与记忆能力，覆盖多领域、多语言和多任务类型。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Qingyao Ai, Yichen Tang, Changyue Wang, Jianming Long, Weihang Su, Yiqun Liu
- **PDF**：[打开 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ai26e/ai26e.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.mlr.press/v306/ai26e.html)

## 摘要

Scaling up data, parameters, and test-time computation has been the mainstream methods to improve LLM systems (LLMsys), but their upper bounds are almost reached due to the gradual depletion of high-quality data and marginal gains obtained from larger computational resource consumption. Inspired by the abilities of human and traditional AI systems in learning from practice, constructing memory and continual learning frameworks for LLMsys has become an important and popular research direction in recent literature. Yet, existing benchmarks for LLM memory often focus on evaluating the system on homogeneous reading comprehension tasks with long-form inputs rather than testing their abilities to learn from accumulated user feedback in service time. Therefore, we propose a user feedback simulation framework and a comprehensive benchmark covering multiple domains, languages, and types of tasks to evaluate the continual learning abilities of LLMsys. Experiments show that the effectiveness and efficiency of state-of-the-art baselines are far from satisfying, and we hope this benchmark could pave the way for future studies on LLM memory and optimization algorithms. Website: https://memorybench.thuir.cn Code: https://github.com/THUIR/MemoryBench Data: https://huggingface.co/datasets/THUIR/MemoryBench Data-Full: https://huggingface.co/datasets/THUIR/MemoryBench-Full

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：用用户反馈模拟框架评测 LLM 系统的持续学习与记忆能力，覆盖多领域、多语言和多任务类型。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：静态记忆 QA → 用户反馈驱动的持续学习评测
- related → [[10_Papers/memoryagentbench|Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions]]：持续学习与增量多轮记忆的不同评测维度

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
