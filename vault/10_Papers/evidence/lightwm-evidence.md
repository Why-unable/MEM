---
type: evidence
paper_id: lightwm
title: "LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/lightwm.pdf"
source_version: "ICML 2026 conference paper"
pages_checked: "1-9"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - small-language-models
  - working-memory
---

# LightWM 证据卡

## 结论先行

- LightWM 面向 **SLM agent 的 procedure-centric 长程任务**：把 working memory 分成 task-level global memory 和 subtask-level local memory。
- 它用一次离线 LLM induction 构建 task-family schema，不在线调用大 LLM，也不更新 SLM 参数。
- ALFWorld valid_unseen 上 Qwen3-4B 达到 **0.910** success，同设置 baseline **<0.320**。

## 研究问题与定位

SLM 在长程 procedure-centric 任务中容易丢失决策相关状态；现有 working-memory 方法依赖非结构化自然语言 summary，会丢事实、产生 state drift、累积错误。

LightWM 要回答：

> 能否用结构化、分层的 working memory，让 SLM 在不训练的情况下稳定执行长流程？

## 方法拆解

### 双层 working memory

1. **Task-level global memory**
   - 保存任务级目标、约束、全局状态。
2. **Subtask-level local memory**
   - 保存当前子任务的状态/观察。
   - 直接条件化 SLM 的 action selection。
   - 通过 structured updates 从新观察更新。

### Offline schema induction

- 每个 task family 用少量成功轨迹，离线让强 LLM 归纳 schema。
- 运行时不调用在线 LLM，也不更新 SLM。
- schema 负责结构化 memory 的读写格式。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmark：ALFWorld（valid_unseen；valid_seen 用于 schema induction）。
- Backbone：Qwen3-4B 等 SLM。
- Baselines：ReAct、Simply Summarize、HiAgent、MemGPT。
- Metric：success rate。

### 主要结果

- Qwen3-4B + LightWM：**0.910** success。
- 同设置 prompting/working-memory baselines：**<0.320**。
- 说明结构化 working memory 对 SLM 的收益非常大。

来源：PDF p.1 abstract；p.6-7，Table 1。

### 消融

- 去掉 task-level / subtask-level memory、structured update、offline schema induction 会显著下降。
- schema induction 的质量决定 memory 结构是否可用。

来源：PDF p.7-8，Ablation。

## 真正的新意

1. **task-level + subtask-level 双层 working memory**。
2. **offline schema induction**：一次构建，运行时零在线 LLM。
3. **structured updates**：不是自然语言 summary，减少 state drift。
4. **小模型优先**：不靠大模型在线控制。

## 局限与威胁

- **procedure-centric**：主要面向有重复 workflow 的任务族；开放对话/科研任务未验证。
- **依赖 schema induction**：需要少量成功轨迹和强 LLM 离线构建。
- **benchmark 单一**：ALFWorld 为主；没有多模态、多 agent、安全。
- **没有长期 episodic memory**：working memory 不是完整长期记忆。
- **schema 迁移**：task family 变化可能需要重新 induction。

## 与主线 C 的关系

- **LightMem-SLM**：两者都用 SLM/轻量控制；LightWM 是 working memory，LightMem-SLM 是长期对话记忆。
- **Mem0/MemoryOS**：LightWM 不做长期存储，只做任务内 working memory。
- **Hippocampus**：Hippocampus 优化检索底层；LightWM 优化任务状态结构。

## 对 RQ1 的意义

LightWM 说明“结构”不一定是图/数据库：

- task/subtask schema 也是一种结构记忆。
- 对小模型，结构化 working memory 可能比更大上下文更有效。

## 可复用点

- task-level / subtask-level 双层 schema。
- offline schema induction。
- structured memory updates。
- SLM + working memory 的 success rate 对照。

## 成本

- 运行时无在线 LLM 调用（除 SLM 本身）。
- 一次性离线 induction 成本未完整量化。
- 主要报告 success rate，没有统一 token/latency 表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/lightwm.pdf`
- ICML 2026（论文记录）
