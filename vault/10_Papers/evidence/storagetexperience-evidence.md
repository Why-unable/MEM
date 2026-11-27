---
type: evidence
paper_id: "storagetexperience"
title: "From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "X"
tags:
  - evidence
  - mainline-x
---

# From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Jinghao Luo, Yuchen Tian, Chuxue Cao, Ziyang Luo, Hongzhan Lin, Kaixin Li, Chuyi Kong, Ruichao Yang, Jing Ma
- **DOI**：10.18653/v1/2026.findings-acl.2069
- **arXiv**：null
- **PDF**：https://aclanthology.org/2026.findings-acl.2069.pdf
- **正式记录**：https://doi.org/10.18653/v1/2026.findings-acl.2069
- **主库角色**：把 LLM agent memory 的演化概括为 Storage → Reflection → Experience 三阶段，并梳理长程一致性、动态环境和持续学习三条驱动线。

## 官方摘要

Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscillating between operating system engineering and cognitive science. This theoretical divide prevents a unified view of technological synthesis and a coherent evolutionary perspective. To bridge this gap, this survey proposes a novel evolutionary framework for LLM agent memory mechanisms, formalizing the development process into three stages: **Storage** (trajectory preservation), **Reflection** (trajectory refinement), and **Experience** (trajectory abstraction). We first formally define these three stages before analyzing the three core drivers of this evolution: the necessity for long-range consistency, the challenges in dynamic environments, and the ultimate goal of continual learning. Furthermore, we specifically explore two transformative mechanisms in the frontier Experience stage: proactive exploration and cross-trajectory abstraction. By synthesizing these disparate views, this work offers robust design principles and a clear roadmap for the development of next-generation LLM agents.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 X 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://aclanthology.org/2026.findings-acl.2069.pdf
- 正式记录：https://doi.org/10.18653/v1/2026.findings-acl.2069
