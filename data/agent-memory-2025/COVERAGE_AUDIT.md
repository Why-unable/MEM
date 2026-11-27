# Agent Memory 2025+：覆盖审计与增补记录

> 审计日期：2026-11-27  
> 当前主库：51 篇正式发表论文  
> 触发原因：用户发现 LightMem 未被收录；进一步审计发现这不是单篇遗漏，而是“系统基线/评测基准”整层覆盖不足。

## 0. 结论

LightMem 确实应该进入主地图：

- 论文：*LightMem: Lightweight and Efficient Memory-Augmented Generation*
- Venue：ICLR 2026
- 层级：`Top-ICLR`
- 官方 proceedings：https://proceedings.iclr.cc/paper_files/paper/2026/hash/a05b72653ec5b473732129829ae04195-Abstract-Conference.html

进一步审计发现，以下正式发表论文也被现有 36 篇主库遗漏，且其中多篇已经被现有地图中的论文当作 baseline 使用：

| 论文 | Venue | 层级 | 为什么重要 |
|---|---|---|---|
| LightMem | ICLR 2026 | Top-ICLR | 三阶段轻量记忆 + sleep-time update；现有论文已把它作为效率 baseline |
| SeCom | ICLR 2025 | Top-ICLR | segment 级记忆 + 压缩去噪；MemGAS/MAGMA 等论文的常见对照 |
| MemoryOS | EMNLP 2025 Main | CCF-B | 三级层次记忆系统；MAGMA/MRAgent 等论文的直接 baseline |
| HippoRAG 2 | ICML 2025 | CCF-A | 图增强 RAG 的重要基线；在 LoCoMo 上常高于 MemGAS |
| SimpleMem | ICML 2026 | CCF-A | 语义无损压缩 + 意图感知检索；高效长期记忆的新路线 |
| GAM | ACL 2026 | CCF-A | 事件进展图 + 主题关联网络；主线 A 的层次图扩展 |
| ReasoningBank | ICLR 2026 | Top-ICLR | 从成功/失败经验蒸馏推理策略；程序性记忆的重要工作 |
| MemoryAgentBench | ICLR 2026 | Top-ICLR | 增量多轮记忆评测，覆盖检索、测试时学习、长程理解、选择性遗忘 |

本次先加入 8 篇（Batch 1）；随后又完成一轮深度检索，加入 7 篇 Batch 2。主库从 36 篇增加到 51 篇，关系从 47 条增加到 81 条。

补充说明：**AgeMem**（*Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents*）已确认是 **ACL 2026 Long Papers（CCF-A）**，DOI `10.18653/v1/2026.acl-long.981`，本轮已加入，并完成 `vault/10_Papers/evidence/agemem-evidence.md` 全文证据卡。

## 1. 为什么之前会漏

原来的 36 篇更偏向：

- 2025–2026 的新架构（A-Mem、MAGMA、MemGAS、MRAgent）
- 已有明确 benchmark 的评测/安全工作
- 能够找到 OpenReview 记录的论文

漏掉的主要是：

1. **被当作 baseline、但不是该地图初始检索核心的系统**：LightMem、SeCom、MemoryOS、HippoRAG 2。
2. **2025 年较早的 ICLR/ICML 论文**：SeCom、HippoRAG 2。
3. **2026 年新增的 systems/evaluation 论文**：SimpleMem、GAM、ReasoningBank、MemoryAgentBench。

这说明之前的检索策略偏“核心方法”，没有系统地把“现有论文的 baseline 列表”反向纳入地图。

## 2. 新增批次（Batch 1）

### 2.1 LightMem

- **定位**：轻量级、低成本的长期记忆系统。
- **核心机制**：sensory memory → topic-aware short-term memory → long-term memory with sleep-time update。
- **为什么重要**：把记忆整合从在线推理移到离线阶段，直接回应“记忆系统的 token/API 成本”问题。
- **与现有地图的关系**：与 Mem0、Hippocampus、LightWM、SimpleMem 构成“高效记忆系统”簇。

### 2.2 SeCom

- **定位**：segment-level memory construction and retrieval。
- **核心机制**：主题连贯的 conversation segmentation + LLMLingua-2 压缩去噪。
- **为什么重要**：直接证明“记忆粒度”会影响检索质量，是 MemGAS 多粒度路线的前置工作。
- **与现有地图的关系**：SeCom → MemGAS 的“segment 级 → 多粒度”演化。

### 2.3 MemoryOS

- **定位**：操作系统式的 agent memory。
- **核心机制**：short-term / mid-term / long-term personal memory；FIFO 与 segmented page 更新。
- **为什么重要**：它是 MAGMA、MRAgent 等论文的直接 baseline；地图里没有它会导致比较基线缺失。
- **与现有地图的关系**：与 MAGMA、MemGAS、MRAgent 的层次/图记忆形成对照。

### 2.4 HippoRAG 2

- **定位**：图增强 RAG / 非参数持续学习。
- **核心机制**：Personalized PageRank + deeper passage integration + online LLM use。
- **为什么重要**：它同时覆盖 factual、sense-making、associative memory，是“图结构是否真的优于普通 RAG”的关键对照。
- **与现有地图的关系**：MAGMA、MemGAS、MRAgent 都把 HippoRAG 2 作为强 baseline。

### 2.5 SimpleMem

- **定位**：高效终身记忆。
- **核心机制**：semantic structured compression + online semantic synthesis + intent-aware retrieval planning。
- **为什么重要**：与 LightMem 一起构成“压缩/效率”路线，直接对应 RQ1 的成本维度。
- **与现有地图的关系**：LightMem / Mem0 / MemGAS 的效率对照。

### 2.6 GAM

- **定位**：层次图 agentic memory。
- **核心机制**：event progression graph + topic associative network；语义偏移时才整合。
- **为什么重要**：它把“快速感知”和“稳定知识保留”解耦，是主线 A 的层次图扩展。
- **与现有地图的关系**：A-Mem → GAM → MAGMA 的图结构演化。

### 2.7 ReasoningBank

- **定位**：推理记忆 / 程序性记忆。
- **核心机制**：从成功和失败轨迹中蒸馏 generalizable reasoning strategies；MaTTS 做记忆感知的 test-time scaling。
- **为什么重要**：把记忆从“存轨迹”推进到“存可复用推理模式”，连接主线 E（程序性记忆）。
- **与现有地图的关系**：Remember Me, Refine Me、MemEvolve 的经验蒸馏路线。

### 2.8 MemoryAgentBench

- **定位**：memory agent 评测基准。
- **核心机制**：把长上下文数据改造成增量多轮交互，覆盖 retrieval、test-time learning、long-range understanding、selective forgetting。
- **为什么重要**：它把“选择性遗忘”纳入统一评测，直接连接 RQ3。
- **与现有地图的关系**：LongMemEval、MemBench、PersistBench 的评测扩展。


## 2.9 Batch 2：深度学习管理、评测与综述

在 Batch 1 之后继续按“正式 venue + 与 RQ1/RQ3 的相关性 + 是否被现有论文引用为 baseline”做深度检索，新增 7 篇：

| 论文 | Venue | 层级 | 为什么重要 |
|---|---|---|---|
| AgeMem | ACL 2026 Long | CCF-A | 把 LTM/STM 管理统一进 agent policy，用 tool actions + 三阶段 RL + step-wise GRPO 训练 |
| E-mem | ICML 2026 | CCF-A | 用多 agent 保留未压缩情境并做 episodic context reconstruction，直接挑战记忆预处理 |
| EverMemOS | ACL 2026 Long | CCF-A | engram-inspired 自组织 memory OS：episodic trace → semantic consolidation → reconstructive recollection |
| Nemori（What Deserves Memory） | ACL 2026 Long | CCF-A | 用预测误差/可预测性决定“什么值得记住”，替代重要性分数等启发式 |
| LightMem (SLM) | ACL 2026 Long | CCF-A | 用 Small Language Models 驱动记忆检索/写入/离线整合，和 ICLR 2026 的 LightMem 是不同工作 |
| MemoryBench | ICML 2026 | CCF-A | 用户反馈驱动的持续学习评测，补 LongMemEval 之外的“服务时学习”能力 |
| From Storage to Experience | ACL Findings 2026 | ACL-Findings | 把 agent memory 演化概括为 Storage → Reflection → Experience，适合做综述骨架 |

### 去重发现：MemoryArena

MemoryArena 已经在主库中，但原记录 ID 为 `interdependent`，标题为官方 PDF 标题 *Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks*，没有 “MemoryArena:” 前缀。因此本轮**没有重复添加**，只补强了它的 role 描述和 arXiv 字段。

## 3. 验证方式

本次新增记录使用了以下来源：

- ICLR 2026 / 2025 official proceedings（LightMem、SeCom、ReasoningBank、MemoryAgentBench）
- PMLR（HippoRAG 2、SimpleMem）
- ACL Anthology + Crossref DOI（MemoryOS、GAM）
- OpenAlex 用于标题、作者、摘要和 venue 交叉核对
- 官方 PDF 首页用于作者名核对

未使用模型记忆直接填写 DOI、authors 或 venue。

## 4. 仍然暂缓的候选

以下工作与主题高度相关，但本次没有直接加入主库，原因如下：

| 候选 | 当前状态 | 暂缓原因 |
|---|---|---|
| MemOS: A Memory OS for AI System | arXiv 2025 | 未确认正式 venue |
| MemOS: An Operating System for Memory-Augmented Generation | arXiv 2025 | 未确认正式 venue |
| MIRIX: Multi-Agent Memory System for LLM-Based Agents | arXiv 2025 | 未确认正式 venue |
| Zep: A Temporal Knowledge Graph Architecture for Agent Memory | arXiv 2025 | 未确认正式 venue |
| O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents | arXiv 2025 | 未确认正式 venue |
| STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? | arXiv 2026 | 未确认正式 venue |
| LightMem-Ego | arXiv 2026 | 未确认正式 venue |
| Memory in the Age of AI Agents | arXiv 2025 survey | 未确认正式 venue |

## 5. 下一步

1. 先为 LightMem、SeCom、MemoryOS、HippoRAG 2 补全文证据卡（它们是现有论文的高频 baseline）。
2. 再补 AgeMem、EverMemOS、E-mem、Nemori 的证据卡，建立“记忆管理/整合”主线。
3. 补 MemoryAgentBench、MemoryBench、MemoryArena 的评测协议对照。
4. 保持规则：arXiv-only 不进入主地图；正式 venue 确认后再迁移。

## 6. 当前计数

```text
论文：51
关系：81
CCF-A：26
Top-ICLR：12
CCF-B：2
Top-MLSys：1
ACL Findings：7
Top-COLM：3
```
