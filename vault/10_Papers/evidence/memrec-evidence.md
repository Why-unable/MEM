---
type: evidence
paper_id: "memrec"
title: "MemRec: Collaborative Memory-Augmented Agentic Recommender System"
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

# MemRec: Collaborative Memory-Augmented Agentic Recommender System — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Weixin Chen, Yuhan Zhao, Jingyuan Huang, Zihe Ye, Mingxuan Ju, Tong Zhao, Neil Shah, Li Chen, Yongfeng Zhang
- **DOI**：null
- **arXiv**：null
- **PDF**：https://aclanthology.org/2026.acl-long.2061.pdf
- **正式记录**：https://openreview.net/forum?id=FaMcfd14pg
- **主库角色**：把协作记忆增强用于 agentic recommender system。

## 官方摘要

The evolution of recommender systems has shifted from traditional collaborative filtering to LLM-based agentic systems, which rely on semantic user and item memories to make predictions. However, existing agents maintain these memories in isolation. This overlooks crucial collaborative signals, such as user-item co-engagements and peer relationships across the community, which significantly limits their ability to uncover hidden preferences and accurately infer user needs, particularly for data-sparse users. To bridge this gap, we introduce collaborative memory, a paradigm that connects isolated semantics to enable the sharing of relational insights. Yet, naively utilizing collaborative memory causes severe context overload and introduces noise to downstream LLMs, alongside prohibitive computational costs. To resolve this, we propose MemRec, a framework that architecturally decouples memory management from reasoning. MemRec introduces a dedicated, lightweight language model LM_Mem to efficiently manage and synthesize a dynamic collaborative memory graph in the background. It provides only distilled, high-signal contexts to a downstream, heavyweight large language model (LLM_Rec) for the final recommendation. Extensive experiments on four benchmarks demonstrate that MemRec achieves state-of-the-art performance. Code: https://github.com/rutgerswiselab/memrecHomepage: https://memrec.weixinchen.com

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
- PDF：https://aclanthology.org/2026.acl-long.2061.pdf
- 正式记录：https://openreview.net/forum?id=FaMcfd14pg
