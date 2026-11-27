---
type: evidence
paper_id: "timem"
title: "TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents"
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

# TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Kai Li, Xuanqing Yu, Ziyi Ni, Yi Zeng, Yao Xu, Zheqing Zhang, Xin Li, Jitao Sang, Xiaogang Duan, Xuelei Wang, Chengbao Liu, Jie Tan
- **DOI**：10.48550/arXiv.2601.02845
- **arXiv**：2601.02845
- **PDF**：https://aclanthology.org/2026.findings-acl.1091.pdf
- **正式记录**：https://openreview.net/forum?id=40y8NAFkq0
- **主库角色**：时间—层次记忆整合，面向长时程对话中的时序信息保持。

## 官方摘要

Long-horizon conversational agents have to manage ever-growing interaction histories that quickly exceed the finite context windows of large language models (LLMs). Existing memory frameworks provide limited support for temporally structured information across hierarchical levels, often leading to fragmented memories and unstable long-horizon personalization. We present TiMem, a temporal–hierarchical memory framework that organizes conversations through a Temporal Memory Tree (TMT), enabling systematic memory consolidation from raw conversational observations to progressively abstracted persona representations. TiMem is characterized by three core properties: (1) temporal–hierarchical organization through TMT; (2) semantic-guided consolidation that enables memory integration across hierarchical levels without fine-tuning; and (3) complexity-aware memory recall that balances precision and efficiency across queries of varying complexity. Under a consistent evaluation setup, TiMem achieves state-of-the-art accuracy on both benchmarks, reaching 75.30% on LoCoMo and 76.88% on LongMemEval-S. It outperforms all evaluated baselines while reducing the recalled memory length by 52.20% on LoCoMo. Manifold analysis indicates clear persona separation on LoCoMo and reduced dispersion on LongMemEval-S. Overall, TiMem treats temporal continuity as a first-class organizing principle for long-horizon memory in conversational agents. The code is available at https://github.com/TiMEM-AI/timem.

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
- PDF：https://aclanthology.org/2026.findings-acl.1091.pdf
- 正式记录：https://openreview.net/forum?id=40y8NAFkq0
