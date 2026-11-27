---
type: evidence
paper_id: "injecmem"
title: "InjecMEM: Memory Injection Attack on LLM Agent Memory Systems"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "G"
tags:
  - evidence
  - mainline-g
---

# InjecMEM: Memory Injection Attack on LLM Agent Memory Systems — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：COLM 2026（Top-COLM）
- **年份**：2026
- **作者**：Hanling Tian, Gengyu Zhang, Zeyang Sha, Jingying Wang, Yuhang Liu, Zhehao Huang, Kun Yang, Xiaolin Huang
- **DOI**：10.48550/arXiv.2608.23471
- **arXiv**：2608.23471
- **PDF**：https://openreview.net/pdf?id=VbXN1Ny912
- **正式记录**：https://openreview.net/forum?id=VbXN1Ny912
- **主库角色**：把注入攻击扩展到记忆系统的写入/检索链路，攻击面更系统。

## 官方摘要

Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose **InjecMEM**, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, we craft the injection with a *retriever-agnostic anchor* and an *adversarial command*. The anchor contains high-recall topical cues so that downstream retrieval consistently associates the record with the target topic. The command is a short sequence optimized to remain effective under uncertain fused contexts, variable placements, and long prompts so that it reliably steers outputs once retrieved. We learn the command via gradient-based coordinate search, averaging over synthetic prompt templates and insertion positions, and extend it to joint optimization across backbones to study transfer. Evaluated across multiple memory systems and backbone models, InjecMEM achieves reliable topic-conditioned retrieval and targeted generation, remains effective under memory drift, and leaves non-target queries unaffected. Our results underscore the need to harden memory systems and provide a reproducible framework for studying agent memory.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 G 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=VbXN1Ny912
- 正式记录：https://openreview.net/forum?id=VbXN1Ny912
