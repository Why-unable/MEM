---
type: evidence
paper_id: reasoningbank
title: "ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/reasoningbank.pdf"
source_version: "ICLR 2026 conference paper (arXiv 2509.25140 for full text)"
pages_checked: "1-8"
mainline: "E"
tags:
  - evidence
  - mainline-e
  - procedural-memory
  - reasoning-memory
  - test-time-scaling
---

# ReasoningBank 证据卡

## 结论先行

- ReasoningBank 把记忆从“存轨迹”推进到“存可泛化的推理策略”：从 self-judged 成功和失败经验中蒸馏 reasoning strategies。
- 它进一步提出 **MaTTS**（memory-aware test-time scaling），把更多 test-time exploration 转化为更好的 memory，再用更好的 memory 指导 scaling。
- WebArena 上 Gemini-2.5-flash 从 40.5 → **48.8**（+8.3），加 MaTTS → **51.8**；steps 从 9.7 降到 8.3 / 7.9。

## 研究问题与定位

现有 memory 主要存 raw trajectories 或 success-only routines；agent 仍会重复犯错、丢弃 insight。ReasoningBank 要回答：

> agent 能否从成功和失败经验中提炼可迁移的推理策略，并在 test time 持续自我进化？

## 方法拆解

### Memory construction

- 用 LLM-as-a-judge 标记 trajectory 成功/失败。
- 从成功经验提取 validated strategies。
- 从失败经验提取 preventive lessons。
- 形成 generalizable reasoning memory items，而不是原始轨迹。

### Test-time learning

- 新任务检索相关 memory。
- 执行后把新经验写回。
- 不需要 ground truth，可在 test time 持续演化。

### MaTTS

- Parallel scaling：同一任务并行采样多条 trajectory。
- Sequential scaling：顺序探索/反思。
- 用成功/失败对比信号合成更高质量 memory。

来源：PDF p.3-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：WebArena、Mind2Web、SWE-Bench-Verified。
- Backbones：Gemini-2.5-flash、Gemini-2.5-pro、Claude-3.7-sonnet。
- Baselines：No Memory、Synapse（trajectory memory）、AWM（workflow memory）。
- Metrics：success rate（SR）、average steps（Step）。

### WebArena 主结果

| Backbone | No Memory SR | ReasoningBank SR | +MaTTS SR |
|---|---:|---:|---:|
| Gemini-2.5-flash | 40.5 | **48.8** | **51.8** |
| Gemini-2.5-pro | 46.7 | **53.9** | **56.3** |
| Claude-3.7-sonnet | 41.7 | **46.3** | **48.8** |

- 相对 no-memory：+8.3 / +7.2 / +4.6。
- 论文报告最高 **20% relative improvement**、**16% fewer interaction steps**。
- Gemini-2.5-flash steps：9.7 → 8.3 → 7.9。

来源：PDF p.7，Table 1。

### Mind2Web / SWE-Bench

- Mind2Web：cross-task / cross-website / cross-domain 均有提升。
- SWE-Bench-Verified：ReasoningBank 也优于 no-memory/Synapse。
- 说明不是只对 WebArena 过拟合。

来源：PDF p.7-8，Table 2-3。

### MaTTS

- MaTTS 比 vanilla test-time scaling 更稳定。
- WebArena-Shopping 上 k=5：parallel 55.1 vs vanilla 52.4；sequential 54.5 vs 51.9。
- 说明 memory 和 test-time compute 有协同。

来源：PDF p.8，Figure 4-5。

## 真正的新意

1. **从成功+失败经验蒸馏 reasoning strategies**，不是存 raw trajectory。
2. **MaTTS**：memory-aware test-time scaling。
3. **test-time learning**：无 ground truth 也可持续进化。
4. **cross-task / cross-website / cross-domain 泛化**。

## 局限与威胁

- **self-judge 噪声**：成功/失败标签可能错误。
- **test-time scaling 成本**：MaTTS 需要更多 rollouts。
- **任务范围**：Web/SWE；其他 agent 领域未验证。
- **没有显式遗忘/删除**：memory 只增不减。
- **策略可能过拟合任务分布**：cross-domain 提升仍需更多验证。

## 与主线 E 的关系

- **ReMe**：ReMe 强调 utility-based refinement/剪枝；ReasoningBank 强调 reasoning strategy + MaTTS。
- **MemEvolve**：ReasoningBank 是经验学习；MemEvolve 进一步进化 memory architecture。
- **PersonaAgent**：ReasoningBank 是技能/策略记忆；PersonaAgent 是用户 persona。
- **LTS**：ReasoningBank 是单 agent；LTS 是多团队共享中间状态。

## 对 RQ5 的意义

ReasoningBank 直接支持“程序性记忆可以提升终身学习”：

- 但它存的是 reasoning strategy，不是具体技能代码。
- RQ5 需要区分 procedural memory 的抽象层级：trajectory → routine → strategy。

## 可复用点

- success/failure distillation。
- reasoning memory item schema。
- MaTTS parallel/sequential scaling。
- WebArena/Mind2Web/SWE-Bench-Verified 评测。
- success rate + steps 双指标。

## 成本

- MaTTS 需要额外 rollouts；成本随 k 增长。
- 论文报告 steps 减少，但未给统一 token/GPU 成本表。
- memory storage 随任务流增长。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/reasoningbank.pdf`
- ICLR 2026 proceedings：https://proceedings.iclr.cc/paper_files/paper/2026/hash/980ea04d23d1f6908964eba2a74afe45-Abstract-Conference.html
- arXiv：https://arxiv.org/abs/2509.25140
