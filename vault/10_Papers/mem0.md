---
id: "mem0"
type: "paper"
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
year: "2025"
venue: "ECAI 2025"
venue_tier: "CCF-B"
category: "system"
authors:
  - "Prateek Chhikara"
  - "Dev Khant"
  - "Saket Aryan"
  - "Taranjeet Singh"
  - "Deshraj Yadav"
doi: "10.48550/arXiv.2504.19413"
arxiv: "2504.19413"
openreview: "https://openreview.net/forum?id=0wxfikDcOa"
pdf: "https://openreview.net/pdf?id=0wxfikDcOa"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-B"
  - "priority/supporting"
---
# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

> **一句话定位**：工业级可扩展长期记忆，强调生产部署中的记忆抽取、更新与检索流水线。

## 元数据

- **Venue**：ECAI 2025（CCF-B）
- **年份**：2025
- **作者**：Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=0wxfikDcOa)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=0wxfikDcOa)

## 摘要

Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements. Through comprehensive evaluations on the LOCOMO benchmark, we systematically compare our approaches against six baseline categories. Empirical results demonstrate that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base Mem0 configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to the full-context approach. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, thereby offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight the critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents. Code: https://mem0.ai/research.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：工业级可扩展长期记忆，强调生产部署中的记忆抽取、更新与检索流水线。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/hippocampus|Hippocampus: An Efficient and Scalable Memory Module for Agentic AI]]：长期记忆系统 → 高效记忆模块
- extends → [[10_Papers/tiermem|TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory]]：记忆压缩与证据保留
- risk → [[10_Papers/privacy|Unveiling Privacy Risks in LLM Agent Memory]]：长期记忆的隐私面
- risk → [[10_Papers/injection|Memory Injection Attacks on LLM Agents via Query-Only Interaction]]：长期记忆的注入面
- extends ← [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：研究原型 → 生产级记忆流水线
- applies ← [[10_Papers/memrec|MemRec: Collaborative Memory-Augmented Agentic Recommender System]]：长期记忆用于推荐
- extends ← [[10_Papers/lightmem|LightMem: Lightweight and Efficient Memory-Augmented Generation]]：生产级记忆流水线 → 轻量级记忆系统
- extends ← [[10_Papers/simplemem|SimpleMem: Efficient Lifelong Memory for LLM Agents]]：生产级记忆流水线 → 语义压缩记忆
- related ← [[10_Papers/lightmem-slm|Lightweight LLM Agent Memory with Small Language Models]]：SLM 驱动记忆 vs 生产级 LLM 记忆
- extends ← [[10_Papers/vikingmem|VikingMem: A Memory Base Management System for Stateful LLM-Based Applications]]：生产级记忆流水线 → Memory Base 管理系统

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
