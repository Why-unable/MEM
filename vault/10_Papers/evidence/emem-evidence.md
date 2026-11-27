---
type: evidence
paper_id: "emem"
title: "E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory"
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

# E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Kaixiang Wang, Yidan Lin, Zihan Wang, Bunyod Suvonov, Zhaojiacheng Zhou, Yuxiang Zheng, Jiaxi Cao, Zhiheng Dong, Chentao Wu, Jiong Lou, Jie Li
- **DOI**：null
- **arXiv**：2601.21714
- **PDF**：https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26ee/wang26ee.pdf
- **正式记录**：https://proceedings.mlr.press/v306/wang26ee.html
- **主库角色**：用多个 assistant agent 保留未压缩的情境上下文，由 master agent 协调局部推理和证据重构，避免记忆预处理造成去语境化。

## 官方摘要

The evolution of Large Language Model (LLM) agents towards System~2 reasoning, characterized by deliberative, high-precision problem-solving, requires maintaining rigorous logical integrity over extended horizons. However, prevalent memory preprocessing paradigms suffer from destructive de-contextualization. By compressing complex sequential dependencies into pre-defined structures (e.g., embeddings or graphs), these methods sever the contextual integrity essential for deep reasoning. To address this, we propose E-mem, a framework shifting from Memory Preprocessing to Episodic Context Reconstruction. Inspired by biological engrams, E-mem employs a heterogeneous hierarchical architecture where multiple assistant agents maintain uncompressed memory contexts, while a central master agent orchestrates global planning. Unlike passive retrieval, our mechanism empowers assistants to locally reason within activated segments, extracting context-aware evidence before aggregation. Evaluations on the LoCoMo benchmark demonstrate that E-mem achieves over 54\% F1, surpassing the state-of-the-art GAM by 7.75\%, while reducing token cost by over 70\%.

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
- PDF：https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26ee/wang26ee.pdf
- 正式记录：https://proceedings.mlr.press/v306/wang26ee.html
