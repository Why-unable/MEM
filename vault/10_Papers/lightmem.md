---
id: "lightmem"
type: "paper"
title: "LightMem: Lightweight and Efficient Memory-Augmented Generation"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "system"
authors:
  - "Jizhan Fang"
  - "Xinle Deng"
  - "Haoming Xu"
  - "Ziyan Jiang"
  - "Yuqi Tang"
  - "Ziwen Xu"
  - "Shumin Deng"
  - "Yunzhi Yao"
  - "Mengru Wang"
  - "Shuofei Qiao"
  - "Huajun Chen"
  - "Ningyu Zhang"
doi: null
arxiv: "2510.18866"
openreview: "https://proceedings.iclr.cc/paper_files/paper/2026/hash/a05b72653ec5b473732129829ae04195-Abstract-Conference.html"
pdf: "https://proceedings.iclr.cc/paper_files/paper/2026/file/a05b72653ec5b473732129829ae04195-Paper-Conference.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/system"
  - "tier/Top-ICLR"
  - "priority/core"
---
# LightMem: Lightweight and Efficient Memory-Augmented Generation

> **一句话定位**：用 sensory / short-term / long-term 三阶段和 sleep-time update，把记忆压缩与整合移出在线推理，主打低成本长期记忆。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang, Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao, Mengru Wang, Shuofei Qiao, Huajun Chen, Ningyu Zhang
- **PDF**：[打开 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/a05b72653ec5b473732129829ae04195-Paper-Conference.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a05b72653ec5b473732129829ae04195-Abstract-Conference.html)

## 摘要

Despite their remarkable capabilities, Large Language Models (LLMs) struggle to effectively leverage historical interaction information in dynamic and complex environments. Memory systems enable LLMs to move beyond stateless interactions by introducing persistent information storage, retrieval, and utilization mechanisms. However, existing memory systems often introduce substantial time and computational overhead. To this end, we introduce a new memory system called LightMem, which strikes a balance between the performance and efficiency of memory systems. Inspired by the Atkinson-Shiffrin model of human memory, LightMem organizes memory into three complementary stages. First, cognition-inspired sensory memory rapidly filters irrelevant information through lightweight compression and groups information according to their topics. Next, topic-aware short-term memory consolidates these topic-based groups, organizing and summarizing content for more structured access. Finally, long-term memory with sleep-time update employs an offline procedure that decouples consolidation from online inference. On LongMemEval and LoCoMo, using GPT and Qwen backbones, LightMem consistently surpasses strong baselines, improving QA accuracy by up to 7.7% / 29.3%, reducing total token usage by up to 38x / 20.9x and API calls by up to 30x / 55.5x, while purely online test-time costs are even lower, achieving up to 106x / 117x token reduction and 159x / 310x fewer API calls. The code is available at https://github.com/zjunlp/LightMem.

## 在研究地图中的位置

- **类别**：系统与效率
- **角色**：用 sensory / short-term / long-term 三阶段和 sleep-time update，把记忆压缩与整合移出在线推理，主打低成本长期记忆。
- **优先级**：核心

## 关系

- extends → [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：生产级记忆流水线 → 轻量级记忆系统
- related → [[10_Papers/hippocampus|Hippocampus: An Efficient and Scalable Memory Module for Agentic AI]]：高效记忆模块的不同系统路线
- related → [[10_Papers/lightwm|LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents]]：低成本长期记忆 vs 小模型工作记忆
- related ← [[10_Papers/simplemem|SimpleMem: Efficient Lifelong Memory for LLM Agents]]：高效长期记忆的两条压缩路线
- related ← [[10_Papers/lightmem-slm|Lightweight LLM Agent Memory with Small Language Models]]：两个同名 LightMem 系统，机制不同，引用时需区分

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
