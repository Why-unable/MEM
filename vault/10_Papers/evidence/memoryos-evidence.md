---
type: evidence
paper_id: "memoryos"
title: "Memory OS of AI Agent"
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

# Memory OS of AI Agent — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：EMNLP 2025（CCF-B）
- **年份**：2025
- **作者**：Jiazheng Kang, Mingming Ji, Zhe Zhao, Ting Bai
- **DOI**：10.18653/v1/2025.emnlp-main.1318
- **arXiv**：null
- **PDF**：https://aclanthology.org/2025.emnlp-main.1318.pdf
- **正式记录**：https://doi.org/10.18653/v1/2025.emnlp-main.1318
- **主库角色**：把操作系统式的分层存储、更新和检索引入 agent memory，建立 short / mid / long-term 三级记忆。

## 官方摘要

Large Language Models (LLMs) face a crucial challenge from fixed context windows and inadequate memory management, leading to a severe shortage of long-term memory capabilities and limited personalization in the interactive experience with AI agents. To overcome this challenge, we innovatively propose a Memory Operating System, i.e., MemoryOS, to achieve comprehensive and efficient memory management for AI agents. Inspired by the memory management principles in operating systems, MemoryOS designs a hierarchical storage architecture and consists of four key modules: memory Storage, Updating, Retrieval, and Generation. Specifically, the architecture comprises three levels of storage units: short-term memory, mid-term memory, and long-term personal memory. Key operations within MemoryOS include dynamic updates between storage units: short-term to mid-term updates follow a dialogue-chain-based FIFO principle, while mid-term to long-term updates use a segmented page organization strategy. Our pioneering MemoryOS enables hierarchical memory integration and dynamic updating. Extensive experiments on the LoCoMo benchmark show an average improvement of 48.36% on F1 and 46.18% on BLEU-1 over the baselines on GPT-4o-mini, showing contextual coherence and personalized memory retention in long conversations.

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
- PDF：https://aclanthology.org/2025.emnlp-main.1318.pdf
- 正式记录：https://doi.org/10.18653/v1/2025.emnlp-main.1318
