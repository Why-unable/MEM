---
type: evidence
paper_id: "membench"
title: "MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents"
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

# MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL Findings 2025（ACL-Findings）
- **年份**：2025
- **作者**：Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, Zhenhua Dong
- **DOI**：10.48550/arXiv.2506.21605
- **arXiv**：2506.21605
- **PDF**：https://aclanthology.org/2025.findings-acl.989.pdf
- **正式记录**：https://openreview.net/forum?id=XOJ5SQe6X0
- **主库角色**：LLM-based agent 记忆的综合评测，覆盖多种记忆能力。

## 官方摘要

Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly limited by the diversity of memory levels and interactive scenarios. They also lack comprehensive metrics to reflect the memory capabilities from multiple aspects. To address these problems, in this paper, we construct a more comprehensive dataset and benchmark to evaluate the memory capability of LLM-based agents. Our dataset incorporates factual memory and reflective memory as different levels, and proposes participation and observation as various interactive scenarios. Based on our dataset, we present a benchmark, named MemBench, to evaluate the memory capability of LLM-based agents from multiple aspects, including their effectiveness, efficiency, and capacity. To benefit the research community, we release our dataset and project at https://github.com/import-myself/Membench.

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
- PDF：https://aclanthology.org/2025.findings-acl.989.pdf
- 正式记录：https://openreview.net/forum?id=XOJ5SQe6X0
