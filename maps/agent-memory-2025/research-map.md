# Agent Memory 2025+ · Research Map

- 论文数：36
- 关系数：47
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
  end
  subgraph training[记忆策略与训练]
    memagent["MemAgent: Reshaping Long-Context LLM wi..."]
    memoryr1["Memory-R1: Enhancing Large Language Mod..."]
    memeolve["MemEvolve: Meta-Evolution of Agent Memo..."]
    umem["UMEM: Unified Memory Extraction and Man..."]
  end
  subgraph system[系统与效率]
    mem0["Mem0: Building Production-Ready AI Agen..."]
    hippocampus["Hippocampus: An Efficient and Scalable ..."]
    lightwm["LightWM: Training-Free Hierarchical Wor..."]
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
```

## 论文清单

| ID | 论文 | Venue | 层级 | 类别 | 定位 |
|---|---|---|---|---|---|
| `amem` | A-Mem: Agentic Memory for LLM Agents | NeurIPS 2025 | CCF-A | 记忆架构 | 提出动态组织、链接和演化的 agentic memory，是 2025 年后记忆结构设计的高频基线。 |
| `gmemory` | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems | NeurIPS 2025 | CCF-A | 记忆架构 | 把多智能体协作轨迹组织成层次记忆，连接个体记忆与团队记忆。 |
| `magma` | MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents | ACL 2026 | CCF-A | 记忆架构 | 用多图结构组织实体、事件和时间关系，强调可解释、可检索的 agent 记忆。 |
| `reconstructed` | Memory is Reconstructed, Not Retrieved:  Graph Memory for LLM Agents | ICML 2026 | CCF-A | 记忆架构 | 把记忆视为“重构”而不是“检索”，用图结构动态重建上下文。 |
| `mplus` | M+: Extending MemoryLLM with Scalable Long-Term Memory | ICML 2025 | CCF-A | 记忆架构 | 扩展 MemoryLLM 的可扩展长期参数记忆，连接参数化记忆与外部记忆。 |
| `memgas` | From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents | ICLR 2026 | Top-ICLR | 记忆架构 | 多粒度记忆关联与选择，缓解长对话中检索粒度不匹配的问题。 |
| `memagent` | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | ICLR 2026 | Top-ICLR | 记忆策略与训练 | 用 multi-conv RL 训练 memory agent 压缩长上下文，代表“记忆策略可学习”路线。 |
| `memoryr1` | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | ACL 2026 | CCF-A | 记忆策略与训练 | 用强化学习训练记忆管理与使用策略，把记忆操作从 prompt 工程推进为可学习策略。 |
| `memeolve` | MemEvolve: Meta-Evolution of Agent Memory Systems | ICML 2026 | CCF-A | 记忆策略与训练 | 用元进化自动设计记忆系统的结构与策略，代表“记忆系统自动设计”方向。 |
| `umem` | UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory | ICML 2026 | CCF-A | 记忆策略与训练 | 统一记忆抽取与管理，强调跨任务、跨场景的泛化记忆能力。 |
| `mem0` | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | ECAI 2025 | CCF-B | 系统与效率 | 工业级可扩展长期记忆，强调生产部署中的记忆抽取、更新与检索流水线。 |
| `hippocampus` | Hippocampus: An Efficient and Scalable Memory Module for Agentic AI | MLSys 2026 | Top-MLSys | 系统与效率 | 面向 agentic AI 的高效、可扩展记忆模块，偏系统实现与部署效率。 |
| `lightwm` | LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents | ICML 2026 | CCF-A | 系统与效率 | 面向小模型 agent 的免训练层次工作记忆，强调低成本与可部署性。 |
| `humanepisodic` | Human-inspired Episodic Memory for Infinite Context LLMs | ICLR 2025 | Top-ICLR | 情景记忆 | 用类人 episodic memory 扩展无限上下文，是 2025 年记忆架构的重要基础工作。 |
| `remem` | REMem: Reasoning with Episodic Memory in Language Agent | ICLR 2026 | Top-ICLR | 情景记忆 | 把 episodic memory 与推理过程结合，强调事件级经验的复用。 |
| `artem` | ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory | AAAI 2026 | CCF-A | 情景记忆 | 时空 episodic memory，关注事件顺序、时间依赖和长期空间经验。 |
| `ema` | EMA: An Episodic Memory Agent for Efficient and Selective Memory | ACL Findings 2026 | ACL-Findings | 情景记忆 | 把对话抽象为 episodic memory unit 并做选择性记忆，降低长对话冗余。 |
| `recmem` | RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents | ACL Findings 2026 | ACL-Findings | 记忆整合 | 基于复现/重复的记忆整合，减少对每条交互做 eager extraction 的开销。 |
| `timem` | TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents | ACL Findings 2026 | ACL-Findings | 记忆整合 | 时间—层次记忆整合，面向长时程对话中的时序信息保持。 |
| `tiermem` | TierMem: Balancing Compressed Memory and Raw Evidence for Long-Horizon Agent Memory | COLM 2026 | Top-COLM | 记忆整合 | 在压缩记忆与原始证据之间做分层权衡，面向长时程 agent memory。 |
| `evoking` | Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval | ICLR 2026 | Top-ICLR | 个性化记忆 | 基于回忆—熟悉度的自适应检索，把个性化记忆从“存什么”推进到“如何取”。 |
| `personaagent` | PersonaAgent: Bridging Memory and Action for Personalized LLM Agents | ACL Findings 2026 | ACL-Findings | 个性化记忆 | 把记忆与行动耦合，做面向个性化任务的 LLM agent。 |
| `multimodal` | Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory | ICLR 2026 | Top-ICLR | 多模态记忆 | 多模态长期记忆 agent，连接视觉、听觉与文本经验。 |
| `rememberrefine` | Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution | ACL Findings 2026 | ACL-Findings | 程序性记忆 | 经验驱动的程序性记忆，让 agent 从历史经验中提炼可复用技能。 |
| `learnshare` | Learning to Share: Selective Memory for Efficient Parallel Agentic Systems | ICML 2026 | CCF-A | 多智能体记忆 | 并行多 agent 系统中的选择性共享记忆，平衡效率与协作收益。 |
| `longmemeval` | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory | ICLR 2025 | Top-ICLR | 评测与基准 | 长期交互记忆基准，已成为记忆系统评测的重要参照。 |
| `interdependent` | Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks | ICML 2026 | CCF-A | 评测与基准 | 多 session 相互依赖任务中的 agent memory 基准，贴近真实长期任务。 |
| `persistbench` | PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? | ICML 2026 | CCF-A | 评测与基准 | 评测“何时应该遗忘”，把记忆持久化边界变成显式研究对象。 |
| `membench` | MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents | ACL Findings 2025 | ACL-Findings | 评测与基准 | LLM-based agent 记忆的综合评测，覆盖多种记忆能力。 |
| `minerva` | Minerva: A Programmable Memory Test Benchmark for Language Models | ICML 2025 | CCF-A | 评测与基准 | 可编程记忆测试基准，把记忆能力拆成可组合的测试程序。 |
| `beyondmillion` | Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs | ICLR 2026 | Top-ICLR | 评测与基准 | 百万 token 级长记忆评测与增强，扩展了长上下文记忆的压力测试。 |
| `privacy` | Unveiling Privacy Risks in LLM Agent Memory | ACL 2025 | CCF-A | 安全与隐私 | 记忆隐私抽取攻击，揭示长期记忆中的敏感信息泄露面。 |
| `injection` | Memory Injection Attacks on LLM Agents via Query-Only Interaction | NeurIPS 2025 | CCF-A | 安全与隐私 | query-only 记忆注入攻击，说明只通过查询交互也能污染 agent 记忆。 |
| `injecmem` | InjecMEM: Memory Injection Attack on LLM Agent Memory Systems | COLM 2026 | Top-COLM | 安全与隐私 | 把注入攻击扩展到记忆系统的写入/检索链路，攻击面更系统。 |
| `poisononce` | Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents | COLM 2026 | Top-COLM | 安全与隐私 | 环境注入的记忆 poisoning：一次污染可被长期利用，面向 Web agent。 |
| `memrec` | MemRec: Collaborative Memory-Augmented Agentic Recommender System | ACL 2026 | CCF-A | 应用 | 把协作记忆增强用于 agentic recommender system。 |

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

## 维护规则

- 新增论文先写入 `data/agent-memory-2025/papers.json`。
- 新增关系先写入 `data/agent-memory-2025/edges.json`。
- 然后运行 `python3 scripts/build_research_map.py --papers ... --edges ... --vault ... --out ...`。
