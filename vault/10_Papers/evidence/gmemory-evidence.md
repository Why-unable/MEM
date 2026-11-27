---
type: evidence
paper_id: gmemory
title: "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems"
status: evidence-checked
checked_at: 2026-11-26
source_pdf: "data/agent-memory-2025/pdfs/gmemory.pdf"
source_version: "arXiv 2506.07398 (preprint); NeurIPS 2025 spotlight DOI 10.52202/085713-0439"
pages_checked: "1-10"
tags:
  - evidence
  - mainline-a
  - agent-memory
  - multi-agent
---

# G-Memory 证据卡

## 结论先行

- G-Memory 的关键不是“多 agent 也存记忆”，而是把记忆分成 **insight / query / interaction** 三层，分别对应跨任务经验、任务检索入口和协作轨迹。
- 它让记忆从“单 agent 的历史”变成“团队的组织记忆”，并证明同一套记忆不能直接套到所有 agent 角色上。
- 它主要解决多 agent 协作和自演化问题，不是直接的“结构记忆 vs 长上下文”实验；对 RQ1 的价值在于说明**记忆结构必须匹配协作单元**。

## 研究问题与定位

论文观察到：多 agent 系统的记忆机制普遍比单 agent 简单，常见做法只保存最终结果或单轮对话，忽略了 agent 之间的协作轨迹；同时缺少跨 trial 的经验积累和 agent-specific 定制。

G-Memory 的目标是给 MAS 提供一个可插拔的层次记忆系统，让团队在多次任务之间积累可复用的组织经验。

## 方法拆解

### 三层图结构

| 层                 | 节点                                   | 作用                      |
| ----------------- | ------------------------------------ | ----------------------- |
| Interaction Graph | 原子 utterance                         | 保存一次任务中 agent 之间的具体协作轨迹 |
| Query Graph       | 历史 query + 状态 + 对应 interaction graph | 作为任务级检索入口               |
| Insight Graph     | 从成功/失败轨迹中蒸馏出的 insight                | 提供跨任务的抽象经验和失败教训         |

来源：PDF p.4，Section 3；PDF p.5-6，Section 4。

### 读取流程

1. **粗粒度检索**：新 query 与历史 query 做 embedding 相似度 top-k，并在 query graph 上做 1-hop 扩展。
2. **向上遍历**：从 query 节点找到关联的 insight 节点，获得高层策略和失败教训。
3. **向下遍历**：用 LLM graph sparsifier 从 interaction graph 中抽取与当前任务相关的核心子图。
4. **角色定制**：根据每个 agent 的 `Role` 过滤 insight 和 trajectory，再注入该 agent 的 memory。
5. **执行后更新**：新增 query 节点和 interaction graph；从本次轨迹生成新 insight；更新 insight 与 query 的关联。

来源：PDF p.5-6，Eq. 4-11。

### 写入与更新

- 不是把完整对话直接塞进记忆，而是保存 **utterance 级交互图**，再在查询时压缩。
- 新 insight 由 LLM 从完整轨迹和任务结果（Resolved / Failed）中总结。
- 旧的 insight 会更新其 supporting query 集合，形成跨 trial 的“经验—任务”关联。
- 没有显式遗忘或删除机制。

## 存储与使用

> 对照：[[10_Papers/evidence/magma-evidence|MAGMA 证据卡]]

- **怎么存**：三层组织记忆。底层是任务执行轨迹，记录谁在什么时候说了什么、做了什么；中层是一次 query/task 的记录，保存任务、成功或失败、对应轨迹；上层是从多次任务中总结出的经验和教训。
- **怎么连**：任务与任务按相似性相连；任务通过“支持这条经验的那些任务”与经验相连；任务本身直接携带自己的执行轨迹。
- **怎么用**：新 query 先找相似历史任务，再向上取相关经验、向下取该任务的协作轨迹；不同 agent 按角色拿不同的记忆。
- **怎么更新**：任务结束后新增一条任务和轨迹；从成功或失败中总结新经验，并把新任务加入相关经验的支持任务集合。

**一句话**：G-Memory 不是一张大图，而是“任务索引 + 经验库 + 轨迹库”三件套；query 是串起三者的把手。

### 一个端到端例子（示意）

场景：多 agent 协作把“干净的鸡蛋放进微波炉”。

**存储**

- 任务轨迹：搜索 agent 找到鸡蛋；检查 agent 发现鸡蛋是脏的；清洁 agent 洗鸡蛋；放置 agent 放进微波炉。
- 任务记录：任务“把干净鸡蛋放进微波炉”、结果“成功”、对应上面的协作轨迹。
- 经验：放置前先检查目标物体是否干净；同时确认容器是否可用。

**更新**

新任务“把干净抹布放到台面”完成后：

- 新增一条任务记录和一条协作轨迹。
- 从这次成功中总结新经验，例如“先检查物体是否已经干净，避免重复清洁”。
- 新任务与相似历史任务相连；新任务也加入相关经验的支持任务集合。

**检索**

新 query：“把干净苹果放进冰箱。”

- 先找到相似历史任务“把干净鸡蛋放进微波炉”。
- 向上取经验：“先检查、必要时清洁，再放置。”
- 向下取协作轨迹：谁负责搜索、谁负责检查、谁负责清洁、谁负责放置。
- 不同角色拿到不同记忆：搜索 agent 看重“找物体”，清洁 agent 看重“先检查”，放置 agent 看重“确认容器”。

**这个例子说明**：G-Memory 不是只存最终答案，而是把“任务是什么、团队怎么做的、从中总结出什么”分开存；检索时再按角色组合。


## 实验与关键数字

### 主实验设置

- 5 个 benchmark：ALFWorld、SciWorld、PDDL、HotpotQA、FEVER。
- 3 个 MAS 框架：AutoGen、DyLAN、MacNet。
- 3 个 backbone：GPT-4o-mini、Qwen-2.5-7B、Qwen-2.5-14B。
- 指标：embodied action 用成功率，知识 QA 用 exact match accuracy。

### GPT-4o-mini / AutoGen

| Benchmark | No-memory | G-Memory |
|---|---:|---:|
| ALFWorld | 77.61 | **88.81** |
| SciWorld | 54.49 | **67.40** |
| PDDL | 23.53 | **27.77** |
| HotpotQA | 28.57 | **35.67** |
| FEVER | 57.13 | **66.24** |
| Average | 48.27 | **57.18** |

来源：PDF p.7, Table 1。

### 其他关键结果

- DyLAN + GPT-4o-mini：平均 43.12 → **50.88**。
- MacNet + GPT-4o-mini：平均 42.01 → **51.95**。
- 最大提升：MacNet + Qwen-2.5-14B 在 ALFWorld 上从 58.21 → **79.10**，提升 **20.89%**（PDF p.8）。
- 知识 QA 最大提升约 **10.12%**（PDF p.1 abstract）。

### 成本

- PDDL + AutoGen：G-Memory 比 no-memory 提升 **10.32%**，额外消耗约 **1.4M tokens**。
- MetaGPT-M 额外消耗约 **2.2M tokens**，只提升 **4.07%**。
- 来源：PDF p.8，Section 5.3。

### 消融与敏感性

- 只保留 fine-grained interactions、去掉 insights：AutoGen 平均下降 **4.47%**，DyLAN 下降 **3.82%**。
- 只保留 insights、去掉 interactions：AutoGen 下降 **3.95%**，DyLAN 下降 **3.39%**。
- 1-hop 扩展通常最好；2-hop/3-hop 会把 PDDL 降到 49.79%。
- 来源：PDF p.8-9，Figure 4。

## 成本分析

- **报告成本**：PDDL + AutoGen 上提升 10.32%，额外约 1.4M tokens；MetaGPT-M 额外约 2.2M tokens，只提升 4.07%。
- **未报告成本**：构建时间、每 query token、端到端延迟；成本证据是不完整的。
- **成本位置**：多 agent 协作、轨迹压缩、经验蒸馏和角色投影，成本分散在整条流水线。
- **对比判断**：只有重复出现的团队任务才能摊薄经验构建成本；一次性任务很可能不划算。

## 真正的新意

1. **把 MAS 记忆分成任务层、协作层和经验层**，不是单一向量库。
2. **双向遍历**：既向上找抽象经验，也向下找具体协作片段。
3. **agent-specific memory**：同一个团队里不同角色拿到不同记忆，而不是共享同一份上下文。
4. **从失败轨迹中学习**：insight 不只看成功案例，也保存失败教训。

## 局限与威胁

- **只验证了 3 个领域**：embodied action、knowledge QA、game；作者自己指出还需要 medical QA 等更多任务（PDF p.10）。
- **依赖 LLM 生成 insight 和 graph sparsification**：质量受底层模型影响，错误经验可能被制度化。
- **多 agent 专用**：不能直接回答单 agent 的结构记忆 vs 长上下文问题。
- **没有遗忘/过期/权限机制**：共享记忆的冲突和删除仍未解决。
- **成本统计不完整**：主要报告 token，不报告端到端延迟和构建时间。
- **版本风险**：本次使用 arXiv 版本，首页标记 `Preprint`；正式 NeurIPS 2025 DOI 已由 Crossref 验证为 `10.52202/085713-0439`，camera-ready 需复核。

## 与主线 A 其他论文的关系

- **A-Mem**：A-Mem 是单 agent 的原子笔记网络；G-Memory 把“记忆单元”提升到 agent 协作轨迹和组织经验。
- **Learning to Share**（主线 C）：G-Memory 关注团队记忆如何被检索和使用，Learning to Share 进一步关注多个并行 agent 之间选择性地共享什么。
- **MAGMA**：两者都使用图结构，但 MAGMA 的关系维度是 semantic/temporal/causal/entity，G-Memory 的维度是 insight/query/interaction。
- **MRAgent**：G-Memory 仍是“检索 + 注入”的被动范式；MRAgent 把检索变成多轮主动重构。

## 对 RQ1 的意义

G-Memory 不是直接的 long-context baseline，但它提供了一个重要变量：**记忆的“单元”必须和任务的组织单元一致**。

- 单 agent 对话：原子笔记或 turn 级记忆可能足够。
- 多 agent 协作：如果只存最终答案，会丢失“谁在什么时候发现了什么”的协作证据。
- 因此 RQ1 的实验不能只比较“长上下文 vs 向量库”，还要比较“记忆粒度是否匹配任务结构”。

## 可复用点

- 三层图 schema：insight / query / interaction。
- 粗检索 + 向上 insight + 向下 trajectory 的双向遍历。
- 按 agent role 过滤记忆，而不是全团队共享同一上下文。
- 从成功/失败结果中蒸馏 insight 的更新流程。
- 用“性能提升 / 额外 token”衡量记忆系统的性价比。

## 待核对

- [ ] 用 NeurIPS 2025 camera-ready 复核主表和 appendix 数字。
- [ ] 核对 `20.89%` 与 `10.12%` 的具体计算口径。
- [ ] 确认 graph sparsifier 的 LLM 调用成本是否计入 token 统计。
- [ ] 把 `papers.json` 的 DOI 更新为正式 DOI。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/gmemory.pdf`
- arXiv：https://arxiv.org/abs/2506.07398
- OpenReview：https://openreview.net/forum?id=mmIAp3cVS0
- 正式 DOI：https://doi.org/10.52202/085713-0439
