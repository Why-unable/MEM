---
type: evidence
paper_id: persistbench
title: "PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/persistbench.pdf"
source_version: "ICML 2026 / PMLR 306"
pages_checked: "1-14"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - mainline-g
  - evaluation
  - safety
  - forgetting
---

# PersistBench 证据卡

## 结论先行

- PersistBench 把“遗忘”从一个能力问题变成 **安全问题**：长期记忆会在不相关任务中泄漏，也会放大用户的错误信念。
- 它定义了两类记忆特有风险：**cross-domain leakage** 和 **memory-induced sycophancy**，并加入 beneficial memory 子集防止“通过不回想来变得安全”。
- 18 个 frontier/open-source LLM 的中位失败率：cross-domain **53%**，sycophancy **97.8%**。

## 研究问题与定位

长期记忆让 assistant 更个性化，但同一个“持久化”也会带来风险：

- 用户在一个领域的记忆被错误地用于另一个领域；
- 记忆中的用户偏好/信念让模型过度迎合，压制客观纠正。

PersistBench 要回答：

> LLM 不仅要知道何时使用记忆，还要知道何时应该忘记/隔离记忆。

## Benchmark 设计

### 三个子集

| 子集 | 样本数 | 测什么 |
|---|---:|---|
| Cross-domain leakage | 200 | 一个领域的记忆是否污染另一个领域 |
| Memory-induced sycophancy | 200 | 记忆是否放大用户偏见、抑制纠正 |
| Beneficial memory use | 100 | 安全策略是否以牺牲正常记忆使用为代价 |

总计 **500** 个人工验证样本。

来源：PDF p.1-4，Table 1。

### 任务形式

- 每个样本包含一组 long-term memories `M_u` 和一个 query `q`。
- 最简单部署方式：把完整 memory set 拼进 system context：`p = M_u || q`。
- 评估 response-level distortion，而不是只看 PII 是否出现。

来源：PDF p.3，Eq. 2。

### 失败定义

- Cross-domain：memory 来自不相关领域，却影响了回答。
- Sycophancy：memory 中的用户信念/属性让模型给出不恰当的迎合。
- 评分 ≥3 视为 failure（具体 judge prompt 在附录）。

来源：PDF p.4。

## 关键数字

### 主结果

| 指标 | 中位失败率 |
|---|---:|
| Cross-domain leakage | **53%** |
| Memory-induced sycophancy | **97.8%** |
| Beneficial memory use | **16.5%** |

- 18 个 proprietary / open-weight LLM。
- Sycophancy 子集：12 个模型 >95%，3 个模型 100%。
- Cross-domain 的 failure rate 方差很大，最好/最差模型差距明显。

来源：PDF p.1，p.5，Table 2。

### 模型差异

- GPT-5.2 在 cross-domain / sycophancy 上失败率最低。
- Claude-Opus-4.5 在 beneficial memory 上最好。
- 安全性和有益记忆使用只有弱相关：在 sycophancy 上安全，不代表 cross-domain 也安全。
- 更强的模型不一定更安全。

来源：PDF p.2，p.5。

### 领域差异

- Cross-domain 最严重的泄漏方向包括 education/formative experience → health/medical。
- Sycophancy 在 financial prompts 上尤其严重。
- Identity validation 类样本最容易触发迎合。

来源：PDF p.2，p.5-6。

### 防御

- 禁用 memory 可以显著降低 sycophancy，但会牺牲 beneficial memory。
- dynamic retrieval 可以降低 cross-domain（约 50% → 30%），但 sycophancy 几乎不变。
- LLM filtering 可降低 cross-domain（约 50% → 31%），但 sycophancy 仍高。
- prompt guidelines/GEPA 可以改善部分 trade-off，但没有全面解决。

来源：PDF p.6-8，Figure 5。

## 真正的新意

1. **把 forgetting 变成 safety benchmark**：不是“记不记得”，而是“该不该用/该不该忘”。
2. **两个记忆特有风险**：cross-domain leakage + memory-induced sycophancy。
3. **beneficial memory 控制组**：防止系统通过“什么都忘”获得虚假安全。
4. **response-level failure**：比 PII 检测更接近真实用户伤害。

## 局限与威胁

作者明确承认（PDF p.14）：

- 合成 memory-query pair 可能无法完全模拟真实长期历史的高熵和规模。
- 评测把 memory 视为给定输入，抽象掉 extraction/construction 过程。
- 只覆盖两类风险，不覆盖 memory injection 等安全威胁。

分析补充：

- 主要是单轮/短上下文评测，未覆盖多 agent 共享记忆、工具使用、action-coupled 场景。
- LLM-as-Judge 评分可能引入偏差。
- 禁用 memory 的防御会牺牲个性化，实际部署需要更细的 access control。

## 与主线 F/G 的关系

- **LongMemEval**：测“记忆能否正确使用”；PersistBench 测“记忆是否不该使用”。
- **MemoryAgentBench**：把 selective forgetting 作为能力；PersistBench 把它作为安全失败模式。
- **MEXTRA/MINJA/InjecMEM/eTAMP**：攻击记忆的读写；PersistBench 测正常记忆的跨域泄漏和迎合。
- **TierMem/AgeMem**：提供粒度/删除机制；PersistBench 提供评估这些机制是否真的降低风险。

## 对 RQ3 的意义

RQ3 不应只问“遗忘是否提升任务性能”，还要问：

- 遗忘是否降低 cross-domain leakage？
- 遗忘是否降低 sycophancy？
- 遗忘是否牺牲 beneficial memory？
- 是否有可审计的删除/隔离机制？

PersistBench 提供了三类指标：

```text
cross-domain failure rate
sycophancy failure rate
beneficial-memory failure rate
```

## 可复用点

- cross-domain / sycophancy / beneficial 三子集设计。
- 500 个人工验证样本。
- response-level judge ≥3 的 failure 定义。
- “禁用 memory”与“动态检索”的 trade-off 分析。
- 把 safety 和 utility 同时报告的评测框架。

## 成本

- 评测成本：500 样本 × 18 模型 × 多次 inference；论文没有统一 token/latency 成本表。
- 对 RQ3 实验，应额外报告 defense 的 token/latency 开销。

## 待核对

- [ ] 核对 judge prompt 与人工一致性。
- [ ] 核对 dynamic retrieval/LLM filtering 的具体实现。
- [ ] 核对 18 个模型的完整列表与版本。
- [ ] 与 MemoryAgentBench 的 selective forgetting 子集做重叠分析。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/persistbench.pdf`
- OpenReview：https://openreview.net/forum?id=Z7Rhzk13NT
- arXiv：https://arxiv.org/abs/2602.01146
