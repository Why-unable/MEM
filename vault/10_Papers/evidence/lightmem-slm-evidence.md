---
type: evidence
paper_id: lightmem-slm
title: "Lightweight LLM Agent Memory with Small Language Models"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/lightmem-slm.pdf"
source_version: "ACL 2026 Long Papers; DOI 10.18653/v1/2026.acl-long.588"
pages_checked: "1-9"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - small-language-models
  - efficiency
---

# LightMem (SLM) 证据卡

## 结论先行

- 这是与 ICLR 2026 LightMem **不同**的另一篇同名工作：它用 Small Language Models 驱动记忆检索、写入和长期巩固。
- 结构是 STM / MTM / LTM，在线固定检索预算，离线做 consolidation；目标是把记忆操作的延迟压到百毫秒级。
- LoCoMo 上平均 F1 比 A-Mem 高约 **2.5**；检索 **83ms**、端到端 **581ms**。

## 研究问题与定位

现有记忆系统有两类极端：

- 纯检索：在线开销低，但 query construction/candidate filtering 不稳定；
- 用大模型反复做在线记忆操作：准确率好，但延迟随交互累积。

LightMem (SLM) 要回答：

> 能否用 SLM 做记忆控制，在固定计算预算下兼顾准确率和低延迟？

## 方法拆解

### 三级记忆

| 层 | 作用 |
|---|---|
| STM | 当前对话上下文 |
| MTM | 可复用交互摘要 |
| LTM | 已巩固知识 |

- 用 user identifiers 支持多用户独立检索和增量维护。

### 在线检索

- 固定 retrieval budget。
- 两阶段：
  1. vector coarse retrieval；
  2. semantic consistency re-ranking。

### 离线 consolidation

- 从交互中抽象可复用 evidence。
- 增量整合到 LTM。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmark：LoCoMo。
- Backbones：不同规模模型。
- Baselines：A-Mem 等 memory systems。
- Metrics：F1、retrieval latency、end-to-end latency。

### 结果

- 平均 F1 比 A-Mem 高约 **2.5**。
- 检索延迟中位数 **83ms**。
- 端到端延迟中位数 **581ms**。
- 在不同模型规模上保持一致增益。

来源：PDF p.1 abstract；p.6-8，Table 2/3。

## 真正的新意

1. **SLM 作为 memory controller**：不是用大模型做每次记忆操作。
2. **固定 retrieval budget**：在线成本可控。
3. **两阶段检索**：vector coarse + semantic consistency re-rank。
4. **STM/MTM/LTM**：兼顾即时上下文、可复用摘要和长期知识。

## 局限与威胁

- **与 ICLR 2026 LightMem 同名**：引用时必须区分，容易混淆。
- **主要是 LoCoMo**：没有 action-coupled、多模态、安全。
- **SLM 能力上限**：复杂 query/长文档可能不如大模型控制。
- **没有显式遗忘/删除**：LTM 只增不减。
- **离线 consolidation 成本**：在线低延迟不等于总成本低。

## 与主线 C 的关系

- **LightMem (ICLR 2026)**：同名不同工作；ICLR 版是 sensory/STM/LTM + sleep-time；本篇是 SLM-driven STM/MTM/LTM。
- **LightWM**：都强调 SLM/轻量控制；LightWM 是 procedure-centric working memory。
- **Mem0**：Mem0 用 LLM extraction；本篇用 SLM 降在线成本。
- **SimpleMem**：都关注压缩/效率，但本篇更偏 SLM 控制。

## 对 RQ1 的意义

LightMem (SLM) 支持“控制器大小”也是效率轴：

- 记忆系统的成本不仅来自存储/检索，还来自控制器的模型大小。
- RQ1 应报告 controller latency 和 end-to-end latency。

## 可复用点

- STM/MTM/LTM 三级 schema。
- fixed retrieval budget。
- vector coarse + semantic consistency re-ranking。
- 多用户 user identifier 隔离。
- 83ms/581ms 的延迟报告。

## 成本

- 检索中位 83ms。
- 端到端中位 581ms。
- 离线 consolidation 成本未完整量化。
- 没有 storage/build token 表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/lightmem-slm.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.588/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.588
