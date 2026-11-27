---
type: evidence
paper_id: memoryos
title: "Memory OS of AI Agent"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/memoryos.pdf"
source_version: "EMNLP 2025 Main; DOI 10.18653/v1/2025.emnlp-main.1318"
pages_checked: "1-9"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - memory-os
  - hierarchical-memory
---

# MemoryOS 证据卡

## 结论先行

- MemoryOS 把操作系统式的分层存储/更新/检索引入 agent memory：short-term、mid-term、long-term personal memory 三级。
- 更新机制是它最像“OS”的部分：short→mid 用 dialogue-chain FIFO，mid→long 用 segmented page organization。
- LoCoMo 上相对 baseline 平均 **F1 +49.11%**、**BLEU-1 +46.18%**；同时 LLM calls 明显少于 A-Mem。

## 研究问题与定位

LLM 固定上下文窗口导致长期记忆和个性化不足。现有方法缺少统一的存储、更新、检索和生成管理。MemoryOS 要回答：

> 能否用操作系统式的层次存储和更新策略，统一管理 agent 的短期/中期/长期记忆？

## 方法拆解

### 四模块

1. Memory Storage
2. Memory Updating
3. Memory Retrieval
4. Memory Generation

### 三级存储

| 层 | 作用 | 更新 |
|---|---|---|
| Short-term | 当前对话/短期上下文 | 对话链 FIFO → mid-term |
| Mid-term | 可复用对话片段 | segmented page organization → long-term |
| Long-term personal | 稳定用户记忆 | 长期保留/检索 |

来源：PDF p.2-5，Method。

### 关键设计

- 用 “page” 组织 mid→long 的更新，避免逐条写入。
- 检索时按层级和 query 选择记忆。
- 目标不是单一向量检索，而是层次化 memory integration。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、GVD。
- Backbone：GPT-4o-mini。
- Baselines：LoCoMo、MemGPT、A-Mem、TiM 等。
- Metrics：F1、BLEU-1、LLM calls、recalled tokens。

### LoCoMo

- 相对 baseline 平均：
  - F1 **+49.11%**
  - BLEU-1 **+46.18%**
- 在 per-category 上，MemoryOS 在 multi-hop/temporal 等类别有优势，但并非所有类别都第一。

来源：PDF p.1 abstract；p.7-8，Table 2。

### 成本

- MemoryOS 平均 LLM calls **4.9**，A-Mem* 约 **13**。
- recalled tokens 也低于 A-Mem。
- 说明层次化 page/FIFO 更新减少了重复 LLM 调用。

来源：PDF p.8，Table 3。

### 消融

- 去掉 Mid-Term Memory（MTM）或 Long-Term Memory 会降低性能。
- 说明三级层次不是装饰，而是有实际贡献。

来源：PDF p.8，Figure 2。

## 真正的新意

1. **OS 类比落到具体机制**：FIFO、page、storage/update/retrieval/generation 四模块。
2. **三级记忆 + 动态更新**：不是静态向量库。
3. **用 LLM calls 作为系统成本指标**：比只看 token 更接近真实部署。
4. **短期→中期→长期的迁移路径**：给“巩固”一个系统实现。

## 局限与威胁

- **OS 类比强于理论保证**：没有真正的地址空间/权限/隔离。
- **主要是 LoCoMo/GVD 对话**：没有 action-coupled、多模态、多 agent 共享。
- **没有显式遗忘/删除/回滚**：长期记忆只增不减。
- **backbone 单一**：主要 GPT-4o-mini。
- **构建/存储成本未完整报告**：LLM calls 和 tokens 有，但 build time/storage 不足。

## 与主线 C 的关系

- **EverMemOS**：EverMemOS 进一步做 self-organizing MemCell/MemScene 生命周期。
- **LightMem**：LightMem 用 online/offline 解耦降成本；MemoryOS 用层次/page 更新。
- **Hippocampus**：Hippocampus 用压缩索引降检索成本；MemoryOS 用层次管理。
- **TierMem**：TierMem 在 query time 选择 summary/raw；MemoryOS 在 write time 分层。

## 对 RQ1 的意义

MemoryOS 提供了“层次结构 + 更新策略”的 baseline：

- 不是所有结构收益都来自检索；更新机制也会影响 accuracy 和 LLM calls。
- RQ1 应把 update policy 作为独立变量。

## 可复用点

- short/mid/long-term 三级存储。
- dialogue-chain FIFO。
- segmented page organization。
- LLM calls + recalled tokens 的成本分析。
- 与 MemGPT/A-Mem 的层次化对照。

## 成本

- LoCoMo：平均 4.9 LLM calls/response；A-Mem* 约 13。
- recalled tokens 低于 A-Mem。
- build time/storage 未完整报告。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memoryos.pdf`
- ACL Anthology：https://aclanthology.org/2025.emnlp-main.1318/
- DOI：https://doi.org/10.18653/v1/2025.emnlp-main.1318
