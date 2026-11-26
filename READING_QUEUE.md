# Reading Queue

> 目标：先精读能支撑 RQ1/RQ3 的论文，不追求平均阅读。

## P0 — 必读

| 论文 | 原因 | 状态 |
|---|---|---|
| A-Mem | 记忆组织基线 | evidence-checked |
| G-Memory | 多智能体层次记忆 | evidence-checked |
| Memory-R1 | 可学习记忆管理 | queued |
| MemAgent | RL memory agent | queued |
| LongMemEval | 长期记忆评测 | queued |
| PersistBench | 遗忘边界 | queued |
| Memory Injection Attacks | 安全攻击面 | queued |
| Privacy Risks in Agent Memory | 隐私攻击面 | queued |

## 主线 A — 已精读

| 论文 | 证据卡 | 状态 |
|---|---|---|
| A-Mem | [[10_Papers/evidence/amem-evidence]] | evidence-checked |
| G-Memory | [[10_Papers/evidence/gmemory-evidence]] | evidence-checked |
| MAGMA | [[10_Papers/evidence/magma-evidence]] | evidence-checked |
| MemGAS | [[10_Papers/evidence/memgas-evidence]] | evidence-checked |
| MRAgent | [[10_Papers/evidence/reconstructed-evidence]] | evidence-checked |

主线综合：[[20_Topics/Mainline A - Memory Architecture]]

## P1 — RQ1 需要

| 论文 | 原因 | 状态 |
|---|---|---|
| Beyond a Million Tokens | 长上下文压力测试 | queued |
| Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks | 多 session 任务 | queued |
| MemBench | 综合评测 | queued |
| Minerva | 可编程记忆测试 | queued |
| Memory is Reconstructed | 重构 vs 检索 | queued |

## P2 — RQ3 需要

| 论文 | 原因 | 状态 |
|---|---|---|
| InjecMEM | 记忆注入 | queued |
| Poison Once, Exploit Forever | 环境 poisoning | queued |
| PersonaAgent | 个性化记忆 | queued |
| Evoking User Memory | 自适应检索 | queued |

## 阅读产出

每篇 P0 论文至少补：

- 方法一句话
- 关键实验
- 主要结论
- 局限
- 与 RQ 的关系
- 可复用点

## 状态说明

```text
queued → reading → notes-done → evidence-checked → synthesized
```
