---
id: "multimodal"
type: "paper"
title: "Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "multimodal"
authors:
  - "Lin Long"
  - "Yichen He"
  - "Wentao Ye"
  - "Yiyuan Pan"
  - "Yuan Lin"
  - "Hang Li"
  - "Junbo Zhao"
  - "Wei Li"
doi: "10.48550/arXiv.2508.09736"
arxiv: "2508.09736"
openreview: "https://openreview.net/forum?id=PMz29A7Muq"
pdf: "https://openreview.net/pdf?id=PMz29A7Muq"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/multimodal"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory

> **一句话定位**：多模态长期记忆 agent，连接视觉、听觉与文本经验。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, Wei Li
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=PMz29A7Muq)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=PMz29A7Muq)

## 摘要

We introduce M3-Agent, a novel multimodal agent framework equipped with long-term memory. Like humans, M3-Agent can process real-time visual and auditory inputs to build and update episodic and semantic memories, gradually accumulating world knowledge. Its memory is organized in an entity-centric, multimodal manner, enabling deeper and more consistent understanding of the environment. Given an instruction, M3-Agent autonomously performs multi-turn reasoning and retrieves relevant memories to complete tasks. To evaluate memory effectiveness and memory-based reasoning in multimodal agents, we develop M3-Bench, a long-video question answering benchmark comprising 100 newly recorded robot-perspective videos (M3-Bench-robot) and 920 diverse web-sourced videos (M3-Bench-web). We annotate QA pairs designed to test capabilities essential for agent applications, such as person understanding, general knowledge extraction, and cross-modal reasoning. Experimental results show that M3-Agent, trained via reinforcement learning, outperforms the strongest baseline, a prompting agent using Gemini-1.5-pro and GPT-4o, achieving 6.7%, 7.7%, and 5.3% higher accuracy on M3-Bench-robot, M3-Bench-web and VideoMME-long, respectively. Our work advances multimodal agents toward more human-like long-term memory and provides insights for their practical design. Models, datasets and code are available at https://github.com/ByteDance-Seed/m3-agent.

## 在研究地图中的位置

- **类别**：多模态记忆
- **角色**：多模态长期记忆 agent，连接视觉、听觉与文本经验。
- **优先级**：支撑/扩展

## 关系

- extends ← [[10_Papers/remem|REMem: Reasoning with Episodic Memory in Language Agent]]：文本事件 → 多模态经验

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
