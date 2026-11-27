---
type: evidence
paper_id: mplus
title: "M+: Extending MemoryLLM with Scalable Long-Term Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/mplus.pdf"
source_version: "ICML 2025 / PMLR 267"
pages_checked: "1-9"
mainline: "A"
tags:
  - evidence
  - mainline-a
  - parametric-memory
  - long-context
---

# M+ 证据卡

## 结论先行

- M+ 是参数化长期记忆路线：在 MemoryLLM 的 latent memory pool 上加入 long-term memory + co-trained retriever。
- 它把知识保留从 **<20K tokens** 扩展到 **>160K tokens**，同时保持相近的 GPU memory overhead。
- 它提醒主线 A：记忆不一定是外部数据库，也可以存在于模型参数/latent state 中。

## 研究问题与定位

MemoryLLM 把过去信息压进 1B 参数的 memory pool，但超过 20K tokens 后保留能力下降。M+ 要回答：

> 能否在参数化 memory 上增加可扩展的长期检索，让模型保留更远的历史？

## 方法拆解

### MemoryLLM 基础

- 跨层 hidden states 形成 memory pool。
- 参数化压缩历史。

### M+ 扩展

- 增加 long-term memory 机制。
- 训练一个 co-trained retriever，在生成时动态检索相关信息。
- 目标：不显著增加 GPU memory，但延长有效记忆。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：LongBook-QA（∞-Bench，351 本书，平均约 192K tokens）、LongBook Event QA。
- Baselines：Llama-3.1-8B-16K、Llama-3.1-8B-BM25、SnapKV、Llama-3.2-3B-128K、MemoryLLM-8B。
- Metrics：long-context understanding / knowledge retention。

### 结果

- 知识保留从 **<20K** 扩展到 **>160K tokens**。
- 显著优于 MemoryLLM 和强 baseline。
- GPU memory overhead 与 MemoryLLM 相近。

来源：PDF p.1 abstract；p.6-8，Results。

## 真正的新意

1. **参数化长期记忆**：不是外部 vector DB。
2. **co-trained retriever**：参数记忆 + 动态检索。
3. **>160K retention**：显著扩展 MemoryLLM。
4. **memory overhead 可控**。

## 局限与威胁

- **参数化记忆不可审计**：难以定位/删除某条记忆。
- **训练成本高**：需要 co-train retriever。
- **主要是长文档 QA**：不是多 session 对话/agent action。
- **没有显式遗忘/删除**。
- **更新困难**：参数记忆的知识更新不如外部记忆直接。

## 与主线 A 的关系

- **A-Mem/MAGMA**：外部结构化记忆；M+ 是参数化记忆。
- **HippoRAG 2**：外部图 RAG；M+ 是 latent memory。
- **TierMem**：外部 summary/raw；M+ 无 raw provenance。
- **MemoryLLM**：M+ 的直接前身。

## 对 RQ1 的意义

M+ 提供了“记忆 substrate”的极端对照：

- 参数化记忆可以扩展上下文，但不可审计/删除。
- RQ1 应把 memory substrate（参数 vs 外部）作为变量。

## 可复用点

- MemoryLLM + long-term memory + co-trained retriever。
- >160K retention 评测。
- GPU memory 对照。
- LongBook-QA/Event QA。

## 成本

- 训练：co-trained retriever + memory model。
- 推理：retrieval + generation；GPU memory 与 MemoryLLM 相近。
- 没有 token/latency 表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/mplus.pdf`
- PMLR 267（ICML 2025）
