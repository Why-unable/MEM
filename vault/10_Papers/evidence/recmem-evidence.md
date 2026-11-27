---
type: evidence
paper_id: recmem
title: "RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/recmem.pdf"
source_version: "ACL Findings 2026"
pages_checked: "1-10"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - consolidation
  - efficiency
---

# RecMem 证据卡

## 结论先行

- RecMem 的核心不是“怎么抽取记忆”，而是 **“什么时候值得调用 LLM 去巩固记忆”**。
- 新交互先进入 subconscious memory layer，用轻量 embedding 检索；只有当语义相似交互持续 **recurrence** 时，才触发 LLM extraction/consolidation。
- 在 LoCoMo 上，GPT-4.1-mini 构建 token 从 Mem0 的 1,520.8K 降到 **193.2K**（-87.3%），同时 overall accuracy 仍高于 Mem0/A-Mem。

## 研究问题与定位

现有 memory systems 对每条 incoming interaction 都调用 LLM 做 extraction/summarization，构建成本极高。RecMem 要回答：

> 能否把“记忆巩固”从 eager/每条都做，改成 recurrence-triggered？

## 方法拆解

### 1. Subconscious memory layer

- 新交互先不做 LLM extraction。
- 用轻量 embedding 编码，支持快速检索。
- 作为“潜意识”层，保留原始交互的可检索性。

### 2. Recurrence-triggered consolidation

- 当语义相似的交互反复出现（sustained recurrence），才调用 LLM。
- 理由：复发意味着这是一个有丰富信息的语义 cluster，值得抽取/总结。
- 触发后生成 episodic + semantic memory。

### 3. Semantic refinement

- 对 extraction 遗漏的细粒度事实做恢复/补充。
- 减少“压缩后丢细节”的问题。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval-S。
- Backbones：GPT-4o-mini、GPT-4.1-mini。
- Baselines：Full Context、Naive RAG、MemoryOS、Mem0、A-Mem。
- Metrics：LLM-judge accuracy、construction token、query token。

### LoCoMo

GPT-4.1-mini：

| 方法 | Overall | Construct Token (K) |
|---|---:|---:|
| Full Context | 84.18 | 0 |
| MemoryOS | 67.60 | 400.7 |
| Mem0 | 62.92 | 1,520.8 |
| A-Mem | 68.83 | 1,459.9 |
| **RecMem** | **81.10** | **193.2** |

- 相对 Mem0：construction token **-87.3%**。
- 相对 A-Mem：**-86.8%**。
- Full Context 仍略高（84.18），说明 RecMem 没有在所有任务上超过长上下文。

来源：PDF p.7，Table 1；p.8。

### LongMemEval-S

GPT-4.1-mini：

| 方法 | Overall | Construct Token (K) |
|---|---:|---:|
| Full Context | 66.20 | 0 |
| MemoryOS | 74.4 | 669.22 |
| Mem0 | 71.20 | 1,626.54 |
| A-Mem | 71.60 | 1,264.25 |
| **RecMem** | **76.80** | **365.49** |

- LongMemEval-S 上 RecMem 超过所有 memory systems，同时 construction token 仍低。
- 相对 Mem0 construction token 降低约 **77.5%**。

来源：PDF p.7，Table 2；p.8。

### 消融

- 去掉 recurrence trigger / semantic refinement 会降低 accuracy 或增加 token。
- 阈值 θ 的敏感性实验显示 accuracy 平滑变化，但 token cost 随阈值明显变化。

来源：PDF p.8-9，Figure 2/4。

## 真正的新意

1. **把 consolidation 从“每条都做”改成“复发才做”**：时间/触发条件成为一等设计变量。
2. **subconscious layer**：未巩固的原始交互仍可检索，不会因为延迟巩固而完全丢失。
3. **semantic refinement**：修复 extraction 的细粒度事实损失。
4. **构建成本大幅下降**：不是靠更小模型，而是靠更少 LLM 调用。

## 局限与威胁

- **低频但重要的事件可能被延迟/漏掉**：recurrence 触发假设“复发=重要”，但一次性安全/偏好事件可能不复发。
- **阈值敏感**：θ 需要按数据集调参。
- **Full Context 在 LoCoMo 仍更强**：RecMem 不是全面超越长上下文。
- **没有显式遗忘/删除**：只决定何时 consolidation，不决定何时 forget。
- **评测以对话 QA 为主**：没有 action-coupled、多模态、安全。

## 与主线 D 的关系

- **Nemori**：Nemori 用 prediction error 决定什么值得记住；RecMem 用 recurrence 决定何时巩固。
- **TierMem**：TierMem 用 query-time escalation 决定证据粒度；RecMem 用 write-time trigger 决定是否 consolidation。
- **TiMem**：TiMem 用时间树做层次巩固；RecMem 用复发触发。
- **EMA**：EMA 用 MemDecider 过滤；RecMem 用延迟 consolidation 降成本。

## 对 RQ1 / RQ3 的意义

### RQ1

RecMem 证明“何时巩固”可以显著改变成本-accuracy Pareto：

- 不是所有交互都值得 LLM 处理。
- RQ1 应把 consolidation trigger 作为独立变量。

### RQ3

- RecMem 没有删除机制；它只是延迟写入。
- RQ3 可以问：什么条件下应该 **不写入**，而不是写入后再删除？

## 可复用点

- subconscious layer + embedding retrieval。
- recurrence-triggered consolidation。
- semantic refinement。
- construction token vs accuracy 的 Pareto 报告。
- 与 Mem0/A-Mem/MemoryOS 的构建成本对照。

## 成本

- LoCoMo GPT-4.1-mini：construct 193.2K tokens vs Mem0 1,520.8K（-87.3%）。
- LongMemEval-S：construct 365.49K vs Mem0 1,626.54K（约 -77.5%）。
- Query token：LoCoMo 2.75K；LongMemEval 5.89K（GPT-4.1-mini）。
- 延迟/存储未完整报告。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/recmem.pdf`
- ACL Anthology：https://aclanthology.org/2026.findings-acl.250/（如页面可用）
