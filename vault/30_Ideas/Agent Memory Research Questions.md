---
type: idea
status: seed
created: 2026-11-19
tags:
  - idea
  - agent-memory
---

# Agent Memory Research Questions

> 这是从 `Agent Memory 2025+` 地图中提取的初始研究问题，不是最终选题。后续应通过论文精读和实验设计逐步收敛。

## RQ1：记忆结构何时优于长上下文？

- 相关：[[10_Papers/amem]]、[[10_Papers/beyondmillion]]、[[10_Papers/longmemeval]]
- 可能变量：任务长度、信息密度、时间依赖、冲突频率
- 需要证据：相同 backbone 下，结构记忆 vs 长上下文 vs RAG 的 Pareto 前沿

## RQ2：记忆策略能否跨领域迁移？

- 相关：[[10_Papers/memagent]]、[[10_Papers/memoryr1]]、[[10_Papers/memeolve]]
- 可能问题：在对话任务上学到的 memory policy，能否迁移到代码 agent、科研 agent、Web agent？
- 需要证据：跨任务 zero-shot / few-shot 迁移，训练成本与稳定性

## RQ3：什么时候应该遗忘？

- 相关：[[10_Papers/persistbench]]、[[10_Papers/privacy]]、[[10_Papers/poisononce]]
- 可能问题：遗忘是否可以同时提升任务性能和安全性？
- 需要证据：遗忘策略对准确率、隐私泄露率、攻击成功率、延迟的联合影响

## RQ4：共享记忆的权限与冲突如何设计？

- 相关：[[10_Papers/gmemory]]、[[10_Papers/learnshare]]
- 可能问题：多 agent 共享记忆时，谁可以写、谁可以读、冲突如何裁决？
- 需要证据：共享粒度 × 权限模型 × 冲突解决的消融

## RQ5：程序性记忆能否带来真正的终身学习？

- 相关：[[10_Papers/rememberrefine]]、[[10_Papers/recmem]]、[[10_Papers/tiermem]]
- 可能问题：从历史经验提炼技能，是否优于保存更多 episodic traces？
- 需要证据：跨任务技能复用、负迁移、遗忘曲线

## 下一步

1. 从 RQ1 或 RQ3 选一个最小可做问题。
2. 精读 5–8 篇相关论文，补“方法/数据/指标/局限”。
3. 写出一个可证伪的假设。
4. 设计一个 1–2 周能跑通的最小实验。
