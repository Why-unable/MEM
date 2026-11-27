---
type: evidence
paper_id: minerva
title: "Minerva: A Programmable Memory Test Benchmark for Language Models"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/minerva.pdf"
source_version: "ICML 2025 / PMLR 267"
pages_checked: "1-9"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - benchmark
  - programmable-tests
---

# Minerva 证据卡

## 结论先行

- Minerva 把 memory 能力拆成可编程的 atomic tests：search、recall、edit、match、compare、compute、stateful processing。
- 它有 **1,110** 个测试，上下文约 **4K**，并支持 composite tests 组合多个原子能力。
- 它解决传统 data benchmark 的静态、易过拟合、难解释问题：失败时可以定位到具体能力。

## 研究问题与定位

传统 memory benchmark 多为手工 QA，难以解释“模型到底缺哪种能力”。Minerva 要回答：

> 能否自动生成可解释、可组合的 memory tests，定位模型的 memory 能力缺口？

## Benchmark 设计

### Atomic tasks

- search
- recall
- edit
- match
- compare
- compute
- stateful processing

### Composite tests

- 把多个 atomic 能力组合成更复杂的 memory 任务。
- 测试模型在结构化 blocks 上维护状态/操作的能力。

### 规模

- 1,110 个测试
- 约 4K 上下文

来源：PDF p.1-6，Benchmark design。

## 关键发现

- Minerva 能精细区分不同模型的 memory 能力，而不是只给一个总分。
- 传统 passkey/key-value/NIAH 只覆盖 search 的一小部分。
- composite tests 暴露了 atomic tests 看不到的组合失败。

来源：PDF p.1 abstract；p.6-9，Results。

## 真正的新意

1. **programmable memory tests**：自动生成、可解释。
2. **atomic + composite**：既能定位能力，又能测组合。
3. **超出 passkey/NIAH**：覆盖 edit/match/compare/compute/stateful。
4. **可复现/可扩展**：不是静态手工数据。

## 局限与威胁

- **上下文较小（约 4K）**：不是长期记忆系统 benchmark。
- **更偏“模型如何使用上下文”**：不等同于 agent memory 的 store/retrieve/forget。
- **不是 action-coupled**：没有 environment loop。
- **没有安全/隐私维度**。
- **任务合成性**：真实世界噪声可能不同。

## 与主线 F 的关系

- **LongMemEval**：LongMemEval 测长期对话能力；Minerva 测上下文 memory 的原子能力。
- **MemoryAgentBench**：MemoryAgentBench 有 selective forgetting；Minerva 更偏上下文操作。
- **BEAM**：BEAM 测规模；Minerva 测能力分解。
- **MemoryArena**：MemoryArena 测 action；Minerva 测 computation。

## 对 RQ1 的意义

Minerva 可以作为“机制诊断”而不是最终排行榜：

- 如果结构记忆在 multi-hop 上失败，Minerva 可以定位是 search、compare 还是 stateful processing 的问题。
- RQ1 应把 Minerva 作为 ablation/诊断工具。

## 可复用点

- atomic task taxonomy。
- composite tests。
- programmable generation。
- 1,110 tests / 4K context 的设计。

## 成本

- 测试自动生成成本低。
- 推理成本取决于模型/测试数。
- 没有系统 build cost。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/minerva.pdf`
- PMLR 267（ICML 2025）
