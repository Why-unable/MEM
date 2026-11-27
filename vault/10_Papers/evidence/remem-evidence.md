---
type: evidence
paper_id: remem
title: "REMem: Reasoning with Episodic Memory in Language Agent"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/remem.pdf"
source_version: "ICLR 2026 conference paper"
pages_checked: "1-10"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - episodic-memory
  - agentic-retrieval
---

# REMem 证据卡

## 结论先行

- REMem 把 episodic memory 从“检索事件文本”推进到“事件级回忆 + 推理”：离线构建 time-aware gist/fact 混合图，在线用 agentic retriever 迭代检索。
- 相对 Mem0/HippoRAG 2，episodic recollection **+3.4%**、episodic reasoning **+13.4%**（绝对）。
- 对不可回答问题有更稳健的 refusal，是 RQ1/评测的重要参照。

## 研究问题与定位

现有 agent memory 主要是 semantic memory，缺少对具体事件及其时空上下文的回忆和推理。REMem 要回答：

> agent 能否像人类一样，记住具体经历并在事件之间推理？

## 方法拆解

### Offline indexing

- 把经验转成 hybrid memory graph：
  - time-aware gists（事件摘要）
  - facts（实体/属性）
  - 时间/语义/同义关系
- 保留事件的时间上下文，而不是只存事实。

### Online inference

- agentic retriever 用一组工具迭代检索：
  - semantic retrieval
  - lexical retrieval
  - graph exploration
  - temporal reasoning
- 不是一次 top-k，而是多步证据收集。

来源：PDF p.3-5，Method，Table 1。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、REALTALK、Complex-TR、Test of Time。
- Backbone：GPT-4.1-mini + NV-Embed-v2。
- Baselines：Full-Context、Qwen3-Embed、NV-Embed-v2、Mem0、Graphiti、HippoRAG 2。
- Metrics：F1、BLEU-1、LLM-J、EM、refusal precision/recall。

### Episodic recollection

LoCoMo：

| 方法 | F1 | LLM-J |
|---|---:|---:|
| Full-Context | 37.8 | 76.7 |
| HippoRAG 2 | 39.0 | 74.0 |
| REMem-I | **42.4** | 76.2 |
| REMem-S | 41.3 | **77.5** |

REALTALK：

| 方法 | F1 | LLM-J |
|---|---:|---:|
| Full-Context | 25.3 | 65.1 |
| HippoRAG 2 | 21.9 | 55.8 |
| REMem-I | 25.6 | 63.7 |
| REMem-S | **26.2** | **65.3** |

来源：PDF p.6，Table 3。

### Episodic reasoning

Complex-TR：

| 方法 | F1 | LLM-J |
|---|---:|---:|
| Full-Context | 74.2 | 81.6 |
| HippoRAG 2 | 78.2 | 81.5 |
| REMem-I | 83.3 | **89.6** |
| REMem-S | 78.5 | 82.6 |

Test of Time：

| 方法 | EM |
|---|---:|
| HippoRAG 2 | 66.9 |
| REMem-I | **93.1** |
| REMem-S | 72.5 |

来源：PDF p.6，Table 4。

### Refusal

- LoCoMo 1,986 queries 中 446 个不可回答。
- REMem 的 refusal F1 **63.96%**，比 baseline 更高，refusals 更少（约三分之一）。

来源：PDF p.7，Table 6。

## 真正的新意

1. **episodic recollection + reasoning 分开评测**。
2. **hybrid gist/fact graph**：兼顾事件摘要和事实。
3. **agentic retriever 工具集**：semantic/lexical/graph/temporal。
4. **refusal 行为**：不仅回答，还要知道何时不知道。

## 局限与威胁

- **离线索引成本**：gist/fact 图构建需要 LLM。
- **在线多步检索延迟**：agentic retriever 比一次 top-k 更重。
- **主要是对话/阅读 benchmark**：没有 action-coupled、多模态、安全。
- **没有显式遗忘/删除**：图只增不减。
- **依赖 LLM-as-Judge**：J 指标有偏差。
- **REALTALK 上 full-context 仍然很强**：结构记忆不是全面胜出。

## 与主线 D 的关系

- **EM-LLM**：事件分割 + 两阶段检索；REMem 用 gist/fact 图 + agentic tools。
- **ARTEM**：ARTEM 用时空事件向量；REMem 用 gist/fact 图。
- **TiMem**：TiMem 用时间树；REMem 用图 + 工具。
- **TierMem**：TierMem 用 provenance 回溯；REMem 用图探索。

## 对 RQ1 的意义

REMem 支持“episodic reasoning 需要多步检索”：

- 一次 top-k 不足以回答复杂事件问题。
- RQ1 应把 retrieval steps / tool use 作为独立变量。

## 可复用点

- time-aware gist/fact 混合图。
- semantic/lexical/graph/temporal 工具集。
- episodic recollection vs reasoning 双任务评测。
- refusal precision/recall/F1。
- 与 Mem0/HippoRAG 2/Full-Context 的对照。

## 成本

- 离线索引：LLM 生成 gist/fact + 图构建。
- 在线：多步 agentic retrieval，延迟高于一次 top-k。
- 具体 token/latency 成本需回附录核对。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/remem.pdf`
- ICLR 2026（论文记录）
