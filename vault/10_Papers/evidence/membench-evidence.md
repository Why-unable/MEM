---
type: evidence
paper_id: membench
title: "MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/membench.pdf"
source_version: "ACL Findings 2025"
pages_checked: "1-9"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - benchmark
  - memory-capability
---

# MemBench 证据卡

## 结论先行

- MemBench 用两个维度组织记忆评测：**factual vs reflective memory**，以及 **participation vs observation** 交互场景。
- 指标覆盖 effectiveness、efficiency、capacity，而不是单一 QA accuracy。
- 它试图补足早期 benchmark “记忆层次单一、交互场景单一、指标单一”的问题。

## 研究问题与定位

现有记忆评测常只测 factual recall，缺少 reflective memory（反思/推理后的记忆）和不同交互角色。MemBench 要回答：

> agent 在不同记忆层次和交互场景下，记忆能力是否一致？

## Benchmark 设计

### 两个记忆层次

- Factual memory：事实、事件、属性。
- Reflective memory：需要推理/反思形成的记忆。

### 两个交互场景

- Participation：agent 参与交互。
- Observation：agent 观察交互。

### 三类指标

- Effectiveness
- Efficiency
- Capacity

来源：PDF p.1-5，Benchmark design。

## 关键发现

- MemBench 能区分不同记忆层次/场景下的能力差异。
- 单一 QA 分数不足以刻画 agent memory。
- 为后续 benchmark 提供了“多维度评测”的模板。

来源：PDF p.1 abstract；p.6-8，Results。

## 真正的新意

1. **factual/reflective 两层**。
2. **participation/observation 两场景**。
3. **effectiveness/efficiency/capacity 三指标**。
4. **多场景数据构造**。

## 局限与威胁

- **任务/数据仍以对话/模拟环境为主**。
- **能力维度与 LongMemEval/MemoryAgentBench 有重叠但不可直接对齐**。
- **没有 action-coupled environment loop**。
- **没有安全/隐私维度**。
- **benchmark 规模相对小**。

## 与主线 F 的关系

- **LongMemEval**：LongMemEval 五能力；MemBench 两层×两场景×三指标。
- **MemoryAgentBench**：MemBench 更偏综合能力；MemoryAgentBench 更偏 incremental multi-turn。
- **PersistBench**：MemBench 测能力；PersistBench 测安全失败。
- **MemoryArena**：MemBench 不是 action loop。

## 对 RQ1 的意义

RQ1 可以用 MemBench 补足：

- 不只测 factual recall，还要测 reflective memory。
- 不只测 participation，还要测 observation。

## 可复用点

- factual/reflective taxonomy。
- participation/observation 场景。
- effectiveness/efficiency/capacity 指标。
- 多场景数据构造。

## 成本

- 评测成本取决于场景数量。
- 没有统一 token/latency 表。
- 主要报告能力指标，不报告系统 build cost。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/membench.pdf`
- ACL Findings 2025（论文记录）
