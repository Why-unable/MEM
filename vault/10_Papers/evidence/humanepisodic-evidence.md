---
type: evidence
paper_id: humanepisodic
title: "Human-inspired Episodic Memory for Infinite Context LLMs"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/humanepisodic.pdf"
source_version: "ICLR 2025 conference paper"
pages_checked: "1-10"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - episodic-memory
  - event-segmentation
---

# EM-LLM 证据卡

## 结论先行

- EM-LLM 用 **Bayesian surprise + graph-theoretic boundary refinement** 在线切分事件，再用两阶段检索访问事件。
- 它把“无限上下文”问题转化为“事件级记忆 + 时间连续检索”，在 LongBench / ∞-Bench 上超过 InfLLM 和 RAG。
- 最醒目的规模证据：可以检索 **10M tokens**，远超 full-context 模型的计算能力。

## 研究问题与定位

LLM 处理超长序列时缺乏人类式的事件组织，导致长程连贯性和检索效率下降。EM-LLM 要回答：

> 能否像人类一样，把 token 流切成 episodic events，并按事件检索？

## 方法拆解

### 事件分割

- 用 Bayesian surprise 检测事件边界。
- 用 graph-theoretic boundary refinement 修正边界。
- 在线构建事件记忆，而不是离线固定 chunk。

### 两阶段检索

1. 相似度检索：找到与 query 相关的事件。
2. 时间连续检索：把相邻事件一起取回，保持上下文连贯。

来源：PDF p.2-5，Method。

### 与 RAG 的区别

- RAG 是固定 chunk + 相似度。
- EM-LLM 是事件边界 + 事件级检索 + 时间邻接扩展。

## 实验与关键数字

### 设置

- Benchmarks：LongBench、∞-Bench（Passkey.Retrieval 到 10.2M tokens）、人类事件分割播客。
- Baselines：InfLLM、full-context、NV-Embed-v2 RAG。
- 多种 base LLM。

### 主要结果

- 在 LongBench/∞-Bench 上优于 InfLLM 和 RAG。
- 在多数任务上超过 full-context 模型。
- 成功在 **10M tokens** 规模做检索。
- 事件分割与人类感知事件有较强相关性。

来源：PDF p.1 abstract；p.6-9，Results。

## 真正的新意

1. **事件边界是记忆结构的第一性问题**。
2. **Bayesian surprise + graph refinement** 的在线分割。
3. **时间连续检索**：不仅找相似事件，还取相邻事件。
4. **10M token 规模**：证明事件级记忆可以扩展到 full-context 不可行的规模。

## 局限与威胁

- **分割质量依赖 surprise 信号**：边界错误会传播。
- **主要是长文本/长对话**：没有 action-coupled、多模态、安全。
- **没有显式遗忘/删除**：事件记忆持续增长。
- **两阶段检索仍有超参数**：top-k、时间邻接范围。
- **没有统一成本表**：token/latency/storage 需二次核对。

## 与主线 D 的关系

- **REMem**：REMem 也是 event/episode 级，但用 gist/fact 图和 agentic retriever。
- **ARTEM**：ARTEM 用 temporal/spatial/entity 事件向量 + STEM。
- **TiMem**：TiMem 用时间树；EM-LLM 用事件分割 + 时间邻接检索。
- **E-mem**：E-mem 保留未压缩 context；EM-LLM 用事件边界组织。

## 对 RQ1 的意义

EM-LLM 支持“事件结构”对长上下文任务的价值：

- 不是简单 chunk，而是语义/时间边界。
- RQ1 应把 event segmentation quality 作为独立变量。

## 可复用点

- Bayesian surprise event segmentation。
- graph-theoretic boundary refinement。
- 相似度 + 时间连续的两阶段检索。
- 10M token 压力测试。
- 与人类事件分割的相关性分析。

## 成本

- 事件分割在线进行；retrieval 是两阶段。
- 10M token 规模可运行，但具体 token/latency/storage 成本未在摘要中给出。
- 需要回附录核对。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/humanepisodic.pdf`
- ICLR 2025（论文记录）
