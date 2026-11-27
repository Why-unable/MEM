---
type: evidence
paper_id: "longmemeval"
title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "F"
tags:
  - evidence
  - mainline-f
---

# LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2025（Top-ICLR）
- **年份**：2025
- **作者**：Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu
- **DOI**：null
- **arXiv**：null
- **PDF**：https://openreview.net/pdf?id=pZiyCaVuti
- **正式记录**：https://openreview.net/forum?id=pZiyCaVuti
- **主库角色**：长期交互记忆基准，已成为记忆系统评测的重要参照。

## 官方摘要

Recent large language model (LLM)-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses. However, their long-term memory capabilities in sustained interactions remain underexplored. We introduce LongMemEval, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, LongMemEval presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions. We then present a unified framework that breaks down the long-term memory design into three stages: indexing, retrieval, and reading. Built upon key experimental insights, we propose several memory design optimizations including session decomposition for value granularity, fact-augmented key expansion for indexing, and time-aware query expansion for refining the search scope. Extensive experiments show that these optimizations greatly improve both memory recall and downstream question answering on LongMemEval. Overall, our study provides valuable resources and guidance for advancing the long-term memory capabilities of LLM-based chat assistants, paving the way toward more personalized and reliable conversational AI. Our benchmark and code are publicly available at https://github.com/xiaowu0162/LongMemEval.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 F 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=pZiyCaVuti
- 正式记录：https://openreview.net/forum?id=pZiyCaVuti
