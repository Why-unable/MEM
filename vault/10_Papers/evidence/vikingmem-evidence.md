---
type: evidence
paper_id: vikingmem
title: "VikingMem: A Memory Base Management System for Stateful LLM-Based Applications"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/vikingmem.pdf"
source_version: "PVLDB Vol. 19 No. 12 (2026), DOI 10.14778/3827998.3828037; full text read from arXiv 2605.29640"
pages_checked: "1-10"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - memory-base
  - production-system
  - event-entity
---

# VikingMem 证据卡

## 结论先行

- VikingMem 提出 **Memory Base**：面向 stateful LLM 应用的持久状态管理范式，运行在 VikingDB 向量引擎上。
- 它用 event + entity 双抽象：event 负责选择性抽取事件，entity 由事件持续更新，形成“活”的用户/工具 profile。
- 在 LoCoMo / LongMemEval 上取得最高 LLM-Judge，且 P95 检索延迟保持在 **0.39–0.89s**；相对 baseline 最高 **30%** retrieval effectiveness 提升。

## 研究问题与定位

LLM 应用从 stateless query 转向长期、stateful 交互，但：

- 现有 memory extraction 过于简化，记忆不完整；
- 很多 extract prompt 只服务单一场景（如 chatbot），缺乏泛化；
- 生产环境要求低延迟、高吞吐、可扩展。

VikingMem 要回答：

> 能否把 memory 从“应用内启发式”提升为 **service-grade Memory Base**，统一管理长期状态？

## 方法拆解

### 三个核心原则

1. **Selective extraction**：从 raw stream 中只抽取高价值记忆。
2. **Statefulness and evolution**：记忆持续总结、纠错、时间加权，优先近期交互。
3. **Generalizable abstraction**：同一套抽象可迁移到教育、推荐、agent memory 等场景。

来源：PDF p.1 abstract。

### Event + Entity

- **Event memory**：事件级抽取，保存可操作的具体经历/动作。
- **Entity memory**：实体由事件动态更新，形成长期 profile。
  - 例：agent tool memory 记录工具使用、失败案例、适用场景，并持续演化。
- 支持 event-centric partitioning 和 deduplication。

来源：PDF p.2-5。

### Memory management

- 时间压缩：topic-wise timeline，把旧事件压缩成高层 summary，并设置 TTL。
- 时间加权 recall：优先近期记忆，旧事件逐渐压缩/淡化。
- multi-vector reranking：在 retrieval 后做多向量重排。
- keyword graph：辅助混合检索。

来源：PDF p.4-7，Section 3。

### 工程实现

- 构建在 **VikingDB** 向量引擎上。
- event memories、entity states、keyword-linked indices 存在 VikingDB。
- 单次 LLM pass 完成多种 memory type 抽取，减少多 pass token 成本。

来源：PDF p.5-6，p.9-10。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval-S。
- Backbones：GPT-4o-mini、GPT-4.1-mini、GPT-4o。
- Baselines：Mem0、Mem0-graph、Zep、RAG、Full-Context、Claude Native Memory、OpenClaw、Mirix。
- Metrics：LLM-Judge、F1、p50/p95 search latency。

### LoCoMo

| Backbone | 方法 | Overall LLM-Judge | p50 | p95 |
|---|---|---:|---:|---:|
| GPT-4o-mini | Full-Context | 77.47 | — | — |
| GPT-4o-mini | Mirix | 78.66 | 10.90s | 25.76s |
| GPT-4o-mini | **VikingMem** | **88.83** | **0.20s** | **0.39s** |
| GPT-4.1-mini | Full-Context | 86.36 | — | — |
| GPT-4.1-mini | **VikingMem** | **90.12** | **0.20s** | **0.39s** |

来源：PDF p.9，Table 1。

### LongMemEval-S

| Backbone | 方法 | Overall LLM-Judge | p50 | p95 |
|---|---|---:|---:|---:|
| GPT-4o-mini | Full-Context | 55.00 | — | — |
| GPT-4o-mini | Zep | 63.21 | 3.80s | 5.45s |
| GPT-4o-mini | **VikingMem** | **66.36** | **0.25s** | **0.89s** |
| GPT-4o | Full-Context | 59.20 | — | — |
| GPT-4o | Zep | 70.40 | 3.80s | 5.45s |
| GPT-4o | **VikingMem** | **75.80** | **0.25s** | **0.89s** |

来源：PDF p.9，Table 1。

### F1

- LoCoMo F1：VikingMem **54.98** vs Full-Context **53.03**。
- 在 Single-Hop、Multi-Hop、Open-Domain 上最好，Temporal 有竞争力。

来源：PDF p.11，Table 6。

### 成本

- P50 **0.20–0.25s**；P95 **0.39–0.89s**。
- 单次 LLM pass 抽取多种 memory type，减少多 pass 的 token 与 build latency。
- 论文报告 P95 相对部分 baseline 降低 **900ms**；retrieval effectiveness 最高 +30%。

来源：PDF p.1 abstract；p.9-10。

## 真正的新意

1. **Memory Base 作为数据管理范式**，不是单个 memory module。
2. **event + entity 双抽象**：事件保存经历，实体保存演化状态。
3. **时间压缩 + TTL + 时间加权**：旧事件被 summary 替代，近期优先。
4. **生产级系统**：VikingDB、低 P95、单 pass 抽取、multi-vector rerank。

## 局限与威胁

作者没有单独 Limitations 章节；以下是分析判断：

- **生产系统/基线 API 依赖**：完全复现需要 VikingDB 和 baseline API。
- **Temporal weighting 在 benchmark 中默认关闭**：因为 LoCoMo/LongMemEval 主要是 fact-based queries；真实时间敏感任务需另测。
- **event/entity schema 依赖 LLM 抽取质量**。
- **没有安全/隐私/多 agent 共享评测**。
- **没有显式删除/回滚/权限治理**：TTL 是压缩/过期，不是可审计删除。
- **主要是对话/agent memory**：多模态、action-coupled 任务未覆盖。

## 与主线 C 的关系

- **Mem0**：Mem0 是 extract-consolidate-retrieve pipeline；VikingMem 进一步做成 Memory Base 系统。
- **MemoryOS**：MemoryOS 是三级 OS；VikingMem 是 event/entity memory base。
- **EverMemOS**：EverMemOS 是 self-organizing lifecycle；VikingMem 更强调生产级存储/检索和低 P95。
- **Hippocampus**：Hippocampus 优化底层压缩检索；VikingMem 构建在 VikingDB 上，优化完整 memory base。
- **MemGAS**：两者都做多粒度/多视图；VikingMem 用 event/entity + temporal compression。

## 对 RQ1 的意义

VikingMem 提供了“生产级 Pareto”证据：

- 高 accuracy + 低 P95 可以同时成立。
- 但 temporal weighting 在 fact QA 上被关闭，说明结构收益依赖任务类型。
- RQ1 应报告 p50/p95 latency、build cost、retrieval effectiveness，而不仅是 judge score。

## 可复用点

- Memory Base 三原则：selective extraction / stateful evolution / generalizable abstraction。
- event + entity schema。
- topic-wise timeline + TTL + time-weighted recall。
- multi-vector reranking。
- VikingDB 上的生产实现。
- LLM-Judge + F1 + p50/p95 的联合评测。

## 成本

- P50 0.20–0.25s；P95 0.39–0.89s。
- 单 pass 抽取降低 token/build latency。
- 存储/构建成本未给统一表；需回 Table 2/3。

## 待核对

- [ ] 核对 Table 2/3 的 token/storage 细节。
- [ ] 核对 temporal weighting 在真实时间敏感任务上的效果。
- [ ] 检查 VikingDB/系统是否可复现。
- [ ] 补正式 PVLDB PDF 版本（当前全文用 arXiv 版本）。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/vikingmem.pdf`
- PVLDB DOI：https://doi.org/10.14778/3827998.3828037
- arXiv：https://arxiv.org/abs/2605.29640
