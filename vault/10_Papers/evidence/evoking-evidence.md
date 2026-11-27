---
type: evidence
paper_id: "evoking"
title: "Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "E"
tags:
  - evidence
  - mainline-e
---

# Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Yingyi Zhang, Junyi Li, Wenlin Zhang, Pengyue Jia, Xianneng Li, Yichao Wang, Derong Xu, Yi Wen, Huifeng Guo, Yong Liu, Xiangyu Zhao
- **DOI**：10.48550/arXiv.2603.09250
- **arXiv**：2603.09250
- **PDF**：https://openreview.net/pdf?id=f7p0F2X6XN
- **正式记录**：https://openreview.net/forum?id=f7p0F2X6XN
- **主库角色**：基于回忆—熟悉度的自适应检索，把个性化记忆从“存什么”推进到“如何取”。

## 官方摘要

Personalized large language models (LLMs) rely on memory retrieval to incorporate user-specific histories, preferences, and contexts. Existing approaches either overload the LLM by feeding all the user's past memory into the prompt, which is costly and unscalable, or simplify retrieval into a one-shot similarity search, which captures only surface matches. Cognitive science, however, shows that human memory operates through a dual process: Familiarity, offering fast but coarse recognition, and Recollection, enabling deliberate, chain-like reconstruction for deeply recovering episodic content.
Current systems lack both the ability to perform recollection retrieval and mechanisms to adaptively switch between the dual retrieval paths, leading to either insufficient recall or the inclusion of noise.
To address this, we propose RF-Mem (Recollection–Familiarity Memory Retrieval), a familiarity uncertainty-guided dual-path memory retriever.
RF-Mem measures the familiarity signal through the mean score and entropy. High familiarity leads to the direct top-$K$ Familiarity retrieval path, while low familiarity activates the Recollection path. In the Recollection path, the system clusters candidate memories and applies $\alpha$-mix with the query to iteratively expand evidence in embedding space, simulating deliberate contextual reconstruction.
This design embeds human-like dual-process recognition into the retriever, avoiding full-context overhead and enabling scalable, adaptive personalization. Experiments across three benchmarks and corpus scales demonstrate that RF-Mem consistently outperforms both one-shot retrieval and full-context reasoning under fixed budget and latency constraints.
Our code can be found in the Reproducibility Statement.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 E 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=f7p0F2X6XN
- 正式记录：https://openreview.net/forum?id=f7p0F2X6XN
