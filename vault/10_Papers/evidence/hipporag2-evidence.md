---
type: evidence
paper_id: "hipporag2"
title: "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "A"
tags:
  - evidence
  - mainline-a
---

# From RAG to Memory: Non-Parametric Continual Learning for Large Language Models — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2025（CCF-A）
- **年份**：2025
- **作者**：Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, Yu Su
- **DOI**：null
- **arXiv**：2502.14802
- **PDF**：https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf
- **正式记录**：https://proceedings.mlr.press/v267/gutierrez25a.html
- **主库角色**：用 Personalized PageRank + passage integration 统一事实、sense-making 和 associative memory 的图增强 RAG。

## 官方摘要

Our ability to continuously acquire, organize, and leverage knowledge is a key feature of human intelligence that AI systems must approximate to unlock their full potential. Given the challenges in continual learning with large language models (LLMs), retrieval-augmented generation (RAG) has become the dominant way to introduce new information. However, its reliance on vector retrieval hinders its ability to mimic the dynamic and interconnected nature of human long-term memory. Recent RAG approaches augment vector embeddings with various structures like knowledge graphs to address some of these gaps, namely sense-making and associativity. However, their performance on more basic factual memory tasks drops considerably below standard RAG. We address this unintended deterioration and propose HippoRAG 2, a framework that outperforms standard RAG comprehensively on factual, sense-making, and associative memory tasks. HippoRAG 2 builds upon the Personalized PageRank algorithm used in HippoRAG and enhances it with deeper passage integration and more effective online use of an LLM. This combination pushes this RAG system closer to the effectiveness of human long-term memory, achieving a 7% improvement in associative memory tasks over the state-of-the-art embedding model while also exhibiting superior factual knowledge and sense-making memory capabilities. This work paves the way for non-parametric continual learning for LLMs. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 A 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf
- 正式记录：https://proceedings.mlr.press/v267/gutierrez25a.html
