---
type: topic
subtype: mainline-analysis
topic: "Agent Memory 2025+"
mainline: "E"
status: evidence-checked
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - mainline-e
  - personalization
  - multimodal
  - procedural-memory
---

# Mainline E - Personalization, Multimodal and Procedural Memory

> 范围：Evoking/RF-Mem、PersonaAgent、M3-Agent、ReMe、ReasoningBank、MemRec、Learning to Share 七篇。
> 阅读方式：六篇全文 PDF 扫描；ReasoningBank 使用摘要 + `EXPERIMENT_LANDSCAPE.md` 交叉核对。
> 说明：本页把“个性化 / 多模态 / 程序性 / 应用 / 多 agent 共享”放在一起，是因为它们共同回答：**记忆到底应该存什么类型的东西？**

## 一句话结论

主线 A–D 主要研究“事实和事件怎么存、怎么取”；主线 E 把记忆对象扩展到：

```text
用户偏好 / persona
视觉与听觉经验
可复用技能 / 推理策略
协作信号
跨团队共享状态
```

核心问题从“记住历史”变成：

> 记忆如何改变 agent 的行动、推荐、协作和技能复用？

## 七篇论文的分工

| 论文 | 记忆类型 | 核心机制 | 关键证据 |
|---|---|---|---|
| [Evoking / RF-Mem](../10_Papers/evoking.md) | 用户个性化记忆 | familiarity 与 recollection 双路径；familiarity uncertainty 决定走哪条 | PersonaMem、PersonaBench、LongMemEval；固定预算下优于 one-shot/full-context |
| [PersonaAgent](../10_Papers/personaagent.md) | persona + episodic/semantic memory | persona prompt 作为 memory-action 中介；test-time preference alignment | LaMP 系列；优于 prompt/ICL/RAG/PAG/ReAct/MemBank |
| [M3-Agent](../10_Papers/multimodal.md) | 多模态 episodic/semantic memory | entity-centric 多模态记忆；多轮推理检索 | M3-Bench-robot +6.7%、M3-Bench-web +7.7%、VideoMME-long +5.3% |
| [ReMe](../10_Papers/rememberrefine.md) | 程序性记忆 | distillation + context-adaptive reuse + utility-based refinement | BFCL-V3、AppWorld；Qwen3-8B+ReMe > Qwen3-14B memoryless |
| [ReasoningBank](../10_Papers/reasoningbank.md) | 推理策略记忆 | 从成功/失败轨迹蒸馏 generalizable reasoning strategies；MaTTS | web browsing / software engineering；优于 raw-trajectory 和 success-only memory |
| [MemRec](../10_Papers/memrec.md) | 协作记忆 | 独立 LM_Mem 管理 collaborative memory graph；LLM_Rec 只接收蒸馏上下文 | 4 个推荐 benchmark SOTA |
| [Learning to Share](../10_Papers/learnshare.md) | 跨团队共享记忆 | global memory bank + learned admission controller；stepwise RL | AssistantBench、GAIA；降低 runtime，性能匹配或提升 |

## 逐篇分析

### Evoking / RF-Mem：familiarity + recollection 双过程

**问题**：个性化记忆要么把所有历史塞进 prompt，要么只做一次相似度检索，无法兼顾召回和噪声。

**方法**：

- 用 similarity 的均值/熵衡量 familiarity。
- 高 familiarity：直接 top-K familiarity retrieval。
- 低 familiarity：进入 recollection path，对候选记忆聚类，用 α-mix 迭代扩展证据。
- 在固定 budget/latency 下自适应切换。

**证据**：PersonaMem（32K/128K/1M）、PersonaBench、LongMemEval；优于 one-shot retrieval 和 full-context。

**意义**：个性化记忆不是“检索更多”，而是“知道什么时候需要深挖”。

**局限**：依赖 familiarity 信号校准；recollection 路径增加延迟；评测集中在个性化 benchmark。

### PersonaAgent：persona 作为记忆与行动的桥梁

**问题**：现有 agent 对用户采用 one-size-fits-all，缺少个性化行动空间。

**方法**：

- personalized memory：episodic + semantic。
- personalized action：工具动作按用户定制。
- persona（用户专属 system prompt）连接 memory 和 action。
- test-time user-preference alignment：模拟最近 n 次交互，用文本 loss 优化 persona。

**证据**：LaMP-1/2M/2N/3；优于 Prompt、ICL、RAG、PAG、ReAct、MemBank。

**意义**：个性化不是“把用户资料塞进 prompt”，而是让记忆影响 **action selection**。

**局限**：persona prompt 可能漂移；test-time 优化成本；隐私和用户控制未展开。

### M3-Agent：实体中心的多模态长期记忆

**问题**：多模态 agent 需要处理实时视觉/听觉输入，并跨时间积累世界知识。

**方法**：

- entity-centric multimodal memory：episodic + semantic。
- 多轮推理和检索。
- 通过 RL 训练。
- 构建 M3-Bench：100 个 robot-perspective 视频 + 920 个 web 视频。

**证据**：

- M3-Bench-robot **+6.7%**。
- M3-Bench-web **+7.7%**。
- VideoMME-long **+5.3%**。
- 对比最强 baseline 是 Gemini-1.5-Pro + GPT-4o prompting agent。

**意义**：多模态记忆的核心单元是 **entity**，而不是文本 chunk。

**局限**：视频 QA 评测；多模态存储/检索成本；隐私（视觉/听觉）风险未展开。

### ReMe：程序性记忆的生命周期

**问题**：现有程序性记忆多为 append-only archive，缺少失败分析、上下文适配和过期清理。

**方法**：

- multi-faceted distillation：成功模式、失败触发、比较性 insight。
- context-adaptive reuse：按场景索引历史 insight。
- utility-based refinement：增加有效记忆，剪除过期记忆。

**证据**：BFCL-V3、AppWorld；Qwen3-8B + ReMe 超过 memoryless Qwen3-14B。

**意义**：程序性记忆的竞争力来自“提炼 + 复用 + 修剪”，不是存更多轨迹。

**局限**：utility 评估依赖任务反馈；跨领域迁移未充分验证；剪枝可能误删低频技能。

### ReasoningBank：从轨迹到推理策略

**问题**：agent 无法从历史交互中学习，重复犯错、丢弃 insight。

**方法**：

- 从 self-judged 成功/失败经验中蒸馏 generalizable reasoning strategies。
- 测试时检索相关 memory，并把新学习写回。
- MaTTS：用 memory-aware test-time scaling 生成更多对比经验。

**证据**：web browsing、software engineering；优于 raw trajectories / success-only memory；MaTTS 进一步增强。

**意义**：记忆的抽象层级从“事件”上升到“推理策略”，这是程序性记忆的核心。

**局限**：self-judge 噪声；test-time scaling 成本；策略可能过拟合任务分布。

### MemRec：协作记忆

**问题**：LLM 推荐 agent 的用户/物品记忆彼此孤立，忽略用户-物品共现和社区关系。

**方法**：

- collaborative memory graph。
- 独立轻量 LM_Mem 在后台管理和合成记忆。
- 只把 distilled high-signal context 交给重型 LLM_Rec。

**证据**：Amazon Books、Goodreads、MovieTV、Yelp 四个 benchmark SOTA。

**意义**：记忆不仅是个人的，也可以是 **群体协作信号**；管理模型与推理模型解耦是系统关键。

**局限**：推荐领域专用；协作记忆的隐私/权限问题未展开；graph 维护成本。

### Learning to Share：跨团队选择性共享

**问题**：并行多 agent 团队会重复计算相似子问题，造成大量冗余。

**方法**：

- global memory bank 对所有团队可见。
- lightweight controller 学习“这个 intermediate step 是否值得写入共享记忆”。
- stepwise RL + usage-aware credit assignment。

**证据**：AssistantBench、GAIA；显著降低 runtime，性能匹配或提升 memory-free parallel baseline。

**意义**：多 agent 记忆的核心不是“共享越多越好”，而是 **admission control**。

**局限**：共享记忆的权限、冲突、责任归属未解决；评测集中在 GAIA/AssistantBench。

## 横向比较

| 维度 | Evoking | PersonaAgent | M3-Agent | ReMe | ReasoningBank | MemRec | LTS |
|---|---|---|---|---|---|---|---|
| 记忆对象 | 用户历史/偏好 | persona + episodic/semantic | 视觉/听觉实体 | 技能/经验 | 推理策略 | 协作信号 | 跨团队中间结果 |
| 访问策略 | familiarity/recollection | persona 中介 + action | 多轮推理检索 | 场景索引 | 检索 + 写回 | 图管理 + 蒸馏 | learned admission |
| 学习方式 | training-free | test-time alignment | RL | 经验蒸馏/剪枝 | 经验蒸馏 + test-time scaling | LM_Mem 管理 | stepwise RL |
| 主要评测 | PersonaMem/LaMP-like | LaMP | M3-Bench/VideoMME | BFCL/AppWorld | Web/SWE | Amazon/Yelp | AssistantBench/GAIA |
| 主要风险 | 延迟/校准 | persona 漂移 | 多模态隐私 | 误剪枝 | self-judge 噪声 | 协作隐私 | 共享权限/冲突 |

## 五条结论

### E1：记忆对象正在从“事实”扩展到“用户、事件、技能、协作信号”

这是主线 E 与 A–D 最大的区别。记忆的“内容类型”决定了它的结构、检索和评测。

**证据强度**：强。

### E2：个性化记忆的关键是“何时深挖”，不是“存多少”

Evoking 的 familiarity/recollection 双路径和 PersonaAgent 的 persona-action 闭环都说明：访问策略比记忆容量更重要。

**证据强度**：中等偏强。

### E3：程序性记忆的核心是“提炼 + 复用 + 修剪”

ReMe 和 ReasoningBank 都不满足于存轨迹；它们提炼成功/失败模式，并强调 utility/refinement。

**证据强度**：强。

### E4：多模态记忆需要实体中心的结构

M3-Agent 的 entity-centric 设计与文本 memory 的 chunk/笔记结构明显不同。

**证据强度**：中等（单篇，但 benchmark 完整）。

### E5：多 agent 共享记忆的关键是 admission control 和权限

LTS 证明“选择性共享”能降成本；但共享权限、冲突裁决、责任归属仍是空白。

**证据强度**：中等偏强。

## 对 RQ 的意义

- **RQ1**：个性化/多模态任务中，full-context 往往不可行，结构记忆的收益更明显；但成本与隐私约束更复杂。
- **RQ2**：程序性记忆的跨领域迁移是 RQ2 的核心证据。
- **RQ3**：ReMe 的剪枝、PersonaAgent 的用户控制、M3-Agent 的多模态隐私都指向记忆治理。
- **RQ4**：LTS 是共享记忆的 admission control，但不是完整权限模型。
- **RQ5**：ReMe/ReasoningBank 直接对应“程序性记忆能否带来终身学习”。

## 建议的下一步实验

```text
任务：个性化 + 程序性
条件：
  full context
  RAG
  persona memory (PersonaAgent-like)
  dual-process retrieval (RF-Mem-like)
  procedural memory (ReMe/ReasoningBank-like)
指标：
  task success
  personalization accuracy
  skill reuse / negative transfer
  token / latency
  privacy leakage (for persona/multimodal)
```

## 证据边界

- 七篇均已完成页码级证据卡（ReasoningBank 使用 arXiv 全文补齐）。
- 尚未为 Evoking、PersonaAgent、M3-Agent、ReMe、ReasoningBank、MemRec、LTS 建立独立页码级证据卡。
- 评测领域差异很大，不能直接把 LaMP、M3-Bench、BFCL、GAIA 的分数横比。
