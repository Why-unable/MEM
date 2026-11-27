---
type: evidence
paper_id: "memagent"
title: "MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent"
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

# MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-Ying Ma, Jingjing Liu, Mingxuan Wang, Hao Zhou
- **DOI**：10.48550/arXiv.2507.02259
- **arXiv**：2507.02259
- **PDF**：https://openreview.net/pdf?id=k5nIOvYGCL
- **正式记录**：https://openreview.net/forum?id=k5nIOvYGCL
- **主库角色**：用 multi-conv RL 训练 memory agent 压缩长上下文，代表“记忆策略可学习”路线。

## 官方摘要

Despite improvements by length extrapolation, efficient attention and memory modules, handling infinitely long documents without performance degradation during extrapolation remains the ultimate challenge in long-text processing. To solve this problem, We introduce a novel agent workflow, \method, which processes text in segments and updates memory through an overwrite strategy, addressing the challenge of long-context task through enhanced memory management. We further extend the DAPO algorithm to directly optimize memory ability in an end-to-end fashion, facilitating training via independent-context multi-conversation generation. Experimental results demonstrate that MemAgent has superb long-context capabilities, being able to extrapolate from an 8K context to a 3.5M QA task with a performance loss of less than 10\% and achieving over 95\% on the 512K NIAH test.

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
- PDF：https://openreview.net/pdf?id=k5nIOvYGCL
- 正式记录：https://openreview.net/forum?id=k5nIOvYGCL
