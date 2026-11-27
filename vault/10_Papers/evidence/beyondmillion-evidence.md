---
type: evidence
paper_id: "beyondmillion"
title: "Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs"
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

# Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Mohammad Tavakoli, Alireza Salemi, Carrie Ye, Mohamed Abdalla, Hamed Zamani, J Ross Mitchell
- **DOI**：10.48550/arXiv.2510.27246
- **arXiv**：2510.27246
- **PDF**：https://openreview.net/pdf?id=y59hf5lrMn
- **正式记录**：https://openreview.net/forum?id=y59hf5lrMn
- **主库角色**：百万 token 级长记忆评测与增强，扩展了长上下文记忆的压力测试。

## 官方摘要

Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is hampered by the existing benchmarks, which often lack narrative coherence, cover narrow domains, and only test simple recall-oriented tasks. This paper introduces a comprehensive solution to these challenges. First, we present a
novel framework for automatically generating long (up to 10M tokens), coherent, and topically diverse conversations, accompanied by probing questions targeting a wide range of memory abilities. From this, we construct BEAM, a new benchmark comprising 100 conversations and 2,000 validated questions. Second, to enhance model performance, we propose LIGHT–a framework inspired by human cognition that equips LLMs with three complementary memory systems: a long-term episodic memory, a short-term working memory, and a scratchpad for accumulating salient facts. Our experiments on BEAM reveal that even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen. In contrast, LIGHT consistently improves performance
across various models, achieving an average improvement of 3.5%–12.69% over the strongest baselines, depending on the backbone LLM. An ablation study further confirms the contribution of each memory component.

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
- PDF：https://openreview.net/pdf?id=y59hf5lrMn
- 正式记录：https://openreview.net/forum?id=y59hf5lrMn
