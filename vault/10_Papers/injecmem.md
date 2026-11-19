---
id: "injecmem"
type: "paper"
title: "InjecMEM: Memory Injection Attack on LLM Agent Memory Systems"
year: "2026"
venue: "COLM 2026"
venue_tier: "Top-COLM"
category: "safety"
authors:
  - "Hanling Tian"
  - "Gengyu Zhang"
  - "Zeyang Sha"
  - "Jingying Wang"
  - "Yuhang Liu"
  - "Zhehao Huang"
  - "Kun Yang"
  - "Xiaolin Huang"
doi: "10.48550/arXiv.2608.23471"
arxiv: "2608.23471"
openreview: "https://openreview.net/forum?id=VbXN1Ny912"
pdf: "https://openreview.net/pdf?id=VbXN1Ny912"
status: "published"
tags:
  - "paper"
  - "topic/Agent-Memory-2025"
  - "category/safety"
  - "tier/Top-COLM"
  - "priority/core"
---
# InjecMEM: Memory Injection Attack on LLM Agent Memory Systems

> **一句话定位**：把注入攻击扩展到记忆系统的写入/检索链路，攻击面更系统。

## 元数据

- **Venue**：COLM 2026（Top-COLM）
- **年份**：2026
- **作者**：Hanling Tian, Gengyu Zhang, Zeyang Sha, Jingying Wang, Yuhang Liu, Zhehao Huang, Kun Yang, Xiaolin Huang
- **PDF**：[打开 PDF](https://openreview.net/pdf?id=VbXN1Ny912)
- **OpenReview / Proceedings**：[查看记录](https://openreview.net/forum?id=VbXN1Ny912)

## 摘要

Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose **InjecMEM**, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, we craft the injection with a *retriever-agnostic anchor* and an *adversarial command*. The anchor contains high-recall topical cues so that downstream retrieval consistently associates the record with the target topic. The command is a short sequence optimized to remain effective under uncertain fused contexts, variable placements, and long prompts so that it reliably steers outputs once retrieved. We learn the command via gradient-based coordinate search, averaging over synthetic prompt templates and insertion positions, and extend it to joint optimization across backbones to study transfer. Evaluated across multiple memory systems and backbone models, InjecMEM achieves reliable topic-conditioned retrieval and targeted generation, remains effective under memory drift, and leaves non-target queries unaffected. Our results underscore the need to harden memory systems and provide a reproducible framework for studying agent memory.

## 在研究地图中的位置

- **类别**：安全与隐私
- **角色**：把注入攻击扩展到记忆系统的写入/检索链路，攻击面更系统。
- **优先级**：核心

## 关系

- extends → [[10_Papers/poisononce|Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents]]：注入 → 长期记忆 poisoning
- extends ← [[10_Papers/injection|Memory Injection Attacks on LLM Agents via Query-Only Interaction]]：查询注入 → 记忆系统注入

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
