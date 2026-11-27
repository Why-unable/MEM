---
type: evidence
paper_id: memrec
title: "MemRec: Collaborative Memory-Augmented Agentic Recommender System"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/memrec.pdf"
source_version: "ACL 2026 Long Papers"
pages_checked: "1-9"
mainline: "E"
tags:
  - evidence
  - mainline-e
  - recommender-system
  - collaborative-memory
---

# MemRec 证据卡

## 结论先行

- MemRec 把推荐系统中的 memory 从“孤立的用户/物品语义记忆”扩展到 **collaborative memory**：用户-物品共现和社区关系。
- 它把记忆管理从推理中解耦：轻量 `LM_Mem` 在后台维护 collaborative memory graph，重型 `LLM_Rec` 只接收蒸馏后的高信号上下文。
- 在 Books / Goodreads / MovieTV / Yelp 四个数据集上，H@1 相对最佳 baseline 提升 **14.91% / 28.98% / 19.75% / 15.77%**。

## 研究问题与定位

LLM 推荐 agent 的用户/物品 memory 通常彼此孤立，忽略 collaborative signals。直接共享 collaborative memory 又会导致 context overload、噪声和成本。

MemRec 要回答：

> 能否用协作记忆图 + 轻量管理器，把 collaborative signal 蒸馏给推荐 LLM？

## 方法拆解

### Collaborative memory

- 连接用户/物品/邻居/共现关系。
- 不是单一用户历史，而是社区级关系信号。

### 解耦架构

- `LM_Mem`：轻量语言模型，后台管理、合成 collaborative memory graph。
- `LLM_Rec`：重型推荐模型，只接收 distilled high-signal context。

### 目标

- 降低 context overload。
- 保留 collaborative signal。
- 减少在线推理成本。

来源：PDF p.3-6，Method。

## 实验与关键数字

### 设置

- Datasets：Amazon Books、Amazon Goodreads、MovieTV、Yelp。
- Baselines：LightGCN、SASRec、P5、Vanilla LLM、iAgent、i2Agent、AgentCF、RecBot。
- Metrics：Hit@K、NDCG@K。

### 主结果（H@1）

| Dataset | Best baseline H@1 | MemRec H@1 | Relative |
|---|---:|---:|---:|
| Books | 0.4453（i2Agent） | **0.5117** | **+14.91%** |
| Goodreads | 0.3099（i2Agent） | **0.3997** | **+28.98%** |
| MovieTV | 0.4912（i2Agent） | **0.5882** | **+19.75%** |
| Yelp | 0.4205（i2Agent） | **0.4868** | **+15.77%** |

来源：PDF p.7，Table 2-3。

### 效率

- 解耦后，在线只查询 distilled collaborative memory，避免重型 LLM 直接处理原始图。
- 论文报告优于 monolithic agent 的 Pareto frontier。
- 具体 latency 见 Table 5（待逐项核对）。

来源：PDF p.7-8。

## 真正的新意

1. **collaborative memory**：从个体语义到群体关系。
2. **memory management / reasoning 解耦**：LM_Mem + LLM_Rec。
3. **collaborative graph 蒸馏**：只把高信号上下文交给推理模型。
4. **推荐任务上的 memory 评测**：Hit@K/NDCG@K。

## 局限与威胁

- **推荐领域专用**：不是通用 agent memory。
- **协作记忆隐私**：用户-物品关系可能敏感；权限未展开。
- **图维护成本**：LM_Mem 后台管理仍需计算。
- **没有显式遗忘/删除**：协作图只增不减。
- **benchmark 是离线推荐**：在线用户反馈/冷启动未充分验证。

## 与主线 E 的关系

- **Evoking/PersonaAgent**：个体个性化；MemRec 群体协作信号。
- **LTS**：LTS 跨团队共享中间步骤；MemRec 共享用户-物品关系。
- **MemoryOS/EverMemOS**：系统层 memory；MemRec 推荐领域 memory。
- **TierMem**：粒度选择；MemRec 管理/推理解耦。

## 对 RQ1/RQ4 的意义

- RQ1：推荐任务中，collaborative signal 是结构记忆的一种。
- RQ4：多用户共享记忆的权限/隐私是直接问题。

## 可复用点

- collaborative memory graph。
- LM_Mem + LLM_Rec 解耦。
- distilled high-signal context。
- Hit@K/NDCG@K 评测。
- 与 i2Agent/AgentCF 等强 baseline 对照。

## 成本

- LM_Mem 后台管理成本 + LLM_Rec 在线推理。
- 在线上下文显著压缩（定性），具体 token/latency 见 Table 5/8。
- 图存储随用户/物品增长。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memrec.pdf`
- ACL Anthology 2026（论文记录）
