---
type: evidence
paper_id: "evermemos"
title: "EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning"
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

# EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Chuanrui Hu, Xingze Gao, Zuyi Zhou, Dannong Xu, Yi Bai, Xintong Li, Hui Zhang, Tong Li, Chong Zhang, Lidong Bing, Yafeng Deng
- **DOI**：10.18653/v1/2026.acl-long.2125
- **arXiv**：null
- **PDF**：https://aclanthology.org/2026.acl-long.2125.pdf
- **正式记录**：https://doi.org/10.18653/v1/2026.acl-long.2125
- **主库角色**：用 engram-inspired 生命周期组织记忆：Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。

## 官方摘要

Large Language Models (LLMs) are increasingly deployed as long-term interactive agents, yet their limited context windows make it difficult to sustain coherent behavior over extended interactions. Existing memory systems for LLMs often store isolated records and retrieve fragments, limiting their ability to consolidate evolving experience and resolve conflicts. We introduce EverMemOS, a self-organizing memory operating system that implements an engram-inspired lifecycle for computational memory. First, Episodic Trace Formation converts dialogue streams into MemCells that capture episodic traces, atomic facts, and time-bounded foresight. Second, Semantic Consolidation organizes MemCells into thematic MemScenes, distilling stable semantic structures and updating user profiles. Finally, Reconstructive Recollection performs MemScene-guided agentic retrieval to compose the necessary and sufficient context for downstream reasoning. Experiments on LoCoMo, LongMemEval, and PersonaMem-v2 show that EverMemOS significantly outperforms state-of-the-art methods on memory-augmented reasoning tasks.

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
- PDF：https://aclanthology.org/2026.acl-long.2125.pdf
- 正式记录：https://doi.org/10.18653/v1/2026.acl-long.2125
