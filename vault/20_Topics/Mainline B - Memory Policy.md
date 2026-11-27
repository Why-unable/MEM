---
type: topic
subtype: mainline-analysis
topic: "Agent Memory 2025+"
mainline: "B"
status: full-text-scan
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - mainline-b
  - memory-policy
---

# Mainline B - Memory Policy

> 范围：AgeMem、Memory-R1、MemAgent、MemEvolve、UMEM 五篇训练型记忆工作。
> 阅读方式：全文 PDF 扫描（方法、实验设置、主结果、消融/局限）+ `EXPERIMENT_LANDSCAPE.md` 交叉核对。
> 注意：五篇的 action space、训练数据和评测任务不同，不能直接把分数横向排名。

## 一句话结论

主线 B 的核心变化是：

```text
手工设计 memory pipeline
→ 让 agent 自己决定何时写、读、更新、总结、删除
→ 让 memory architecture 本身也可以被演化
```

这条线把记忆从“外部模块”推进为 **policy**。它也是 RQ1 中“访问策略是否比存储结构更关键”的直接实验场。

## 五篇论文的分工

| 论文 | 学习对象 | 核心机制 | 主要证据 |
|---|---|---|---|
| [AgeMem](../10_Papers/evidence/agemem-evidence.md) | LTM + STM 的 tool actions | ADD/UPDATE/DELETE + RETRIEVE/SUMMARY/FILTER；三阶段 RL + step-wise GRPO | 五个长程 benchmark；平均 41.96 / 54.31 |
| [Memory-R1](../10_Papers/memoryr1.md) | 外部记忆管理 | Memory Manager + Answer Agent；ADD/UPDATE/DELETE/NOOP；PPO/GRPO | 152 条训练 QA；LoCoMo/MSC/LongMemEval；3B–14B |
| [MemAgent](../10_Papers/memagent.md) | 长文档上下文压缩 | 分段处理 + overwrite memory + multi-conv RL | 8K 训练上下文外推到 3.5M QA；512K NIAH >95% |
| [MemEvolve](../10_Papers/memeolve.md) | memory architecture 本身 | 元进化 encode/store/retrieve/manage 设计空间 | 四个 agentic benchmark；最高 17.06% 提升 |
| [UMEM](../10_Papers/umem.md) | 记忆抽取 + 管理 | joint extraction/management；semantic neighborhood + GRPO | 五个 benchmark；多轮任务最高 +11.49 分 |

## 逐篇分析

### AgeMem：统一 LTM/STM 的 tool policy

**问题**：LTM 和 STM 通常分开设计，依赖 heuristic 或 auxiliary controller，无法端到端优化。

**方法**：

- 六类工具：`ADD / UPDATE / DELETE / RETRIEVE / SUMMARY / FILTER`。
- Stage 1：交互并写入 LTM。
- Stage 2：清空上下文、保留 LTM、注入 distractor，训练 STM 控制。
- Stage 3：需要同时使用 STM 和 LTM 的整合任务。
- Step-wise GRPO：把 terminal advantage broadcast 到每个记忆操作。

**关键结果**：

- Qwen2.5-7B：平均 28.05 → **41.96**。
- Qwen3-4B：平均 43.97 → **54.31**。
- RL 相对 no-RL：**+8.53 / +8.72** 个百分点。
- MQ：**0.533 / 0.605**。
- DELETE 从 0 增加到 0.08（Qwen2.5），说明 RL 真的学会了“丢弃”动作。

**最重要的含义**：AgeMem 把“遗忘”从评测问题变成了 policy 问题。但它的 DELETE 由任务奖励驱动，不是隐私/合规/审计驱动。

**局限**：固定工具集；两个 Qwen backbone；受控 benchmark；没有正式的删除审计/回滚机制。

### Memory-R1：最小监督的记忆管理

**问题**：现有 memory pipeline 是静态、heuristic 的，缺少“存什么、更新什么、检索什么”的学习机制。

**方法**：

- Memory Manager：学习 `ADD / UPDATE / DELETE / NOOP`。
- Answer Agent：先预选相关记忆，再推理回答。
- 两个 agent 分别用 PPO / GRPO 训练。
- 训练数据只有 **152 条 QA**。

**关键结果**：

- 在 LLaMA-3.1-8B 上，GRPO 相对基线提升 F1 **28.5%**、BLEU-1 **34.0%**、LLM-Judge **30.2%**（相对值）。
- 在 LoCoMo、MSC、LongMemEval 上泛化，覆盖 3B–14B。
- 说明“少量 outcome-driven 监督”可以学到可迁移的记忆管理行为。

**局限**：Manager 与 Answer Agent 分离；训练依赖特定数据构造；没有统一 action space；评测仍以 QA 为主。

### MemAgent：用 RL 学“怎么压缩上下文”

**问题**：无限长文档处理中，固定长度上下文和普通 length extrapolation 都会退化。

**方法**：

- 把长文本分段处理。
- 每段更新一个 overwrite memory。
- 用 multi-conv RL（DAPO 扩展）直接优化记忆能力，而不是只做 SFT。

**关键结果**：

- 从 **8K** 训练上下文外推到 **3.5M** QA，性能损失 **<10%**。
- 512K NIAH **>95%**。
- RL 版本显著优于 no-RL 版本。

**最重要的含义**：MemAgent 把“记忆”理解为可学习的 **compression policy**，不是外部数据库。它和 AgeMem 的区别是：AgeMem 管理 LTM+STM 的多种操作，MemAgent 专注长文档的 overwrite/compression。

**局限**：主要是长文档 QA/NIAH，不是多 session 对话；overwrite 可能丢失早期证据；没有多模态和真实交互环境。

### MemEvolve：让记忆架构本身进化

**问题**：即使记忆能帮 agent 进化，记忆架构本身仍是手工设计、静态的。

**方法**：

- 联合进化 agent 的经验知识和 memory architecture。
- EvolveLab：把 12 个代表性记忆系统抽象成 `encode / store / retrieve / manage` 模块。
- 在统一 codebase 中做跨任务、跨 backbone 的架构搜索/进化。

**关键结果**：

- 四个 agentic benchmark：GAIA、WebWalkerQA、xBench-DeepSearch、TaskCraft。
- SmolAgent / Flash-Searcher 最高提升 **17.06%**。
- 进化出的架构可以跨任务、跨 LLM 迁移。

**最重要的含义**：记忆系统的“设计空间”本身可以成为优化对象。这是从“学 policy”到“学 architecture”的跳跃。

**局限**：进化成本和搜索空间大；架构搜索的评测仍集中在 agentic benchmark；安全/遗忘/权限没有进入搜索目标。

### UMEM：联合优化抽取与管理

**问题**：现有方法主要优化 memory management，把 memory extraction 当成静态过程，导致积累 instance-specific noise。

**方法**：

- 同时优化 extraction 和 management。
- Semantic Neighborhood Modeling：在语义近邻 query 集群上评估记忆效用。
- Neighborhood-level marginal utility reward + GRPO。

**关键结果**：

- 五个 benchmark：AIME24+25、GPQA-Diamond、HLE、HotpotQA、ALFWorld。
- 多轮交互任务最高 **+11.49** 分。
- 连续演化过程中保持稳定提升。

**最重要的含义**：记忆的质量不只取决于“怎么管”，还取决于“抽取出什么”。Extraction 和 management 必须联合优化。

**局限**：需要构造语义邻域和 reward；评测跨推理、QA、embodied，任务异质性高；没有遗忘治理。

## 横向比较

| 维度 | AgeMem | Memory-R1 | MemAgent | MemEvolve | UMEM |
|---|---|---|---|---|---|
| 学习对象 | LTM+STM actions | memory manager + answer | context compression | memory architecture | extraction + management |
| 动作空间 | 6 tools | ADD/UPDATE/DELETE/NOOP | segment/overwrite | encode/store/retrieve/manage | extract/manage |
| 训练信号 | task+context+memory reward | outcome RL | multi-conv RL | evolutionary search | neighborhood utility + GRPO |
| 监督量 | 课程 + RL | 152 QA | 长文档任务 | benchmark-driven | 多 benchmark |
| 主要评测 | 5 long-horizon | 3 memory QA | RULER/LongBench/NIAH | 4 agentic | 5 heterogeneous |
| 显式 DELETE | 有 | 有 | 否 | 可搜索 | 否 |
| 主要风险 | 固定工具/受控环境 | 分离 agent/数据依赖 | 长文档偏置 | 搜索成本 | reward/邻域设计 |

## 五条结论

### B1：记忆正在从“模块”变成“policy”

AgeMem、Memory-R1、MemAgent 都在学习“何时做什么”，而不是只设计一个静态 memory store。

**证据强度**：强（多篇、多种 action space、多个 benchmark）。

### B2：统一 LTM/STM 管理比分别优化更有潜力

AgeMem 的 full system 在三个代表性 benchmark 上分别提升 +13.9% / +21.7% / +16.1%，并且 STM 工具带来额外收益。

**证据强度**：中等偏强（主要来自单篇，但消融完整）。

### B3：少量 outcome supervision 可以产生可迁移的记忆行为

Memory-R1 只用 152 条 QA，仍能泛化到 MSC、LongMemEval 和 3B–14B。

**证据强度**：中等（单篇；需要独立复现）。

### B4：记忆架构本身可以成为优化对象

MemEvolve 的 EvolveLab 和跨任务迁移说明“学 architecture”是可行方向。

**证据强度**：中等（单篇；搜索成本和可解释性仍是问题）。

### B5：遗忘仍主要是“任务奖励”而不是“治理”

AgeMem 和 Memory-R1 都有 DELETE，但目标是任务效用；没有 provenance、权限、审计、回滚和合规约束。

**证据强度**：强（跨多篇的共同缺口）。

## 对 RQ 的意义

- **RQ1**：B 线提供“policy vs structure”的对照。应比较 `graph + passive retrieval` 与 `flat + learned policy`。
- **RQ2**：Memory-R1 / MemEvolve / UMEM 都声称跨任务/跨 backbone 泛化，但缺少统一定义和压力测试。
- **RQ3**：AgeMem / Memory-R1 的 DELETE 是 RQ3 的策略入口，但不是治理入口。
- **RQ4**：多 agent 共享记忆的策略学习尚未出现；LTS 是准入控制，不是完整共享 policy。
- **RQ5**：ReasoningBank / ReMe 在 E 线处理程序性记忆，B 线的 policy 还没有和技能库结合。

## 建议的下一步实验

同一 backbone（Qwen2.5-7B 或 GPT-4o-mini）、同一 benchmark（LongMemEval-s + LoCoMo）：

```text
heuristic memory (A-Mem / Mem0)
vs learned manager (Memory-R1)
vs learned LTM+STM (AgeMem)
vs learned compression (MemAgent)
```

必须同时报告：

- task accuracy
- memory quality
- total training cost
- online token / latency
- delete/update success
- cross-benchmark transfer

## 证据边界

- AgeMem、Memory-R1、MemAgent 已完成页码级证据卡。
- MemEvolve、UMEM 已完成全文扫描，但尚未各自建立页码级证据卡。
- 五篇论文的分数不能直接横比；本页只做机制和证据方向比较。
