---
type: evidence
paper_id: "hippocampus"
title: "Hippocampus: An Efficient and Scalable Memory Module for Agentic AI"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "C"
tags:
  - evidence
  - mainline-c
---

# Hippocampus: An Efficient and Scalable Memory Module for Agentic AI — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：MLSys 2026（Top-MLSys）
- **年份**：2026
- **作者**：Yi Li, Lianjie Cao, Faraz Ahmed, Puneet Sharma, Bingzhe Li
- **DOI**：10.48550/arXiv.2602.13594
- **arXiv**：2602.13594
- **PDF**：https://openreview.net/pdf?id=0sUYZh9D4a
- **正式记录**：https://openreview.net/forum?id=0sUYZh9D4a
- **主库角色**：面向 agentic AI 的高效、可扩展记忆模块，偏系统实现与部署效率。

## 官方摘要

Agentic AI systems require persistent memory to store user-specific histories beyond the limited context window of LLMs. Existing memory systems rely on the dense vector databases, knowledge-graph traversal, or hybrids, which incur high retrieval latency and poor storage scalability.
We introduce HIPPOCAMPUS, an agentic memory management system that uses compact binary signatures for semantic search and lossless token-ID streams for exact content reconstruction. Its core is a Dynamic Wavelet Matrix (DWM) that compresses and co-indexes
both streams to support ultra-fast search in the compressed domain, thus avoiding costly dense-vector or graph computations. For a fixed tokenizer vocabulary, the storage footprint of this design grows linearly with memory size, making it suitable for long-horizon agentic deployments. Empirically, across LoCoMo and LongMemEval, HIPPOCAMPUS achieves end-to-end retrieval latency that is comparable to or lower than the evaluated agentic memory baselines, with 1.1X–31.5X speedups over the evaluated baselines, and reduces per-query token footprint by 1.1X–14.5X, while maintaining competitive task accuracy.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 C 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=0sUYZh9D4a
- 正式记录：https://openreview.net/forum?id=0sUYZh9D4a
