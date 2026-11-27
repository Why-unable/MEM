---
type: evidence
paper_id: "memoryr1"
title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "B"
tags:
  - evidence
  - mainline-b
---

# Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe Bi, Kristian Kersting, Jeff Z. Pan, Hinrich Schütze, Volker Tresp, Yunpu Ma
- **DOI**：10.48550/arXiv.2508.19828
- **arXiv**：2508.19828
- **PDF**：https://aclanthology.org/2026.acl-long.583.pdf
- **正式记录**：https://openreview.net/forum?id=inJIfKNFuE
- **主库角色**：用强化学习训练记忆管理与使用策略，把记忆操作从 prompt 工程推进为可学习策略。

## 官方摘要

Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLMs with an external memory bank, yet most existing pipelines are static and heuristic-driven, lacking a learned mechanism for deciding what to store, update, or retrieve. We present Memory-R1, a reinforcement learning (RL) framework that equips LLMs with the ability to actively manage and utilize external memory through two specialized agents: a Memory Manager that learns structured operations, including ADD, UPDATE, DELETE, and NOOP; and an Answer Agent that pre-selects and reasons over relevant entries. Both agents are fine-tuned with outcome-driven RL (PPO and GRPO), enabling adaptive memory management with minimal supervision. With only 152 training QA pairs, Memory-R1 outperforms strong baselines and generalizes across diverse question types, three benchmarks (LoCoMo, MSC, LongMemEval), and multiple model scales (3B–14B).

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 B 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://aclanthology.org/2026.acl-long.583.pdf
- 正式记录：https://openreview.net/forum?id=inJIfKNFuE
