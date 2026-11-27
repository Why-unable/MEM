---
type: topic
subtype: mainline-analysis
topic: "Agent Memory 2025+"
mainline: "C"
status: full-text-scan
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - mainline-c
  - system
  - efficiency
---

# Mainline C - Systems and Efficiency

> 范围：LightMem、Mem0、MemoryOS、EverMemOS、Hippocampus、LightWM、LightMem (SLM)、SimpleMem 八篇系统/效率工作。
> 阅读方式：全文 PDF 扫描（系统架构、写入/巩固路径、实验设置、成本指标）+ `EXPERIMENT_LANDSCAPE.md` 交叉核对。
> 注意：token、latency、API calls、build time、storage 是不同成本维度，不能混为一个“效率分数”。

## 一句话结论

主线 C 的共同问题是：

> 记忆系统不是“能不能记住”，而是“用什么成本、在什么时间、以什么精度记住”。

八篇论文形成了四个系统设计方向：

```text
层次化 memory OS        MemoryOS / EverMemOS
在线-离线解耦           LightMem / LightMem (SLM)
压缩与索引               SimpleMem / Hippocampus
小模型/小上下文控制       LightWM / LightMem (SLM)
```

## 八篇论文的分工

| 论文 | 系统定位 | 核心机制 | 主要成本/效果证据 |
|---|---|---|---|
| [LightMem](../10_Papers/lightmem.md) | 轻量长期记忆 | sensory → short-term → long-term；sleep-time update | QA 最高 +7.7% / +29.3%；token 最多降 38x / 20.9x；API calls 降 30x / 55.5x |
| [Mem0](../10_Papers/mem0.md) | 生产级记忆流水线 | extract → consolidate → retrieve；可选 graph memory | LLM-Judge 相对 OpenAI +26%；p95 latency -91%；token -90%+ |
| [MemoryOS](../10_Papers/memoryos.md) | 分层 memory OS | short / mid / long-term；FIFO + segmented page | LoCoMo F1 +48.36%、BLEU-1 +46.18% over baselines（GPT-4o-mini） |
| [EverMemOS](../10_Papers/evermemos.md) | 自组织 memory OS | Episodic Trace → Semantic Consolidation → Reconstructive Recollection | LoCoMo / LongMemEval / PersonaMem-v2 优于 SOTA |
| [Hippocampus](../10_Papers/hippocampus.md) | 高效可扩展记忆模块 | compact binary signatures + lossless token-ID streams + DWM | 1.1x–31.5x 检索加速；1.1x–14.5x token 降低 |
| [LightWM](../10_Papers/lightwm.md) | 小模型工作记忆 | task/subtask 两层 memory；一次离线 schema induction | Qwen3-4B ALFWorld valid_unseen 0.910 vs 基线 <0.320 |
| [LightMem (SLM)](../10_Papers/lightmem-slm.md) | SLM 驱动记忆 | STM/MTM/LTM；固定检索预算；两阶段检索 | LoCoMo F1 平均 +2.5 over A-Mem；检索 83ms、端到端 581ms |
| [SimpleMem](../10_Papers/simplemem.md) | 压缩型终身记忆 | semantic structured compression + online synthesis + intent-aware planning | LoCoMo 平均 F1 +26.4%；推理 token 最多降 30x |

## 逐篇分析

### LightMem：把 consolidation 移出在线推理

- **问题**：现有记忆系统在线处理成本高。
- **方法**：sensory memory 过滤 → topic-aware short-term memory 组织 → long-term memory 做 sleep-time update。
- **关键点**：把高成本整合放到 offline，在线只做轻量压缩和检索。
- **证据**：QA 最高提升 7.7% / 29.3%；总 token 最多降 38x / 20.9x；在线 token 最多降 106x / 117x。
- **局限**：依赖 topic/compression 质量；没有遗忘治理；收益主要在 LoCoMo/LongMemEval。

### Mem0：生产级 extract-consolidate-retrieve

- **问题**：多 session 对话中固定上下文窗口导致不一致。
- **方法**：从对话中抽取 salient memory，持续 consolidate，再按 query 检索；可选 graph memory 捕捉关系。
- **证据**：LLM-Judge 相对 OpenAI memory +26%；Mem0g 比 base Mem0 再高约 2%；p95 latency -91%，token -90%+。
- **局限**：extraction 质量依赖 LLM；graph 变体增加复杂度；没有显式删除/审计。

### MemoryOS：操作系统式三级存储

- **问题**：缺少系统级的存储、更新、检索和生成管理。
- **方法**：short-term / mid-term / long-term personal memory；short→mid 用 dialogue-chain FIFO，mid→long 用 segmented page。
- **证据**：LoCoMo 上 F1 +48.36%、BLEU-1 +46.18%（GPT-4o-mini）。
- **局限**：主要是对话 benchmark；OS 类比强但缺少真实系统资源指标；无 forgetting governance。

### EverMemOS：自组织 memory OS

- **问题**：记忆系统只存孤立记录、检索碎片，无法巩固经验和解决冲突。
- **方法**：
  - Episodic Trace Formation：对话流 → MemCell（episodic trace + atomic fact + foresight）。
  - Semantic Consolidation：MemCell → MemScene，更新用户 profile。
  - Reconstructive Recollection：MemScene-guided agentic retrieval。
- **证据**：LoCoMo、LongMemEval、PersonaMem-v2 优于 SOTA。
- **局限**：三层生命周期复杂；场景/主题质量依赖 LLM；尚未给出统一成本 Pareto。

### Hippocampus：压缩域检索

- **问题**：dense vector、KG traversal、hybrid 检索延迟高、存储扩展差。
- **方法**：compact binary signatures 做语义搜索，lossless token-ID streams 做精确内容重构；Dynamic Wavelet Matrix 同时压缩/索引两路。
- **证据**：1.1x–31.5x 检索加速；1.1x–14.5x token footprint 降低；LoCoMo/LongMemEval 上 accuracy 有竞争力。
- **局限**：系统实现复杂；对 tokenizer/压缩结构有依赖；评测以检索和 QA 为主。

### LightWM：小模型的分层工作记忆

- **问题**：SLM 在长程 procedure-centric 任务中难以保留状态。
- **方法**：task-level global memory + subtask-level local memory；用少量成功轨迹离线 induction schema；训练-free。
- **证据**：Qwen3-4B 在 ALFWorld valid_unseen 达到 **0.910**，同设置基线 **<0.320**。
- **局限**：主要面向 procedure-centric/embodied 任务；schema induction 依赖任务族；不是通用对话记忆。

### LightMem (SLM)：小模型做记忆控制器

- **问题**：LLM 在线记忆操作延迟高；纯检索又不稳定。
- **方法**：STM/MTM/LTM；固定检索预算；vector coarse retrieval + semantic consistency re-ranking；offline consolidation。
- **证据**：LoCoMo F1 平均比 A-Mem 高约 **2.5**；检索 **83ms**、端到端 **581ms**。
- **局限**：与 ICLR 2026 的 LightMem 同名但不同工作，引用时必须区分；主要面向对话记忆。

### SimpleMem：语义无损压缩

- **问题**：全历史冗余；迭代推理过滤噪声又太贵。
- **方法**：
  - Semantic Structured Compression：交互 → compact multi-view indexed units。
  - Online Semantic Synthesis：会话内即时合并。
  - Intent-Aware Retrieval Planning：根据 intent 决定检索范围。
- **证据**：LoCoMo 平均 F1 **+26.4%**；推理 token 最多降 **30x**。
- **局限**：压缩可能损失证据；intent planning 依赖 LLM；缺少长期更新/删除。

## 横向比较

| 维度 | LightMem | Mem0 | MemoryOS | EverMemOS | Hippocampus | LightWM | LightMem (SLM) | SimpleMem |
|---|---|---|---|---|---|---|---|---|
| 核心抽象 | 三阶段 | 流水线 | OS 三级 | 生命周期 | 压缩索引 | 双层 working memory | SLM 三阶段 | 压缩流水线 |
| 在线/离线解耦 | 强 | 中 | 中 | 强 | 强 | 强（离线 induction） | 强 | 中 |
| 结构 | 主题/阶段 | 记忆条目 | 层次 | MemCell/MemScene | 二进制+token stream | task/subtask | STM/MTM/LTM | multi-view units |
| 主要优化 | token/API | latency/token | 层次更新 | 巩固/冲突 | latency/storage | SLM 成功率 | latency/token | token/密度 |
| 主要评测 | LoCoMo/LongMemEval | LoCoMo | LoCoMo | LoCoMo/LongMemEval/PersonaMem | LoCoMo/LongMemEval | ALFWorld | LoCoMo | LoCoMo |
| 显式遗忘 | 无 | 无 | 无 | 无 | 无 | 无 | 无 | 无 |

## 五条结论

### C1：在线/离线解耦是系统效率的核心设计

LightMem、LightMem (SLM)、LightWM、EverMemOS 都把高成本 consolidation/induction 放到离线或后台。

**证据强度**：强（多篇、多种实现）。

### C2：层次化存储仍然是主流系统抽象

MemoryOS、EverMemOS、LightWM 都采用不同形式的层次结构，说明“短期/长期”“全局/局部”是有效的组织原则。

**证据强度**：中等偏强。

### C3：压缩/索引可以显著降低 token 和延迟，但证据保留是代价

SimpleMem、Hippocampus、LightMem 都报告了大幅成本下降；但压缩是否保留关键证据、如何处理冲突和更新，仍缺少统一评测。

**证据强度**：中等。

### C4：小模型可以承担记忆控制，但任务范围有限

LightWM 和 LightMem (SLM) 说明 SLM 可以在特定任务上做记忆控制/检索；但主要是 procedure-centric 或对话任务，尚未证明通用性。

**证据强度**：中等。

### C5：系统效率的“成本口径”仍不统一

- LightMem：total token / API calls / online token。
- Mem0：p95 latency / token cost。
- MemoryOS：F1/BLEU。
- Hippocampus：speedup / token footprint。
- LightWM：success rate。
- LightMem (SLM)：F1 / latency。
- SimpleMem：F1 / token。

**证据强度**：强（跨论文事实）。这也是 RQ1 必须解决的测量问题。

## 对 RQ1 的意义

主线 C 给 RQ1 增加了“效率轴”：

```text
accuracy
× total token
× online token
× latency
× API calls
× storage
× build time
```

如果只比较 accuracy，会高估“重型结构记忆”；如果只比较 query token，会低估构建成本。RQ1 的 Pareto 前沿必须同时包含在线和离线成本。

## 建议的最小实验

同一 backbone、同一 benchmark：

```text
full context
vs Mem0-like pipeline
vs LightMem-like offline consolidation
vs MemoryOS-like hierarchy
vs SimpleMem-like compression
```

报告：

- accuracy / judge
- online token
- offline/build token
- p50/p95 latency
- storage footprint
- update/delete cost

## 证据边界

- 八篇均已完成全文扫描。
- LightMem 已完成页码级证据卡。
- Mem0、MemoryOS、EverMemOS、Hippocampus、LightWM、LightMem (SLM)、SimpleMem 尚未建立独立页码级证据卡。
- 分数不可直接横比；本页只比较系统设计和成本维度。
