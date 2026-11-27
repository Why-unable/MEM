---
type: evidence
paper_id: "mem0"
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
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

# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ECAI 2025（CCF-B）
- **年份**：2025
- **作者**：Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav
- **DOI**：10.48550/arXiv.2504.19413
- **arXiv**：2504.19413
- **PDF**：https://openreview.net/pdf?id=0wxfikDcOa
- **正式记录**：https://openreview.net/forum?id=0wxfikDcOa
- **主库角色**：工业级可扩展长期记忆，强调生产部署中的记忆抽取、更新与检索流水线。

## 官方摘要

Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements. Through comprehensive evaluations on the LOCOMO benchmark, we systematically compare our approaches against six baseline categories. Empirical results demonstrate that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base Mem0 configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to the full-context approach. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, thereby offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight the critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents. Code: https://mem0.ai/research.

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
- PDF：https://openreview.net/pdf?id=0wxfikDcOa
- 正式记录：https://openreview.net/forum?id=0wxfikDcOa
