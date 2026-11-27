# Reading Queue

> 目标：先精读能支撑 RQ1/RQ3 的论文，不追求平均阅读。

## P0 — 必读

| 论文 | 原因 | 状态 |
|---|---|---|
| A-Mem | 记忆组织基线 | evidence-checked |
| G-Memory | 多智能体层次记忆 | evidence-checked |
| Memory-R1 | 可学习记忆管理 | evidence-checked |
| MemAgent | RL memory agent | evidence-checked |
| LongMemEval | 长期记忆评测 | evidence-checked |
| PersistBench | 遗忘边界 | evidence-checked |
| Memory Injection Attacks | 安全攻击面 | evidence-checked |
| Privacy Risks in Agent Memory | 隐私攻击面 | evidence-checked |
| LightMem | 高效长期记忆核心基线 | evidence-checked |
| SeCom | segment 级记忆与压缩去噪 | evidence-checked |
| MemoryOS | 三级层次记忆基线 | evidence-checked |
| HippoRAG 2 | 图增强 RAG 强基线 | evidence-checked |
| AgeMem | 统一 LTM/STM 的 RL memory policy | evidence-checked |
| VikingMem | Memory Base / 生产级事件-实体记忆系统 | evidence-checked |

## 新增批次 — evidence 已完成

> 当前主库 52/52 均已完成页码级 evidence；本队列现在用于安排阅读优先级，而不是表示证据尚未完成。

| 论文 | 原因 | 状态 |
|---|---|---|
| SimpleMem | 语义压缩与意图感知检索 | evidence-checked |
| GAM | 事件图 + 主题关联网络 | evidence-checked |
| ReasoningBank | 推理/程序性记忆 | evidence-checked |
| MemoryAgentBench | 增量多轮记忆评测 | evidence-checked |
| E-mem | episodic context reconstruction | evidence-checked |
| EverMemOS | 自组织 memory OS | evidence-checked |
| Nemori | 预测误差驱动的记忆蒸馏 | evidence-checked |
| LightMem (SLM) | 小模型驱动的轻量记忆 | evidence-checked |
| MemoryBench | 持续学习/用户反馈评测 | evidence-checked |
| From Storage to Experience | 记忆演化综述骨架 | evidence-checked |

覆盖审计：`data/agent-memory-2025/COVERAGE_AUDIT.md`

实验/baseline 参照：[[40_Maps/Agent Memory 2025+ Baseline Timeline]]


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
| Beyond a Million Tokens | 长上下文压力测试 | evidence-checked |
| Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks | 多 session 任务 | evidence-checked |
| MemBench | 综合评测 | evidence-checked |
| Minerva | 可编程记忆测试 | evidence-checked |
| Memory is Reconstructed | 重构 vs 检索 | evidence-checked |

## P2 — RQ3 需要

| 论文 | 原因 | 状态 |
|---|---|---|
| InjecMEM | 记忆注入 | evidence-checked |
| Poison Once, Exploit Forever | 环境 poisoning | evidence-checked |
| PersonaAgent | 个性化记忆 | evidence-checked |
| Evoking User Memory | 自适应检索 | evidence-checked |

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
evidence-checked → verified → synthesized
```
