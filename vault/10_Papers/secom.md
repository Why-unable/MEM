---
id: "secom"
type: "paper"
title: "On Memory Construction and Retrieval for Personalized Conversational Agents"
year: "2025"
venue: "ICLR 2025"
venue_tier: "Top-ICLR"
category: "architecture"
authors:
  - "Zhuoshi Pan"
  - "Qianhui Wu"
  - "Huiqiang Jiang"
  - "Xufang Luo"
  - "Hao Cheng"
  - "Dongsheng Li"
  - "Yuqing Yang"
  - "Chin-Yew Lin"
  - "H. Vicky Zhao"
  - "Lili Qiu"
  - "Jianfeng Gao"
doi: null
arxiv: "2502.05589"
openreview: "https://proceedings.iclr.cc/paper_files/paper/2025/hash/e56f394bbd4f0ec81393d767caa5a31b-Abstract-Conference.html"
pdf: "https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# On Memory Construction and Retrieval for Personalized Conversational Agents

> **一句话定位**：以主题连贯的 segment 作为记忆单元，并用 prompt compression 去噪，直接研究记忆粒度对检索的影响。

## 元数据

- **Venue**：ICLR 2025（Top-ICLR）
- **年份**：2025
- **作者**：Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Xufang Luo, Hao Cheng, Dongsheng Li, Yuqing Yang, Chin-Yew Lin, H. Vicky Zhao, Lili Qiu, Jianfeng Gao
- **PDF**：[打开 PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e56f394bbd4f0ec81393d767caa5a31b-Abstract-Conference.html)

## 摘要

To deliver coherent and personalized experiences in long-term conversations, existing approaches typically perform retrieval augmented response generation by constructing memory banks from conversation history at either the turn-level, session-level, or through summarization techniques.In this paper, we present two key findings: (1) The granularity of memory unit matters: turn-level, session-level, and summarization-based methods each exhibit limitations in both memory retrieval accuracy and the semantic quality of the retrieved content. (2) Prompt compression methods, such as LLMLingua-2, can effectively serve as a denoising mechanism, enhancing memory retrieval accuracy across different granularities. Building on these insights, we propose SeCom, a method that constructs the memory bank at segment level by introducing a conversation segmentation model that partitions long-term conversations into topically coherent segments, while applying compression based denoising on memory units to enhance memory retrieval. Experimental results show that SeCom exhibits a significant performance advantage over baselines on long-term conversation benchmarks LOCOMO and Long-MT-Bench+. Additionally, the proposed conversation segmentation method demonstrates superior performance on dialogue segmentation datasets such as DialSeg711, TIAGE, and SuperDialSeg.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：以主题连贯的 segment 作为记忆单元，并用 prompt compression 去噪，直接研究记忆粒度对检索的影响。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]]：segment 级记忆 → 多粒度记忆
- related → [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：记忆粒度选择 vs 原子笔记组织

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
