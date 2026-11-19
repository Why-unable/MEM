# Agent Memory 2025+ — Research Synthesis

> 基于主库 36 篇正式发表论文的概念地图。这里给出研究脉络、争议和可做的问题；具体实验数字仍需回论文 PDF 复核。

## 1. 一句话判断

2025–2026 的 agent memory 正在从“把历史塞进向量库/上下文”转向四个更细的问题：

1. **怎么组织记忆**：图、层次、多粒度、时间结构。
2. **怎么决定写什么、读什么、忘什么**：memory policy 与 RL。
3. **怎么把经验变成能力**：episodic / procedural memory、整合与重构。
4. **怎么证明它真的有效、且安全**：长期任务 benchmark、遗忘评测、隐私与注入攻击。

## 2. 七条主线

### 主线 A：记忆架构从“检索”走向“组织 + 重构”

代表：A-Mem、G-Memory、MAGMA、MemGAS、Memory is Reconstructed。

- A-Mem 用 Zettelkasten 式动态索引和链接组织记忆，是后续工作的常见基线。
- G-Memory 把多智能体协作轨迹做成层次记忆，开始处理“团队记忆”而不是单 agent 记忆。
- MAGMA 用多图结构组织实体、事件和时间关系。
- MemGAS 强调多粒度关联与选择。
- Memory is Reconstructed 直接把记忆定义为“重构”而非“检索”。

**研究含义**：记忆的质量不只取决于 embedding 相似度，还取决于结构、时间、因果关系和重构策略。

### 主线 B：memory policy 变成可学习对象

代表：MemAgent、Memory-R1、MemEvolve、UMEM。

- MemAgent 用 multi-conv RL 训练 memory agent 压缩长上下文。
- Memory-R1 用 RL 训练记忆管理与使用。
- MemEvolve 进一步把记忆系统的结构/策略作为进化对象。
- UMEM 试图统一记忆抽取与管理。

**研究含义**：从“设计一个固定 memory pipeline”转向“学习一个 memory controller”。

### 主线 C：系统效率与生产可用性

代表：Mem0、Hippocampus、LightWM、Learning to Share。

- Mem0 关注生产级长期记忆的抽取、更新与检索。
- Hippocampus 关注高效、可扩展的记忆模块。
- LightWM 面向小模型 agent 的免训练工作记忆。
- Learning to Share 处理并行多 agent 的选择性共享记忆。

**研究含义**：memory 不只是算法问题，也是存储、延迟、吞吐、权限和成本问题。

### 主线 D：episodic memory 与记忆整合

代表：Human-inspired Episodic Memory、REMem、ARTEM、EMA、RecMem、TiMem、TierMem。

- Human-inspired Episodic Memory 用类人机制扩展无限上下文。
- REMem 把 episodic memory 与推理结合。
- ARTEM 增加时空事件结构。
- EMA 把对话抽象为 episodic memory unit。
- RecMem / TiMem 处理记忆整合与长时程对话。
- TierMem 在压缩记忆和原始证据之间做权衡。

**研究含义**：关键问题从“存多少”转向“如何把事件压缩成可复用经验，同时保留证据”。

### 主线 E：个性化、多模态与程序性记忆

代表：Evoking User Memory、PersonaAgent、Seeing/Listening/Remembering、Remember Me Refine Me、MemRec。

- 个性化记忆强调“回忆—熟悉度”式检索和记忆-行动耦合。
- 多模态记忆把视觉、听觉和文本经验放在同一长期记忆中。
- 程序性记忆把历史经验提炼为可复用技能。
- MemRec 展示记忆在推荐系统中的应用。

**研究含义**：memory 正在从“对话历史”扩展到用户模型、跨模态经验和技能库。

### 主线 F：评测从“记住没有”走向“何时该忘”

代表：LongMemEval、Beyond a Million Tokens、Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks、PersistBench、MemBench、Minerva。

- LongMemEval 是长期交互记忆的核心参照。
- Beyond a Million Tokens 把压力推到百万 token 级。
- Interdependent 关注多 session 相互依赖的真实任务。
- PersistBench 把“何时应该遗忘”变成显式评测对象。
- MemBench / Minerva 试图覆盖更综合或更可编程的记忆能力。

**研究含义**：单一 QA 分数不够；需要同时测保留、更新、冲突、遗忘、迁移和任务收益。

### 主线 G：记忆安全成为独立攻击面

代表：Unveiling Privacy Risks、Memory Injection Attacks、InjecMEM、Poison Once Exploit Forever。

- 隐私工作展示长期记忆可被抽取。
- 注入工作说明 query-only 交互也可能污染记忆。
- InjecMEM 把攻击扩展到记忆系统链路。
- Poison Once 展示一次环境注入可被长期利用。

**研究含义**：memory system 需要 write authorization、provenance、trust、expiration、rollback 和 audit。

## 3. 关键争议

### 争议 1：记忆应该“检索”还是“重构”？

传统 RAG 把记忆当作检索问题；A-Mem / Memory is Reconstructed 更强调动态组织和重构。前者工程简单，后者更接近人类记忆，但更难评测。

### 争议 2：memory policy 应该手工设计还是学习？

Mem0 / MAGMA 等偏系统设计；MemAgent / Memory-R1 / MemEvolve 偏学习。学习路线更自适应，但训练成本、稳定性和可迁移性仍未解决。

### 争议 3：长期记忆是否等于长期上下文？

Beyond a Million Tokens 等工作说明“上下文更长”不等于“记忆更好”。关键仍是选择、压缩、更新和冲突解决。

### 争议 4：遗忘是缺陷还是能力？

PersistBench 把遗忘作为能力来评测；隐私与安全研究则要求可删除、可审计、可回滚。未来需要把“遗忘”纳入 memory system 的一等公民。

## 4. 研究空白与机会

1. **统一记忆评测协议**：跨会话、跨模态、跨任务，同时测保留、更新、遗忘和迁移。
2. **可审计记忆治理**：provenance、权限、过期、删除、回滚和 poisoning 检测。
3. **记忆策略的迁移学习**：在一个领域学到的 memory policy 能否迁移到另一个领域？
4. **多智能体共享记忆**：共享粒度、冲突解决、责任归属和隐私边界。
5. **程序性记忆与技能学习**：从“记住事实”走向“记住怎么做”。
6. **记忆压缩与证据保留的 Pareto 前沿**：TierMem 提出了问题，但还没有统一答案。

## 5. 推荐阅读顺序

1. A-Mem → G-Memory → LongMemEval
2. MemAgent → Memory-R1 → MemEvolve
3. RecMem → TiMem → TierMem
4. PersistBench → Privacy Risks → Memory Injection → Poison Once
5. REMem → Seeing/Listening/Remembering → Remember Me Refine Me

## 6. 使用提醒

- 本 synthesis 是对标题/摘要/venue 的概念性综合，不是系统综述的最终结论。
- 每篇论文的实验设置、baseline、数据集和指标必须回 PDF 核对。
- 关系边是研究地图边，不等于引文边。
