---
type: evidence
paper_id: "nemori"
title: "What Deserves Memory: Adaptive Memory Distillation for LLM Agents"
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

# What Deserves Memory: Adaptive Memory Distillation for LLM Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Wenquan Ma, Jiayan Nan, Wenlong Wu
- **DOI**：10.18653/v1/2026.acl-long.1607
- **arXiv**：null
- **PDF**：https://aclanthology.org/2026.acl-long.1607.pdf
- **正式记录**：https://doi.org/10.18653/v1/2026.acl-long.1607
- **主库角色**：把“什么值得记住”转化为可预测性/预测误差驱动的自适应蒸馏（Nemori），避免重要性分数等启发式规则。

## 官方摘要

Memory systems for LLM agents struggle to determine what information deserves retention. Existing approaches rely on predefined heuristics such as importance scores, emotional tags, or factual templates, encoding designer intuition rather than learning from the data itself. Inspired by cognitive ideas, we propose Nemori , an adaptive memory distillation framework that casts the assessment of the experience’s future utility as a matter of predictability. Specifically, Nemori comprises two cascading modules: Episodic Memory Integration transforms raw interactions into coherent narratives, and Semantic Knowledge Distillation extracts insights via prediction error. Centering on distillation, the framework remains agnostic to downstream management. Extensive experiments confirm that Nemori achieves strong performance, efficiency, and storage reduction. Our work suggests that observing the intrinsic properties of interaction sequences offers a viable, data-driven alternative to heuristic-based memory design.

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
- PDF：https://aclanthology.org/2026.acl-long.1607.pdf
- 正式记录：https://doi.org/10.18653/v1/2026.acl-long.1607
