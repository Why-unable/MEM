---
type: evidence
paper_id: rememberrefine
title: "Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/rememberrefine.pdf"
source_version: "ACL Findings 2026"
pages_checked: "1-9"
mainline: "E"
tags:
  - evidence
  - mainline-e
  - procedural-memory
  - experience-reuse
---

# ReMe 证据卡

## 结论先行

- ReMe 把程序性记忆从 append-only archive 变成“提炼 → 复用 → 修剪”的生命周期。
- 三个机制：multi-faceted distillation（成功/失败/比较）、context-adaptive reuse、utility-based refinement。
- Qwen3-14B + ReMe dynamic 在 BFCL-V3/AppWorld 平均 Pass@4 **63.71**，Qwen3-32B 达 **69.97**。

## 研究问题与定位

现有程序性记忆多为被动积累，缺少失败分析、上下文适配和过期清理。ReMe 要回答：

> 如何把历史经验提炼成可复用技能，并保持经验池的高质量？

## 方法拆解

### Multi-faceted distillation

- 成功模式
- 失败触发
- 比较性 insight（成功 vs 失败）

### Context-adaptive reuse

- 按场景索引历史 insight。
- 新任务到来时选择适配的经验。

### Utility-based refinement

- 增加被验证有效的记忆。
- 剪除过期/低效用记忆。
- 维持 compact、high-quality experience pool。

来源：PDF p.3-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：BFCL-V3、AppWorld。
- Backbones：Qwen3-8B、14B、32B。
- Baselines：No Memory、A-Mem、LangMem、ReMe fixed/dynamic。
- Metrics：Avg@4、Pass@4。

### 主结果（Avg@4 / Pass@4）

| 模型 | 方法 | Avg@4 | Pass@4 |
|---|---|---:|---:|
| Qwen3-8B | No Memory | 27.65 | 46.20 |
| Qwen3-8B | ReMe dynamic | **34.94** | **55.03** |
| Qwen3-14B | No Memory | 35.62 | 54.65 |
| Qwen3-14B | ReMe dynamic | **44.66** | **63.71** |
| Qwen3-32B | ReMe dynamic | **49.10** | **69.97** |

- Qwen3-8B + ReMe 在 Pass@4 上超过 Qwen3-14B no-memory（55.03 vs 54.65）；
- Avg@4 仍略低（34.94 vs 35.62），所以“超过更大模型”要按指标说明。

来源：PDF p.6，Table 1。

### 消融

- fixed vs dynamic：dynamic 更好，说明上下文适配/更新重要。
- 去掉 distillation/refinement 会下降。
- 细粒度经验抽象优于 trajectory-level 直接复用。

来源：PDF p.6-8，Table 2-3。

## 真正的新意

1. **程序性记忆生命周期**：不只是存，还要提炼、复用、修剪。
2. **失败分析**：从失败轨迹中提炼触发条件。
3. **context-adaptive reuse**：经验按场景索引。
4. **utility-based refinement**：经验池可修剪。

## 局限与威胁

- **依赖任务反馈**：utility 需要成功/失败信号。
- **剪枝可能误删低频技能**。
- **跨领域迁移未充分验证**：BFCL/AppWorld 都是工具/应用任务。
- **没有安全/权限治理**：程序性记忆可能被污染。
- **memory-scaling 比较需按指标**：Avg@4/Pass@4 结论不同。

## 与主线 E 的关系

- **ReasoningBank**：都从成功/失败经验蒸馏；ReMe 更强调 utility refinement/剪枝。
- **MemEvolve**：ReMe 是固定框架下的经验进化；MemEvolve 进化框架本身。
- **PersonaAgent**：ReMe 是技能记忆；PersonaAgent 是用户 persona。
- **LTS**：ReMe 是单 agent 程序性记忆；LTS 是多 agent 共享。

## 对 RQ5 的意义

ReMe 直接对应 RQ5（程序性记忆与终身学习）：

- 技能复用可以提升小模型表现。
- 但需要区分 Avg@4 与 Pass@4，避免过度概括。

## 可复用点

- multi-faceted distillation。
- context-adaptive reuse。
- utility-based refinement/pruning。
- BFCL-V3/AppWorld 评测。
- fixed vs dynamic 对照。

## 成本

- 经验蒸馏/refinement 需要 LLM 调用。
- 剪枝降低成本，但 utility 评估有成本。
- 没有统一 token/latency 表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/rememberrefine.pdf`
- ACL Findings 2026（论文记录）
