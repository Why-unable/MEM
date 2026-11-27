---
id: "lightmem-slm"
type: "paper"
title: "Lightweight LLM Agent Memory with Small Language Models"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "system"
authors:
  - "Jiaquan Zhang"
  - "Chaoning Zhang"
  - "Shuxu Chen"
  - "Zhenzhen Huang"
  - "Pengcheng Zheng"
  - "Zhicheng Wang"
  - "Ping Guo"
  - "Fan Mo"
  - "Sung-Ho Bae"
  - "Jie Zou"
  - "Jiwei Wei"
  - "Yang Yang"
doi: "10.18653/v1/2026.acl-long.588"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2026.acl-long.588"
pdf: "https://aclanthology.org/2026.acl-long.588.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-A"
  - "priority/supporting"
---
# Lightweight LLM Agent Memory with Small Language Models

> **一句话定位**：用 Small Language Models 驱动记忆检索、写入和离线整合，分离 online 与 offline 处理，强调低延迟和固定检索预算。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Zhenzhen Huang, Pengcheng Zheng, Zhicheng Wang, Ping Guo, Fan Mo, Sung-Ho Bae, Jie Zou, Jiwei Wei, Yang Yang
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.588.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2026.acl-long.588)

## 摘要

Although LLM agents can leverage tools for complex tasks, they still need memory to maintain cross-turn consistency and accumulate reusable information in long-horizon interactions. However, retrieval-based external memory systems incur low online overhead but suffer from unstable accuracy due to limited query construction and candidate filtering. In contrast, many systems use repeated large-model calls for online memory operations, improving accuracy but accumulating latency over long interactions. We propose LightMem, a lightweight memory system for better agent memory driven by Small Language Models (SLMs). LightMem modularizes memory retrieval, writing, and long-term consolidation, and separates online processing from offline consolidation to enable efficient memory invocation under bounded compute. We organize memory into short-term memory (STM) for immediate conversational context, mid-term memory (MTM) for reusable interaction summaries, and long-term memory (LTM) for consolidated knowledge, and uses user identifiers to support independent retrieval and incremental maintenance in multi-user settings. Online, LightMem operates under a fixed retrieval budget and selects memories via a two-stage procedure: vector-based coarse retrieval followed by semantic consistency re-ranking. Offline, it abstracts reusable interaction evidence and incrementally integrates it into LTM. Experiments show consistent gains across model scales, with an average F1 improvement of about 2.5 over A-MEM on LoCoMo, while achieving higher efficiency and low median latency (83 ms for retrieval and 581 ms end-to-end).

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：用 Small Language Models 驱动记忆检索、写入和离线整合，分离 online 与 offline 处理，强调低延迟和固定检索预算。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/lightmem|LightMem: Lightweight and Efficient Memory-Augmented Generation]]：两个同名 LightMem 系统，机制不同，引用时需区分
- related → [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：SLM 驱动记忆 vs 生产级 LLM 记忆

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
