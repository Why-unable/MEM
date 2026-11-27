---
type: evidence
paper_id: longmemeval
title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/longmemeval_iclr.pdf"
source_version: "ICLR 2025 conference paper"
pages_checked: "1-10"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - evaluation
  - long-term-memory
---

# LongMemEval 证据卡

## 结论先行

- LongMemEval 把长期记忆评测拆成五种能力：**information extraction、multi-session reasoning、temporal reasoning、knowledge update、abstention**。
- 它用 500 个手工问题，把历史扩到 115K / 1.5M tokens，直接暴露 commercial assistants 和 long-context LLM 的 **30%–60%** 性能下降。
- 它不只提出 benchmark，还给出 indexing / retrieval / reading 三阶段的设计分析，是主线 F 的“事实标准”之一。

## 研究问题与定位

现有长期对话 benchmark 往往：

- 历史太短；
- 只测简单 recall；
- 不覆盖 multi-session、knowledge update、abstention；
- 没有区分 memory 的 indexing / retrieval / reading 阶段。

LongMemEval 要回答：

> chat assistant 在持续交互中，能否准确提取、跨 session 推理、处理时间、更新知识，并在不知道时 abstain？

## Benchmark 设计

### 五种能力

| 能力 | 含义 |
|---|---|
| Information Extraction (IE) | 从历史中提取用户/助手信息 |
| Multi-session Reasoning (MR) | 聚合两个以上 session 的信息 |
| Temporal Reasoning (TR) | 使用时间元数据和相对时间 |
| Knowledge Update (KU) | 识别用户状态/事实的更新 |
| Abstention (ABS) | 对不可回答问题选择不答 |

来源：PDF p.1-2。

### 规模

- 500 个手工创建问题。
- 历史是可扩展的 user-assistant chat。
- LongMemEval-S：约 **115K tokens/question**。
- LongMemEval-M：**500 sessions**，约 **1.5M tokens**。
- 每个问题都带 evidence statements / evidence sessions。

来源：PDF p.2-3，Table 1。

### 评测框架

论文把 memory assistant 拆成：

1. **Indexing**：value / key 的粒度与结构。
2. **Retrieval**：query 构造、检索策略。
3. **Reading**：如何把检索结果交给 LLM 使用。

四个控制点：value、key、query、reading strategy。

来源：PDF p.3-5。

## 关键实验发现

### 1. 长上下文模型会显著退化

- commercial assistants 和 long-context LLMs 在持续交互中出现 **30%–60%** 的性能下降。
- 在更简单的 setting 中，一些系统也只有 30%–70% accuracy。

来源：PDF p.1-2，p.4。

### 2. round 比 session 更适合作为记忆粒度

- 把 session 切成 round 存储，通常比直接存 session 更好。
- 进一步压缩成 individual user facts 会损失整体性能，但能提升 multi-session reasoning。

来源：PDF p.5-6，Section 5.2。

### 3. fact-augmented keys 提升 recall 和 QA

- 用 extracted user facts 扩展 key：
  - recall@k **+9.4%**
  - downstream QA accuracy **+5.4%**

来源：PDF p.6，Section 5.3。

### 4. time-aware query expansion 提升 temporal reasoning

- 把 timestamp 与 fact 显式关联，并缩小搜索范围。
- temporal reasoning 的 memory recall 提升 **6.8%–11.3%**（使用强 LLM 做 query expansion）。

来源：PDF p.6，Section 5.4，Table 4。

### 5. reading strategy 仍然重要

- 即使 memory recall 完美，如何把 retrieved items 交给 LLM 仍然影响很大。
- Chain-of-Note + structured data format 可提升最多 **10 个绝对点**。

来源：PDF p.6，Section 5.5。

### 6. LLM-as-Judge 可用但要校准

- prompt-engineered GPT-4o judge 与人类专家有较高一致性。
- 在 single-session-preference/abstention 上略有偏差。

来源：PDF p.10，Table 6。

## 真正的新意

1. **五能力拆分**：长期记忆不再是一个单一 accuracy。
2. **可扩展历史**：从 115K 到 1.5M，支持压力测试。
3. **三阶段设计分析**：indexing / retrieval / reading，而不是只报端到端分数。
4. **可操作的 design insights**：round granularity、fact-augmented keys、time-aware query expansion、Chain-of-Note。

## 局限与威胁

作者没有单独 Limitations 章节；以下是分析判断：

- **主要是对话 QA**：没有 action-coupled memory、工具调用、多 agent 共享记忆。
- **没有安全/隐私维度**：不测 leakage、sycophancy、poisoning。
- **历史是构造/扩展的**：与真实用户长期历史的熵和噪声仍有差距。
- **LLM-as-Judge 依赖**：judge 偏差会影响结论。
- **abstention 的定义/评分**：不同系统对“不知道”策略不同，可能影响可比性。
- **没有统一成本指标**：token/latency 不是 benchmark 的核心输出。

## 与主线 F 其他 benchmark 的关系

- **MemoryArena**：LongMemEval 测“记忆能否回答”，MemoryArena 测“记忆能否指导行动”。
- **PersistBench**：LongMemEval 测能力，PersistBench 测记忆持久化的安全风险。
- **MemoryAgentBench**：LongMemEval 的五能力 + MemoryAgentBench 的 test-time learning/selective forgetting。
- **BEAM**：LongMemEval 是 115K/1.5M；BEAM 推到 128K–10M，并加入 10 类能力。
- **MemBench/MemoryBench**：LongMemEval 更偏 personal chat QA；MemBench 更综合，MemoryBench 更偏 continual learning。

## 对 RQ1 的意义

LongMemEval 应该作为 RQ1 的核心评测之一，但必须按能力拆分报告：

```text
IE / MR / TR / KU / ABS
```

不能只报 overall，否则会掩盖“结构记忆在 temporal/update 上强、在 single-hop 上弱”的模式。

## 可复用点

- 五能力 taxonomy。
- 500 问 + evidence statements/sessions 的设计。
- 三阶段 memory 分析框架。
- round/session/fact 粒度对照。
- fact-augmented key + time-aware query expansion。
- Chain-of-Note / structured reading。

## 成本

- LongMemEval-S：约 115K tokens/question。
- LongMemEval-M：500 sessions，约 1.5M tokens。
- 论文主要报告 accuracy，不是统一 token/latency 成本；RQ1 需要额外记录。

## 待核对

- [ ] 核对 LongMemEval-M 的具体 token 统计。
- [ ] 核对 judge 与人类一致性的细节。
- [ ] 核对 abstention 的评分规则。
- [ ] 与 MemoryAgentBench / BEAM 的题目重叠分析。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/longmemeval_iclr.pdf`
- OpenReview：https://openreview.net/forum?id=pZiyCaVuti
- 代码/数据：https://github.com/xiaowu0162/LongMemEval
