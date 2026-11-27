---
type: evidence
paper_id: "umem"
title: "UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "B"
tags:
  - evidence
  - mainline-b
---

# UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Yongshi Ye, Hui Jiang, Feihu Jiang, Tian Lan, Yichao Du, Biao Fu, Xiaodong Shi, Qianghuai Jia, Longyue Wang, Weihua Luo
- **DOI**：null
- **arXiv**：null
- **PDF**：https://openreview.net/pdf?id=BoiXvrwtdi
- **正式记录**：https://openreview.net/forum?id=BoiXvrwtdi
- **主库角色**：统一记忆抽取与管理，强调跨任务、跨场景的泛化记忆能力。

## 官方摘要

Self-evolving memory serves as the trainable parameters for Large Language Models (LLMs)-based agents, where extraction (distilling insights from experience) and management (updating the memory bank) must be tightly coordinated.
Existing methods predominantly optimize memory management while treating memory extraction as a static process, resulting in poor generalization, where agents accumulate instance-specific noise rather than robust memories.
To address this, we propose Unified Memory Extraction and Management (UMEM), a self-evolving agent framework that jointly optimizes a LLM to simultaneously extract and manage memories.
To mitigate overfitting to specific instances, we introduce Semantic Neighborhood Modeling and optimize the model with a neighborhood-level marginal utility reward via GRPO.
This approach ensures memory generalizability by evaluating memory utility across clusters of semantically related queries.
Extensive experiments across five benchmarks demonstrate that UMEM significantly outperforms highly competitive baselines, achieving up to 11.49 points improvement in multi-turn interactive tasks. Furthermore, UMEM maintains a stable improvement trend during continuous evolution.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 B 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=BoiXvrwtdi
- 正式记录：https://openreview.net/forum?id=BoiXvrwtdi
