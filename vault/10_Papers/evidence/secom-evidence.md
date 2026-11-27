---
type: evidence
paper_id: secom
title: "On Memory Construction and Retrieval for Personalized Conversational Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/secom.pdf"
source_version: "ICLR 2025 conference paper"
pages_checked: "1-10"
mainline: "A"
tags:
  - evidence
  - mainline-a
  - memory-granularity
  - retrieval
---

# SeCom 证据卡

## 结论先行

- SeCom 的核心发现是：**记忆粒度本身就是架构变量**。turn-level、session-level、summary-based 各有缺陷。
- 它用 conversation segmentation 把长期对话切成主题连贯的 segment，再用 LLMLingua-2 压缩去噪。
- 在 LoCoMo 上 GPT4Score **71.57**，高于最强 baseline **65.92**；在 Long-MT-Bench+ 上 **88.81**，高于 **85.14**。

## 研究问题与定位

现有长期对话 memory 通常按 turn 或 session 切分，再检索/摘要。SeCom 研究：

> 记忆单元应该切多细？prompt compression 是否能作为检索去噪机制？

它把 memory construction 和 retrieval 分开分析，强调 segment-level 记忆。

## 方法拆解

### 记忆构建

1. 用 conversation segmentation model 把长期对话切成 topically coherent segments。
2. 每个 segment 作为一个 memory unit。
3. 用 LLMLingua-2 对 memory unit 做 compression-based denoising。
4. 检索时按 segment 粒度返回上下文。

来源：PDF p.2-5，Method。

### 关键设计

- **不是固定 turn/session**：segment 由主题边界决定。
- **压缩不是摘要**：LLMLingua-2 保留 token 级信息，减少噪声。
- **分割模型可训练/可迁移**：在 DialSeg711、TIAGE、SuperDialSeg 上评估。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、Long-MT-Bench+。
- Baselines：Zero/Full History、Turn-Level、Session-Level、SumMem、RecurSum、ConditionMem、MemoChat。
- Retrieval budget：LoCoMo 4K tokens；Long-MT-Bench+ 1K tokens。
- Backbones：GPT-4o-mini / Mistral-7B 等。

### LoCoMo

| 方法 | GPT4Score |
|---|---:|
| Full History | 54.15 |
| Turn-Level (BM25) | 65.58 |
| ConditionMem | 65.92 |
| MemoChat | 65.10 |
| **SeCom (BM25, GPT-4 Seg)** | **71.57** |
| SeCom (MPNet, GPT-4 Seg) | 69.33 |

来源：PDF p.6，Table 1。

### Long-MT-Bench+

| 方法 | GPT4Score |
|---|---:|
| Full History | 63.85 |
| Turn-Level (MPNet) | 84.91 |
| MemoChat | 85.14 |
| **SeCom (MPNet, GPT-4 Seg)** | **88.81** |

来源：PDF p.6，Table 1。

### Segmentation

- 在 DialSeg711、SuperDialSeg、TIAGE 上，SeCom 的 segmentation model 优于基线。
- 说明 segment 质量不是偶然，而是可训练的组件。

来源：PDF p.8，Table 4。

### Denoising ablation

- 去掉 compression-based denoising 会降低 retrieval accuracy 和 QA。
- 压缩率 75% 左右是论文分析的重点设置。

来源：PDF p.8，Table 2。

## 真正的新意

1. **把“粒度”作为 memory architecture 的一等变量**。
2. **主题连贯 segment** 比固定 turn/session 更贴近语义单元。
3. **compression 作为 denoising**，而不是 summary。
4. **segmentation 模型可迁移到多个对话分割数据集**。

## 局限与威胁

作者没有单独 Limitations 章节；以下是分析判断：

- **依赖 segmentation 质量**：分割错误会传播到检索。
- **压缩可能丢失细节**：虽然比 summary 保留更多 token，但仍是有损的。
- **主要是对话 QA**：没有 action-coupled、多模态、安全评测。
- **没有更新/遗忘机制**：memory unit 一旦构建，缺少版本化/删除。
- **backbone/retriever 敏感**：Table 1 显示 BM25/MPNet 差异很大。

## 与主线 A 的关系

- **MemGAS**：SeCom 是 segment 级；MemGAS 进一步做 session/turn/summary/keyword 多粒度。
- **A-Mem**：A-Mem 是原子笔记 + 链接；SeCom 是 segment + 去噪。
- **HippoRAG 2**：两者都关注 retrieval 结构，但 HippoRAG 2 是图/RAG，SeCom 是粒度/压缩。
- **TierMem**：TierMem 在 query time 选择 summary/raw；SeCom 在 write time 选择 segment。

## 对 RQ1 的意义

SeCom 支持“粒度是结构的一部分”：

- 不是“图 vs 向量”，而是“turn vs session vs segment”。
- RQ1 应把 memory unit granularity 作为独立变量。

## 可复用点

- conversation segmentation + compression 的两阶段构建。
- segment-level retrieval budget 设置。
- 在多个 dialogue segmentation 数据集上验证分割器。
- 与 turn/session/summary 三种粒度的对照。

## 成本

- Retrieval context budget：4K tokens（LoCoMo）/ 1K tokens（Long-MT-Bench+）。
- Segmentation 和 compression 有额外构建成本；论文没有统一 GPU 成本表。
- 没有报告 build/query token 的完整拆分。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/secom.pdf`
- ICLR Proceedings：https://proceedings.iclr.cc/paper_files/paper/2025/hash/e56f394bbd4f0ec81393d767caa5a31b-Abstract-Conference.html
- arXiv：https://arxiv.org/abs/2502.05589
