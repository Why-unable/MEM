---
type: evidence
paper_id: nemori
title: "What Deserves Memory: Adaptive Memory Distillation for LLM Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/nemori.pdf"
source_version: "ACL 2026 Long Papers; DOI 10.18653/v1/2026.acl-long.1607"
pages_checked: "1-10"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - consolidation
  - prediction-error
---

# Nemori 证据卡

## 结论先行

- Nemori 把“什么值得记住”从重要性分数/情感标签等启发式，改成 **未来可预测性 / prediction error**。
- 两个模块：Episodic Memory Integration（把交互变成连贯叙事）和 Semantic Knowledge Distillation（用预测误差提取 insight）。
- LoCoMo GPT-4o-mini **73.0** vs full-context **72.3**；LongMemEval-S **64.2** vs full **55.0**；response tokens **-88%**。

## 研究问题与定位

现有 memory systems 依赖预定义 heuristic 决定保留什么，编码的是设计者直觉，而不是数据本身。Nemori 要回答：

> 能否用交互序列的内在可预测性，判断哪些经验值得保留？

## 方法拆解

### Episodic Memory Integration

- 把 raw interaction 组织成 coherent narratives。
- 以 episode 为基本单位，而不是 message/turn。

### Semantic Knowledge Distillation

- 用 prediction error 提取 insight。
- 与 downstream management 解耦：Nemori 只负责 distillation，不强制某种 retrieval/management。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval。
- Backbones：GPT-4o-mini、GPT-4.1-mini。
- Baselines：Full Context、LangMem、A-Mem、Zep、MemoryOS、Mem0。
- Metrics：LLM-Judge、F1、BLEU、tokens、latency。

### LoCoMo

| 方法 | LLM-J (GPT-4o-mini) | LLM-J (GPT-4.1-mini) |
|---|---:|---:|
| Full Context | 72.3 | 80.6 |
| A-Mem | 52.5 | — |
| Mem0 | 61.3 | — |
| **Nemori** | **73.0** | **80.8** |

- 相对 Full Context：+0.7 / +0.2。
- 相对 A-Mem/Mem0：明显更高。
- 说明 episode-centric distillation 可以在不增加上下文的情况下略胜 full-context。

来源：PDF p.7-8，Table 2。

### LongMemEval-S

| Backbone | Full Context | Nemori |
|---|---:|---:|
| GPT-4o-mini | 55.0 | **64.2** |
| GPT-4.1-mini | 65.6 | **74.6** |

- 相对提升 **+16.7% / +13.7%**（论文表述）。
- 使用 **95–96% fewer tokens**。

来源：PDF p.8，Table 8。

### 成本

- LoCoMo response tokens：**2,745** vs Full Context **23,653**（-88%）。
- Latency：**3,053ms** vs **5,806ms**（-47%）。
- Memory construction 成本也在 Table 3/9 中报告。

来源：PDF p.8，Table 4。

## 真正的新意

1. **prediction error 作为记忆价值信号**：替代 importance/emotion/fact template。
2. **episode-centric distillation**：先整合成叙事，再抽取 semantic insight。
3. **management-agnostic**：distillation 与 downstream management 解耦。
4. **接近/超过 full-context 的 token 效率**：不是用更大上下文换性能。

## 局限与威胁

- **prediction error 是代理指标**：不等于真实未来效用。
- **对一次性重要事件可能不敏感**：低频但关键的 safety/preference 事件可能没有预测误差信号。
- **依赖叙事生成**：episodic integration 质量影响 distillation。
- **没有显式遗忘/删除**：只决定保留什么，不决定何时删除。
- **主要是对话 QA**：没有 action-coupled、多模态、安全。

## 与主线 D 的关系

- **RecMem**：RecMem 用 recurrence 决定何时 consolidation；Nemori 用 prediction error 决定保留什么。
- **TiMem**：TiMem 用时间树组织；Nemori 用叙事/预测误差。
- **TierMem**：TierMem 用 query-time sufficiency；Nemori 用 write-time distillation。
- **EMA**：EMA 过滤进入上下文的内容；Nemori 决定长期保留什么。

## 对 RQ1 / RQ3 的意义

### RQ1

Nemori 说明“什么值得记”本身可以影响 accuracy–token Pareto：

- 不是所有 token 都值得进入长期记忆。
- RQ1 应把 distillation policy 作为独立变量。

### RQ3

- Nemori 没有删除机制；它只决定保留。
- RQ3 可以问：prediction error 低的记忆是否应该被删除/过期？

## 可复用点

- episodic integration + semantic distillation 两阶段。
- prediction error 作为 retention signal。
- management-agnostic 设计。
- token/latency 的 Pareto 报告。
- 与 Full Context/Mem0/A-Mem 的对照。

## 成本

- LoCoMo：2,745 response tokens，3,053ms。
- Full Context：23,653 tokens，5,806ms。
- Memory construction 成本见 Table 3/9（待核对）。
- 没有 storage 删除策略。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/nemori.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.1607/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.1607
