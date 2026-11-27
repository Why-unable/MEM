---
type: evidence
paper_id: interdependent
title: "MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/interdependent.pdf"
source_version: "ICML 2026 / PMLR 306"
pages_checked: "1-10"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - benchmark
  - action-coupled-memory
---

# MemoryArena 证据卡

## 结论先行

- MemoryArena 把记忆评测从“回忆过去”推进到“记忆是否指导未来行动”：multi-session Memory-Agent-Environment loop。
- 四类任务：web navigation、preference-constrained planning、progressive information search、sequential formal reasoning。
- 核心发现：在 LoCoMo 等长上下文 benchmark 上接近饱和的 agent，在 interdependent agentic 任务上表现很差。

## 研究问题与定位

现有 memory benchmark 有两类：

- 只测 memorization/recall，不测记忆如何指导行动；
- 只测单 session agent，不需要长期记忆。

MemoryArena 要回答：

> 当记忆和行动紧密耦合时，agent 是否真的能用过去经验解决未来子任务？

## Benchmark 设计

### 任务结构

- 每个任务由显式相互依赖的 subtasks 组成。
- agent 先执行一些 action，获得反馈并写入 memory。
- 后续 subtask 需要检索/使用前面学到的经验。
- 不是一次性 QA，而是 multi-session loop。

### 四个环境

1. Bundled Web Shopping
2. Group Travel Planning
3. Progressive Web Search
4. Math/Physics Formal Reasoning

来源：PDF p.1-5，Benchmark design。

## 关键发现

- LoCoMo 等长上下文 benchmark 上接近饱和的 agent，在 MemoryArena 上表现很差。
- 说明“记忆 recall 分数”不能代表“记忆能指导行动”。
- 记忆必须与 environment feedback、action selection 结合。

来源：PDF p.1 abstract；p.6-9，Results。

## 真正的新意

1. **action-coupled memory**：记忆评测进入 agent-environment loop。
2. **interdependent multi-session**：子任务之间有依赖，不能独立回答。
3. **四类环境**：web、planning、search、formal reasoning。
4. **暴露 benchmark gap**：LoCoMo 饱和 ≠ agentic memory 可用。

## 局限与威胁

- **环境/任务工程复杂**：评分与 agent scaffold 耦合。
- **主要是 Web/规划/推理**：没有多模态、安全、隐私。
- **benchmark 新**：与 LoCoMo/LongMemEval 不可直接比较。
- **scaffold 敏感**：不同 agent 框架可能改变结果。

## 与主线 F 的关系

- **LongMemEval**：测“记忆能否回答”；MemoryArena 测“记忆能否指导行动”。
- **MemoryAgentBench**：MemoryAgentBench 更偏 incremental competencies；MemoryArena 更偏 environment loop。
- **BEAM**：BEAM 是长对话压力测试；MemoryArena 是 action-coupled 任务。
- **PersistBench**：PersistBench 测安全失败；MemoryArena 测任务失败。

## 对 RQ1 的意义

RQ1 应至少包含一个 action-coupled benchmark：

- 否则会高估结构记忆在真实 agent 任务中的价值。
- 需要报告 task success、subtask completion、memory usage、runtime。

## 可复用点

- Memory-Agent-Environment loop。
- 四类 interdependent tasks。
- task success vs memory recall 的对照。
- 与 LoCoMo 饱和模型的 gap 分析。

## 成本

- 评测 runtime 高（agent loop）。
- 没有统一 token/latency 表；MemoryArena 更关注 task success。
- 环境运行成本需单独报告。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/interdependent.pdf`
- PMLR 306（ICML 2026）
