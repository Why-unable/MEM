---
type: evidence
paper_id: timem
title: "TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/timem.pdf"
source_version: "ACL Findings 2026"
pages_checked: "1-10"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - consolidation
  - temporal-memory
---

# TiMem 证据卡

## 结论先行

- TiMem 把时间连续性作为记忆组织的第一性原则：用 **Temporal Memory Tree (TMT)** 从 raw observations 逐层抽象到 persona representation。
- 它用 semantic-guided consolidation（training-free）和 complexity-aware recall 在不同层次间选择。
- LoCoMo **75.30%**，LongMemEval-S **76.88%**；recalled memory length 比 Mem0 降低 **52.20%**。

## 研究问题与定位

长期对话 agent 面临：

- 历史不断增长；
- 时间结构被压平；
- 记忆碎片化，长期个性化不稳定。

TiMem 要回答：

> 能否用时间层次树组织记忆，让不同复杂度的 query 访问不同抽象层？

## 方法拆解

### Temporal Memory Tree

- 从原始对话观察开始，逐层抽象：
  - raw observations
  - episodic/semantic summaries
  - 更高层 persona representation
- 时间连续性决定节点如何连接/合并。

### Semantic-guided consolidation

- 不 fine-tune LLM。
- 用语义相似度/引导把下层记忆整合到上层。
- 兼顾时间顺序和语义一致性。

### Complexity-aware recall

- 简单 query：高层/摘要记忆。
- 复杂 query：更深层/更细粒度记忆。
- 用 adaptive planner 在 accuracy 和 token 之间权衡。

来源：PDF p.2-6，Method。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval-S。
- Baselines：MemoryBank、Mem0、A-Mem、MemoryOS、MemOS。
- Backbones：GPT-4o-mini、GPT-4o。
- Metrics：LLM-Judge accuracy、F1、ROUGE-L、memory tokens、latency。

### LoCoMo

| 方法 | Overall LLJ |
|---|---:|
| A-Mem | 51.29 |
| Mem0 | 57.79 |
| MemoryOS | — |
| **TiMem** | **75.30** |

- F1 **54.40**，ROUGE-L **54.68**。
- Memory context 511.25 tokens/query。
- 比 Mem0 的 1,070.10 tokens 低 **52.20%**。
- P50 recall latency **2.35s**。

来源：PDF p.7，Table 1，Table 6。

### LongMemEval-S

| 方法 | Overall LLJ |
|---|---:|
| A-Mem | 55.44 |
| Mem0 | 67.56 |
| **TiMem** | **76.88** |

- 使用 GPT-4o 作为 answer model 时，TiMem 可到 **78.96%**。
- Memory context 1,270.62 tokens/query。
- P50 latency **1.76s**。

来源：PDF p.7，Table 2，Table 6。

### 层次/召回消融

- Adaptive planner 比固定 scope 更好：LoCoMo 75.30 vs 73.38，LongMemEval 76.88 vs 75.00。
- 去掉 hierarchy 或 recall gating 会降低 accuracy。
- 树深度/召回预算需要按数据集调参。

来源：PDF p.7-8，Table 3-4。

## 真正的新意

1. **时间层次树**：不是平面 summary 堆叠，而是按时间/抽象层级组织。
2. **complexity-aware recall**：query 复杂度决定访问哪一层。
3. **training-free consolidation**：不 fine-tune。
4. **persona representation 作为树顶**：长期个性化有明确抽象层。

## 局限与威胁

- **树构建/维护成本**：LLM consolidation calls 可能很高；论文报告 amortized calls，但长期部署需核对。
- **层次深度敏感**：树太深/太浅都可能损失 accuracy。
- **主要是对话 QA**：没有 action-coupled、多模态、安全评测。
- **没有显式遗忘/删除**：树节点只增不减。
- **persona 抽象可能丢证据**：需要 provenance/回溯机制。
- **Mem0 的 temporal F1 仍可能更强**（不同 backbone 下）。

## 与主线 D 的关系

- **RecMem**：RecMem 决定何时 consolidation；TiMem 定义 consolidation 后的时间层次。
- **TierMem**：TierMem 用 summary/raw 两层 + provenance；TiMem 用多层时间树。
- **Nemori**：Nemori 用 prediction error 决定保留；TiMem 用时间/语义层次组织。
- **EM-LLM/REMem**：都强调事件/时间结构，但 TiMem 更偏长期 persona 抽象。

## 对 RQ1 的意义

TiMem 提供了“层次结构 + 访问策略”的组合证据：

- 结构（TMT）和访问（complexity-aware recall）必须一起设计。
- RQ1 应报告 memory context length 和 latency，而不只是 accuracy。

## 可复用点

- Temporal Memory Tree schema。
- semantic-guided consolidation。
- complexity-aware recall / adaptive planner。
- LLJ + F1 + ROUGE-L + memory tokens + latency 的多指标报告。

## 成本

- LoCoMo：511.25 tokens/query，P50 2.35s。
- LongMemEval-S：1,270.62 tokens/query，P50 1.76s。
- Consolidation calls：论文 Table 5 报告 amortized 成本，需回表核对。
- 存储：树节点增长，未给统一 storage 指标。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/timem.pdf`
- ACL Anthology / Findings 2026（见论文记录）
