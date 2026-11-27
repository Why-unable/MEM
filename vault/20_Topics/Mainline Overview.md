---
type: topic
subtype: roadmap
topic: "Agent Memory 2025+"
status: full-text-scan
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - overview
---

# Agent Memory 2025+ · Mainline Overview

> 目的：把 51 篇主库论文组织成七条可读、可比较、可做实验的主线。
> 状态：A 线有 5 张页码级证据卡；AgeMem 有 1 张；B–G 已做全文扫描与主线综合（ReasoningBank 除外，使用摘要/实验地图），尚未逐篇建卡。

## 七条主线

| 主线 | 核心问题 | 论文数 | 分析入口 |
|---|---|---:|---|
| A · Memory Architecture | 记忆应该怎么组织：笔记、图、层次、粒度、重构？ | 10 | [[20_Topics/Mainline A - Memory Architecture]] |
| B · Memory Policy | 何时写、读、更新、总结、删除？这些策略能否学习？ | 5 | [[20_Topics/Mainline B - Memory Policy]] |
| C · Systems and Efficiency | 如何降低 token、latency、API calls、storage 和构建成本？ | 8 | [[20_Topics/Mainline C - Systems and Efficiency]] |
| D · Episodic Memory and Consolidation | 如何切事件、何时巩固、如何压缩但不丢证据？ | 8 | [[20_Topics/Mainline D - Episodic Memory and Consolidation]] |
| E · Personalization, Multimodal and Procedural | 记忆应该存什么：用户、视觉/听觉、技能、协作信号？ | 7 | [[20_Topics/Mainline E - Personalization Multimodal and Procedural]] |
| F · Evaluation | 如何证明记忆真的有效、可迁移、可遗忘、可安全使用？ | 8 | [[20_Topics/Mainline F - Evaluation]] |
| G · Safety and Privacy | 记忆被读、写、检索、跨会话复用时会产生什么攻击面？ | 4 | [[20_Topics/Mainline G - Safety and Privacy]] |

另有 1 篇横切综述：

- [[10_Papers/storagetexperience|From Storage to Experience]] — 把记忆演化概括为 Storage → Reflection → Experience。

## 一页读懂主线关系

```text
A 架构：怎么组织
   ↓
B 策略：怎么管理
   ↓
C 系统：怎么高效运行
   ↓
D 巩固：怎么把经验变成长期记忆
   ↓
E 扩展：记忆什么类型的内容
   ↓
F 评测：怎么证明有效
   ↓
G 安全：怎么防止被利用
```

这不是单向依赖，而是七个正交视角。同一篇论文可能同时属于多个主线：

- MAGMA：A + C
- AgeMem：B + G（DELETE）
- TierMem：C + D
- MemoryAgentBench：F + D + G
- ReasoningBank：E + B
- LTS：E + B + C

## 当前最重要的五个判断

1. **结构记忆不是全面优于长上下文。**  
   优势集中在 multi-hop、temporal/causal、adversarial；single-hop、knowledge-update 仍常由 full-context 胜出。

2. **访问策略可能比存储结构更关键。**  
   MAGMA 的 adaptive policy、MRAgent 的 active reconstruction、AgeMem 的 learned policy 都支持这一点。

3. **“何时巩固”与“如何巩固”同等重要。**  
   RecMem 的 recurrence、Nemori 的 prediction error、TierMem 的 query-time escalation 都在改变 consolidation 时机。

4. **记忆系统的成本是多维的。**  
   token、latency、API calls、build time、storage 不能混为一个“效率分数”。

5. **遗忘和安全是共同缺口。**  
   A–E 线大多没有显式删除/回滚/权限；G 线证明这会带来真实攻击面。

## 主线之间的研究空白

| 空白 | 涉及主线 | 可做的 RQ |
|---|---|---|
| 结构 vs 策略的干净消融 | A + B | RQ1 |
| 记忆策略的跨领域迁移 | B + E | RQ2 |
| 可审计遗忘 | B + D + G | RQ3 |
| 多 agent 共享记忆的权限/冲突 | E + G | RQ4 |
| 程序性记忆与终身学习 | E + B | RQ5 |
| 统一评测协议 | F + 所有 | 方法论文 |

## 证据深度说明

| 深度 | 含义 | 当前覆盖 |
|---|---|---|
| L1 · metadata | 标题、venue、摘要 | 51/51 |
| L2 · experiment landscape | 数据集、baseline、主要设置 | 36/51（新增 15 篇待回填） |
| L3 · full-text scan | 方法、结果、局限、主线综合 | 50/51（ReasoningBank 使用摘要/实验地图） |
| L4 · evidence card | 页码级关键数字与来源 | 6/51 |
| L5 · reproduction | 代码/数据复现 | 0/51 |

> 下一步应优先把 L3 的核心论文提升到 L4，而不是继续无边界扩论文。

## 推荐阅读顺序

1. [[20_Topics/Mainline A - Memory Architecture]]
2. [[20_Topics/Mainline B - Memory Policy]]
3. [[20_Topics/Mainline D - Episodic Memory and Consolidation]]
4. [[20_Topics/Mainline C - Systems and Efficiency]]
5. [[20_Topics/Mainline F - Evaluation]]
6. [[20_Topics/Mainline G - Safety and Privacy]]
7. [[20_Topics/Mainline E - Personalization Multimodal and Procedural]]

## 下一步

1. 把 B–G 的核心论文各补 1–2 张 L4 证据卡。
2. 建立 `CLAIMS.md`，把七条主线的结论转成 claim–evidence–confidence。
3. 选定 RQ1，设计统一实验协议。
4. 把 `EXPERIMENT_LANDSCAPE.md` 的 15 篇新增论文回填。
