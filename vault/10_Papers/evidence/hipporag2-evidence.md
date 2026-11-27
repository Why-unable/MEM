---
type: evidence
paper_id: hipporag2
title: "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/hipporag2.pdf"
source_version: "ICML 2025 / PMLR 267"
pages_checked: "1-10"
mainline: "A"
tags:
  - evidence
  - mainline-a
  - graph-rag
  - continual-learning
---

# HippoRAG 2 证据卡

## 结论先行

- HippoRAG 2 是对“图结构 RAG 会牺牲 factual memory”的直接修正：它要同时保住 factual、sense-making 和 associative memory。
- 核心是 Personalized PageRank + passage nodes + phrase/entity nodes + query-to-node linking。
- 在 QA 平均 F1 上 **59.8**，高于最强 embedding baseline NV-Embed-v2 的 **57.0**；passage recall@5 平均 **78.2**，高于 **73.4**。

## 研究问题与定位

普通 RAG 依赖向量检索，难以模拟长期记忆的关联结构。图增强 RAG 能提升 sense-making/associativity，但在简单 factual QA 上可能反而不如标准 RAG。

HippoRAG 2 要回答：

> 能否用一个图结构 RAG 同时覆盖 factual、sense-making、associative memory，而不是在它们之间取舍？

## 方法拆解

### 图结构

- **Passage nodes**：原始 passage。
- **Phrase/entity nodes**：从 passage 中抽取的短语/实体。
- **Query-to-node linking**：query 直接连接到相关 phrase/entity。
- **Passage integration**：更深层的 passage 连接，避免只靠实体图。

### 检索

- 用 Personalized PageRank 在图上传播 relevance。
- 从 query 的 seed nodes 出发，聚合 passage-level 证据。
- 使用 LLM 做在线过滤/整合。

来源：PDF p.2-4，Method。

## 实验与关键数字

### 设置

- QA reader：Llama-3.3-70B-Instruct。
- Retriever：NV-Embed-v2。
- Benchmarks：NQ、PopQA、MuSiQue、2Wiki、HotpotQA、LV-Eval、NarrativeQA。
- Baselines：BM25、Contriever、GTR、NV-Embed-v2、RAPTOR、GraphRAG、LightRAG、HippoRAG。

### QA 平均 F1

| 方法 | Avg F1 |
|---|---:|
| NV-Embed-v2 | 57.0 |
| HippoRAG | 53.1 |
| GraphRAG | 49.6 |
| RAPTOR | 48.8 |
| **HippoRAG 2** | **59.8** |

来源：PDF p.7，Table 2。

### Passage recall@5

| 方法 | Avg recall@5 |
|---|---:|
| NV-Embed-v2 | 73.4 |
| HippoRAG (reproduced) | 63.8 |
| **HippoRAG 2** | **78.2** |

来源：PDF p.7，Table 3。

### 关键细分

- 2Wiki：HippoRAG 2 比 NV-Embed-v2 **+9.5 F1**。
- LV-Eval：**+3.1 F1**。
- 在 simple QA 上也不输标准 RAG，在 multi-hop 上明显更强。

来源：PDF p.7。

### 消融

Passage recall@5 平均：

| 配置 | Avg |
|---|---:|
| Full HippoRAG 2 | **87.1** |
| w/o passage node | 81.0 |
| w/ NER to node | 74.6 |
| w/ query to node | 59.6 |
| w/o filter | 86.4 |

来源：PDF p.8，Table 4。

## 真正的新意

1. **同时优化 factual / sense-making / associative**，而不是只追求 multi-hop。
2. **passage integration**：避免图结构只保留实体关系而丢失原文证据。
3. **PPR + query-to-node**：比单纯向量检索更适合关联记忆。
4. **图结构不是目的**：如果图损害 factual memory，就不算真正的 memory。

## 局限与威胁

作者没有单独 Limitations 章节；以下是分析判断：

- **不是对话 agent memory**：主要是 RAG QA benchmark，不是多 session 个人记忆。
- **构图成本高**：需要 LLM 抽实体/短语、建图、在线 PPR。
- **依赖 passage/entity 抽取质量**：抽取错误会传播。
- **没有更新/遗忘机制**：图是静态/增量构建，缺少版本化删除。
- **评测以 QA 为主**：没有 action-coupled、多模态、安全评测。

## 与主线 A 的关系

- **A-Mem**：A-Mem 是 agent 自组织笔记；HippoRAG 2 是文档 RAG 图。
- **MAGMA**：MAGMA 用 semantic/temporal/causal/entity 多图；HippoRAG 2 更偏 passage/entity PPR。
- **MemGAS**：MemGAS 多粒度检索；HippoRAG 2 图检索。
- **MRAgent**：MRAgent 主动重构；HippoRAG 2 仍是单轮 PPR 检索。

## 对 RQ1 的意义

HippoRAG 2 提供了一个关键对照：

- 图结构可以提升 associative/multi-hop，但必须同时保住 factual。
- RQ1 不能只比较“图 vs 向量”，还要比较“图是否保留原始证据”。

## 可复用点

- passage node + phrase/entity node 的图 schema。
- Personalized PageRank 检索。
- query-to-node linking。
- passage recall@5 + QA F1 双指标。
- 与 NV-Embed-v2/GraphRAG/HippoRAG 的强 baseline 对照。

## 成本

- 构图：LLM 抽取 + 图索引；论文 Appendix F 有 token/time/memory 分析（待核对）。
- 检索：PPR + passage integration；比普通向量检索更重。
- 没有统一的 build/query 成本表在正文。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/hipporag2.pdf`
- PMLR：https://proceedings.mlr.press/v267/gutierrez25a.html
- arXiv：https://arxiv.org/abs/2502.14802
