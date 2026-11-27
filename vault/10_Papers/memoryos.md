---
id: "memoryos"
type: "paper"
title: "Memory OS of AI Agent"
year: "2025"
venue: "EMNLP 2025"
venue_tier: "CCF-B"
category: "system"
authors:
  - "Jiazheng Kang"
  - "Mingming Ji"
  - "Zhe Zhao"
  - "Ting Bai"
doi: "10.18653/v1/2025.emnlp-main.1318"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2025.emnlp-main.1318"
pdf: "https://aclanthology.org/2025.emnlp-main.1318.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/CCF-B"
  - "priority/supporting"
---
# Memory OS of AI Agent

> **一句话定位**：把操作系统式的分层存储、更新和检索引入 agent memory，建立 short / mid / long-term 三级记忆。

## 元数据

- **Venue**：EMNLP 2025（CCF-B）
- **年份**：2025
- **作者**：Jiazheng Kang, Mingming Ji, Zhe Zhao, Ting Bai
- **PDF**：[打开 PDF](https://aclanthology.org/2025.emnlp-main.1318.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2025.emnlp-main.1318)

## 摘要

Large Language Models (LLMs) face a crucial challenge from fixed context windows and inadequate memory management, leading to a severe shortage of long-term memory capabilities and limited personalization in the interactive experience with AI agents. To overcome this challenge, we innovatively propose a Memory Operating System, i.e., MemoryOS, to achieve comprehensive and efficient memory management for AI agents. Inspired by the memory management principles in operating systems, MemoryOS designs a hierarchical storage architecture and consists of four key modules: memory Storage, Updating, Retrieval, and Generation. Specifically, the architecture comprises three levels of storage units: short-term memory, mid-term memory, and long-term personal memory. Key operations within MemoryOS include dynamic updates between storage units: short-term to mid-term updates follow a dialogue-chain-based FIFO principle, while mid-term to long-term updates use a segmented page organization strategy. Our pioneering MemoryOS enables hierarchical memory integration and dynamic updating. Extensive experiments on the LoCoMo benchmark show an average improvement of 48.36% on F1 and 46.18% on BLEU-1 over the baselines on GPT-4o-mini, showing contextual coherence and personalized memory retention in long conversations.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：把操作系统式的分层存储、更新和检索引入 agent memory，建立 short / mid / long-term 三级记忆。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/magma|MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents]]：三级层次存储 vs 多关系图记忆
- related → [[10_Papers/reconstructed|Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents]]：层次记忆系统作为主动重建的对照
- extends ← [[10_Papers/evermemos|EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning]]：分层 memory OS → 自组织 memory OS
- related ← [[10_Papers/vikingmem|VikingMem: A Memory Base Management System for Stateful LLM-Based Applications]]：Memory Base vs 分层 memory OS

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
