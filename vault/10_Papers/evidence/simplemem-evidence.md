---
type: evidence
paper_id: simplemem
title: "SimpleMem: Efficient Lifelong Memory for LLM Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/simplemem.pdf"
source_version: "ICML 2026 / PMLR 306"
pages_checked: "1-9"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - compression
  - efficiency
---

# SimpleMem 证据卡

## 结论先行

- SimpleMem 的核心是 **semantic lossless compression**：把交互压成 compact、multi-view indexed memory units，再在线合并和按 intent 检索。
- 三步：Semantic Structured Compression → Online Semantic Synthesis → Intent-Aware Retrieval Planning。
- LoCoMo 上平均 F1 **+26.4%**，推理 token 最多降低 **30x**。

## 研究问题与定位

现有方法要么保留完整历史（冗余、token 高），要么靠迭代推理过滤噪声（也贵）。SimpleMem 要回答：

> 能否通过语义压缩和意图感知检索，在长期记忆中获得更好的 accuracy–token Pareto？

## 方法拆解

### 1. Semantic Structured Compression

- 把非结构化交互压成 compact memory units。
- 每个 unit 有多视图索引（语义/关键词/上下文等）。

### 2. Online Semantic Synthesis

- 在 session 内即时合并相关上下文。
- 消除冗余，形成统一抽象表示。

### 3. Intent-Aware Retrieval Planning

- 推断 query 的检索意图。
- 动态决定检索范围和上下文构造，而不是固定 top-k。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmark：LoCoMo（及论文附录中的其他基准）。
- Baselines：full history、RAG、memory systems。
- Metrics：F1、retrieval efficiency、inference token。

### 结果

- LoCoMo 平均 F1 **+26.4%**。
- 推理 token 最多降低 **30x**。
- 在 accuracy、retrieval efficiency、inference cost 三方面均优于 baseline。

来源：PDF p.1 abstract；p.6-8，Table 1-2。

### 消融

- 去掉 semantic compression / online synthesis / intent-aware planning 会降低 accuracy 或增加 token。
- 说明三步都是必要的。

来源：PDF p.8，Ablation。

## 真正的新意

1. **语义无损压缩**：不是简单摘要，而是保留多视图索引。
2. **在线 synthesis**：session 内即时合并，减少重复。
3. **intent-aware retrieval planning**：检索范围由 query intent 决定。
4. **accuracy–token Pareto**：同时报告准确率和推理成本。

## 局限与威胁

- **压缩可能丢证据**：semantic lossless 是作者命名，但仍是有损摘要/索引。
- **主要是 LoCoMo**：没有 action-coupled、多模态、安全。
- **没有显式遗忘/删除**：memory units 只增不减。
- **intent planner 依赖 LLM**：错误 intent 会导致检索范围错误。
- **长期更新/冲突**：论文没有系统评估。

## 与主线 C 的关系

- **LightMem**：都做压缩/效率；LightMem 更强调 online/offline 解耦，SimpleMem 更强调 compression + intent planning。
- **Mem0**：Mem0 是生产级 extract-consolidate-retrieve；SimpleMem 是 semantic compression pipeline。
- **Hippocampus**：Hippocampus 优化底层索引；SimpleMem 优化 memory unit 表示。
- **TierMem**：TierMem 用 summary+raw 两层；SimpleMem 用 multi-view compressed units。

## 对 RQ1 的意义

SimpleMem 提供了“压缩 + 意图检索”的 Pareto：

- 结构记忆的收益可能来自更小的 memory unit + 更精准的 retrieval scope。
- RQ1 应报告 inference token、retrieval latency、accuracy。

## 可复用点

- semantic structured compression。
- online semantic synthesis。
- intent-aware retrieval planning。
- multi-view indexed memory units。
- accuracy–token Pareto 报告。

## 成本

- 推理 token 最多降低 30x。
- 平均 F1 +26.4%。
- build/retrieval latency 细节见论文实验表（待核对）。
- 没有统一 storage 成本。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/simplemem.pdf`
- PMLR：https://proceedings.mlr.press/v306/liu26dx.html
- arXiv：https://arxiv.org/abs/2601.02553
