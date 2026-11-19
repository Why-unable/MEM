---
id: "poisononce"
type: "paper"
title: "Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents"
year: "2026"
venue: "COLM 2026"
venue_tier: "Top-COLM"
category: "safety"
authors:
  - "Mingwen Dong"
  - "Wei Zou"
  - "Miguel Romero Calvo"
  - "Shuaichen Chang"
  - "Jiang Guo"
  - "Dongkyu Lee"
  - "Xing Niu"
  - "Xiaofei Ma"
  - "Yanjun Qi"
  - "Jiarong Jiang"
doi: null
arxiv: null
openreview: "https://openreview.net/forum?id=sfUpgUKF2Y"
pdf: "https://openreview.net/pdf?id=sfUpgUKF2Y"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/safety"
  - "tier/Top-COLM"
  - "priority/core"
---
# Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents

> **一句话定位**：环境注入的记忆 poisoning：一次污染可被长期利用，面向 Web agent。

## 元数据

- **Venue**：COLM 2026（Top-COLM）
- **年份**：2026
- **作者**：Mingwen Dong, Wei Zou, Miguel Romero Calvo, Shuaichen Chang, Jiang Guo, Dongkyu Lee, Xing Niu, Xiaofei Ma, Yanjun Qi, Jiarong Jiang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=sfUpgUKF2Y)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=sfUpgUKF2Y)

## 摘要

Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions. While existing security research on memory assumes attackers can directly inject into memory storage or exploit shared memory across users, we present a more realistic threat model: contamination through environmental observation alone. We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access. A single contaminated observation (e.g., viewing a manipulated product page) silently poisons an agent's memory and activates during future tasks on different websites, bypassing permission-based defenses. Our experiments on (Visual)WebArena reveal two key findings. First, eTAMP achieves substantial attack success rates: up to 32.5\% on GPT-5-mini, 23.4\% on GPT-5.2, and 19.5\% on GPT-OSS-120B. Second, we discover Frustration Exploitation: agents under environmental stress become dramatically more susceptible, with ASR increasing up to 9 times when agents struggle with dropped clicks or garbled text.  Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance. As LLM-based agents increasingly interact with untrusted
web environments, our findings underscore the need for defenses against environment-injected memory poisoning.

## 在研究地图中的位置

- **类别**：安全与隐私
- **角色**：环境注入的记忆 poisoning：一次污染可被长期利用，面向 Web agent。
- **优先级**：核心

## 关系

- extends ← [[10_Papers/injecmem|InjecMEM: Memory Injection Attack on LLM Agent Memory Systems]]：注入 → 长期记忆 poisoning

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
