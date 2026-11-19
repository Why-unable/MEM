---
id: "injection"
type: "paper"
title: "Memory Injection Attacks on LLM Agents via Query-Only Interaction"
year: "2025"
venue: "NeurIPS 2025"
venue_tier: "CCF-A"
category: "safety"
authors:
  - "Shen Dong"
  - "Shaochen Xu"
  - "Pengfei He"
  - "Yige Li"
  - "Jiliang Tang"
  - "Tianming Liu"
  - "Hui Liu"
  - "Zhen Xiang"
doi: "10.52202/085713-1554"
arxiv: "2503.03704"
openreview: "https://openreview.net/forum?id=QINnsnppv8"
pdf: "https://openreview.net/pdf?id=QINnsnppv8"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/safety"
  - "tier/CCF-A"
  - "priority/core"
---
# Memory Injection Attacks on LLM Agents via Query-Only Interaction

> **一句话定位**：query-only 记忆注入攻击，说明只通过查询交互也能污染 agent 记忆。

## 元数据

- **Venue**：NeurIPS 2025（CCF-A）
- **年份**：2025
- **作者**：Shen Dong, Shaochen Xu, Pengfei He, Yige Li, Jiliang Tang, Tianming Liu, Hui Liu, Zhen Xiang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=QINnsnppv8)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=QINnsnppv8)

## 摘要

Agents powered by large language models (LLMs) have demonstrated strong capabilities in a wide range of complex, real-world applications.
However, LLM agents with a compromised memory bank may easily produce harmful outputs when the past records retrieved for demonstration are malicious.
In this paper, we propose a novel Memory INJection Attack, MINJA, without assuming that the attacker can directly modify the memory bank of the agent.
The attacker injects malicious records into the memory bank by only **interacting with the agent via queries and output observations**.
These malicious records are designed to elicit a sequence of malicious reasoning steps corresponding to a different target query during the agent's execution of the victim user's query.
Specifically, we introduce a sequence of *bridging steps* to link victim queries to the malicious reasoning steps.
During the memory injection, we propose an *indication prompt* that guides the agent to autonomously generate similar bridging steps, with a *progressive shortening strategy* that gradually removes the indication prompt, such that the malicious record will be easily retrieved when processing later victim queries.
Our extensive experiments across diverse agents demonstrate the effectiveness of MINJA in compromising agent memory.
With minimal requirements for execution, MINJA enables any user to influence agent memory, highlighting the risk.

## 在研究地图中的位置

- **类别**：安全与隐私
- **角色**：query-only 记忆注入攻击，说明只通过查询交互也能污染 agent 记忆。
- **优先级**：核心

## 关系

- extends → [[10_Papers/injecmem|InjecMEM: Memory Injection Attack on LLM Agent Memory Systems]]：查询注入 → 记忆系统注入
- risk ← [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：长期记忆的注入面
- related ← [[10_Papers/privacy|Unveiling Privacy Risks in LLM Agent Memory]]：隐私抽取与记忆注入的攻击面对照

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
