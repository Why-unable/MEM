---
id: "evoking"
type: "paper"
title: "Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "personalization"
authors:
  - "Yingyi Zhang"
  - "Junyi Li"
  - "Wenlin Zhang"
  - "Pengyue Jia"
  - "Xianneng Li"
  - "Yichao Wang"
  - "Derong Xu"
  - "Yi Wen"
  - "Huifeng Guo"
  - "Yong Liu"
  - "Xiangyu Zhao"
doi: "10.48550/arXiv.2603.09250"
arxiv: "2603.09250"
openreview: "https://openreview.net/forum?id=f7p0F2X6XN"
pdf: "https://openreview.net/pdf?id=f7p0F2X6XN"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/personalization"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval

> **一句话定位**：基于回忆—熟悉度的自适应检索，把个性化记忆从“存什么”推进到“如何取”。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Yingyi Zhang, Junyi Li, Wenlin Zhang, Pengyue Jia, Xianneng Li, Yichao Wang, Derong Xu, Yi Wen, Huifeng Guo, Yong Liu, Xiangyu Zhao
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=f7p0F2X6XN)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=f7p0F2X6XN)

## 摘要

Personalized large language models (LLMs) rely on memory retrieval to incorporate user-specific histories, preferences, and contexts. Existing approaches either overload the LLM by feeding all the user's past memory into the prompt, which is costly and unscalable, or simplify retrieval into a one-shot similarity search, which captures only surface matches. Cognitive science, however, shows that human memory operates through a dual process: Familiarity, offering fast but coarse recognition, and Recollection, enabling deliberate, chain-like reconstruction for deeply recovering episodic content.
Current systems lack both the ability to perform recollection retrieval and mechanisms to adaptively switch between the dual retrieval paths, leading to either insufficient recall or the inclusion of noise.
To address this, we propose RF-Mem (Recollection–Familiarity Memory Retrieval), a familiarity uncertainty-guided dual-path memory retriever.
RF-Mem measures the familiarity signal through the mean score and entropy. High familiarity leads to the direct top-$K$ Familiarity retrieval path, while low familiarity activates the Recollection path. In the Recollection path, the system clusters candidate memories and applies $\alpha$-mix with the query to iteratively expand evidence in embedding space, simulating deliberate contextual reconstruction.
This design embeds human-like dual-process recognition into the retriever, avoiding full-context overhead and enabling scalable, adaptive personalization. Experiments across three benchmarks and corpus scales demonstrate that RF-Mem consistently outperforms both one-shot retrieval and full-context reasoning under fixed budget and latency constraints.
Our code can be found in the Reproducibility Statement.

## 在研究地图中的位置

- **类别**：个性化记忆
- **角色**：基于回忆—熟悉度的自适应检索，把个性化记忆从“存什么”推进到“如何取”。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]]：个性化检索 → 长期交互评测
- extends ← [[10_Papers/personaagent|PersonaAgent: Bridging Memory and Action for Personalized LLM Agents]]：记忆-行动耦合 → 个性化检索

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
