---
type: evidence
paper_id: evoking
title: "Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/evoking.pdf"
source_version: "ICLR 2026 conference paper"
pages_checked: "1-9"
mainline: "E"
tags:
  - evidence
  - mainline-e
  - personalization
  - dual-process
---

# Evoking / RF-Mem 证据卡

## 结论先行

- Evoking 把个性化记忆检索建模为人类记忆的双过程：**Familiarity**（快速、粗粒度）与 **Recollection**（慢速、链式重构）。
- RF-Mem 用 similarity 的均值/熵衡量 familiarity，高 familiarity 直接 top-K；低 familiarity 才进入 recollection path。
- 在 PersonaMem 的 32K / 128K / 1M 语料上，RF-Mem 都取得最佳 overall accuracy，同时把延迟控制在接近 one-shot retrieval 的水平。

## 研究问题与定位

现有个性化记忆要么全量塞入 prompt（贵），要么一次相似度检索（浅）。Evoking 要回答：

> 能否像人类一样，根据“熟悉度”自适应选择快检索或深重构？

## 方法拆解

### Familiarity path

- 计算 query 与 memory 的 similarity 分布。
- 用均值/熵衡量 familiarity。
- 高 familiarity：直接 top-K retrieval。

### Recollection path

- 低 familiarity 时激活。
- 对候选记忆聚类。
- 用 α-mix 与 query 迭代扩展证据。
- 模拟 deliberate contextual reconstruction。

### Adaptive switch

- 由 familiarity uncertainty 决定走哪条路径。
- 在固定 budget/latency 下平衡 recall 和噪声。

来源：PDF p.3-6，Method。

## 实验与关键数字

### 设置

- Benchmarks：PersonaMem（32K/128K/1M）、PersonaBench、LongMemEval。
- Baselines：Zero Memory、Full Context、Dense Retrieval、Recollection、RF-Mem。
- Retriever backbones：MiniLM、MPNet、BGE。
- Metrics：accuracy、Recall@K、latency。

### PersonaMem

- RF-Mem overall accuracy：
  - 32K：**0.6350**
  - 128K：**0.5394**
  - 1M：最佳 overall（具体值见 Table 1）
- 在每个 corpus scale 上都是最佳 overall。
- 相比 always-on recollection：
  - 32K：5.09ms vs 7.09ms
  - 128K：4.27ms vs 7.86ms
  - 1M：6.28ms vs 7.12ms

来源：PDF p.6-7，Table 1。

### PersonaBench / LongMemEval

- PersonaBench：RF-Mem 在 overall Recall@5/Recall@10 上匹配或超过最佳 baseline。
- LongMemEval：RF-Mem 在 Recall@10 上稳定（如 MiniLM 0.7351 vs 0.7136）。
- Latency 接近 familiarity（9–15ms），但 recall 更高。

来源：PDF p.7-8，Table 2-3。

## 真正的新意

1. **双过程检索**：familiarity + recollection，不是单一 top-k。
2. **熵驱动切换**：根据不确定性决定是否深挖。
3. **α-mix 迭代重构**：在 embedding space 里逐步扩展证据。
4. **固定 budget/latency**：不是无限增加检索深度。

## 局限与威胁

- **familiarity 校准**：均值/熵阈值需要调参。
- **recollection 延迟**：低 familiarity query 仍会增加延迟。
- **主要是个性化 benchmark**：没有 action-coupled、多模态、安全。
- **没有显式遗忘/删除**：用户记忆只增不减。
- **隐私**：个性化记忆的访问控制未展开。

## 与主线 E 的关系

- **PersonaAgent**：PersonaAgent 用 persona 连接 memory 和 action；Evoking 用双过程选择检索路径。
- **MemRec**：MemRec 是协作记忆；Evoking 是个人记忆检索。
- **TierMem**：TierMem 用 sufficiency router；Evoking 用 familiarity uncertainty。
- **MRAgent**：MRAgent 用 LLM action selection；Evoking 用 entropy-gated dual path。

## 对 RQ1 的意义

Evoking 支持“访问策略”在个性化任务中的价值：

- 不是检索更多，而是知道何时需要深挖。
- RQ1 应把 retrieval depth / latency 作为独立变量。

## 可复用点

- familiarity 均值/熵信号。
- familiarity/recollection 双路径。
- α-mix 迭代扩展。
- fixed budget/latency 的 accuracy–latency Pareto。

## 成本

- 32K：5.09ms vs 7.09ms（always-on recollection）。
- 128K：4.27ms vs 7.86ms。
- 1M：6.28ms vs 7.12ms。
- 没有 build/storage 成本表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/evoking.pdf`
- ICLR 2026（论文记录）
