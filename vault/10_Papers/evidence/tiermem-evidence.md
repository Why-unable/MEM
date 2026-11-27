---
type: evidence
paper_id: "tiermem"
title: "TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "D"
tags:
  - evidence
  - mainline-d
---

# TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：COLM 2026（Top-COLM）
- **年份**：2026
- **作者**：Qiming Zhu, Shunian Chen, Rui Yu, Zhehao Wu, Benyou Wang
- **DOI**：null
- **arXiv**：null
- **PDF**：https://openreview.net/pdf?id=svKCa4itcd
- **正式记录**：https://openreview.net/forum?id=svKCa4itcd
- **主库角色**：在压缩记忆与原始证据之间做分层权衡，面向长时程 agent memory。

## 官方摘要

Long-horizon agents must preserve past experience before knowing what future queries will require. Compact memory makes growing histories efficient to reuse by distilling experience into reusable abstractions, while raw history preserves fine-grained evidence for faithful grounding. Because future queries require different levels of detail, the appropriate memory granularity cannot be reliably fixed when memory is written. We therefore argue that memory granularity should be determined when the future information need becomes known. We introduce \textbf{TierMem}, a provenance-linked two-tier memory framework that allocates memory granularity according to evidence sufficiency. TierMem retrieves compact memory by default, uses a learned router to identify when finer-grained evidence is required, and follows provenance links to recover relevant raw evidence. Recovered evidence can be consolidated into compact memory for future reuse. Across two long-horizon memory benchmarks, TierMem recovers much of the quality enabled by raw evidence while substantially reducing inference cost. Further analyses show that provenance improves evidence recovery and that consolidation progressively increases the share of queries served by compact memory.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 D 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=svKCa4itcd
- 正式记录：https://openreview.net/forum?id=svKCa4itcd
