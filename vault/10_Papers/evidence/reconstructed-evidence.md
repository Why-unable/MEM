---
type: evidence
paper_id: reconstructed
title: "Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents"
status: evidence-checked
checked_at: 2026-11-26
source_pdf: "data/agent-memory-2025/pdfs/reconstructed.pdf"
source_version: "ICML 2026, PMLR 306"
pages_checked: "1-9"
tags:
  - evidence
  - mainline-a
  - agent-memory
  - active-retrieval
---

# MRAgent（Memory is Reconstructed）证据卡

## 结论先行

- 这篇论文的核心不是再设计一种图结构，而是改变访问范式：从一次 top-k 检索，变成由 LLM 在图上多轮选择、扩展、剪枝的 **active reconstruction**。
- 它用 Cue–Tag–Content 图把“细粒度线索 → 关系标签 → 具体记忆”分开，避免直接在 content 节点上做 N-hop 扩展造成组合爆炸。
- 实验上，主动重构在 LoCoMo 和 LongMemEval 上显著优于 A-Mem、MemoryOS、LangMem、Mem0，并且总 token 成本低于 A-Mem；代价是重建深度带来的延迟和不断增长的静态记忆。

## 研究问题与定位

论文批评现有记忆系统仍是 **passive retrieve-then-reason**：

- 检索策略是 query 的固定函数；
- 不能根据中间证据调整下一步；
- 图扩展依赖预定义 N-hop，容易引入噪声；
- 复杂多跳问题需要的信息可能不在初始 top-k 邻居中。

MRAgent 把记忆访问定义为一个序列决策过程：每一步根据当前证据选择下一步检索动作，直到证据足够。

## 方法拆解

### Cue–Tag–Content 图

- **Cue**：细粒度关键词、实体、属性。
- **Tag**：连接 cue 和 content 的关系标签，表示“这个线索为什么能指向这条记忆”。
- **Content**：具体记忆内容。
- 三层记忆类型：
  - Episodic：具体事件；
  - Semantic：稳定事实、偏好、属性；
  - Topic：跨事件的高层主题。

来源：PDF p.3-4，Section 3。

### 重建状态

在步骤 `t`：

```text
S(t) = (Z(t), H(t))
```

- `Z(t)`：当前 active set（cues / tags / contents）
- `H(t)`：已累积的证据上下文

来源：PDF p.5，Eq. 7。

### 动作空间

- `Cue → Tag`
- `(Cue, Tag) → Content`
- `Content → (Cue, Tag)`（反向扩展）

LLM 根据 `query + H(t) + Z(t)` 选择动作；执行后得到候选节点，再由 LLM routing/pruning 更新 `Z(t+1)` 和 `H(t+1)`。

来源：PDF p.5-6，Eq. 8-12。

### 终止

LLM 判断当前证据是否足够回答；不足则继续重建。

## 存储与使用

- **怎么存**：Cue–Tag–Content 结构。Cue 是线索，比如实体、属性、关键词；Tag 说明“这条线索为什么能指向这条记忆”；Content 是具体事件或事实。另有 episodic、semantic、topic 三层。
- **怎么连**：不是预先存一张固定图，而是由“线索—标签—内容”的引用关系在运行时组成图；同一内容可以被多个线索和标签访问。
- **怎么用**：query 先抽线索，LLM 决定下一步查哪个 tag 或 content；查到新证据后可能产生新线索，再继续走，直到证据足够。它是多轮主动重构，不是一次相似度检索。
- **怎么更新**：当前实现是静态构建，不更新、不整合、不遗忘；记忆随对话增加而单调增长。

**一句话**：MRAgent 存的是“线索、关系理由、内容”的三层索引；检索是 LLM 带着证据一步步重建答案。

### 一个端到端例子（示意）

场景：用户在多次对话中提到 Jonna 的剧本项目。

**存储**

- 线索：`Jonna`、`剧本`、`7 月`、`拒绝`。
- 内容事件 A：Jonna 在 7 月提交了剧本。
- 内容事件 B：Jonna 的剧本在 8 月被拒绝。
- 内容事件 C：Jonna 在 9 月开始了一个新项目。
- 关系标签：`提交 → 被拒`、`被拒 → 开始新项目`。
- 更高层：topic“剧本项目”；semantic 事实“Jonna 是编剧”。

**连接**

- 线索 `Jonna` 指向多个事件。
- 标签解释“为什么这条线索能指向这条内容”。
- 从内容 B 还可以反向得到新线索 `拒绝`，继续指向内容 C。

**更新**

- 当前实现是静态构建：新对话只会增加事件和线索。
- 不做记忆整合、删除或遗忘。
- 因此这张图会随对话增长，但不会自我整理。

**检索**

query：“Jonna 为什么开始新项目？”

- 先从 query 抽到线索 `Jonna`、`新项目`。
- LLM 选择先查 `Jonna → 剧本`，找到事件 A、B。
- 发现 B 是“被拒绝”，把 `拒绝` 作为新线索，继续找到 C。
- 剪掉无关事件，判断证据已经足够。
- 回答：因为她的剧本在 8 月被拒绝，所以 9 月开始新项目。

**这个例子说明**：MRAgent 不是一次检索后把一堆片段塞给 LLM，而是让 LLM 沿着“线索 → 关系理由 → 内容”一步步重建证据链。


## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval。
- Backbones：Gemini-2.5-Flash、Claude-Sonnet-4.5。
- Baselines：RAG、LangMem、A-Mem、MemoryOS、Mem0。
- 指标：F1、LLM-Judge、evidence recall。

### LoCoMo Overall LLM-Judge

| Backbone | 最强 baseline | MRAgent |
|---|---:|---:|
| Gemini-2.5-Flash | Mem0 68.31 | **84.21**（+23.3% relative） |
| Claude-Sonnet-4.5 | LangMem 78.61 | **88.32**（+12.4%） |

来源：PDF p.7, Table 1。

分类结果（Claude）：

- Multi-hop：MRAgent 90.19 vs Mem0 75.88
- Temporal：MRAgent 85.34 vs LangMem 80.68
- Open-domain：MRAgent 71.57 vs Mem0 56.25
- Single-hop：MRAgent 91.10 vs LangMem 83.12

### LongMemEval LLM-Judge

| 方法 | Overall |
|---|---:|
| MemoryOS | 54.92 |
| A-Mem | 52.98 |
| RAG | 54.65 |
| **MRAgent (Gemini)** | **72.95** |
| MRAgent* (Claude retrieval, Gemini memory) | 86.76 |

来源：PDF p.7, Table 2。`MRAgent*` 使用 Claude 做检索、Gemini 构建记忆，不是严格同 backbone 对比，不能直接当作纯架构收益。

### 成本（LongMemEval, Gemini）

| 方法 | Token consumption | Runtime (s) |
|---|---:|---:|
| A-Mem | 632K | 1,122.23 |
| MemoryOS | 273K | 3,135.54 |
| LangMem | 3,268K | 1,209.57 |
| Mem0 | 245K | 533.29 |
| **MRAgent** | **118K** | **586.11** |

来源：PDF p.7, Table 3。MRAgent 比 A-Mem 少约 81% token、快约 48%；但 Mem0 的 runtime 更短（533s），说明“低成本”不是绝对的。

### 消融与多轮分析

- 结构变体：CE（Cue→Episode）→ CTE（Cue–Tag–Episode）→ CTC（Cue–Tag–Content），性能单调提升。
- 有 reasoning 的变体一致优于无 reasoning 的变体；说明收益主要来自多轮重建，而不只是图结构。
- 去掉 semantic memory 会明显下降，说明 episodic + semantic 互补。
- 单跳/时间查询约 3 轮达到接近完美 recall；多跳查询的 recall 随轮次提升超过 30%。
- 平均轮数与最大有效轮数接近，说明 LLM 能较好判断何时停止。

来源：PDF p.8，Figure 5-6。

### 理论结果

论文给出 Theorem 4.1：在 `T >= 2` 时，active retrieval 的 hypothesis class 严格包含 passive retrieval。

来源：PDF p.6。

注意：这是 **expressivity** 结果，不等于样本效率、训练稳定性或实际成本更优。

## 成本分析

- **报告成本**：118K tokens/sample、586s/sample（构建 + 检索）；A-Mem 为 632K / 1,122s；MemoryOS 为 273K / 3,136s；LangMem 为 3,268K / 1,210s；Mem0 为 245K / 533s。
- **成本位置**：构建轻、查询重；多轮重建让延迟随探索深度增长。
- **横向对比**：总 token 低于 A-Mem，但延迟高于 Mem0；且 sample 口径不能直接当 per-query 口径。
- **对比判断**：适合少量困难查询；大量简单查询会让多轮探索成本迅速累积。

## 真正的新意

1. **把 retrieval 变成 sequential decision process**：不是“先检索再推理”，而是“推理驱动检索”。
2. **Cue–Tag–Content 作为可解释的中间层**：tag 解释了“为什么这条线索指向这条记忆”。
3. **反向遍历**：检索到的 content 可以激活新的 cue/tag，支持多跳补证。
4. **显式终止判断**：LLM 决定证据是否充分，而不是固定 top-k。

## 局限与威胁

作者明确承认（PDF p.9）：

- **重建成本随探索深度增长**：需要多步遍历的 query 延迟更高。
- **静态构建**：记忆图只增长，不更新、不整合。
- **没有遗忘机制**：长期部署会持续增加存储。
- **图构建简单**：作者把复杂关系推理推迟到 retrieval，构建阶段没有做复杂更新。

分析补充：

- **只在 2 个 benchmark 上验证**：LoCoMo、LongMemEval；未覆盖多 agent、工具使用、多模态。
- **理论假设较强**：Theorem 4.1 是表达能力结论，不保证有限数据/有限步数下的性能。
- **依赖 LLM 的 action selection/routing**：错误剪枝可能丢失关键证据，且难以审计。
- **baseline 版本差异**：A-Mem、MemoryOS 等是重实现，需核对代码配置。
- **MRAgent\*** 的 Claude/Gemini 混合结果不能与同 backbone 结果直接比较。

## 与主线 A 其他论文的关系

- **A-Mem**：A-Mem 代表“先组织、再单轮 top-k 检索”；MRAgent 直接挑战其 passive retrieval。
- **MAGMA**：MAGMA 也是 policy-guided traversal，但主要是单轮 intent-aware beam search；MRAgent 是多轮、状态依赖的重建。
- **MemGAS**：MemGAS 用 entropy router 选择粒度；MRAgent 用 LLM 选择动作和路径。
- **G-Memory**：G-Memory 的多层记忆仍通过一次双向遍历注入；MRAgent 把遍历变成迭代过程。

## 对 RQ1 的意义

MRAgent 把 RQ1 的关键变量从“记忆结构”推进到“访问策略”：

- **结构相同，策略不同，结果可能差很多**：CE→CTE→CTC 有提升，但 reasoning/no-reasoning 的差异更一致。
- **主动重建在 multi-hop/temporal 上收益最大**，这与 A-Mem/MAGMA 的类别优势一致。
- **成本不是简单的“结构越复杂越贵”**：MRAgent 通过按需访问，总 token 反而低于 A-Mem。
- **但延迟和存储是新的代价**：需要把 token、latency、storage、update cost 分开报告。

## 可复用点

- `S(t) = (Z(t), H(t))` 的重建状态定义。
- Cue–Tag–Content 图 schema。
- 前向/反向动作空间。
- LLM action selection + routing/pruning + sufficiency check 的循环。
- evidence recall 作为过程指标，而不只看最终答案。
- 用总 token / runtime 同时报告构建和检索成本。

## 待核对

- [ ] 核对 Theorem 4.1 的完整假设和证明。
- [ ] 检查 Figure 5 的具体 ablation 数值（文本提取不完整）。
- [ ] 核对代码版本与 LoCoMo/LongMemEval 配置。
- [ ] 确认 Table 3 的 token/runtime 是否包含所有构建和检索调用。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/reconstructed.pdf`
- arXiv：https://arxiv.org/abs/2606.06036
- OpenReview：https://openreview.net/forum?id=xRVWftS3ES
- PMLR 306（ICML 2026）
