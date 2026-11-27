---
type: evidence
paper_id: memoryr1
title: "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/memoryr1.pdf"
source_version: "ACL 2026 Long Papers; official DOI 10.18653/v1/2026.acl-long.583"
pages_checked: "1-10"
mainline: "B"
tags:
  - evidence
  - mainline-b
  - memory-policy
  - reinforcement-learning
---

# Memory-R1 证据卡

## 结论先行

- Memory-R1 把外部记忆管理拆成两个可训练角色：**Memory Manager** 决定 `ADD / UPDATE / DELETE / NOOP`，**Answer Agent** 负责检索后蒸馏和回答。
- 它用 PPO / GRPO 做 outcome-driven RL，只需要 **152 条训练 QA**，就能在 LoCoMo、MSC、LongMemEval 和 3B–14B 模型上泛化。
- 它是“少量监督 + 可学习记忆操作”的最清晰证据之一，也是 AgeMem 的前置工作。

## 研究问题与定位

现有 memory pipeline 大多是静态、heuristic 的：开发者预先定义何时写入、何时更新、检索多少条、如何拼接上下文。Memory-R1 要回答：

> 能否用 outcome reward 训练 agent 自己决定记忆操作，而不是手工设计规则？

它把记忆管理建模为 RL 问题，但不训练一个端到端的大 policy，而是拆成 Manager 和 Answer Agent 两个阶段。

## 方法拆解

### 两阶段框架

1. **Stage 1 · Memory Manager**
   - 输入：新对话信息 + 当前 memory bank。
   - 输出：`ADD / UPDATE / DELETE / NOOP` 及更新内容。
   - 目标：产生一个让 Answer Agent 更容易答对的 memory state。
2. **Stage 2 · Answer Agent**
   - 对每个 query 检索 60 条候选记忆。
   - 学习 memory distillation：从候选中选出有用条目，再生成答案。

来源：PDF p.3-5，Figure 2。

### 训练

- Memory Manager：PPO 和 GRPO 两个版本。
- Answer Agent：同样用 PPO / GRPO。
- Memory Manager 的 reward：下游 QA 的 exact match（outcome-driven）。
- Answer Agent 的 reward：最终答案的 exact match。
- GRPO 用 group-relative advantage，不需要 value function。

来源：PDF p.4-5，Eq. 1-6。

### 数据

- 只在 LoCoMo 上训练。
- 排除 adversarial 子集，按 1:1:8 划分：
  - train 152
  - validation 81
  - test 1307
- zero-shot 迁移到 MSC、LongMemEval。
- 每个 query 检索 60 条候选记忆。

来源：PDF p.5。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、MSC、LongMemEval。
- Backbones：LLaMA-3.1-8B-Instruct、Qwen2.5-3B/7B/14B-Instruct。
- Baselines：LoCoMo(RAG)、A-Mem、Mem0、MemoryOS、Memory-SFT。
- Metrics：F1、BLEU-1（B1）、LLM-as-a-Judge（J）。

### LoCoMo 主结果

LLaMA-3.1-8B-Instruct：

| 方法 | Overall F1 | Overall B1 | Overall J |
|---|---:|---:|---:|
| MemoryOS | 35.04 | 27.99 | 48.20 |
| Memory-SFT | 42.81 | 32.98 | 58.76 |
| Memory-R1-PPO | 41.05 | 32.91 | 57.54 |
| **Memory-R1-GRPO** | **45.02** | **37.51** | **62.74** |

Qwen2.5-7B-Instruct：

| 方法 | Overall F1 | Overall B1 | Overall J |
|---|---:|---:|---:|
| MemoryOS | 34.64 | 29.36 | 51.26 |
| Memory-SFT | 39.51 | 30.84 | 61.13 |
| Memory-R1-PPO | 41.72 | 33.70 | 59.53 |
| **Memory-R1-GRPO** | **43.14** | **36.44** | **61.51** |

来源：PDF p.6, Table 1。

### 相对提升

- LLaMA-3.1-8B GRPO 相对最强 baseline MemoryOS：
  - F1 **+28.5%**
  - B1 **+34.0%**
  - J **+30.2%**（相对值）
- Qwen2.5-7B GRPO 相对 MemoryOS：
  - F1 **+24.5%**
  - B1 **+24.1%**
  - J **+20.0%**
- PPO 也稳定优于非 RL baseline。

来源：PDF p.6。

### 泛化与规模

- 在 Qwen2.5-3B/7B/14B 上，PPO/GRPO 都持续优于 base model。
- 只在 LoCoMo 训练，zero-shot 迁移到 MSC、LongMemEval 仍有一致提升。
- 说明记忆管理行为可以部分迁移，而不是只记住 LoCoMo 的模式。

来源：PDF p.7，Figure 3-4。

### 消融

- 去掉 RL-fine-tuned Memory Manager：
  - PPO：F1 41.0 → 34.5，B1 32.9 → 28.1，J 57.5 → 49.0。
  - GRPO：F1 → 37.5，B1 → 30.6，J → 52.9。
- 去掉 RL-fine-tuned Answer Agent 也会显著下降。
- 说明 Manager 和 Answer Agent 都是必要组件。

来源：PDF p.7，Figure 5。

## 真正的新意

1. **把记忆管理拆成可解释的 operations**：ADD / UPDATE / DELETE / NOOP。
2. **用 outcome-driven RL 训练 Manager**：不需要人工标注每一步操作，只看最终 QA 是否正确。
3. **Manager + Answer Agent 分工**：一个决定“存什么/改什么”，一个决定“取什么/怎么用”。
4. **极少监督**：152 条 QA 足以训练出可迁移的记忆操作。

## 局限与威胁

作者没有单独 Limitations 章节；以下是分析判断：

- **两阶段分离**：Manager 和 Answer Agent 分别训练，可能不是全局最优。
- **训练数据小且集中**：152 条 LoCoMo QA；跨领域泛化仍有限。
- **DELETE 是任务奖励驱动**：没有 provenance、权限、审计、回滚。
- **评测以 QA 为主**：没有 action-coupled memory（MemoryArena）或安全/隐私维度。
- **候选检索固定 60 条**：Answer Agent 的表现受 retriever 上限约束。
- **LLM-as-Judge 偏差**：J 指标依赖 judge 模型。

## 与主线 B 其他论文的关系

- **AgeMem**：AgeMem 把 LTM+STM 统一进一个 policy，并加入 STM 的 SUMMARY/FILTER；Memory-R1 更聚焦 LTM 的 ADD/UPDATE/DELETE。
- **MemAgent**：MemAgent 学的是长文档 compression policy；Memory-R1 学的是外部 memory bank 的管理操作。
- **MemEvolve**：MemEvolve 进一步把 memory architecture 本身作为进化对象。
- **UMEM**：UMEM 联合优化 extraction 和 management；Memory-R1 的 extraction 主要是静态的数据构造。

## 对 RQ 的意义

### RQ1

Memory-R1 支持“访问/管理策略可以独立于存储结构带来收益”：

- 它没有引入复杂的图结构，而是学习 memory operations。
- 这说明结构记忆的收益可能来自“会管理”，而不只是“存得多”。

### RQ2

- 只在 LoCoMo 训练，迁移到 MSC/LongMemEval 仍有提升，是 RQ2 的一个早期证据。
- 但迁移范围仍是对话 QA，尚未覆盖代码、科研、Web agent。

### RQ3

- DELETE 是动作空间的一部分，但目标是任务效用，不是隐私/合规。
- 这给 RQ3 一个清晰切口：**可学习删除 ≠ 可治理删除**。

## 可复用点

- `ADD / UPDATE / DELETE / NOOP` 的 Manager action space。
- Manager 用下游 QA exact match 作为 reward 的 outcome-driven 训练。
- Answer Agent 的 60-candidate memory distillation。
- 只用 152 条训练 QA 的低监督设置。
- PPO vs GRPO 的对照实验。

## 成本

论文主要报告训练/推理设置，没有完整成本表：

- 训练：152 QA + PPO/GRPO，具体 GPU 成本未在正文汇总。
- 推理：每 query 检索 60 条候选记忆。
- 没有 build token、latency、storage 的统一报告。

**待核对**：附录中的训练超参数、GPU 小时、每 query token 成本。

## 待核对

- [ ] 核对附录 B 的数据构造细节。
- [ ] 核对 PPO/GRPO 的训练成本。
- [ ] 核对 MSC/LongMemEval 的 zero-shot 设置。
- [ ] 把 `papers.json` 的 DOI 从 arXiv DOI 更新为 `10.18653/v1/2026.acl-long.583`。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memoryr1.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.583/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.583
- arXiv：https://arxiv.org/abs/2508.19828
