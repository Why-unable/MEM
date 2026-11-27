---
id: "simplemem"
type: "paper"
title: "SimpleMem: Efficient Lifelong Memory for LLM Agents"
year: "2026"
venue: "ICML 2026"
venue_tier: "CCF-A"
category: "system"
authors:
  - "Jiaqi Liu"
  - "Yaofeng Su"
  - "Peng Xia"
  - "Siwei Han"
  - "Zeyu Zheng"
  - "Cihang Xie"
  - "Mingyu Ding"
  - "Huaxiu Yao"
doi: null
arxiv: "2601.02553"
openreview: "https://proceedings.mlr.press/v306/liu26dx.html"
pdf: "https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26dx/liu26dx.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-A"
  - "priority/supporting"
---
# SimpleMem: Efficient Lifelong Memory for LLM Agents

> **一句话定位**：用语义结构化压缩、在线综合和意图感知检索规划，在长期记忆中同时优化准确率与 token 成本。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Jiaqi Liu, Yaofeng Su, Peng Xia, Siwei Han, Zeyu Zheng, Cihang Xie, Mingyu Ding, Huaxiu Yao
- **PDF**：[打开 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26dx/liu26dx.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.mlr.press/v306/liu26dx.html)

## 摘要

To support long-term interaction in complex environments, LLM agents require memory systems that manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which distills unstructured interactions into compact, multi-view indexed memory units; (2) Online Semantic Synthesis, an intra-session process that instantly integrates related context into unified abstract representations to eliminate redundancy; and (3) Intent-Aware Retrieval Planning, which infers search intent to dynamically determine retrieval scope and construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% in LoCoMo while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：用语义结构化压缩、在线综合和意图感知检索规划，在长期记忆中同时优化准确率与 token 成本。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/lightmem|LightMem: Lightweight and Efficient Memory-Augmented Generation]]：高效长期记忆的两条压缩路线
- extends → [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：生产级记忆流水线 → 语义压缩记忆

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
