---
type: evidence
paper_id: memoryagentbench
title: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/memoryagentbench.pdf"
source_version: "ICLR 2026 conference paper"
pages_checked: "1-9"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - benchmark
  - memory-agent
---

# MemoryAgentBench 证据卡

## 结论先行

- MemoryAgentBench 把 long-context 数据改造成增量多轮交互，专门评测 memory agent。
- 四项核心能力：accurate retrieval、test-time learning、long-range understanding、selective forgetting。
- 现有 memory agents（context-based、RAG、external memory、tool-integrated）没有同时掌握四项能力。

## 研究问题与定位

现有 benchmark 多测 reasoning/planning/execution，memory 评测不足；长上下文 QA 又是静态、非增量的。MemoryAgentBench 要回答：

> 在增量多轮交互中，agent 是否同时具备 retrieval、test-time learning、long-range understanding、selective forgetting？

## Benchmark 设计

### 四项能力

1. accurate retrieval
2. test-time learning
3. long-range understanding
4. selective forgetting

### 构造

- 把现有 long-context 数据集改造成 incremental multi-turn 格式。
- 加入新构造数据集，覆盖四项能力。
- 评测对象从 context-based/RAG 到 external memory/tool agents。

来源：PDF p.2-6，Benchmark design。

## 关键发现

- 没有现有方法同时掌握四项能力。
- 一些方法 retrieval 强，但 selective forgetting/test-time learning 弱。
- 说明 memory agent 需要“多能力联合”而不是单一 QA 分数。

来源：PDF p.1 abstract；p.6-9，Results。

## 真正的新意

1. **incremental multi-turn 格式**：不是静态长上下文。
2. **四项能力**：retrieval + test-time learning + long-range + selective forgetting。
3. **覆盖多种 memory agent**。
4. **把 forgetting 纳入统一评测**。

## 局限与威胁

- **仍是模拟增量交互**：不是真实 environment loop。
- **action coupling 不如 MemoryArena**。
- **安全维度不如 PersistBench**。
- **benchmark 新**：与 LongMemEval/MemBench 不可直接对齐。
- **没有统一成本指标**。

## 与主线 F 的关系

- **LongMemEval**：LongMemEval 五能力；MemoryAgentBench 四项能力，强调 test-time learning/forgetting。
- **PersistBench**：PersistBench 测安全；MemoryAgentBench 测能力。
- **MemoryArena**：MemoryArena 测 action loop；MemoryAgentBench 测 incremental memory。
- **MemoryBench**：MemoryBench 测持续学习；MemoryAgentBench 测四项核心能力。

## 对 RQ1/RQ3 的意义

- RQ1：MemoryAgentBench 的 retrieval/long-range 子集适合结构记忆。
- RQ3：selective forgetting 子集直接对应遗忘。

## 可复用点

- 四项能力 taxonomy。
- incremental multi-turn 改造。
- 多类 memory agent 评测。
- selective forgetting 子集。

## 成本

- 增量多轮评测比静态 QA 成本高。
- 没有统一 token/latency 表。
- 需要按能力子集报告。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memoryagentbench.pdf`
- ICLR 2026（论文记录）
