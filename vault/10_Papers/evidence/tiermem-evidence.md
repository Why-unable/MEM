---
type: evidence
paper_id: tiermem
title: "TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/tiermem.pdf"
source_version: "COLM 2026 conference paper"
pages_checked: "1-10"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - consolidation
  - compression
  - provenance
---

# TierMem 证据卡

## 结论先行

- TierMem 的核心判断是：**记忆粒度不应该在写入时固定，而应该在查询时根据证据是否充分来决定。**
- 它用两层记忆：Tier-1 是带 provenance 的摘要缓存，Tier-2 是不可变的原始 page；router 决定 `ANSWER` 还是 `ESCALATE`。
- 它在 LoCoMo 上几乎保住 raw-only accuracy（0.851 vs 0.873），同时把 input tokens 降 **54.1%**、latency 降 **60.7%**。

## 研究问题与定位

现有 memory 系统面临一个结构性矛盾：

- 压缩记忆（summary）高效，但可能在写入时丢掉未来需要的证据；
- raw history 保真，但每次查询成本高；
- 写入时不知道未来 query 需要多细的粒度。

TierMem 把这个问题定义为 **write-before-query barrier**，并把检索重新表述为：

> 在推理时分配最小充分证据：默认用 summary，只有证据不足时才升级到 raw。

## 方法拆解

### 双层记忆

| 层 | 内容 | 作用 |
|---|---|---|
| Tier-1 | summary + embedding + provenance links | 快速语义缓存 |
| Tier-2 | immutable raw pages（约 1000 tokens/page） | 可审计的原始证据源 |

- Tier-2 使用固定大小 page，保持稳定 ID，便于引用和回滚。
- Tier-1 的每条 summary 都必须记录它来自哪些 Tier-2 page，不能有“无来源摘要”。

来源：PDF p.2，Section 2.1。

### 推理协议

1. 用户 query 到达。
2. 从 Tier-1 检索 summary。
3. Router 判断 summary 是否足够：
   - `ANSWER`：直接用 summary 回答。
   - `ESCALATE`：沿 provenance links 找到 Tier-2 raw pages，必要时做 bounded global retrieval。
4. 用 raw evidence 回答后，做 verified write-back：只把有 grounding 的结论写回 Tier-1，并保留 provenance。

来源：PDF p.2-3，Section 2.2。

### Router

- 轻量 policy `π_θ(query, retrieved summaries) → ANSWER / ESCALATE`。
- 训练目标：如果 summary 缺少精确约束（否定、数字、时间、attribution），必须 escalate。
- 训练方式：SFT + GRPO；zero-shot router 协议遵循差、输出 token 多。

来源：PDF p.2，p.5，Section 5.2。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval。
- Backbone：GPT-4.1-mini。
- 对比：
  - summary-only
  - raw-only (always Tier-2)
  - router
  - router + stronger GPT-4.1-mini reference

### LoCoMo

| 指标 | TierMem router | Raw-only |
|---|---:|---:|
| Accuracy | **0.851** | 0.873 |
| Avg input tokens | **3,396** | 7,398 |
| Latency | **6.76s** | 17.18s |

- Input tokens：**-54.1%**
- Latency：**-60.7%**
- Summary-only：0.755 accuracy，UOR 15.4%。
- Router 升级 39.0% 的 query，召回 71.7% 的 oracle-hard cases。
- Routing overhead：约 **678 tokens/query**（584 input + 94.5 output）。

来源：PDF p.4-6，Table 1，Table 3。

### LongMemEval

- Static summary 在 long-range update 上会丢失近 **30%** 的可回答证据（例如 Mem0 UOR 29.6%）。
- TierMem router 通过选择性 escalation 缩小 summary-raw gap。
- 具体数值见 Table 2（本卡未逐行抄录，待二次核对）。

来源：PDF p.4-5，Table 2。

### Provenance 消融

- Linked（有 provenance）：**85.1%** accuracy。
- No-Linked（全局 BM25 回溯）：**83.6%** accuracy。
- 提升 **+1.5pp**，集中在 escalated queries：
  - Acc@R 从 77.5% → **81.7%**（+4.2pp）
  - ANSWER path 不变。

来源：PDF p.5，Table 4。

### Consolidation

- verified write-back 可以逐步提高 cheap-path coverage，而不降低 accuracy。
- 论文用 epoch-wise replay 模拟持续巩固。

来源：PDF p.5-6，Section 5.4。

## 真正的新意

1. **把“粒度选择”推迟到 query time**：直接挑战固定 chunk/summary 的设计。
2. **provenance-linked two-tier memory**：summary 和 raw evidence 之间有显式链接。
3. **learned sufficiency router**：不是“检索更多”，而是判断“证据够不够”。
4. **verified write-back**：只把有 grounding 的结论写回，兼顾在线巩固和审计。

## 局限与威胁

作者没有单独 Limitations 章节；以下是分析判断：

- **router 是新的错误源**：false HIT 会直接导致错误答案；false MISS 会增加成本。
- **Tier-2 存储仍随历史增长**：raw page 不可变，长期部署需要压缩/归档策略。
- **router 训练成本**：SFT + GRPO，且需要 oracle-hard cases/训练数据。
- **评测集中在 LoCoMo/LongMemEval**：没有 action-coupled、多模态、安全评测。
- **provenance 依赖 page ID 正确性**：page 切分/索引错误会破坏回溯。
- **没有显式 forgetting**：Tier-2 只增不减；RQ3 仍未解决。

## 与主线 D 其他论文的关系

- **RecMem**：RecMem 决定“何时巩固”；TierMem 决定“何时升级到原始证据”。
- **TiMem**：TiMem 用时间树组织层次；TierMem 用 provenance-linked two-tier 组织层次。
- **Nemori**：Nemori 用 prediction error 决定什么值得记住；TierMem 用 sufficiency router 决定什么需要回看。
- **EMA**：EMA 用 MemDecider 过滤；TierMem 用 router 升级，而不是简单过滤。

## 对 RQ1 / RQ3 的意义

### RQ1

TierMem 给出了 accuracy–token–latency 的清晰 Pareto：

- summary-only 最便宜但丢证据；
- raw-only 最准但贵；
- router 在两者之间接近 raw accuracy，同时大幅降成本。

这应成为 RQ1 实验的核心 baseline 之一。

### RQ3

- Tier-2 的不可变 page + provenance 是“可审计记忆”的基础。
- 但 TierMem 没有删除/过期/回滚机制；RQ3 可以在此基础上增加 TTL、删除传播、审计日志。

## 可复用点

- Tier-1/Tier-2 两层 schema。
- provenance links + page ID。
- ANSWER/ESCALATE router。
- verified write-back。
- UOR（Unverifiable Omission Rate）指标。
- routing overhead / hard-case recall / Acc@R 分析。

## 成本

- Query：3,396 input tokens vs raw 7,398（LoCoMo）。
- Latency：6.76s vs 17.18s。
- Router overhead：678 tokens/query。
- Build/storage：Tier-2 raw pages 线性增长；Tier-1 额外 summary/embedding。
- Training：SFT + GRPO，成本未在正文完整汇总。

## 待核对

- [ ] 核对 LongMemEval Table 2 的具体数值。
- [ ] 核对 router 训练数据规模和 GPU 成本。
- [ ] 核对 Tier-2 page 大小与存储增长。
- [ ] 检查代码/数据是否公开。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/tiermem.pdf`
- OpenReview：https://openreview.net/forum?id=svKCa4itcd
