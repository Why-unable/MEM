---
id: "privacy"
type: "paper"
title: "Unveiling Privacy Risks in LLM Agent Memory"
year: "2025"
venue: "ACL 2025"
venue_tier: "CCF-A"
category: "safety"
authors:
  - "Bo Wang"
  - "Weiyi He"
  - "Shenglai Zeng"
  - "Zhen Xiang"
  - "Yue Xing"
  - "Jiliang Tang"
  - "Pengfei He"
doi: "10.48550/arXiv.2502.13172"
arxiv: "2502.13172"
openreview: "https://openreview.net/forum?id=GZWGC1fDnc"
pdf: "https://aclanthology.org/2025.acl-long.1227.pdf"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/safety"
  - "tier/CCF-A"
  - "priority/core"
---
# Unveiling Privacy Risks in LLM Agent Memory

> **一句话定位**：记忆隐私抽取攻击，揭示长期记忆中的敏感信息泄露面。

## 元数据

- **Venue**：ACL 2025（CCF-A）
- **年份**：2025
- **作者**：Bo Wang, Weiyi He, Shenglai Zeng, Zhen Xiang, Yue Xing, Jiliang Tang, Pengfei He
- **PDF**：[打开 PDF](https://aclanthology.org/2025.acl-long.1227.pdf)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=GZWGC1fDnc)

## 摘要

Large Language Model (LLM) agents have become increasingly prevalent across various real-world applications. They enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks for LLM agents. In this work, we systematically investigate the vulnerability of LLM agents to our proposed Memory EXTRaction Attack (MEXTRA) under a black-box setting. To extract private information from memory, we propose an effective attacking prompt design and an automated prompt generation method based on different levels of knowledge about the LLM agent. Experiments on two representative agents demonstrate the effectiveness of MEXTRA. Moreover, we explore key factors influencing memory leakage from both the agent designer’s and the attacker’s perspectives. Our findings highlight the urgent need for effective memory safeguards in LLM agent design and deployment.

## 在研究地图中的位置

- **类别**：安全与隐私
- **角色**：记忆隐私抽取攻击，揭示长期记忆中的敏感信息泄露面。
- **优先级**：核心

## 关系

- related → [[10_Papers/injection|Memory Injection Attacks on LLM Agents via Query-Only Interaction]]：隐私抽取与记忆注入的攻击面对照
- risk ← [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]]：长期记忆的隐私面

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
