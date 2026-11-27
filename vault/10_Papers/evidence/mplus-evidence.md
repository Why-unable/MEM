---
type: evidence
paper_id: "mplus"
title: "M+: Extending MemoryLLM with Scalable Long-Term Memory"
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

# M+: Extending MemoryLLM with Scalable Long-Term Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2025（CCF-A）
- **年份**：2025
- **作者**：Yu Wang, Dmitry Krotov, Yuanzhe Hu, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, Zexue He
- **DOI**：10.48550/arXiv.2502.00592
- **arXiv**：2502.00592
- **PDF**：https://openreview.net/pdf?id=OcqbkROe8J
- **正式记录**：https://openreview.net/forum?id=OcqbkROe8J
- **主库角色**：扩展 MemoryLLM 的可扩展长期参数记忆，连接参数化记忆与外部记忆。

## 官方摘要

Equipping large language models (LLMs) with latent-space memory has attracted increasing attention as they can extend the context window of existing language models. However, retaining information from the distant past remains a challenge. For example, MemoryLLM (Wang et al., 2024a), as a representative work with latent-space memory, compresses past information into hidden states across all layers, forming a memory pool of 1B parameters. While effective for sequence lengths up to 16k tokens, it struggles to retain knowledge beyond 20k tokens. In this work, we address this limitation by introducing M+, a memory-augmented model based on MemoryLLM that significantly enhances long-term information retention. M+ integrates a long-term memory mechanism with a co-trained retriever, dynamically retrieving relevant information during text generation. We evaluate M+ on diverse benchmarks, including long-context understanding and knowledge retention tasks. Experimental results show that M+ significantly outperforms MemoryLLM and recent strong baselines, extending knowledge retention from under 20k to over 160k tokens with similar GPU memory overhead.

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
- PDF：https://openreview.net/pdf?id=OcqbkROe8J
- 正式记录：https://openreview.net/forum?id=OcqbkROe8J
