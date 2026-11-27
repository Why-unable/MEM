---
type: evidence
paper_id: "artem"
title: "ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory"
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

# ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：AAAI 2026（CCF-A）
- **年份**：2026
- **作者**：Cassandra Hui-Ming Tan, Budhitama Subagdja, Ah-Hwee Tan
- **DOI**：10.1609/aaai.v40i30.39773
- **arXiv**：null
- **PDF**：https://ojs.aaai.org/index.php/AAAI/article/download/39773/43734
- **正式记录**：https://openreview.net/forum?id=fwbNOrflIy
- **主库角色**：时空 episodic memory，关注事件顺序、时间依赖和长期空间经验。

## 官方摘要

Current large language models (LLMs) exhibit significant deficiencies in episodic memory tasks including encoding, storing, and retrieving specific information from temporally dependent events over a long period of time. Recent approaches to handle memory tasks in LLMs, such as in-context learning, retrieval-augmented generation (RAG), and fine-tuning, may resolve the long-term retention issues, but are still inadequate to handle tasks requiring chronological awareness of the stored information. We introduce Agentic Retrieval with Temporal-Episodic Memory (ARTEM), a hybrid LLM-based agent architecture integrating LLMs with a self-organizing neural network named Spatial-Temporal Episodic Memory (STEM), designed to handle episodic memory tasks. Our approach employs LLMs for event extraction from the inputs to represent temporal, spatial, entitative, and semantic information that may facilitate future retrieval, aside from generating outputs or direct responses. The extracted events can then be encoded vectorially and stored in a fast and stable manner in the episodic memory through an instance-based incremental learning in STEM. STEM supports precise episodes retrieval and helps reduce computational overhead in generating the appropriate responses by LLMs. Evaluation on standardized episodic memory benchmarks across four tasks—partial cue retrieval, epistemic uncertainty detection, recent event identification, and chronological recall—demonstrates superior performance of ARTEM compared to in-context learning, RAG, and fine-tuning in various popular LLMs.

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
- PDF：https://ojs.aaai.org/index.php/AAAI/article/download/39773/43734
- 正式记录：https://openreview.net/forum?id=fwbNOrflIy
