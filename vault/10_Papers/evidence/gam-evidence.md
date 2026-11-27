---
type: evidence
paper_id: gam
title: "GAM: Hierarchical Graph-based Agentic Memory for LLM Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/gam.pdf"
source_version: "ACL 2026 Long Papers; DOI 10.18653/v1/2026.acl-long.1600"
pages_checked: "1-10"
mainline: "A"
tags:
  - evidence
  - mainline-a
  - graph-memory
  - consolidation
---

# GAM 证据卡

## 结论先行

- GAM 的核心是把 **记忆编码** 和 **记忆整合** 解耦：当前对话先进入 event progression graph，只有发生 semantic shift 时才整合到 topic associative network。
- 这样既保留快速感知，又减少 transient noise 对长期知识结构的干扰。
- 在 LoCoMo 上 GPT-4o-mini Average F1 **43.14**；在 LongDialQA 上 Qwen2.5-7B Average F1 **12.55**，比 MemoryOS 高 **86%**。

## 研究问题与定位

现有 memory 系统有两类问题：

- 统一 stream-based memory 更新快，但容易被 transient noise 干扰；
- 离散 structured memory 保留好，但难以适应叙事演化。

GAM 要回答：

> 能否让“当前事件流”和“长期主题结构”分开，只在语义偏移时整合？

## 方法拆解

### 双层图

1. **Event Progression Graph**
   - 保存当前对话/事件链。
   - 快速写入，保留时间顺序和局部上下文。
2. **Topic Associative Network**
   - 保存长期主题、实体和跨事件关联。
   - 只在 semantic shift 时整合 event graph。

来源：PDF p.2-4，Method。

### Semantic-Event-Triggered Consolidation

- 用 semantic boundary detector 判断是否发生主题/事件偏移。
- 偏移触发时，才把 event progression 合并到 topic network。
- 避免每条新信息都改写长期图。

### Retrieval

- Graph-guided, multi-factor retrieval：同时考虑 topic、event、role、time 等因素。
- 不是单纯 embedding top-k。

来源：PDF p.4-6。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongDialQA。
- Backbones：Llama-3.2-3B、Qwen2.5-7B/14B、GPT-4o-mini。
- Baselines：MemoryBank、ReadAgent、MemGPT、MemoryOS、Mem0、A-Mem。
- Metrics：F1、BLEU-1；成本：tokens/query、latency。

### LoCoMo

- GPT-4o-mini：Average F1 **43.14**，为最高。
- Qwen2.5-7B：Temporal F1 比 Mem0 高 **18%+**。
- 重要反例：GPT-4o-mini 上 Mem0 的 Temporal F1 **56.42** > GAM **51.96**，说明强 backbone 下直接检索原始时间线索可能更好。

来源：PDF p.7，Table 1。

### LongDialQA

- Qwen2.5-7B：Average F1 **12.55**，比 MemoryOS 高 **86%**。
- 在多 party、speaker switching 频繁的叙事中优势明显。

来源：PDF p.7，Table 2。

### 成本

- LoCoMo 上平均 **1,370 tokens/query**。
- 论文报告在 token 成本上优于多个 baseline，同时保持较高 F1。

来源：PDF p.9，Table 4。

### 消融

- 去掉 event progression graph、semantic-event-triggered window、fixed window 等都会下降。
- 论文报告平均 F1 最高 **40.00** 的消融配置（具体配置需回 Table 3 核对）。

来源：PDF p.8，Table 3。

## 真正的新意

1. **编码/整合解耦**：不是所有新信息都立即改写长期结构。
2. **event graph + topic network 双层**：局部事件流和长期主题网分开。
3. **semantic shift 触发 consolidation**：用语义偏移而不是固定时间窗口。
4. **multi-factor retrieval**：topic/event/role/time 共同参与。

## 局限与威胁

- **时间线索可能被压缩**：GPT-4o-mini 上 Mem0 Temporal F1 更高，说明 GAM 的结构化整合会丢失部分精确时间信息。
- **Open-Domain 较弱**：论文承认这是 GAM 最难的类别。
- **没有显式遗忘/删除**：长期主题网只增不减。
- **主要是对话 benchmark**：没有 action-coupled、多模态、安全评测。
- **语义偏移检测依赖模型/阈值**：错误触发会污染 topic network。

## 与主线 A 的关系

- **A-Mem**：A-Mem 是原子笔记 + 链接；GAM 是 event/topic 双层图。
- **MAGMA**：MAGMA 是多关系图；GAM 是时间事件 + 主题网络。
- **MemGAS**：MemGAS 多粒度；GAM 是事件/主题两层。
- **TierMem**：TierMem 在 query time 选择 summary/raw；GAM 在 write time 决定何时整合。

## 对 RQ1 的意义

GAM 支持“结构记忆的收益来自整合时机”：

- 不是“图越复杂越好”，而是“何时把短期事件合并到长期结构”。
- RQ1 应把 **consolidation trigger** 作为独立变量。

## 可复用点

- event progression graph + topic associative network 的双层 schema。
- semantic-event-triggered consolidation。
- graph-guided multi-factor retrieval。
- tokens/query + F1 的 Pareto 报告。
- 与 Mem0/MemoryOS 的强 baseline 对照。

## 成本

- Query：1,370 tokens/query（LoCoMo）。
- Build：event graph + topic network + semantic boundary detection；具体 LLM 调用成本未在正文汇总。
- 没有完整 build time/storage 表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/gam.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.1600/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.1600
