---
id: "lightwm"
type: "paper"
title: "LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "system"
authors:
  - "Ziyi Wang"
  - "Haonan Jin"
  - "Zian Wang"
  - "Wendong Wang"
  - "Lanshan Zhang"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=WLnpZpShzr"
pdf: "https://openreview.net/pdf?id=WLnpZpShzr"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-A"
  - "priority/supporting"
---
# LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents

> **一句话定位**：面向小模型 agent 的免训练层次工作记忆，强调低成本与可部署性。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Ziyi Wang, Haonan Jin, Zian Wang, Wendong Wang, Lanshan Zhang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=WLnpZpShzr)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=WLnpZpShzr)

## 摘要

Small language models (SLMs) are attractive for low-cost agent deployment, and their growing capabilities make them promising for procedure-centric workloads that repeatedly execute specialized task families with similar workflows.
However, SLM agents still struggle in long-horizon interaction because limited context budgets make it difficult to reliably retain and reuse decision-relevant state across many steps.
Existing working-memory methods attempt to mitigate context growth, but their reliance on unstructured natural-language summarization can discard critical facts, introduce state drift, and compound errors in SLM execution.
We present LightWM, a training-free hierarchical working-memory framework that decomposes procedure-centric tasks into subgoals and organizes memory into task-level global memory and subtask-level local memory, where local memory directly conditions SLM action selection and is updated from new observations through structured updates.
To instantiate such memories without training, a one-time offline LLM-based induction pipeline builds reusable schemas per task family from a few successful traces, requiring no SLM parameter updates or online LLM calls.
On ALFWorld valid_unseen, Qwen3-4B reaches 0.910 success, whereas representative prompting and prior working-memory baselines under the same setting remain below 0.320.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：面向小模型 agent 的免训练层次工作记忆，强调低成本与可部署性。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/ema|EMA: An Episodic Memory Agent for Efficient and Selective Memory]]：小模型工作记忆 vs 事件记忆
- related ← [[10_Papers/lightmem|LightMem: Lightweight and Efficient Memory-Augmented Generation]]：低成本长期记忆 vs 小模型工作记忆

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
