---
type: evidence
subtype: cost-comparison
status: evidence-checked
checked_at: 2026-11-26
tags:
  - evidence
  - mainline-a
  - cost
---

# Mainline A — 成本对比

> 范围：A-Mem、G-Memory、MAGMA、MemGAS、MRAgent，以及长上下文 baseline。
> 原则：不直接比较不同论文的原始分数；先看成本口径，再看成本位置。

## 一句话结论

**成本不是谁更低，而是谁把成本放在哪里。**

- A-Mem、MemGAS：构建重、查询轻。
- MAGMA：构建与查询较均衡，查询延迟最低。
- MRAgent：构建轻、查询重，延迟随探索深度增长。
- G-Memory：为多 agent 协作和经验复用付费。
- 长上下文：构建为零，但每次查询都重新付长历史成本。

## 报告成本对照

| 方法 | 构建 / 写入 | 查询 | 延迟 | 成本位置 |
|---|---|---|---|---|
| A-Mem | 每张卡片多次 LLM 调用；总构建成本未完整报告 | 约 1.2K tokens/次；表中 1.2K–2.5K | 5.4s（GPT-4o-mini）/ 1.1s（Llama 3.2 1B） | 卡片生成、建链、演化 |
| G-Memory | 额外约 1.4M tokens（PDDL+AutoGen） | 多 agent 推理 + 记忆注入；未单列 | 未报告 | 轨迹压缩、经验蒸馏、角色投影 |
| MAGMA | 约 0.39h | 3.37K tokens/query；LongMemEval 0.7–4.2K | 1.47s/query | 后台因果/实体关系整合 |
| MemGAS | 52.9M input / 5.2M output tokens | 8,829 tokens/query | 2.55s/query | 多粒度构建与关联 |
| MRAgent | 构建轻、静态构图 | 118K tokens/sample（构建+检索） | 586s/sample；随深度增长 | 查询时多轮重建 |
| 长上下文 | 几乎为零 | LoCoMo 8.53K；LongMemEval 101K | 1.74s / 9.39s | 每次查询重复付历史成本 |

## 成本曲线

| 方法 | 构建 | 查询 | 延迟 | 工程复杂度 | 更适合 |
|---|---:|---:|---:|---:|---|
| A-Mem | 高 | 低 | 中 | 低–中 | 长历史、重复查询 |
| G-Memory | 中–高 | 高 | 未报告 | 高 | 重复的多 agent 团队任务 |
| MAGMA | 中 | 低 | 低 | 高 | 长历史、低延迟查询 |
| MemGAS | 高 | 低–中 | 中 | 中–高 | 大语料、多次查询 |
| MRAgent | 低 | 高 | 高 | 中 | 少量困难查询 |
| 长上下文 | 零 | 很高 | 低–中 | 极低 | 短历史、一次性查询 |

## 盈亏平衡

```text
总成本(N) = 构建成本 + N × 单次查询成本
N* = 构建成本 / (长上下文单次成本 - 结构记忆单次成本)
```

含义：

- `N` 小 → 长上下文更便宜。
- `N` 大且历史长 → 构建一次的结构记忆更便宜。
- 如果结构记忆的单次查询成本并不低 → 永远不划算。

粗略例子（MemGAS，LongMemEval-s）：

```text
长上下文：103.1K tokens/query
MemGAS：8.8K tokens/query
构建：52.9M input tokens

N* ≈ 52.9M / (103.1K - 8.8K) ≈ 560 queries
```

这只是一阶 token 估算，没有计入 output tokens、延迟、存储和维护成本，实际盈亏点更高。

## 关键判断

1. **A-Mem 省的是查询 token，不是构建成本。** 1.2K tokens/次不能当成总成本。
2. **G-Memory 的成本证据最弱。** 没有 build time、per-query token 和延迟，难以证明一次性任务能回本。
3. **MAGMA 的成本曲线最均衡。** 后台整合换低查询延迟，但工程复杂度最高。
4. **MemGAS 是典型“构建一次、查询多次”。** 查询次数少时，多粒度构建很难回本。
5. **MRAgent 是“少量难题”方案。** 查询越多、越简单，多轮重建越不划算。
6. **长上下文仍然有成本优势。** 短历史、一次性、低复用场景下，它是最简单也常常是最便宜的选择。

## 对 RQ1 的含义

RQ1 不能只比较准确率，还要比较：

- 构建成本
- 查询 token
- p50 / p95 延迟
- 存储与维护成本
- 更新 / 删除成本
- 工程复杂度

建议报告 **准确率 vs 总成本** 的 Pareto 前沿，并按 workload 分层：

- 短历史、一次性查询：长上下文
- 长历史、重复查询：A-Mem / MemGAS / MAGMA
- 重复的团队任务：G-Memory
- 少量困难查询：MRAgent

## 口径警告

- A-Mem 报告的是 tokens/op，G-Memory 是额外总 tokens，MAGMA 是 tokens/query + build hours，MemGAS 是 tokens/query + build tokens，MRAgent 是 tokens/sample。
- 这些数字不能直接横比。
- 各论文使用不同 backbone、数据集和 judge。
- 多数论文没有报告 p95 延迟、构建 token、更新/删除成本。

## 证据卡

- [[10_Papers/evidence/amem-evidence|A-Mem]]
- [[10_Papers/evidence/gmemory-evidence|G-Memory]]
- [[10_Papers/evidence/magma-evidence|MAGMA]]
- [[10_Papers/evidence/memgas-evidence|MemGAS]]
- [[10_Papers/evidence/reconstructed-evidence|MRAgent]]
