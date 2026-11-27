---
type: evidence
paper_id: learnshare
title: "Learning to Share: Selective Memory for Efficient Parallel Agentic Systems"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/learnshare.pdf"
source_version: "ICML 2026 / PMLR 306"
pages_checked: "1-9"
mainline: "E"
tags:
  - evidence
  - mainline-e
  - multi-agent
  - shared-memory
---

# Learning to Share (LTS) 证据卡

## 结论先行

- LTS 解决并行多 agent 团队的重复计算：多个 team 独立探索相似子问题，浪费大量 runtime。
- 它用一个 global memory bank + lightweight admission controller，学习“哪些 intermediate steps 值得写入共享记忆”。
- 在 AssistantBench / GAIA 上，LTS 同时提升 accuracy 并显著降低 wall-clock runtime。

## 研究问题与定位

并行多 team 能提高鲁棒性，但会产生重复推理和工具调用。共享所有中间结果又会引入噪声、增加上下文。

LTS 要回答：

> 能否学习一个 selective shared memory，只共享对跨团队有用的信息？

## 方法拆解

### Global memory bank

- 所有 team 可访问。
- 存储被 controller 选中的 intermediate steps。

### Admission controller

- 轻量语言模型/策略。
- 输入：当前 step / query / 团队状态。
- 输出：是否写入共享记忆。
- 训练：stepwise RL + usage-aware credit assignment。

### 目标

- 减少重复计算。
- 控制 context growth。
- 保持/提升最终答案质量。

来源：PDF p.3-6，Method。

## 实验与关键数字

### 设置

- Benchmarks：AssistantBench、GAIA。
- Teams：K=3 parallel teams。
- Baselines：MagenticOne、M1-Parallel、LTS-AddAll、LTS-LLM、LTS。
- Models：Qwen3-32B、GPT-5.1。

### 主结果（Qwen3-32B）

| Benchmark | M1-Parallel Acc / Runtime | LTS Acc / Runtime |
|---|---|---|
| AssistantBench | 14.7 / 2239s | **20.3 / 1479s（-40.8%）** |
| GAIA | 24.8 / 1569s | **30.4 / 892s（-55.0%）** |

### 主结果（GPT-5.1）

| Benchmark | M1-Parallel Acc / Runtime | LTS Acc / Runtime |
|---|---|---|
| AssistantBench | 24.0 / 1389s | **26.7 / 882s（-44.6%）** |
| GAIA | 47.9 / 1005s | **49.1 / 781s（-25.1%）** |

来源：PDF p.7，Table 1。

### Admission 策略

- LTS-AddAll：共享所有步骤，runtime 降但 accuracy 可能被噪声拖累。
- LTS-LLM：LLM filtering，部分缓解但仍不如 learned controller。
- LTS：learned selective admission 达到最佳 accuracy–runtime balance。

来源：PDF p.7，Table 2。

## 真正的新意

1. **shared memory admission 是学习问题**，不是“共享所有”。
2. **global memory bank + per-step controller**。
3. **usage-aware credit assignment**：奖励真正被其他团队使用的记忆。
4. **accuracy + runtime 双目标**：不是只看 token。

## 局限与威胁

- **共享权限/冲突/责任归属未解决**。
- **benchmark 是 GAIA/AssistantBench**：其他多 agent 场景未验证。
- **controller 训练成本**：stepwise RL。
- **共享记忆可能传播错误**：admission 不能保证内容正确。
- **没有删除/过期/回滚**：共享 bank 只增不减。

## 与主线 E 的关系

- **G-Memory**：G-Memory 是层次团队记忆；LTS 是并行团队的选择性共享。
- **MemRec**：MemRec 共享 collaborative signals；LTS 共享 intermediate steps。
- **PersonaAgent**：单用户 persona；LTS 多团队共享。
- **ReasoningBank/ReMe**：程序性经验；LTS 是任务中间状态。

## 对 RQ4 的意义

LTS 是 RQ4（共享记忆权限/冲突）的直接入口：

- 共享多少、共享什么、何时共享，是 policy 问题。
- 但 LTS 没有回答“谁有权写/读/删”。

## 可复用点

- global memory bank + admission controller。
- stepwise RL + usage-aware credit。
- LTS-AddAll / LTS-LLM / LTS 对照。
- accuracy + wall-clock runtime 双指标。

## 成本

- Runtime 降低 25.1%–55.0%（不同模型/benchmark）。
- controller 训练成本未完整量化。
- shared memory storage 未给出统一指标。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/learnshare.pdf`
- PMLR 306（ICML 2026）
