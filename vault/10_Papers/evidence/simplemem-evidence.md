---
type: evidence
paper_id: "simplemem"
title: "SimpleMem: Efficient Lifelong Memory for LLM Agents"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "C"
tags:
  - evidence
  - mainline-c
---

# SimpleMem: Efficient Lifelong Memory for LLM Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Jiaqi Liu, Yaofeng Su, Peng Xia, Siwei Han, Zeyu Zheng, Cihang Xie, Mingyu Ding, Huaxiu Yao
- **DOI**：null
- **arXiv**：2601.02553
- **PDF**：https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26dx/liu26dx.pdf
- **正式记录**：https://proceedings.mlr.press/v306/liu26dx.html
- **主库角色**：用语义结构化压缩、在线综合和意图感知检索规划，在长期记忆中同时优化准确率与 token 成本。

## 官方摘要

To support long-term interaction in complex environments, LLM agents require memory systems that manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which distills unstructured interactions into compact, multi-view indexed memory units; (2) Online Semantic Synthesis, an intra-session process that instantly integrates related context into unified abstract representations to eliminate redundancy; and (3) Intent-Aware Retrieval Planning, which infers search intent to dynamically determine retrieval scope and construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% in LoCoMo while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 C 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26dx/liu26dx.pdf
- 正式记录：https://proceedings.mlr.press/v306/liu26dx.html
