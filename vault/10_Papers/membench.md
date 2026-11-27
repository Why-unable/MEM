---
id: "membench"
type: "paper"
title: "MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents"
year: "2025"
venue: "ACL Findings 2025"
venue_tier: "ACL-Findings"
category: "evaluation"
authors:
  - "Haoran Tan"
  - "Zeyu Zhang"
  - "Chen Ma"
  - "Xu Chen"
  - "Quanyu Dai"
  - "Zhenhua Dong"
doi: "10.48550/arXiv.2506.21605"
arxiv: "2506.21605"
openreview: "https://openreview.net/forum?id=XOJ5SQe6X0"
pdf: "https://aclanthology.org/2025.findings-acl.989.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/evaluation"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents

> **一句话定位**：LLM-based agent 记忆的综合评测，覆盖多种记忆能力。

## 元数据

- **Venue**：ACL Findings 2025（ACL-Findings）
- **年份**：2025
- **作者**：Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, Zhenhua Dong
- **PDF**：[打开 PDF](https://aclanthology.org/2025.findings-acl.989.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=XOJ5SQe6X0)

## 摘要

Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly limited by the diversity of memory levels and interactive scenarios. They also lack comprehensive metrics to reflect the memory capabilities from multiple aspects. To address these problems, in this paper, we construct a more comprehensive dataset and benchmark to evaluate the memory capability of LLM-based agents. Our dataset incorporates factual memory and reflective memory as different levels, and proposes participation and observation as various interactive scenarios. Based on our dataset, we present a benchmark, named MemBench, to evaluate the memory capability of LLM-based agents from multiple aspects, including their effectiveness, efficiency, and capacity. To benefit the research community, we release our dataset and project at https://github.com/import-myself/Membench.

## 在研究地图中的位置

- **类别**：评测与基准
- **角色**：LLM-based agent 记忆的综合评测，覆盖多种记忆能力。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/minerva|Minerva: A Programmable Memory Test Benchmark for Language Models]]：综合评测 vs 可编程测试
- evaluated-by → [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：agent memory 综合评测参照
- related ← [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：长期交互 → 综合记忆评测
- related ← [[10_Papers/memoryagentbench|Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions]]：综合记忆评测的不同维度

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
