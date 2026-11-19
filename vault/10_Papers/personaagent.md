---
id: "personaagent"
type: "paper"
title: "PersonaAgent: Bridging Memory and Action for Personalized LLM Agents"
year: "2026"
venue: "ACL Findings 2026"
venue_tier: "ACL-Findings"
category: "personalization"
authors:
  - "Weizhi Zhang"
  - "Xinyang Zhang"
  - "Chenwei Zhang"
  - "Liangwei Yang"
  - "Jingbo Shang"
  - "Zhepei Wei"
  - "Henry Peng Zou"
  - "Zijie Huang"
  - "Zhengyang Wang"
  - "Yifan Gao"
  - "Xiaoman Pan"
  - "Lian Xiong"
  - "Jingguo Liu"
  - "Philip S. Yu"
  - "Xian Li"
doi: "10.18653/v1/2026.findings-acl.1315"
arxiv: "2506.06254"
openreview: "https://openreview.net/forum?id=hOHAyeGYAP"
pdf: "https://aclanthology.org/2026.findings-acl.1315.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/personalization"
  - "tier/ACL-Findings"
  - "priority/supporting"
---
# PersonaAgent: Bridging Memory and Action for Personalized LLM Agents

> **一句话定位**：把记忆与行动耦合，做面向个性化任务的 LLM agent。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Weizhi Zhang, Xinyang Zhang, Chenwei Zhang, Liangwei Yang, Jingbo Shang, Zhepei Wei, Henry Peng Zou, Zijie Huang, Zhengyang Wang, Yifan Gao, Xiaoman Pan, Lian Xiong, Jingguo Liu, Philip S. Yu, Xian Li
- **PDF**：[打开 PDF](https://aclanthology.org/2026.findings-acl.1315.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=hOHAyeGYAP)

## 摘要

Large Language Model (LLM) empowered agents have recently emerged as advanced paradigms that exhibit impressive capabilities in a wide range of domains and tasks. Despite their potential, current LLM agents often adopt a one-size-fits-all approach, lacking the flexibility to respond to users’ varying needs and preferences. This limitation motivates us to develop PersonaAgent, the first personalized LLM agent framework designed to address versatile personalization tasks. Specifically, PersonaAgent integrates two complementary components: a personalized memory module that includes episodic and semantic memory mechanisms; a personalized action module that enables the agent to perform tool actions tailored to the user. At the core, the persona (defined as unique system prompt for each user) functions as an intermediary: it leverages insights from personalized memory to control agent actions, while the outcomes of these actions in turn refine the memory. Based on the framework, we propose a test-time user-preference alignment strategy that simulate the latest n interactions to optimize the persona prompt, ensuring real-time user preference alignment through textual loss feedback between simulated and ground-truth responses. Experimental evaluations demonstrate that PersonaAgent significantly outperforms other baseline methods by not only personalizing the action space effectively but also scaling during test-time real-world applications. These results underscore the feasibility and potential of our approach in delivering tailored, dynamic user experiences.

## 在研究地图中的位置

- **类别**：个性化记忆
- **角色**：把记忆与行动耦合，做面向个性化任务的 LLM agent。
- **优先级**：支撑/扩展

## 关系

- extends → [[10_Papers/evoking|Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval]]：记忆-行动耦合 → 个性化检索

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
