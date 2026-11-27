---
id: "gam"
type: "paper"
title: "GAM: Hierarchical Graph-based Agentic Memory for LLM Agents"
year: "2026"
venue: "ACL 2026"
venue_tier: "CCF-A"
category: "architecture"
authors:
  - "Zhaofen Wu"
  - "Hanrong Zhang"
  - "Fulin Lin"
  - "Wujiang Xu"
  - "Xinran Xu"
  - "Yankai Chen"
  - "Henry Peng Zou"
  - "Shaowen Chen"
  - "Weizhi Zhang"
  - "Xue Liu"
  - "Philip S. Yu"
  - "Hongwei Wang"
doi: "10.18653/v1/2026.acl-long.1600"
arxiv: null
openreview: "https://doi.org/10.18653/v1/2026.acl-long.1600"
pdf: "https://aclanthology.org/2026.acl-long.1600.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/architecture"
  - "tier/CCF-A"
  - "priority/supporting"
---
# GAM: Hierarchical Graph-based Agentic Memory for LLM Agents

> **一句话定位**：用事件进展图 + 主题关联网络解耦记忆编码与整合，降低瞬态噪声对长期知识结构的干扰。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Zhaofen Wu, Hanrong Zhang, Fulin Lin, Wujiang Xu, Xinran Xu, Yankai Chen, Henry Peng Zou, Shaowen Chen, Weizhi Zhang, Xue Liu, Philip S. Yu, Hongwei Wang
- **PDF**：[打开 PDF](https://aclanthology.org/2026.acl-long.1600.pdf)
- **OpenReview / Proceedings**：[查看记录](https://doi.org/10.18653/v1/2026.acl-long.1600)

## 摘要

To sustain coherent long-term interactions, Large Language Model (LLM) agents must navigate the tension between acquiring new information and retaining prior knowledge. Current unified stream-based memory systems facilitate context updates but remain vulnerable to interference from transient noise. Conversely, discrete structured memory architectures provide robust knowledge retention but often struggle to adapt to fluid narrative evolution. To address this, we propose GAM, a hierarchical Graph-based Agentic Memory framework that explicitly decouples memory encoding from consolidation to effectively resolve the conflict between rapid context perception and stable knowledge retention. By isolating ongoing dialogue in a event progression graph and integrating it into a topic associative network only upon semantic shifts, our approach minimizes interference while preserving long-term consistency. Additionally, we introduce a Graph-guided, Multi-factor Retrieval strategy to enhance context precision. Experiments on LoCoMo and LongDialQA benchmarks indicate that our method consistently outperforms state-of-the-art baselines in both reasoning accuracy and computational efficiency.

## 在研究地图中的位置

- **类别**：记忆架构
- **角色**：用事件进展图 + 主题关联网络解耦记忆编码与整合，降低瞬态噪声对长期知识结构的干扰。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]]：原子笔记 → 分层事件/主题图记忆
- related → [[10_Papers/magma|MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents]]：层次图 vs 多关系图
- related ← [[10_Papers/emem|E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory]]：E-mem 在 LoCoMo 上以 GAM 为强基线

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
