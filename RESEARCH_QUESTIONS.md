# Research Questions

> 主题：Agent Memory 2025+
> 详细想法页：`vault/30_Ideas/Agent Memory Research Questions.md`
> 当前实验/baseline 参照：`vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md`
> 开题设计与写作规范：`开题报告/README.md`

## 当前优先级

| ID | 问题 | 状态 | 核心论文 | 下一步 |
|---|---|---|---|---|
| RQ1 | 记忆结构何时优于长上下文？ | exploring | A-Mem、LongMemEval、Beyond a Million Tokens | 比较结构记忆 vs 长上下文 vs RAG 的 Pareto 前沿 |
| RQ2 | 记忆策略能否跨领域迁移？ | seed | MemAgent、Memory-R1、MemEvolve | 定义迁移任务与训练成本 |
| RQ3 | 什么时候应该遗忘？ | exploring | PersistBench、Privacy Risks、Poison Once | 建立“性能—隐私—攻击”联合指标 |
| RQ4 | 共享记忆的权限与冲突如何设计？ | seed | G-Memory、Learning to Share | 建立共享粒度/权限模型 |
| RQ5 | 程序性记忆能否带来真正的终身学习？ | seed | Remember Me Refine Me、RecMem、TiMem | 设计负迁移与技能复用实验 |

## RQ1 — 记忆结构何时优于长上下文？

### 假设

当任务存在长时程依赖、冲突更新或跨会话证据复用时，结构化记忆的收益高于单纯增加上下文窗口。

### 需要的证据

- 相同 backbone 下的结构记忆 / 长上下文 / RAG 对照
- token 成本、延迟、准确率、冲突解决率
- 任务长度与信息密度的切片分析

### 风险

- 不同论文的数据集与指标不可直接比较
- 结构记忆可能只是隐式增加了计算量

## RQ2 — 记忆策略能否跨领域迁移？

### 假设

在对话任务上学到的 memory policy 可以部分迁移到代码 agent、科研 agent 或 Web agent，但需要领域适配。

### 需要的证据

- zero-shot / few-shot 迁移
- 训练成本与稳定性
- 记忆写入/检索/遗忘策略的消融

## RQ3 — 什么时候应该遗忘？

### 假设

有选择的遗忘可以同时提升任务性能和安全性，但需要显式的 provenance 与过期机制。

### 需要的证据

- 准确率 / 隐私泄露率 / 攻击成功率 / 延迟
- 删除、回滚、过期、冲突解决的联合评测

## RQ4 — 共享记忆的权限与冲突如何设计？

### 假设

多 agent 共享记忆需要“读写权限 + 证据来源 + 冲突裁决”三元结构，而不是单纯共享向量库。

## RQ5 — 程序性记忆能否带来真正的终身学习？

### 假设

从经验中提炼程序性记忆比保留更多 episodic traces 更接近终身学习，但可能引入负迁移。

## 选择规则

优先选择：

1. 能用 1–2 周做最小实验
2. 有明确反例
3. 能用现有 52 篇论文和 baseline timeline 建立基线
4. 有可复现指标

## 下一次收敛

建议先做 RQ1 或 RQ3。RQ1 更偏系统与评测，RQ3 更偏安全与记忆治理。
