---
id: "reasoningbank"
type: "paper"
title: "ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory"
year: "2026"
venue: "ICLR 2026"
venue_tier: "Top-ICLR"
category: "procedural"
authors:
  - "Siru Ouyang"
  - "Jun Yan"
  - "I-Hung Hsu"
  - "Yanfei Chen"
  - "Ke Jiang"
  - "Zifeng Wang"
  - "Rujun Han"
  - "Long T. Le"
  - "Samira Daruki"
  - "Xiangru Tang"
  - "Vishy Tirumalashetty"
  - "George Lee"
  - "Mahsan Rofouei"
  - "Hangfei Lin"
  - "Jiawei Han"
  - "Chen-Yu Lee"
  - "Tomas Pfister"
doi: null
arxiv: "2509.25140"
openreview: "https://proceedings.iclr.cc/paper_files/paper/2026/hash/980ea04d23d1f6908964eba2a74afe45-Abstract-Conference.html"
pdf: "https://proceedings.iclr.cc/paper_files/paper/2026/file/980ea04d23d1f6908964eba2a74afe45-Paper-Conference.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/procedural"
  - "tier/Top-ICLR"
  - "priority/supporting"
---
# ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

> **一句话定位**：从成功与失败经验中蒸馏可泛化的推理策略，把记忆从“存轨迹”推进到“存可复用推理模式”。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, Tomas Pfister
- **PDF**：[打开 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/980ea04d23d1f6908964eba2a74afe45-Paper-Conference.pdf)
- **OpenReview / Proceedings**：[查看记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/980ea04d23d1f6908964eba2a74afe45-Abstract-Conference.html)

## 摘要

With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arise. Our code can be found at https://github.com/google-research/reasoning-bank.

## 在研究地图中的位置

- **类别**：程序性记忆
- **角色**：从成功与失败经验中蒸馏可泛化的推理策略，把记忆从“存轨迹”推进到“存可复用推理模式”。
- **优先级**：支撑/扩展

## 关系

- related → [[10_Papers/rememberrefine|Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution]]：程序性记忆与经验蒸馏
- related → [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]]：经验驱动的记忆进化
- related ← [[10_Papers/storagetexperience|From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms]]：Experience 阶段的跨轨迹抽象

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
