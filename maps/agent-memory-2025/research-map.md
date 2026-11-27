# Agent Memory 2025+ · Research Map

- 论文数：51
- 关系数：81
- 范围：2025-01-01 至 2026-11-19
- 说明：边为概念关系，不等同于逐条引文。

## 全景图

```mermaid
flowchart LR
  subgraph architecture[记忆架构]
    amem["A-Mem: Agentic Memory for LLM Agents"]
    gmemory["G-Memory: Tracing Hierarchical Memory f..."]
    magma["MAGMA: A Multi-Graph based Agentic Memo..."]
    memgas["From Single to Multi-Granularity: Towar..."]
    reconstructed["Memory is Reconstructed, Not Retrieved:..."]
    mplus["M+: Extending MemoryLLM with Scalable L..."]
    secom["On Memory Construction and Retrieval fo..."]
    hipporag2["From RAG to Memory: Non-Parametric Cont..."]
    gam["GAM: Hierarchical Graph-based Agentic M..."]
    emem["E-mem: Multi-agent based Episodic Conte..."]
  end
  subgraph training[记忆策略与训练]
    memagent["MemAgent: Reshaping Long-Context LLM wi..."]
    memoryr1["Memory-R1: Enhancing Large Language Mod..."]
    memeolve["MemEvolve: Meta-Evolution of Agent Memo..."]
    umem["UMEM: Unified Memory Extraction and Man..."]
    agemem["Agentic Memory: Learning Unified Long-T..."]
  end
  subgraph system[系统与效率]
    mem0["Mem0: Building Production-Ready AI Agen..."]
    hippocampus["Hippocampus: An Efficient and Scalable ..."]
    lightwm["LightWM: Training-Free Hierarchical Wor..."]
    lightmem["LightMem: Lightweight and Efficient Mem..."]
    memoryos["Memory OS of AI Agent"]
    simplemem["SimpleMem: Efficient Lifelong Memory fo..."]
    evermemos["EverMemOS: A Self-Organizing Memory Ope..."]
    lightmem-slm["Lightweight LLM Agent Memory with Small..."]
  end
  subgraph episodic[情景记忆]
    remem["REMem: Reasoning with Episodic Memory i..."]
    artem["ARTEM: Enhancing Large Language Model A..."]
    humanepisodic["Human-inspired Episodic Memory for Infi..."]
    ema["EMA: An Episodic Memory Agent for Effic..."]
  end
  subgraph consolidation[记忆整合]
    recmem["RecMem: Recurrence-based Memory Consoli..."]
    timem["TiMem: Temporal-Hierarchical Memory Con..."]
    tiermem["TierMem: Balancing Compressed Memory an..."]
    nemori["What Deserves Memory: Adaptive Memory D..."]
  end
  subgraph personalization[个性化记忆]
    evoking["Evoking User Memory: Personalizing LLM ..."]
    personaagent["PersonaAgent: Bridging Memory and Actio..."]
  end
  subgraph multimodal[多模态记忆]
    multimodal["Seeing, Listening, Remembering, and Rea..."]
  end
  subgraph procedural[程序性记忆]
    rememberrefine["Remember Me, Refine Me: A Dynamic Proce..."]
    reasoningbank["ReasoningBank: Scaling Agent Self-Evolv..."]
  end
  subgraph multiagent[多智能体记忆]
    learnshare["Learning to Share: Selective Memory for..."]
  end
  subgraph evaluation[评测与基准]
    longmemeval["LongMemEval: Benchmarking Chat Assistan..."]
    beyondmillion["Beyond a Million Tokens: Benchmarking a..."]
    interdependent["Benchmarking Agent Memory in Interdepen..."]
    persistbench["PersistBench: When Should Long-Term Mem..."]
    membench["MemBench: Towards More Comprehensive Ev..."]
    minerva["Minerva: A Programmable Memory Test Ben..."]
    memoryagentbench["Evaluating Memory in LLM Agents via Inc..."]
    memorybench["MemoryBench: A Benchmark for Memory and..."]
  end
  subgraph safety[安全与隐私]
    privacy["Unveiling Privacy Risks in LLM Agent Me..."]
    injection["Memory Injection Attacks on LLM Agents ..."]
    injecmem["InjecMEM: Memory Injection Attack on LL..."]
    poisononce["Poison Once, Exploit Forever: Environme..."]
  end
  subgraph application[应用]
    memrec["MemRec: Collaborative Memory-Augmented ..."]
  end
  subgraph survey[综述与框架]
    storagetexperience["From Storage to Experience: A Survey on..."]
  end
  amem -->|extends| gmemory
  amem -->|extends| magma
  amem -->|extends| memgas
  amem -->|extends| reconstructed
  amem -->|extends| memoryr1
  amem -->|extends| memagent
  amem -->|extends| memeolve
  amem -->|extends| umem
  amem -->|extends| mem0
  gmemory -->|extends| learnshare
  gmemory -->|related| memeolve
  memagent -->|related| memoryr1
  memoryr1 -->|extends| memeolve
  memoryr1 -->|related| umem
  memeolve -->|related| umem
  mem0 -->|extends| hippocampus
  mem0 -->|extends| tiermem
  mem0 -->|risk| privacy
  mem0 -->|risk| injection
  humanepisodic -->|extends| remem
  humanepisodic -->|extends| artem
  remem -->|extends| ema
  remem -->|extends| multimodal
  ema -->|related| recmem
  recmem -->|extends| timem
  timem -->|extends| tiermem
  tiermem -->|evaluates| persistbench
  evoking -->|related| longmemeval
  personaagent -->|extends| evoking
  rememberrefine -->|related| memeolve
  memrec -->|applies| mem0
  longmemeval -->|related| membench
  longmemeval -->|extends| beyondmillion
  longmemeval -->|extends| interdependent
  longmemeval -->|extends| persistbench
  membench -->|related| minerva
  beyondmillion -->|related| interdependent
  privacy -->|related| injection
  injection -->|extends| injecmem
  injecmem -->|extends| poisononce
  longmemeval -->|evaluated-by| amem
  membench -->|evaluated-by| amem
  persistbench -->|evaluated-by| memoryr1
  mplus -->|related| reconstructed
  lightwm -->|related| ema
  artem -->|related| humanepisodic
  learnshare -->|related| memagent
  lightmem -->|extends| mem0
  lightmem -->|related| hippocampus
  lightmem -->|related| lightwm
  secom -->|extends| memgas
  secom -->|related| amem
  memoryos -->|related| magma
  memoryos -->|related| reconstructed
  hipporag2 -->|related| magma
  hipporag2 -->|related| reconstructed
  hipporag2 -->|related| memgas
  simplemem -->|related| lightmem
  simplemem -->|extends| mem0
  gam -->|extends| amem
  gam -->|related| magma
  reasoningbank -->|related| rememberrefine
  reasoningbank -->|related| memeolve
  memoryagentbench -->|extends| longmemeval
  memoryagentbench -->|related| membench
  memoryagentbench -->|related| persistbench
  agemem -->|extends| memoryr1
  agemem -->|related| memagent
  agemem -->|related| persistbench
  emem -->|related| reconstructed
  emem -->|related| gam
  evermemos -->|extends| memoryos
  evermemos -->|related| memgas
  nemori -->|related| memgas
  nemori -->|related| recmem
  lightmem-slm -->|related| lightmem
  lightmem-slm -->|related| mem0
  memorybench -->|extends| longmemeval
  memorybench -->|related| memoryagentbench
  storagetexperience -->|related| amem
  storagetexperience -->|related| reasoningbank
```

## 论文清单

| ID | 论文 | Venue | 层级 | 类别 | 定位 |
|---|---|---|---|---|---|
| `amem` | A-Mem: Agentic Memory for LLM Agents | NeurIPS 2025 | CCF-A | 记忆架构 | 提出动态组织、链接和演化的 agentic memory，是 2025 年后记忆结构设计的高频基线。 |
| `gmemory` | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | NeurIPS 2025 | CCF-A | 记忆架构 | 把多智能体协作轨迹组织成层次记忆，连接个体记忆与团队记忆。 |
| `hipporag2` | From RAG to Memory: Non-Parametric Continual Learning for Large Language Models | ICML 2025 | CCF-A | 记忆架构 | 用 Personalized PageRank + passage integration 统一事实、sense-making 和 associative memory 的图增强 RAG。 |
| `magma` | MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents | ACL 2026 | CCF-A | 记忆架构 | 用多图结构组织实体、事件和时间关系，强调可解释、可检索的 agent 记忆。 |
| `reconstructed` | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | ICML 2026 | CCF-A | 记忆架构 | 把记忆视为“重构”而不是“检索”，用图结构动态重建上下文。 |
| `mplus` | M+: Extending MemoryLLM with Scalable Long-Term Memory | ICML 2025 | CCF-A | 记忆架构 | 扩展 MemoryLLM 的可扩展长期参数记忆，连接参数化记忆与外部记忆。 |
| `secom` | On Memory Construction and Retrieval for Personalized Conversational Agents | ICLR 2025 | Top-ICLR | 记忆架构 | 以主题连贯的 segment 作为记忆单元，并用 prompt compression 去噪，直接研究记忆粒度对检索的影响。 |
| `memgas` | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | ICLR 2026 | Top-ICLR | 记忆架构 | 多粒度记忆关联与选择，缓解长对话中检索粒度不匹配的问题。 |
| `gam` | GAM: Hierarchical Graph-based Agentic Memory for LLM Agents | ACL 2026 | CCF-A | 记忆架构 | 用事件进展图 + 主题关联网络解耦记忆编码与整合，降低瞬态噪声对长期知识结构的干扰。 |
| `emem` | E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory | ICML 2026 | CCF-A | 记忆架构 | 用多个 assistant agent 保留未压缩的情境上下文，由 master agent 协调局部推理和证据重构，避免记忆预处理造成去语境化。 |
| `memagent` | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | ICLR 2026 | Top-ICLR | 记忆策略与训练 | 用 multi-conv RL 训练 memory agent 压缩长上下文，代表“记忆策略可学习”路线。 |
| `memoryr1` | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | ACL 2026 | CCF-A | 记忆策略与训练 | 用强化学习训练记忆管理与使用策略，把记忆操作从 prompt 工程推进为可学习策略。 |
| `memeolve` | MemEvolve: Meta-Evolution of Agent Memory Systems | ICML 2026 | CCF-A | 记忆策略与训练 | 用元进化自动设计记忆系统的结构与策略，代表“记忆系统自动设计”方向。 |
| `umem` | UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory | ICML 2026 | CCF-A | 记忆策略与训练 | 统一记忆抽取与管理，强调跨任务、跨场景的泛化记忆能力。 |
| `agemem` | Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents | ACL 2026 | CCF-A | 记忆策略与训练 | 把 long-term / short-term memory 操作统一成 agent policy 的 tool actions，并用三阶段 RL + step-wise GRPO 训练。 |
| `lightmem` | LightMem: Lightweight and Efficient Memory-Augmented Generation | ICLR 2026 | Top-ICLR | 系统与效率 | 用 sensory / short-term / long-term 三阶段和 sleep-time update，把记忆压缩与整合移出在线推理，主打低成本长期记忆。 |
| `mem0` | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | ECAI 2025 | CCF-B | 系统与效率 | 工业级可扩展长期记忆，强调生产部署中的记忆抽取、更新与检索流水线。 |
| `memoryos` | Memory OS of AI Agent | EMNLP 2025 | CCF-B | 系统与效率 | 把操作系统式的分层存储、更新和检索引入 agent memory，建立 short / mid / long-term 三级记忆。 |
| `hippocampus` | Hippocampus: An Efficient and Scalable Memory Module for Agentic AI | MLSys 2026 | Top-MLSys | 系统与效率 | 面向 agentic AI 的高效、可扩展记忆模块，偏系统实现与部署效率。 |
| `lightwm` | LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents | ICML 2026 | CCF-A | 系统与效率 | 面向小模型 agent 的免训练层次工作记忆，强调低成本与可部署性。 |
| `simplemem` | SimpleMem: Efficient Lifelong Memory for LLM Agents | ICML 2026 | CCF-A | 系统与效率 | 用语义结构化压缩、在线综合和意图感知检索规划，在长期记忆中同时优化准确率与 token 成本。 |
| `evermemos` | EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning | ACL 2026 | CCF-A | 系统与效率 | 用 engram-inspired 生命周期组织记忆：Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。 |
| `lightmem-slm` | Lightweight LLM Agent Memory with Small Language Models | ACL 2026 | CCF-A | 系统与效率 | 用 Small Language Models 驱动记忆检索、写入和离线整合，分离 online 与 offline 处理，强调低延迟和固定检索预算。 |
| `humanepisodic` | Human-inspired Episodic Memory for Infinite Context LLMs | ICLR 2025 | Top-ICLR | 情景记忆 | 用类人 episodic memory 扩展无限上下文，是 2025 年记忆架构的重要基础工作。 |
| `remem` | REMem: Reasoning with Episodic Memory in Language Agent | ICLR 2026 | Top-ICLR | 情景记忆 | 把 episodic memory 与推理过程结合，强调事件级经验的复用。 |
| `artem` | ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory | AAAI 2026 | CCF-A | 情景记忆 | 时空 episodic memory，关注事件顺序、时间依赖和长期空间经验。 |
| `ema` | EMA: An Episodic Memory Agent for Efficient and Selective Memory | ACL Findings 2026 | ACL-Findings | 情景记忆 | 把对话抽象为 episodic memory unit 并做选择性记忆，降低长对话冗余。 |
| `recmem` | RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents | ACL Findings 2026 | ACL-Findings | 记忆整合 | 基于复现/重复的记忆整合，减少对每条交互做 eager extraction 的开销。 |
| `timem` | TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents | ACL Findings 2026 | ACL-Findings | 记忆整合 | 时间—层次记忆整合，面向长时程对话中的时序信息保持。 |
| `tiermem` | TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory | COLM 2026 | Top-COLM | 记忆整合 | 在压缩记忆与原始证据之间做分层权衡，面向长时程 agent memory。 |
| `nemori` | What Deserves Memory: Adaptive Memory Distillation for LLM Agents | ACL 2026 | CCF-A | 记忆整合 | 把“什么值得记住”转化为可预测性/预测误差驱动的自适应蒸馏（Nemori），避免重要性分数等启发式规则。 |
| `evoking` | Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval | ICLR 2026 | Top-ICLR | 个性化记忆 | 基于回忆—熟悉度的自适应检索，把个性化记忆从“存什么”推进到“如何取”。 |
| `personaagent` | PersonaAgent: Bridging Memory and Action for Personalized LLM Agents | ACL Findings 2026 | ACL-Findings | 个性化记忆 | 把记忆与行动耦合，做面向个性化任务的 LLM agent。 |
| `multimodal` | Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory | ICLR 2026 | Top-ICLR | 多模态记忆 | 多模态长期记忆 agent，连接视觉、听觉与文本经验。 |
| `rememberrefine` | Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution | ACL Findings 2026 | ACL-Findings | 程序性记忆 | 经验驱动的程序性记忆，让 agent 从历史经验中提炼可复用技能。 |
| `reasoningbank` | ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | ICLR 2026 | Top-ICLR | 程序性记忆 | 从成功与失败经验中蒸馏可泛化的推理策略，把记忆从“存轨迹”推进到“存可复用推理模式”。 |
| `learnshare` | Learning to Share: Selective Memory for Efficient Parallel Agentic Systems | ICML 2026 | CCF-A | 多智能体记忆 | 并行多 agent 系统中的选择性共享记忆，平衡效率与协作收益。 |
| `longmemeval` | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | ICLR 2025 | Top-ICLR | 评测与基准 | 长期交互记忆基准，已成为记忆系统评测的重要参照。 |
| `interdependent` | Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks | ICML 2026 | CCF-A | 评测与基准 | MemoryArena：多 session、agent-environment 相互依赖任务中的记忆评测，检验记忆是否真正指导后续行动。 |
| `persistbench` | PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | ICML 2026 | CCF-A | 评测与基准 | 评测“何时应该遗忘”，把记忆持久化边界变成显式研究对象。 |
| `membench` | MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents | ACL Findings 2025 | ACL-Findings | 评测与基准 | LLM-based agent 记忆的综合评测，覆盖多种记忆能力。 |
| `minerva` | Minerva: A Programmable Memory Test Benchmark for Language Models | ICML 2025 | CCF-A | 评测与基准 | 可编程记忆测试基准，把记忆能力拆成可组合的测试程序。 |
| `beyondmillion` | Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs | ICLR 2026 | Top-ICLR | 评测与基准 | 百万 token 级长记忆评测与增强，扩展了长上下文记忆的压力测试。 |
| `memoryagentbench` | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | ICLR 2026 | Top-ICLR | 评测与基准 | 把长期记忆评测改造成增量多轮交互，覆盖检索、测试时学习、长程理解和选择性遗忘四项能力。 |
| `memorybench` | MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems | ICML 2026 | CCF-A | 评测与基准 | 用用户反馈模拟框架评测 LLM 系统的持续学习与记忆能力，覆盖多领域、多语言和多任务类型。 |
| `privacy` | Unveiling Privacy Risks in LLM Agent Memory | ACL 2025 | CCF-A | 安全与隐私 | 记忆隐私抽取攻击，揭示长期记忆中的敏感信息泄露面。 |
| `injection` | Memory Injection Attacks on LLM Agents via Query-Only Interaction | NeurIPS 2025 | CCF-A | 安全与隐私 | query-only 记忆注入攻击，说明只通过查询交互也能污染 agent 记忆。 |
| `injecmem` | InjecMEM: Memory Injection Attack on LLM Agent Memory Systems | COLM 2026 | Top-COLM | 安全与隐私 | 把注入攻击扩展到记忆系统的写入/检索链路，攻击面更系统。 |
| `poisononce` | Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents | COLM 2026 | Top-COLM | 安全与隐私 | 环境注入的记忆 poisoning：一次污染可被长期利用，面向 Web agent。 |
| `memrec` | MemRec: Collaborative Memory-Augmented Agentic Recommender System | ACL 2026 | CCF-A | 应用 | 把协作记忆增强用于 agentic recommender system。 |
| `storagetexperience` | From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms | ACL Findings 2026 | ACL-Findings | 综述与框架 | 把 LLM agent memory 的演化概括为 Storage → Reflection → Experience 三阶段，并梳理长程一致性、动态环境和持续学习三条驱动线。 |

## 关系边

| From | 类型 | To | 解释 |
|---|---|---|---|
| A-Mem: Agentic Memory for LLM Agents | extends | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | 单 agent 记忆 → 多 agent 层次记忆 |
| A-Mem: Agentic Memory for LLM Agents | extends | MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents | 动态记忆组织 → 多图结构 |
| A-Mem: Agentic Memory for LLM Agents | extends | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | 记忆组织 → 多粒度关联 |
| A-Mem: Agentic Memory for LLM Agents | extends | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | 检索 → 重构 |
| A-Mem: Agentic Memory for LLM Agents | extends | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | 记忆结构 → 可学习记忆策略 |
| A-Mem: Agentic Memory for LLM Agents | extends | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | 记忆结构 → RL memory agent |
| A-Mem: Agentic Memory for LLM Agents | extends | MemEvolve: Meta-Evolution of Agent Memory Systems | 手工设计 → 元进化 |
| A-Mem: Agentic Memory for LLM Agents | extends | UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory | 动态组织 → 统一抽取与管理 |
| A-Mem: Agentic Memory for LLM Agents | extends | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | 研究原型 → 生产级记忆流水线 |
| G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | extends | Learning to Share: Selective Memory for Efficient Parallel Agentic Systems | 团队记忆 → 选择性共享记忆 |
| G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | related | MemEvolve: Meta-Evolution of Agent Memory Systems | 多 agent 记忆 → 记忆系统进化 |
| MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | related | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | RL memory agent 的两条实现路线 |
| Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | extends | MemEvolve: Meta-Evolution of Agent Memory Systems | 记忆策略学习 → 记忆系统进化 |
| Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | related | UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory | 记忆管理与统一管理 |
| MemEvolve: Meta-Evolution of Agent Memory Systems | related | UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory | 自动设计 vs 统一抽取 |
| Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | extends | Hippocampus: An Efficient and Scalable Memory Module for Agentic AI | 长期记忆系统 → 高效记忆模块 |
| Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | extends | TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory | 记忆压缩与证据保留 |
| Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | risk | Unveiling Privacy Risks in LLM Agent Memory | 长期记忆的隐私面 |
| Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | risk | Memory Injection Attacks on LLM Agents via Query-Only Interaction | 长期记忆的注入面 |
| Human-inspired Episodic Memory for Infinite Context LLMs | extends | REMem: Reasoning with Episodic Memory in Language Agent | 类人 episodic memory → 推理中的事件记忆 |
| Human-inspired Episodic Memory for Infinite Context LLMs | extends | ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory | 无限上下文 → 时空 episodic memory |
| REMem: Reasoning with Episodic Memory in Language Agent | extends | EMA: An Episodic Memory Agent for Efficient and Selective Memory | 事件级记忆 → 选择性 episodic unit |
| REMem: Reasoning with Episodic Memory in Language Agent | extends | Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory | 文本事件 → 多模态经验 |
| EMA: An Episodic Memory Agent for Efficient and Selective Memory | related | RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents | 选择性记忆 → 复现式整合 |
| RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents | extends | TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents | 整合 → 时间层次整合 |
| TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents | extends | TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory | 时间层次 → 压缩/证据分层 |
| TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory | evaluates | PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | 压缩记忆的遗忘边界 |
| Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval | related | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | 个性化检索 → 长期交互评测 |
| PersonaAgent: Bridging Memory and Action for Personalized LLM Agents | extends | Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval | 记忆-行动耦合 → 个性化检索 |
| Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution | related | MemEvolve: Meta-Evolution of Agent Memory Systems | 程序性记忆 vs 元进化 |
| MemRec: Collaborative Memory-Augmented Agentic Recommender System | applies | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | 长期记忆用于推荐 |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | related | MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents | 长期交互 → 综合记忆评测 |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | extends | Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs | 长期交互 → 百万 token 压力测试 |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | extends | Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks | 单会话评测 → 多 session 任务 |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | extends | PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | 记忆保留 → 何时遗忘 |
| MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents | related | Minerva: A Programmable Memory Test Benchmark for Language Models | 综合评测 vs 可编程测试 |
| Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs | related | Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks | 规模压力 vs 任务依赖 |
| Unveiling Privacy Risks in LLM Agent Memory | related | Memory Injection Attacks on LLM Agents via Query-Only Interaction | 隐私抽取与记忆注入的攻击面对照 |
| Memory Injection Attacks on LLM Agents via Query-Only Interaction | extends | InjecMEM: Memory Injection Attack on LLM Agent Memory Systems | 查询注入 → 记忆系统注入 |
| InjecMEM: Memory Injection Attack on LLM Agent Memory Systems | extends | Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents | 注入 → 长期记忆 poisoning |
| LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | evaluated-by | A-Mem: Agentic Memory for LLM Agents | A-Mem 类系统的长期记忆评测参照 |
| MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents | evaluated-by | A-Mem: Agentic Memory for LLM Agents | agent memory 综合评测参照 |
| PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | evaluated-by | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | 记忆管理与遗忘边界 |
| M+: Extending MemoryLLM with Scalable Long-Term Memory | related | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | 参数化记忆 vs 图重构记忆 |
| LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents | related | EMA: An Episodic Memory Agent for Efficient and Selective Memory | 小模型工作记忆 vs 事件记忆 |
| ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory | related | Human-inspired Episodic Memory for Infinite Context LLMs | 时空事件记忆与类人机制 |
| Learning to Share: Selective Memory for Efficient Parallel Agentic Systems | related | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | 并行记忆共享 vs 长上下文压缩 |
| LightMem: Lightweight and Efficient Memory-Augmented Generation | extends | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | 生产级记忆流水线 → 轻量级记忆系统 |
| LightMem: Lightweight and Efficient Memory-Augmented Generation | related | Hippocampus: An Efficient and Scalable Memory Module for Agentic AI | 高效记忆模块的不同系统路线 |
| LightMem: Lightweight and Efficient Memory-Augmented Generation | related | LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents | 低成本长期记忆 vs 小模型工作记忆 |
| On Memory Construction and Retrieval for Personalized Conversational Agents | extends | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | segment 级记忆 → 多粒度记忆 |
| On Memory Construction and Retrieval for Personalized Conversational Agents | related | A-Mem: Agentic Memory for LLM Agents | 记忆粒度选择 vs 原子笔记组织 |
| Memory OS of AI Agent | related | MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents | 三级层次存储 vs 多关系图记忆 |
| Memory OS of AI Agent | related | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | 层次记忆系统作为主动重建的对照 |
| From RAG to Memory: Non-Parametric Continual Learning for Large Language Models | related | MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents | 图增强 RAG vs 多关系 agent memory |
| From RAG to Memory: Non-Parametric Continual Learning for Large Language Models | related | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | 图检索基线 vs 主动重构 |
| From RAG to Memory: Non-Parametric Continual Learning for Large Language Models | related | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | 图检索与多粒度记忆的对照 |
| SimpleMem: Efficient Lifelong Memory for LLM Agents | related | LightMem: Lightweight and Efficient Memory-Augmented Generation | 高效长期记忆的两条压缩路线 |
| SimpleMem: Efficient Lifelong Memory for LLM Agents | extends | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | 生产级记忆流水线 → 语义压缩记忆 |
| GAM: Hierarchical Graph-based Agentic Memory for LLM Agents | extends | A-Mem: Agentic Memory for LLM Agents | 原子笔记 → 分层事件/主题图记忆 |
| GAM: Hierarchical Graph-based Agentic Memory for LLM Agents | related | MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents | 层次图 vs 多关系图 |
| ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | related | Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution | 程序性记忆与经验蒸馏 |
| ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | related | MemEvolve: Meta-Evolution of Agent Memory Systems | 经验驱动的记忆进化 |
| Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | extends | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | 静态长期记忆评测 → 增量多轮能力评测 |
| Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | related | MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents | 综合记忆评测的不同维度 |
| Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | related | PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | 选择性遗忘与遗忘边界评测 |
| Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents | extends | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | 分离的记忆操作 → 统一 LTM/STM 策略 |
| Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents | related | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | RL memory agent 的不同统一管理路线 |
| Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents | related | PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | 可学习 discard 动作与遗忘边界评测 |
| E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory | related | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | episodic context reconstruction vs active reconstruction |
| E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory | related | GAM: Hierarchical Graph-based Agentic Memory for LLM Agents | E-mem 在 LoCoMo 上以 GAM 为强基线 |
| EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning | extends | Memory OS of AI Agent | 分层 memory OS → 自组织 memory OS |
| EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning | related | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | 语义整合 + scene-guided retrieval |
| What Deserves Memory: Adaptive Memory Distillation for LLM Agents | related | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | 自适应记忆蒸馏 vs 多粒度记忆 |
| What Deserves Memory: Adaptive Memory Distillation for LLM Agents | related | RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents | 预测误差驱动整合 vs recurrence-based consolidation |
| Lightweight LLM Agent Memory with Small Language Models | related | LightMem: Lightweight and Efficient Memory-Augmented Generation | 两个同名 LightMem 系统，机制不同，引用时需区分 |
| Lightweight LLM Agent Memory with Small Language Models | related | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | SLM 驱动记忆 vs 生产级 LLM 记忆 |
| MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems | extends | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | 静态记忆 QA → 用户反馈驱动的持续学习评测 |
| MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems | related | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | 持续学习与增量多轮记忆的不同评测维度 |
| From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms | related | A-Mem: Agentic Memory for LLM Agents | 综述框架：Storage → Reflection → Experience |
| From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms | related | ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | Experience 阶段的跨轨迹抽象 |

## 维护规则

- 新增论文先写入 `data/agent-memory-2025/papers.json`。
- 新增关系先写入 `data/agent-memory-2025/edges.json`。
- 然后运行 `python3 scripts/build_research_map.py --papers ... --edges ... --vault ... --out ...`。
