---
type: topic
subtype: mainline-analysis
topic: "Agent Memory 2025+"
mainline: "A"
status: evidence-checked
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - mainline-a
  - evidence
---

# Mainline A - Memory Architecture

> 范围：核心五篇（A-Mem、G-Memory、MAGMA、MemGAS、MRAgent）+ 扩展四篇（SeCom、HippoRAG 2、GAM、E-mem）。
> 方法：十篇均已完成页码级 evidence card，并对 benchmark、backbone、judge 与成本口径做交叉核对。
> 注意：十篇论文的 benchmark、backbone、judge 和成本口径不同，**不能直接把分数横向排名**。

## 一句话结论

主线 A 的演进不是“从没有记忆到有更多记忆”，而是：

```text
静态存储 + 单轮相似度检索
→ 结构化组织
→ 多关系 / 多粒度 / 多智能体层次
→ 由 LLM 驱动的主动访问策略
```

十篇论文共同支持一个更精确的判断：

> **结构化记忆的优势主要集中在多跳、时间/因果推理和对抗性问题上；在单点事实回忆和知识更新上，长上下文仍然是强 baseline。**

## 五篇论文的分工

| 论文                                                         | 核心贡献                                                              | 在主线 A 中的位置              |
| ---------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------- |
| [A-Mem](../10_Papers/evidence/amem-evidence.md)            | Zettelkasten 式原子笔记 + 链接生成 + 记忆演化                                  | 建立“结构化 + 可演化”的基线        |
| [G-Memory](../10_Papers/evidence/gmemory-evidence.md)      | insight / query / interaction 三层图                                 | 把记忆单元从单 agent 历史扩展到团队协作 |
| [MAGMA](../10_Papers/evidence/magma-evidence.md)           | semantic / temporal / causal / entity 多图 + intent-aware traversal | 把“关系类型”变成检索策略           |
| [MemGAS](../10_Papers/evidence/memgas-evidence.md)         | session / turn / summary / keyword 多粒度 + entropy router           | 把“粒度选择”变成自适应对象          |
| [MRAgent](../10_Papers/evidence/reconstructed-evidence.md) | Cue–Tag–Content 图 + 多轮 active reconstruction                      | 把“访问”从单轮检索变成序列决策        |

## 概念演进链

```text
A-Mem
  单 agent 原子笔记
  “记忆应该被组织和演化”
        ↓
G-Memory
  多智能体三层图
  “记忆单元应该匹配协作结构”
        ↓
MAGMA
  四类正交关系图
  “不同 query 需要不同关系视角”
        ↓
MemGAS
  四种记忆粒度
  “不同 query 需要不同粗细的证据”
        ↓
MRAgent
  Cue–Tag–Content + 多轮重建
  “检索本身应该由推理驱动”
```

这不是严格的时间顺序，而是**问题抽象层级**的递进。

## 对比矩阵

| 维度 | A-Mem | G-Memory | MAGMA | MemGAS | MRAgent |
|---|---|---|---|---|---|
| 记忆单元 | 原子笔记 | utterance / query / insight | event node | session / turn / summary / keyword | cue / tag / content |
| 结构 | 演化链接图 | 三层图 | 四类关系多图 | 多粒度关联图 | 异构图 + 三层记忆 |
| 写入 | LLM 生成元数据 + 链接 | 记录轨迹 + 蒸馏 insight | fast path + async consolidation | LLM 元数据 + GMM 关联 | LLM 离线蒸馏 |
| 检索 | cosine top-k | 粗检索 + 双向遍历 | intent + RRF + beam search | entropy router + PPR | 多轮 action selection |
| 更新 | 旧记忆演化 | 新 query/insight 更新 | 异步补 causal/entity 边 | 新记忆 GMM 关联 | 无更新/整合（作者承认） |
| 遗忘 | 无显式机制 | 无显式机制 | 无显式机制 | 查询时过滤 | 无显式机制 |
| 训练 | training-free | training-free | training-free | training-free | training-free |
| 主要评测 | LoCoMo, DialSim | 5 benchmarks × 3 MAS × 3 LLM | LoCoMo, LongMemEval | 4 long-term memory benchmarks | LoCoMo, LongMemEval |
| 成本特征 | 查询 token 低，构建多次 LLM 调用 | 额外 token 中等 | 构建 0.39h，1.47s/query | 构建 52.9M tokens，2.55s/query | 118K tokens/sample，586s |

## 五条证据结论

### 结论 1：结构化记忆在多跳、时间/因果、对抗性任务上更占优

支持证据：

- A-Mem 在 GPT-4o-mini 上：Multi-hop F1 25.02 → 27.02，Temporal 18.41 → 45.85（PDF p.6）。
- MAGMA 在 LoCoMo：Overall 0.481 → 0.700，Adversarial 0.205 → 0.742（PDF p.7）。
- MRAgent 在 LoCoMo：Claude backbone Overall J 84.21/88.32，显著高于 A-Mem、MemoryOS、LangMem、Mem0（PDF p.7）。
- MemGAS 在 LongMemEval-s：GPT4o-J 50.60 → 60.20（PDF p.7）。

判断：**强支持**。但需要注意各论文的 baseline 和 judge 不同。

### 结论 2：长上下文仍是强 baseline，结构记忆不是全面替代

反例：

- A-Mem 在 GPT-4o 上，Single-hop F1 48.43 vs full-context 61.56；Adversarial 36.35 vs 52.61（PDF p.6）。
- MAGMA 在 LongMemEval 上，Single-session-assistant 83.9% vs full-context 89.3%；Knowledge-update 66.7% vs 78.2%（PDF p.8）。
- MemGAS 在 LoCoMo 上，GPT4o-J 41.07 vs HippoRAG 2 45.62（PDF p.7）。

判断：**强支持**。因此 RQ1 不应是“结构 vs 长上下文谁更好”，而应是“在哪些任务维度上谁更好”。

### 结论 3：访问策略（policy）比单纯的存储结构更关键

支持证据：

- MAGMA 去掉 Adaptive Policy：0.700 → 0.637；去掉 Entity Links 只降到 0.666（PDF p.8）。
- MemGAS 去掉 Router：60.20 → 56.60；去掉 GMM：60.20 → 57.20（PDF p.8）。
- MRAgent 的 reasoning vs no-reasoning 差异一致存在；CE → CTE → CTC 的结构提升不如“是否主动重建”稳定（PDF p.8）。
- A-Mem 的 link generation + memory evolution 消融：Multi-hop 27.02 → 21.35（去 ME）→ 9.65（去 LG+ME）（PDF p.7）。

判断：**中等偏强**。这五篇论文仍把 policy 写在 prompt/规则里，不是学习出来的 policy；但“有没有 policy”比“图有多少种边”更能解释差异。

### 结论 4：成本没有消失，只是从查询时转移到构建/整合时

证据：

- A-Mem：查询约 1,200 tokens/次，但构建阶段需要多次 LLM 调用（PDF p.7）。
- MAGMA：0.39h 构建，3.37K tokens/query，1.47s/query（PDF p.8）。
- MemGAS：52.9M 构建 input tokens；查询 8,829 tokens/query（PDF p.7, p.23）。
- MRAgent：118K tokens/sample，586s；虽然低于 A-Mem 的 632K/1122s，但仍有显著延迟（PDF p.7）。

判断：**强支持**。必须同时报告 build cost、query cost、latency、storage，不能只报 token/query。

### 结论 5：遗忘、更新和治理是五篇论文的共同空白

- A-Mem：memory evolution 是改写，不是删除/回滚。
- G-Memory：更新 insight，但没有过期或权限。
- MAGMA：有时间图，但没有 forgetting。
- MemGAS：查询时 LLM filter，不是持久删除。
- MRAgent：作者明确说静态构建、记忆单调增长（PDF p.9）。

判断：**强支持**。这是 RQ3 的直接入口，也是主线 A 与安全/隐私主线的桥。

## 对 RQ1 的重新表述

原问题：

> 记忆结构何时优于长上下文？

建议拆成四个可检验子问题：

### RQ1a：任务结构

在 multi-hop、temporal/causal、adversarial、single-hop、knowledge-update 五类任务上，结构记忆与长上下文的胜负是否稳定？

**假设 H1**：结构记忆在 multi-hop、temporal/causal、adversarial 上占优；长上下文在 single-hop 和 knowledge-update 上占优。

### RQ1b：结构 vs 策略

收益主要来自“存储结构”还是“访问策略”？

**假设 H2**：在相同存储结构下，加入 intent-aware / active reconstruction policy 的收益，大于单纯增加关系类型或图密度。

### RQ1c：总成本

在相同准确率下，结构记忆的 build + query + latency + storage 总成本是否低于长上下文？

**假设 H3**：结构记忆在重复查询、长历史、多 session 场景下总成本更低；在一次性、短对话场景下长上下文更便宜。

### RQ1d：更新与遗忘

当记忆需要更新、删除或冲突裁决时，结构记忆是否仍优于长上下文？

**假设 H4**：当前结构记忆在 update/forget 上不如“显式版本化 + provenance”的方案；这是主线 A 的共同缺口。

## 建议的最小实验

### 条件

同一 backbone、同一 embedding、同一 judge：

1. Full context
2. Truncation + RAG
3. A-Mem-like：原子笔记 + 链接 + 单轮 top-k
4. MAGMA-like：多关系图 + intent-aware traversal
5. MRAgent-like：Cue–Tag–Content + 多轮 active reconstruction
6. （可选）MemGAS-like：多粒度 + entropy router

### 数据

- LoCoMo
- LongMemEval-s
- 可选：MemBench / Minerva

### 分层

按 query type 分层报告：

```text
single-hop
multi-hop
temporal
knowledge-update
adversarial
preference
```

### 指标

| 维度 | 指标 |
|---|---|
| 答案质量 | LLM-Judge、F1、evidence recall |
| 检索质量 | Recall@k、NDCG@k |
| 成本 | build tokens、query tokens、latency、storage |
| 更新 | update success、stale-memory rate |
| 遗忘 | deletion success、leakage rate（若接入 RQ3） |

### 关键消融

- structure-only vs structure + policy
- flat memory + active policy vs graph memory + passive retrieval
- 1-hop vs adaptive traversal
- single-granularity vs multi-granularity

### 预期结果与可证伪点

- 若 H1 成立：结构记忆应在 multi-hop/temporal/adversarial 上稳定胜出，在 single-hop/update 上不显著优于长上下文。
- 若 H2 成立：flat + active policy 应接近 graph + passive retrieval，说明策略是主因。
- 若 H3 成立：结构记忆的 Pareto 前沿应在长历史、多 session 场景占优。
- 若 H4 成立：引入 update/forget 后，现有五篇方法的优势会显著缩小。

## 当前不能下的结论

- 不能根据不同论文的分数直接说“MAGMA > MRAgent”或“MemGAS > A-Mem”；benchmark、backbone、judge 不同。
- 不能把 LLM-Judge 分数当作绝对正确率；需要人工抽查和 evidence recall。
- 不能把 MRAgent 的 expressivity theorem 当作实际性能保证。
- 不能忽略构建成本，只比较 query token。
- 不能把 A-Mem/G-Memory 的 arXiv 版本当作最终 camera-ready。

## 下一步阅读

主线 A 之后，建议补三类论文：

1. **评测主线**：LongMemEval、MemBench、Minerva、PersistBench。
2. **策略学习主线**：MemAgent、Memory-R1、MemEvolve（把手工 policy 变成学习 policy）。
3. **遗忘与治理主线**：PersistBench、Privacy Risks、Memory Injection、Poison Once。

## 证据卡

- [[10_Papers/evidence/amem-evidence|A-Mem 证据卡]]
- [[10_Papers/evidence/gmemory-evidence|G-Memory 证据卡]]
- [[10_Papers/evidence/magma-evidence|MAGMA 证据卡]]
- [[10_Papers/evidence/memgas-evidence|MemGAS 证据卡]]
- [[10_Papers/evidence/reconstructed-evidence|MRAgent 证据卡]]

## 来源与版本

| 论文 | 本地 PDF | 版本 |
|---|---|---|
| A-Mem | `data/agent-memory-2025/pdfs/amem.pdf` | arXiv 2502.12110；NeurIPS 2025 poster |
| G-Memory | `data/agent-memory-2025/pdfs/gmemory.pdf` | arXiv 2506.07398；NeurIPS 2025 spotlight |
| MAGMA | `data/agent-memory-2025/pdfs/magma.pdf` | ACL 2026 Long Papers |
| MemGAS | `data/agent-memory-2025/pdfs/memgas.pdf` | ICLR 2026 |
| MRAgent | `data/agent-memory-2025/pdfs/reconstructed.pdf` | ICML 2026, PMLR 306 |

---

# 2026-11-27 扩展：新增四篇架构工作

> 这四篇是在主库从 36 篇扩展到 51 篇后加入的。它们让 A 线从“五篇核心论文”变成更完整的架构谱系。

## 扩展论文

| 论文                                      | 核心机制                                                    | 对 A 线的意义                              |
| --------------------------------------- | ------------------------------------------------------- | ------------------------------------- |
| [SeCom](../10_Papers/secom.md)          | 主题连贯的 segment 级记忆 + prompt compression 去噪               | 直接研究“记忆粒度”本身，是 MemGAS 多粒度路线的前置工作      |
| [HippoRAG 2](../10_Papers/hipporag2.md) | Personalized PageRank + passage integration 的图增强 RAG    | 证明图结构必须同时保住 factual memory，否则不如普通 RAG |
| [GAM](../10_Papers/gam.md)              | event progression graph + topic associative network     | 把“快速感知”和“稳定知识保留”解耦，是层次图的另一种实现         |
| [E-mem](../10_Papers/emem.md)           | 多 agent 保留未压缩情境，master agent 协调 episodic reconstruction | 直接挑战“先压缩成结构再检索”的预处理范式                 |
| [M+](../10_Papers/mplus.md)             | 扩展 MemoryLLM 的可扩展长期参数记忆                                 | 证明记忆可以存在于模型参数中，而不只是外部存储               |

## 扩展论文的关键点

### SeCom：粒度本身就是架构变量

- 不是固定 turn/session 粒度，而是用 conversation segmentation 找主题连贯的 segment。
- 用 LLMLingua-2 压缩去噪。
- 在 LoCoMo、Long-MT-Bench+ 上优于固定粒度基线。
- 对 A 线的含义：**“记忆单元怎么切”与“记忆图怎么连”同等重要。**

### HippoRAG 2：图结构不能牺牲事实记忆

- 用 Personalized PageRank 做 passage integration。
- 同时覆盖 factual、sense-making、associative memory。
- 论文明确指出：一些图/RAG 结构在 sense-making 上强，但在基础 factual memory 上反而不如标准 RAG。
- 对 A 线的含义：**结构记忆必须通过“事实保真”门槛，否则图只是更贵的噪声。**

### GAM：编码与整合解耦

- 用 event progression graph 保存当前事件链。
- 只有发生 semantic shift 时才整合到 topic associative network。
- 在 LoCoMo、LongDialQA 上优于 SOTA。
- 对 A 线的含义：**不是所有新信息都应该立刻改写长期结构；需要“缓冲 → 整合”的两阶段。**

### M+：参数化长期记忆

- 扩展 MemoryLLM 的长期参数记忆。
- 在 LongBook-QA（∞-Bench，351 本书，平均约 192K tokens）和 LongBook Event QA 上评估。
- 对 A 线的含义：**记忆不一定是外部数据库；参数化记忆也是结构记忆的一种极端形式。**

### E-mem：反预处理路线

- 多个 assistant agent 保留未压缩的 episodic context。
- master agent 做全局规划，assistant 在激活 segment 内局部推理后再聚合。
- LoCoMo 上 F1 超过 54%，比 GAM 高 7.75%，token 成本降低 70%+。
- 对 A 线的含义：**“压缩成图”不是唯一解；保留原始情境 + 局部重构也可能是更优的 Pareto 点。**

## 更新后的 A 线谱系

```text
A-Mem            原子笔记 + 链接 + 演化
SeCom            segment 级记忆 + 压缩去噪
G-Memory         多 agent 三层图
MAGMA            多关系图 + intent-aware traversal
MemGAS           多粒度 + entropy router
GAM              事件图 + 主题网络，编码/整合解耦
HippoRAG 2       图增强 RAG，事实/关联/意义三重目标
MRAgent          Cue–Tag–Content + 多轮主动重构
E-mem            未压缩情境 + 多 agent episodic reconstruction
```

## 对 RQ1 的更新

新增四篇后，RQ1 的“结构”不能只按“图 vs 向量”分类，而应拆成四个正交维度：

1. **单元粒度**：turn / session / segment / event / note / entity。
2. **关系类型**：semantic / temporal / causal / entity / topic。
3. **整合时机**：即时写入 / 语义偏移触发 / 离线巩固 / 查询时重构。
4. **访问策略**：top-k / PPR / beam search / 多轮 action selection / 局部 agent 推理。

这意味着：

> 结构化记忆的收益不是来自“有图”，而是来自 **粒度、关系、整合时机、访问策略四者的匹配**。

## 证据边界

- 十篇均已完成页码级证据卡。
- SeCom、HippoRAG 2、GAM、E-mem 的数字来自各自论文的实验表/摘要，不能与核心五篇直接横比。
