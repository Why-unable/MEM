---
type: evidence
paper_id: "remem"
title: "REMem: Reasoning with Episodic Memory in Language Agent"
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

# REMem: Reasoning with Episodic Memory in Language Agent — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Yiheng Shu, Saisri Padmaja Jonnalagedda, Xiang Gao, Bernal Jiménez Gutiérrez, Weijian Qi, Kamalika Das, Huan Sun, Yu Su
- **DOI**：10.48550/arXiv.2602.13530
- **arXiv**：2602.13530
- **PDF**：https://openreview.net/pdf?id=fugnQxbvMm
- **正式记录**：https://openreview.net/forum?id=fugnQxbvMm
- **主库角色**：把 episodic memory 与推理过程结合，强调事件级经验的复用。

## 官方摘要

Humans excel at remembering concrete experiences along spatiotemporal contexts and performing reasoning across those events, i.e., the capacity for episodic memory. In contrast, memory in language agents remains mainly semantic, and current agents are not yet capable of effectively recollecting and reasoning over interaction histories. We identify and formalize the core challenges of episodic recollection and reasoning from this gap, and observe that existing work often overlooks episodicity, lacks explicit event modeling, or overemphasizes simple retrieval rather than complex reasoning. We present REMem, a two-phase framework for constructing and reasoning with episodic memory: 1) Offline indexing, where REMem converts experiences into a hybrid memory graph that flexibly links time-aware gists and facts. 2) Online inference, where REMem employs an agentic retriever with carefully curated tools for iterative retrieval over the memory graph. Comprehensive evaluation across four episodic memory benchmarks shows that REMem substantially outperforms state-of-the-art memory systems such as Mem0 and HippoRAG 2, showing 3.4% and 13.4% absolute improvements on episodic recollection and reasoning tasks, respectively. Moreover, REMem also demonstrates more robust refusal behavior for unanswerable questions.

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
- PDF：https://openreview.net/pdf?id=fugnQxbvMm
- 正式记录：https://openreview.net/forum?id=fugnQxbvMm
