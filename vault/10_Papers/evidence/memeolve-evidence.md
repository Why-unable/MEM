---
type: evidence
paper_id: memeolve
title: "MemEvolve: Meta-Evolution of Agent Memory Systems"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/memeolve.pdf"
source_version: "ICML 2026 / PMLR 306"
pages_checked: "1-9"
mainline: "B"
tags:
  - evidence
  - mainline-b
  - meta-evolution
  - memory-architecture
---

# MemEvolve 证据卡

## 结论先行

- MemEvolve 不只进化 agent 的经验，还进化 **memory architecture 本身**。
- 它提出 EvolveLab：把 12 个代表性 memory systems 抽象成 `encode / store / retrieve / manage` 模块。
- 四个 agentic benchmark 上，SmolAgent / Flash-Searcher 最高提升 **17.06%**，并显示跨任务/跨 LLM 迁移。

## 研究问题与定位

现有 self-evolving memory 仍是手工架构：agent 能积累经验，但 memory 系统本身不能 meta-adapt。MemEvolve 要回答：

> 能否让 memory architecture 也参与进化，而不是只进化经验？

## 方法拆解

### EvolveLab

- 统一 12 个 memory systems。
- 模块化设计空间：
  - encode
  - store
  - retrieve
  - manage
- 提供标准化实现和公平实验 arena。

### Meta-evolution

- 联合进化 experiential knowledge + memory architecture。
- 外循环优化架构，内循环积累经验。
- 目标是跨任务/跨 LLM 迁移。

来源：PDF p.3-6，Method。

## 实验与关键数字

### 设置

- Benchmarks：GAIA、WebWalkerQA、xBench-DeepSearch、TaskCraft。
- Baselines：No-Memory、Voyager、ExpeL、DILU、AWM、Mobile-E、Dynamic Cheatsheet；Smolagents / Flash-Searcher / OWL / Agent KB 等框架。
- Metrics：task success/accuracy、cost、delay、steps。

### 结果

- SmolAgent / Flash-Searcher 最高提升 **17.06%**。
- 四个 benchmark 上均有提升。
- 进化出的 memory architecture 可跨任务、跨 LLM 迁移。
- 成本与 no-memory 接近（论文 Table 3：GAIA $0.085 vs $0.086；xBench $0.136 vs $0.141）。

来源：PDF p.1 abstract；p.6-8，Table 2-3。

## 真正的新意

1. **memory architecture 作为进化对象**。
2. **EvolveLab**：12 个系统的统一设计空间。
3. **跨任务/跨 LLM 迁移**。
4. **成本可控**：不是靠无限增加 API 成本。

## 局限与威胁

- **搜索/进化成本**：外循环需要大量实验。
- **架构空间有限**：encode/store/retrieve/manage 四模块。
- **评测集中在 agentic benchmark**：没有多模态/安全。
- **可解释性**：进化出的架构可能难以理解。
- **没有遗忘/权限治理**。

## 与主线 B 的关系

- **Memory-R1/AgeMem**：学 policy；MemEvolve 学 architecture。
- **UMEM**：联合 extraction/management；MemEvolve 联合 experience/architecture。
- **ReasoningBank**：经验蒸馏；MemEvolve 进一步进化学习方式。
- **M+**：参数化记忆；MemEvolve 外部架构。

## 对 RQ2 的意义

MemEvolve 直接对应 RQ2（迁移）：

- 进化出的架构能否跨任务/跨 LLM 迁移？
- 需要报告迁移矩阵和搜索成本。

## 可复用点

- EvolveLab 四模块设计空间。
- meta-evolution 外循环/内循环。
- 跨任务/跨 LLM 迁移评测。
- cost/delay/steps 分析。

## 成本

- API cost 接近 no-memory（GAIA $0.085 vs $0.086；xBench $0.136 vs $0.141）。
- 进化搜索成本未在摘要中量化，需回附录。
- 没有统一 GPU 成本表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memeolve.pdf`
- PMLR 306（ICML 2026）
