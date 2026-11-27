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
| LightMem | 高效长期记忆核心基线 | queued |
| SeCom | segment 级记忆与压缩去噪 | queued |
| MemoryOS | 三级层次记忆基线 | queued |
| HippoRAG 2 | 图增强 RAG 强基线 | queued |
| AgeMem | 统一 LTM/STM 的 RL memory policy | evidence-checked |
| VikingMem | Memory Base / 生产级事件-实体记忆系统 | evidence-checked |

## 新增批次 — 待补证据卡

> LightMem、SeCom、MemoryOS、HippoRAG 2、AgeMem 已加入上述 P0；这里列其余新增论文。

| 论文 | 原因 | 状态 |
|---|---|---|
| SimpleMem | 语义压缩与意图感知检索 | queued |
| GAM | 事件图 + 主题关联网络 | queued |
| ReasoningBank | 推理/程序性记忆 | queued |
| MemoryAgentBench | 增量多轮记忆评测 | queued |
| E-mem | episodic context reconstruction | queued |
| EverMemOS | 自组织 memory OS | queued |
| Nemori | 预测误差驱动的记忆蒸馏 | queued |
| LightMem (SLM) | 小模型驱动的轻量记忆 | queued |
| MemoryBench | 持续学习/用户反馈评测 | queued |
| From Storage to Experience | 记忆演化综述骨架 | queued |

覆盖审计：`data/agent-memory-2025/COVERAGE_AUDIT.md`

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
