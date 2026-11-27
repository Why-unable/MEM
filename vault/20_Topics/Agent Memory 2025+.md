---
type: topic
topic: "Agent Memory 2025+"
paper_count: 51
updated: 2026-11-19
tags:
  - topic
  - agent-memory
---

# Agent Memory 2025+

## 范围

- 时间：2025-01-01 至 2026-11-19
- 对象：LLM/agent 的长期记忆、episodic memory、memory policy、记忆整合、记忆评测与安全
- 发表要求：优先 CCF-A/顶会正式发表；ICLR、COLM、MLSys 等顶级但非 CCF-A 的 venue 单独标注
- 收录：51 篇

## 统计

- 类别分布：记忆架构 10, 系统与效率 8, 评测与基准 8, 记忆策略与训练 5, 情景记忆 4, 记忆整合 4, 安全与隐私 4, 个性化记忆 2, 程序性记忆 2, 多模态记忆 1, 应用 1, 多智能体记忆 1, 综述与框架 1
- Venue 层级：CCF-A 26, Top-ICLR 12, ACL-Findings 7, Top-COLM 3, CCF-B 2, Top-MLSys 1

## 深度综合

完整的研究综合、争议、空白和阅读顺序见：

- [[40_Maps/Agent Memory 2025+ Synthesis]]

## 快速阅读路径

1. 先读 [[10_Papers/amem|A-Mem]]、[[10_Papers/gmemory|G-Memory]]、[[10_Papers/longmemeval|LongMemEval]] 建立问题框架。
2. 再读 [[10_Papers/memoryr1|Memory-R1]]、[[10_Papers/memagent|MemAgent]]、[[10_Papers/memeolve|MemEvolve]] 看“记忆策略学习”路线。
3. 接着读 [[10_Papers/recmem|RecMem]]、[[10_Papers/timem|TiMem]]、[[10_Papers/tiermem|TierMem]] 看记忆整合与压缩。
4. 最后读 [[10_Papers/injection|Memory Injection]]、[[10_Papers/privacy|Privacy Risks]]、[[10_Papers/poisononce|Poison Once]] 看安全边界。

## 记忆架构


- [[10_Papers/amem|A-Mem: Agentic Memory for LLM Agents]] — NeurIPS 2025 — 提出动态组织、链接和演化的 agentic memory，是 2025 年后记忆结构设计的高频基线。
- [[10_Papers/hipporag2|From RAG to Memory: Non-Parametric Continual Learning for Large Language Models]] — ICML 2025 — 用 Personalized PageRank + passage integration 统一事实、sense-making 和 associative memory 的图增强 RAG。
- [[10_Papers/gmemory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]] — NeurIPS 2025 — 把多智能体协作轨迹组织成层次记忆，连接个体记忆与团队记忆。
- [[10_Papers/magma|MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents]] — ACL 2026 — 用多图结构组织实体、事件和时间关系，强调可解释、可检索的 agent 记忆。
- [[10_Papers/reconstructed|Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents]] — ICML 2026 — 把记忆视为“重构”而不是“检索”，用图结构动态重建上下文。
- [[10_Papers/mplus|M+: Extending MemoryLLM with Scalable Long-Term Memory]] — ICML 2025 — 扩展 MemoryLLM 的可扩展长期参数记忆，连接参数化记忆与外部记忆。
- [[10_Papers/secom|On Memory Construction and Retrieval for Personalized Conversational Agents]] — ICLR 2025 — 以主题连贯的 segment 作为记忆单元，并用 prompt compression 去噪，直接研究记忆粒度对检索的影响。
- [[10_Papers/emem|E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory]] — ICML 2026 — 用多个 assistant agent 保留未压缩的情境上下文，由 master agent 协调局部推理和证据重构，避免记忆预处理造成去语境化。
- [[10_Papers/memgas|From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents]] — ICLR 2026 — 多粒度记忆关联与选择，缓解长对话中检索粒度不匹配的问题。
- [[10_Papers/gam|GAM: Hierarchical Graph-based Agentic Memory for LLM Agents]] — ACL 2026 — 用事件进展图 + 主题关联网络解耦记忆编码与整合，降低瞬态噪声对长期知识结构的干扰。



## 记忆策略与训练


- [[10_Papers/agemem|Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents]] — ACL 2026 — 把 long-term / short-term memory 操作统一成 agent policy 的 tool actions，并用三阶段 RL + step-wise GRPO 训练。
- [[10_Papers/memagent|MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent]] — ICLR 2026 — 用 multi-conv RL 训练 memory agent 压缩长上下文，代表“记忆策略可学习”路线。
- [[10_Papers/memeolve|MemEvolve: Meta-Evolution of Agent Memory Systems]] — ICML 2026 — 用元进化自动设计记忆系统的结构与策略，代表“记忆系统自动设计”方向。
- [[10_Papers/memoryr1|Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning]] — ACL 2026 — 用强化学习训练记忆管理与使用策略，把记忆操作从 prompt 工程推进为可学习策略。
- [[10_Papers/umem|UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory]] — ICML 2026 — 统一记忆抽取与管理，强调跨任务、跨场景的泛化记忆能力。



## 系统与效率


- [[10_Papers/lightmem|LightMem: Lightweight and Efficient Memory-Augmented Generation]] — ICLR 2026 — 用 sensory / short-term / long-term 三阶段和 sleep-time update，把记忆压缩与整合移出在线推理，主打低成本长期记忆。
- [[10_Papers/mem0|Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory]] — ECAI 2025 — 工业级可扩展长期记忆，强调生产部署中的记忆抽取、更新与检索流水线。
- [[10_Papers/memoryos|Memory OS of AI Agent]] — EMNLP 2025 — 把操作系统式的分层存储、更新和检索引入 agent memory，建立 short / mid / long-term 三级记忆。
- [[10_Papers/evermemos|EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning]] — ACL 2026 — 用 engram-inspired 生命周期组织记忆：Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。
- [[10_Papers/hippocampus|Hippocampus: An Efficient and Scalable Memory Module for Agentic AI]] — MLSys 2026 — 面向 agentic AI 的高效、可扩展记忆模块，偏系统实现与部署效率。
- [[10_Papers/lightwm|LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents]] — ICML 2026 — 面向小模型 agent 的免训练层次工作记忆，强调低成本与可部署性。
- [[10_Papers/lightmem-slm|Lightweight LLM Agent Memory with Small Language Models]] — ACL 2026 — 用 Small Language Models 驱动记忆检索、写入和离线整合，分离 online 与 offline 处理，强调低延迟和固定检索预算。
- [[10_Papers/simplemem|SimpleMem: Efficient Lifelong Memory for LLM Agents]] — ICML 2026 — 用语义结构化压缩、在线综合和意图感知检索规划，在长期记忆中同时优化准确率与 token 成本。



## 情景记忆


- [[10_Papers/humanepisodic|Human-inspired Episodic Memory for Infinite Context LLMs]] — ICLR 2025 — 用类人 episodic memory 扩展无限上下文，是 2025 年记忆架构的重要基础工作。
- [[10_Papers/remem|REMem: Reasoning with Episodic Memory in Language Agent]] — ICLR 2026 — 把 episodic memory 与推理过程结合，强调事件级经验的复用。
- [[10_Papers/artem|ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory]] — AAAI 2026 — 时空 episodic memory，关注事件顺序、时间依赖和长期空间经验。
- [[10_Papers/ema|EMA: An Episodic Memory Agent for Efficient and Selective Memory]] — ACL Findings 2026 — 把对话抽象为 episodic memory unit 并做选择性记忆，降低长对话冗余。



## 记忆整合


- [[10_Papers/recmem|RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents]] — ACL Findings 2026 — 基于复现/重复的记忆整合，减少对每条交互做 eager extraction 的开销。
- [[10_Papers/timem|TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents]] — ACL Findings 2026 — 时间—层次记忆整合，面向长时程对话中的时序信息保持。
- [[10_Papers/tiermem|TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory]] — COLM 2026 — 在压缩记忆与原始证据之间做分层权衡，面向长时程 agent memory。
- [[10_Papers/nemori|What Deserves Memory: Adaptive Memory Distillation for LLM Agents]] — ACL 2026 — 把“什么值得记住”转化为可预测性/预测误差驱动的自适应蒸馏（Nemori），避免重要性分数等启发式规则。



## 个性化记忆


- [[10_Papers/evoking|Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval]] — ICLR 2026 — 基于回忆—熟悉度的自适应检索，把个性化记忆从“存什么”推进到“如何取”。
- [[10_Papers/personaagent|PersonaAgent: Bridging Memory and Action for Personalized LLM Agents]] — ACL Findings 2026 — 把记忆与行动耦合，做面向个性化任务的 LLM agent。



## 多模态记忆


- [[10_Papers/multimodal|Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory]] — ICLR 2026 — 多模态长期记忆 agent，连接视觉、听觉与文本经验。



## 程序性记忆


- [[10_Papers/reasoningbank|ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory]] — ICLR 2026 — 从成功与失败经验中蒸馏可泛化的推理策略，把记忆从“存轨迹”推进到“存可复用推理模式”。
- [[10_Papers/rememberrefine|Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution]] — ACL Findings 2026 — 经验驱动的程序性记忆，让 agent 从历史经验中提炼可复用技能。



## 多智能体记忆


- [[10_Papers/learnshare|Learning to Share: Selective Memory for Efficient Parallel Agentic Systems]] — ICML 2026 — 并行多 agent 系统中的选择性共享记忆，平衡效率与协作收益。



## 评测与基准


- [[10_Papers/longmemeval|LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory]] — ICLR 2025 — 长期交互记忆基准，已成为记忆系统评测的重要参照。
- [[10_Papers/interdependent|Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks]] — ICML 2026 — MemoryArena：多 session、agent-environment 相互依赖任务中的记忆评测，检验记忆是否真正指导后续行动。
- [[10_Papers/persistbench|PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?]] — ICML 2026 — 评测“何时应该遗忘”，把记忆持久化边界变成显式研究对象。
- [[10_Papers/membench|MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents]] — ACL Findings 2025 — LLM-based agent 记忆的综合评测，覆盖多种记忆能力。
- [[10_Papers/minerva|Minerva: A Programmable Memory Test Benchmark for Language Models]] — ICML 2025 — 可编程记忆测试基准，把记忆能力拆成可组合的测试程序。
- [[10_Papers/beyondmillion|Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs]] — ICLR 2026 — 百万 token 级长记忆评测与增强，扩展了长上下文记忆的压力测试。
- [[10_Papers/memoryagentbench|Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions]] — ICLR 2026 — 把长期记忆评测改造成增量多轮交互，覆盖检索、测试时学习、长程理解和选择性遗忘四项能力。
- [[10_Papers/memorybench|MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems]] — ICML 2026 — 用用户反馈模拟框架评测 LLM 系统的持续学习与记忆能力，覆盖多领域、多语言和多任务类型。



## 安全与隐私


- [[10_Papers/injection|Memory Injection Attacks on LLM Agents via Query-Only Interaction]] — NeurIPS 2025 — query-only 记忆注入攻击，说明只通过查询交互也能污染 agent 记忆。
- [[10_Papers/privacy|Unveiling Privacy Risks in LLM Agent Memory]] — ACL 2025 — 记忆隐私抽取攻击，揭示长期记忆中的敏感信息泄露面。
- [[10_Papers/injecmem|InjecMEM: Memory Injection Attack on LLM Agent Memory Systems]] — COLM 2026 — 把注入攻击扩展到记忆系统的写入/检索链路，攻击面更系统。
- [[10_Papers/poisononce|Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents]] — COLM 2026 — 环境注入的记忆 poisoning：一次污染可被长期利用，面向 Web agent。



## 应用


- [[10_Papers/memrec|MemRec: Collaborative Memory-Augmented Agentic Recommender System]] — ACL 2026 — 把协作记忆增强用于 agentic recommender system。



## 综述与框架


- [[10_Papers/storagetexperience|From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms]] — ACL Findings 2026 — 把 LLM agent memory 的演化概括为 Storage → Reflection → Experience 三阶段，并梳理长程一致性、动态环境和持续学习三条驱动线。


## 关键研究缺口

- **统一评测**：LongMemEval、MemBench、Minerva、PersistBench 各自强调不同能力，仍缺少跨任务、跨模态的统一协议。
- **记忆策略学习**：Memory-R1、MemAgent、MemEvolve 代表 RL/进化路线，但训练成本、稳定性和可迁移性仍未解决。
- **遗忘与隐私**：PersistBench 关注“何时忘”，隐私/注入工作关注“不能忘什么”，两者还没有形成统一的记忆治理框架。
- **多智能体共享记忆**：G-Memory、Learning to Share 是起点，但共享粒度、权限和冲突解决仍是空白。
- **从记忆到能力**：程序性记忆与经验复用（Remember Me, Refine Me）可能比“检索更多历史”更接近真正的终身学习。

## 说明

本页是**概念地图**，边表示研究主题之间的继承、扩展、对照或应用关系，不等同于逐条引文关系。每篇论文的正式 venue、PDF 与源记录见论文笔记。
