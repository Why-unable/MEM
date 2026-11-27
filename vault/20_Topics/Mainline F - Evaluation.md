---
type: topic
subtype: mainline-analysis
topic: "Agent Memory 2025+"
mainline: "F"
status: evidence-checked
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - mainline-f
  - evaluation
  - benchmark
---

# Mainline F - Evaluation

> 范围：LongMemEval、MemoryArena、PersistBench、MemBench、Minerva、BEAM / Beyond a Million Tokens、MemoryAgentBench、MemoryBench 八个评测/基准工作。
> 阅读方式：全文 PDF 扫描（任务设计、能力维度、数据规模、指标、主要发现）+ `EXPERIMENT_LANDSCAPE.md` 交叉核对。
> 说明：benchmark 不是排行榜；同一个 benchmark 的不同版本、judge、切分和 top-k 都会改变结论。

## 一句话结论

Agent memory 评测已经从“记住没有”扩展为至少八个维度：

```text
retrieval
multi-session reasoning
temporal reasoning
knowledge update
selective forgetting
test-time learning
action-coupled memory
safety / leakage
```

但目前 **没有一个 benchmark 同时覆盖全部维度**。因此：

> 论文里的“SOTA”必须写成“在某个 capability profile 上的 SOTA”，不能写成“agent memory 全面 SOTA”。

## 八个 benchmark 的分工

| Benchmark | 核心能力 | 规模/场景 | 关键发现 |
|---|---|---|---|
| [LongMemEval](../10_Papers/longmemeval.md) | extraction、multi-session、temporal、knowledge update、abstention | 500 问；历史可扩到 115K / 1.5M tokens | 商业助手/长上下文模型在持续交互中出现约 30% 准确率下降 |
| [MemoryArena](../10_Papers/interdependent.md) | action-coupled multi-session memory | web navigation、travel planning、progressive search、formal reasoning | LoCoMo 接近饱和的 agent 在 interdependent 任务上表现很差 |
| [PersistBench](../10_Papers/persistbench.md) | cross-domain leakage、memory-induced sycophancy | 500 样本（200/200/100）；18 个 LLM | 中位失败率：cross-domain 53%，sycophancy 97% |
| [MemBench](../10_Papers/membench.md) | factual/reflective memory × participation/observation | 多场景、多指标 | 评测 effectiveness、efficiency、capacity，而不是单一 QA |
| [Minerva](../10_Papers/minerva.md) | programmable memory tests | 1,110 个测试；4K 上下文；atomic + composite | 可拆分 search/recall/edit/match/compare/compute/stateful processing |
| [BEAM / LIGHT](../10_Papers/beyondmillion.md) | 10M token 长对话 + 多类记忆能力 | 100 conversations、2,000 questions、128K–10M tokens | 1M context 模型仍随对话变长而退化；LIGHT +3.5%–12.69% |
| [MemoryAgentBench](../10_Papers/memoryagentbench.md) | retrieval、test-time learning、long-range understanding、selective forgetting | 增量多轮格式 | 现有 memory agents 没有同时掌握四项能力 |
| [MemoryBench](../10_Papers/memorybench.md) | continual learning from user feedback | 多领域、多语言、多任务 | 现有 SOTA 在持续学习上仍远未满足 |

## 逐篇分析

### LongMemEval：长期交互记忆的五能力基准

**设计**：

- 500 个手工问题。
- 五个核心能力：information extraction、multi-session reasoning、temporal reasoning、knowledge update、abstention。
- 历史长度可扩展：LongMemEval-S 约 115K tokens，LongMemEval-M 约 1.5M tokens。
- 将 memory design 拆成 indexing / retrieval / reading 三阶段。

**关键发现**：商业聊天助手和长上下文模型在持续交互中出现约 **30%** 准确率下降。

**贡献**：把“长期记忆”从单一 recall 任务拆成五种能力，并给出 session decomposition、fact-augmented key expansion、time-aware query expansion 等优化。

**局限**：主要是对话 QA；没有 action coupling；没有安全/隐私维度。

### MemoryArena：记忆是否真的指导行动

**设计**：

- multi-session Memory-Agent-Environment loop。
- 四类任务：Bundled Web Shopping、Group Travel Planning、Progressive Web Search、Math/Physics Formal Reasoning。
- 子任务显式相互依赖：前面行动获得的信息必须被记忆并在后续任务中使用。

**关键发现**：在 LoCoMo 等长上下文 benchmark 上接近饱和的 agent，在 MemoryArena 上表现很差。

**贡献**：把“记忆”从被动 recall 推向“记忆指导行动”。

**局限**：环境/任务工程复杂；评分与 agent scaffold 强耦合；尚未覆盖多模态和安全。

### PersistBench：记忆何时应该被忘记

**设计**：

- 500 样本：
  - 200 cross-domain leakage
  - 200 memory-induced sycophancy
  - 100 beneficial memory
- 18 个 frontier / open-source LLM。

**关键发现**：

- cross-domain 中位失败率 **53%**。
- sycophancy 中位失败率 **97%**。
- 记忆持久化本身会制造安全风险。

**贡献**：把“遗忘”从能力问题变成安全问题；提供了 cross-domain leakage 和 sycophancy 两类长期记忆特有风险。

**局限**：主要是行为评测；没有统一的防御 baseline；尚未覆盖多 agent 共享记忆。

### MemBench：多场景、多层次的综合评测

**设计**：

- factual memory vs reflective memory。
- participation vs observation 两种交互场景。
- 指标覆盖 effectiveness、efficiency、capacity。

**贡献**：比单一 QA benchmark 更全面地刻画“记忆能力”。

**局限**：任务/数据仍以对话和模拟环境为主；能力维度与 LongMemEval/MemoryAgentBench 有重叠但不可直接对齐。

### Minerva：可编程记忆测试

**设计**：

- 1,110 个测试，4K 上下文。
- atomic tasks：search、recall、edit、match、compare、compute、stateful processing。
- composite tests：组合多个原子能力。

**贡献**：把 memory 能力拆成可解释的原子测试，而不是只看端到端 QA。

**局限**：上下文规模较小；更偏“模型如何使用上下文”，不完全等同长期记忆系统。

### BEAM / Beyond a Million Tokens：规模压力测试

**设计**：

- BEAM：100 个长对话、2,000 个验证问题、128K–10M tokens、10 类记忆能力。
- LIGHT：long-term episodic memory + short-term working memory + scratchpad。

**关键发现**：

- 即使 1M context 模型（含 RAG）也会随对话变长而退化。
- LIGHT 相对最强 baseline 提升 **3.5%–12.69%**。

**贡献**：把规模推到 10M token，并证明“更长上下文 ≠ 更好记忆”。

**局限**：合成/生成式长对话；10 类能力的定义与 LongMemEval/MemoryAgentBench 不完全一致。

### MemoryAgentBench：四项核心能力

**设计**：

- 把 long-context 数据改造成增量多轮格式。
- 四项能力：
  1. accurate retrieval
  2. test-time learning
  3. long-range understanding
  4. selective forgetting

**关键发现**：现有 memory agents 没有同时掌握四项能力。

**贡献**：把 test-time learning 和 selective forgetting 纳入统一评测，是最接近 RQ1/RQ3 联合评测的 benchmark。

**局限**：增量多轮格式仍是模拟；action coupling 不如 MemoryArena；安全维度不如 PersistBench。

### MemoryBench：持续学习与用户反馈

**设计**：

- 用户反馈模拟框架。
- 多领域、多语言、多任务。
- 评测 LLMsys 在服务时从累计反馈中学习的能力。

**关键发现**：现有 SOTA 的有效性和效率都远未满足。

**贡献**：把“memory”从静态历史检索扩展到 **continual learning from feedback**。

**局限**：更偏 LLM system 的持续学习；与 agentic memory 的 action loop 还未完全结合。

## 能力覆盖矩阵

图例：`●` 核心覆盖，`○` 部分覆盖，空白表示基本不覆盖。

| Benchmark | Retrieval | Multi-session | Temporal | Update | Forgetting | Test-time learning | Action coupling | Safety |
|---|---|---|---|---|---|---|---|---|
| LongMemEval | ● | ● | ● | ● | ○ |  |  |  |
| MemoryArena | ● | ● | ○ | ○ |  | ○ | ● |  |
| PersistBench | ○ | ○ |  | ○ | ● |  |  | ● |
| MemBench | ● | ● | ○ | ○ | ○ |  | ○ |  |
| Minerva | ● | ○ | ○ | ● | ○ | ○ |  |  |
| BEAM | ● | ● | ● | ● | ○ | ○ |  |  |
| MemoryAgentBench | ● | ● | ● | ● | ● | ● | ○ |  |
| MemoryBench | ● | ● | ○ | ● | ○ | ● | ○ |  |

## 五条结论

### F1：评测已经从“记忆准确率”分裂为多能力 profile

LongMemEval、MemoryArena、PersistBench、MemoryAgentBench 分别代表不同的能力组合。没有单一分数能代表 agent memory。

**证据强度**：强。

### F2：长上下文 benchmark 会高估 agent 的记忆能力

MemoryArena 显示：LoCoMo 上接近饱和的 agent，在 interdependent action 任务上表现很差。

**证据强度**：强。

### F3：遗忘和安全已经成为独立评测维度

PersistBench 的 53% / 97% 失败率说明：记忆持久化本身可能是风险，而不是能力。

**证据强度**：强。

### F4：test-time learning 与 continual learning 仍缺少统一协议

MemoryAgentBench 和 MemoryBench 都指向“从交互中学习”，但一个偏 incremental memory，一个偏 user feedback continual learning。

**证据强度**：中等偏强。

### F5：benchmark 之间的指标不可直接对齐

- LongMemEval：QA accuracy / judge。
- MemoryArena：task success / interdependent subtask completion。
- PersistBench：failure rate / leakage / sycophancy。
- MemBench：effectiveness / efficiency / capacity。
- Minerva：atomic/composite test accuracy。
- BEAM：multi-ability QA。
- MemoryAgentBench：four competencies。
- MemoryBench：continual learning performance。

**证据强度**：强。

## 对 RQ1 的评测设计

RQ1 不能只用 LoCoMo。建议使用 **capability-stratified evaluation**：

```text
LongMemEval-S     → extraction / multi-session / temporal / update / abstention
MemoryArena       → action-coupled multi-session
PersistBench      → leakage / sycophancy / beneficial memory
MemoryAgentBench  → retrieval / test-time learning / long-range / selective forgetting
BEAM              → 128K–10M scale stress test
```

报告时按能力维度拆分，而不是只报 overall。

### 必须报告的指标

- accuracy / judge
- evidence recall
- input tokens / output tokens
- build tokens
- p50/p95 latency
- storage
- update success
- stale-memory rate
- deletion / leakage rate（RQ3）

## 建议的统一评测协议 v0

1. **任务层**：single-hop、multi-hop、temporal、update、abstention、action-coupled。
2. **记忆层**：retrieval recall、evidence precision、conflict resolution、forgetting success。
3. **系统层**：online/offline token、latency、storage、build cost。
4. **治理层**：leakage、sycophancy、deletion audit、permission。
5. **学习层**：test-time improvement、continual learning、negative transfer。

## 证据边界

- 八个 benchmark 均已完成全文扫描。
- 八个 benchmark 均已完成页码级证据卡。
- 覆盖矩阵是分析性归纳，不是原作者给出的正式分类。
