---
type: evidence
paper_id: magma
title: "MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents"
status: evidence-checked
checked_at: 2026-11-26
source_pdf: "data/agent-memory-2025/pdfs/magma.pdf"
source_version: "ACL 2026 Long Papers, DOI 10.18653/v1/2026.acl-long.1709"
pages_checked: "1-9"
tags:
  - evidence
  - mainline-a
  - agent-memory
  - graph-memory
---

# MAGMA 证据卡

## 结论先行

- MAGMA 把 agent memory 从“单一语义相似度图”拆成 **semantic / temporal / causal / entity** 四个正交关系图，再用 intent-aware traversal 选择检索路径。
- 它是主线 A 里最直接回应 RQ1 的论文之一：在 LoCoMo 和 LongMemEval 上，结构化多图记忆总体优于 full-context，同时把长上下文压缩到千级 token。
- 但 full-context 仍在 single-session-assistant 和 knowledge-update 类别上更强，说明“结构记忆全面替代长上下文”并不成立。

## 研究问题与定位

论文的出发点是：现有 Memory-Augmented Generation 系统大多把记忆放在一个扁平存储里，主要靠 semantic similarity 检索，无法区分“发生了什么”“什么时候发生”“为什么发生”“涉及谁”。

MAGMA 的目标是把这些关系显式建模为多个图，并把检索从静态 top-k 变成 policy-guided traversal。

## 方法拆解

### 数据层

- **Event node**：`n_i = (content, timestamp, dense vector, attributes)`。
- **Semantic graph**：内容相似的 event 之间建边。
- **Temporal graph**：按时间戳形成严格有序链。
- **Causal graph**：由 LLM 在异步 consolidation 中推断“原因 → 结果”边。
- **Entity graph**：把 event 连接到抽象 entity 节点，支持跨时间线的实体一致性。
- 同时维护 vector database 和 sparse keyword index。

来源：PDF p.4-6，Section 3.2-3.4。

### 写入与更新

MAGMA 使用双流：

1. **Fast path / synaptic ingestion**：事件分割、向量索引、更新时间链，不做阻塞式 LLM 推理。
2. **Slow path / structural consolidation**：后台 worker 分析近邻，异步推断 causal / entity 边。

来源：PDF p.6，Algorithm 2-3。

### 查询流程

1. **Query analysis**：把 query 分类为 `WHY / WHEN / ENTITY`，解析时间窗口，生成 dense embedding 和 sparse keywords。
2. **Anchor identification**：用 dense、lexical、temporal 三路信号做 Reciprocal Rank Fusion，选 anchor nodes。
3. **Adaptive traversal**：用 heuristic beam search，转移分数同时考虑关系类型与 query intent 的结构匹配，以及语义相似度。
4. **Context synthesis**：对 causal 子图做 topological sort，序列化时为每个节点保留 timestamp、content 和 reference ID；用 salience-based token budgeting 压缩低相关节点。

来源：PDF p.4-6，Section 3.3。

## 实验与关键数字

### LoCoMo（GPT-4o-mini，LLM-as-Judge）

| 方法 | Overall | Temporal | Adversarial |
|---|---:|---:|---:|
| Full Context | 0.481 | 0.562 | 0.205 |
| A-MEM | 0.580 | 0.474 | 0.616 |
| MemoryOS | 0.553 | 0.422 | 0.428 |
| Nemori | 0.590 | 0.649 | 0.325 |
| **MAGMA** | **0.700** | **0.650** | **0.742** |

来源：PDF p.7, Table 1。

MAGMA 相对其他方法的总体提升幅度为 18.6%–45.5%（论文表述，PDF p.7）。

### LongMemEval（平均上下文超过 100K tokens）

| 方法 | Average | 每 query token |
|---|---:|---:|
| Full-context | 55.0% | ~101K |
| Nemori | 56.2% | 3.7–4.8K |
| **MAGMA** | **61.2%** | **0.7–4.2K** |

分类结果中的关键反例：

- Single-session-assistant：Full-context **89.3%** > MAGMA 83.9%。
- Knowledge-update：Full-context **78.2%** > MAGMA 66.7%。
- Single-session-preference：MAGMA **73.3%** > Full-context 6.7%。
- Temporal-reasoning：MAGMA **45.1%** > Full-context 42.1%。

来源：PDF p.8, Table 2。

### 效率

| 方法 | Build time (h) | Tokens/query (K) | Latency (s) |
|---|---:|---:|---:|
| Full Context | N/A | 8.53 | 1.74 |
| A-MEM | 1.01 | **2.62** | 2.26 |
| MemoryOS | 0.91 | 4.76 | 32.68 |
| Nemori | 0.29 | 3.46 | 2.59 |
| **MAGMA** | 0.39 | 3.37 | **1.47** |

来源：PDF p.8, Table 3。这里的 token/query 与 LongMemEval 的 101K 口径不同，不能直接混用。

### 消融

| 配置 | Judge score |
|---|---:|
| Full MAGMA | **0.700** |
| w/o Adaptive Policy | 0.637 |
| w/o Causal Links | 0.644 |
| w/o Temporal Backbone | 0.647 |
| w/o Entity Links | 0.666 |

来源：PDF p.8, Table 4。

单图消融（PDF p.9, Table 5）：

- Causal only：0.590
- Temporal only：0.577
- Entity only：0.531
- Full MAGMA：0.700

## 真正的新意

1. **关系维度正交化**：不是把所有关系混在一个图里，而是 semantic / temporal / causal / entity 分开建模。
2. **query intent 参与检索**：`WHY` 查询偏向 causal，`WHEN` 偏向 temporal，`ENTITY` 偏向 entity。
3. **双流更新**：把低延迟写入和高成本结构推理拆开，这是系统工程上的关键设计。
4. **可追溯上下文**：序列化时保留 timestamp、content、reference ID，并用 causal topological sort 组织证据。

## 局限与威胁

- **图质量依赖 LLM**：causal/entity 边由 LLM 推断，可能 hallucinate 或漏边，并传播到检索（PDF p.9）。
- **多图存储和工程复杂度高**：比扁平向量库更难部署，作者承认在资源受限环境下可能不适用（PDF p.9）。
- **没有显式遗忘/删除/冲突裁决**：temporal graph 只提供顺序，不提供过期或回滚。
- **评测范围有限**：主要是长对话和 agentic benchmark，未覆盖多模态或异构 observation streams（PDF p.9）。
- **full-context 仍是强 baseline**：在 single-session-assistant 和 knowledge-update 上更强。
- **与 A-Mem 的对比不完全公平**：A-Mem 使用自己的实现/摘要策略，MAGMA 的图构建成本另计。

## 与主线 A 其他论文的关系

- **A-Mem**：MAGMA 把 A-Mem 的单一语义链接扩展为多关系图，并把 A-MEM 作为主要 baseline。
- **G-Memory**：两者都是多层图，但 G-Memory 的层是 insight/query/interaction，MAGMA 的层是关系类型。
- **MemGAS**：MemGAS 关注“粒度选择”，MAGMA 关注“关系类型选择”；两者可以组合成“多粒度 × 多关系”的记忆。
- **MRAgent**：MRAgent 进一步把“选择哪条路径”变成多轮 active reconstruction；MAGMA 仍是单轮/有限步的 policy-guided traversal。

## 对 RQ1 的意义

MAGMA 是 RQ1 目前最强的支持证据之一：

- **结构记忆在 multi-hop、temporal、adversarial 上明显优于长上下文。**
- **结构记忆能用 0.7–4.2K tokens 达到接近或超过 101K token full-context 的平均效果。**
- **但优势是类别依赖的**：single-session-assistant 和 knowledge-update 仍由 full-context 胜出。

因此 RQ1 不应问“结构记忆是否更好”，而应问：

> 在哪些任务维度上，结构记忆的收益超过其构建成本和信息损失？

MAGMA 的 ablation 还提示：**adaptive policy 的贡献大于单一关系图**（去掉 policy 掉 0.063，去掉 entity 只掉 0.034）。这支持“access policy 比 storage structure 更关键”的假设。

## 可复用点

- 四类关系图 schema：semantic / temporal / causal / entity。
- intent classification + temporal parsing + dense/sparse RRF anchor selection。
- 结构匹配 + 语义相似度的 beam search 转移分数。
- causal topological sort + provenance + token budgeting 的 context synthesizer。
- fast path / slow path 分离的写入架构。
- 用 build time、tokens/query、latency 三个维度报告系统成本。

## 待核对

- [ ] 核对 Table 3 的 full-context token/query 口径（8.53K 与 LongMemEval 101K 的区别）。
- [ ] 用官方 ACL 版本复核所有数字（本卡已使用 ACL PDF）。
- [ ] 检查代码是否开源以及 graph consolidation 的 prompt 细节。
- [ ] 把 `papers.json` 的 DOI 从 arXiv DOI 更新为 `10.18653/v1/2026.acl-long.1709`。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/magma.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.1709/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.1709
- OpenReview：https://openreview.net/forum?id=ktbwLLO9nX
