---
type: evidence
paper_id: beyondmillion
title: "Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/beyondmillion.pdf"
source_version: "ICLR 2026 conference paper"
pages_checked: "1-9"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - benchmark
  - long-context
---

# BEAM / LIGHT 证据卡

## 结论先行

- BEAM 把长期记忆压力推到 **128K–10M tokens**：100 个长对话、2,000 个验证问题、10 类记忆能力。
- 即使 1M context 模型（含 RAG）也会随对话变长而退化。
- LIGHT 用 long-term episodic + short-term working memory + scratchpad，相对最强 baseline 提升 **3.5%–12.69%**。

## 研究问题与定位

现有长期记忆 benchmark 往往叙事不连贯、领域窄、只测简单 recall。BEAM 要回答：

> 在 10M token、连贯、多主题的对话中，LLM 的长期记忆是否仍然有效？

## Benchmark 设计

- 自动生成最长 10M tokens 的连贯对话。
- 100 conversations。
- 2,000 validated questions。
- 10 类 memory abilities。
- 长度档：128K / 500K / 1M / 10M（摘要范围）。

来源：PDF p.1-5，Benchmark design。

## Method · LIGHT

- long-term episodic memory
- short-term working memory
- scratchpad for salient facts
- 三个记忆系统互补。

来源：PDF p.5-7，Method。

## 关键发现

- 1M context 模型 + RAG 仍随对话变长而退化。
- LIGHT 在不同 backbone 上稳定提升：
  - 平均 **+3.5%–12.69%**
- 说明“更长上下文 ≠ 更好记忆”。

来源：PDF p.1 abstract；p.7-9，Results。

## 真正的新意

1. **10M token 规模**。
2. **10 类记忆能力**。
3. **BEAM + LIGHT 同时提供 benchmark 和 method**。
4. **长上下文模型的退化曲线**。

## 局限与威胁

- **合成/生成式长对话**：与真实用户历史仍有差距。
- **10 类能力定义**与 LongMemEval/MemoryAgentBench 不完全一致。
- **计算成本高**：10M token 评测昂贵。
- **没有 action-coupled/安全维度**。
- **LIGHT 是 method baseline**，不是通用 solution。

## 与主线 F 的关系

- **LongMemEval**：LongMemEval 115K/1.5M；BEAM 到 10M。
- **MemoryArena**：BEAM 不是 action loop。
- **MemoryAgentBench**：BEAM 更偏规模/能力；MemoryAgentBench 更偏 incremental competencies。
- **Minerva**：BEAM 是端到端长对话；Minerva 是原子能力诊断。

## 对 RQ1 的意义

BEAM 是规模压力测试：

- 结构记忆在超长上下文下的优势应在这里验证。
- 必须报告 token/latency，因为 10M 评测成本极高。

## 可复用点

- BEAM 生成框架。
- LIGHT 三层记忆。
- 128K–10M 长度档。
- 10 类 memory ability。

## 成本

- 10M token 评测成本高。
- LIGHT 增加 memory 模块成本。
- 论文没有统一 GPU 成本表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/beyondmillion.pdf`
- ICLR 2026（论文记录）
