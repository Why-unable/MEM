# Agent Memory 2025+：实验数据集与对比基线全景

> 更新时间：2026-11-26  
> 范围：`data/agent-memory-2025/papers.json` 中的 36 篇正式发表论文  
> 方法：优先读取论文 PDF 的 Experiments / Experimental Setup / Baselines 段落；已完成的 5 张主线 A 证据卡用于交叉核对  
> 说明：本文是“实验设置地图”，不是排行榜。不同论文的 backbone、judge、数据切分、token 预算和 baseline 重实现方式不同，数字不能直接横比。

## 0. 先给结论

1. **评测高度集中在两个对话记忆基准上。**  
   在 26 篇方法论文中，至少 12 篇使用 **LoCoMo**，9 篇使用 **LongMemEval**，13 篇至少使用两者之一。它们已经成为 agent memory 的“事实标准”，但两者测的能力并不相同。

2. **离开对话记忆后，评测迅速碎片化。**  
   embodied agent 用 ALFWorld / SciWorld / PDDL；deep research 用 GAIA / WebWalkerQA / xBench；工具调用用 BFCL-V3 / AppWorld；Web agent 用 WebArena / WebShop；个性化用 LaMP；推荐用 Amazon / Yelp；多模态用 M3-Bench；安全用 MIMIC-III / eICU / MMLU / WebShop。

3. **基线已经形成几个稳定家族。**  
   `no-memory / full-context`、`RAG / BM25 / dense retrieval`、`MemGPT / MemoryBank / A-Mem / Mem0 / MemoryOS / LangMem`、`HippoRAG 2 / GraphRAG / MemoRAG`、`SFT / PPO / GRPO` 学习型策略，以及各类 agent framework。

4. **“结构化记忆优于长上下文”不是普遍结论。**  
   A-Mem、MAGMA、MRAgent 等在 multi-hop / temporal 上通常更强，但在 single-hop、knowledge-update、adversarial 上，full-context 仍然经常赢。真正稳定的结论更像是：**记忆结构和访问策略要与任务结构匹配**。

5. **当前最缺的不是更多 baseline，而是统一实验协议。**  
   同用 LoCoMo 的论文，可能在 backbone、LLM judge、数据切分、是否排除 adversarial、检索 top-k、构建 token 是否计入成本上完全不同。这使“SOTA”很难被严格比较。

---

## 1. 三个容易混淆的概念

### Dataset

原始数据集合，例如：

- LoCoMo：多会话对话 + QA；
- MIMIC-III：ICU 电子病历数据库；
- Amazon Books：用户-商品交互记录。

### Benchmark

在数据集之上定义的任务、指标和评测协议，例如：

- LongMemEval：500 个问题，测 information extraction、multi-session reasoning、knowledge update、temporal reasoning、abstention；
- BEAM：128K 到 10M token 的 100 个长对话，测 10 类记忆能力；
- Minerva：1110 个可编程记忆测试；
- MemoryArena：4 个多会话 agent 环境。

有些论文同时提出 benchmark 和 method，例如 LongMemEval、BEAM + LIGHT、MemoryArena、MemBench、PersistBench、M3-Bench + M3-Agent。

### Baseline

被拿来对比的方法。它可能是：

- 一个完整记忆系统：Mem0、A-Mem、MemoryOS；
- 一个检索方法：BM25、dense retrieval、RAG；
- 一个模型：GPT-4o、Llama 3.1、Qwen2.5；
- 一个训练变体：Memory-SFT、Memory-R1-PPO、Memory-R1-GRPO；
- 一个消融版本：w/o router、w/o causal links、No RL。

**注意同名歧义：** A-Mem 和 Mem0 的表里，`LoCoMo` 有时指“在 LoCoMo 上运行的 RAG-style baseline”，不是指数据集本身。Memory-R1 也把 `LoCoMo (RAG)` 当作 baseline 名称。

---

## 2. 数据集与 benchmark 全景

### 2.1 多会话对话记忆

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **LoCoMo** | 10 组长期多会话对话，平均约 600 turns、26K tokens | single-hop、multi-hop、temporal、open-domain、adversarial QA | A-Mem、Memory-R1、MAGMA、Mem0、REMem、MemGAS、MRAgent、Hippocampus、EMA、RecMem、TiMem、TierMem |
| **LongMemEval** | 500 个手工问题，分 LongMemEval-S（约 115K tokens）和 LongMemEval-M（约 1.5M tokens） | information extraction、multi-session reasoning、knowledge update、temporal reasoning、abstention | Memory-R1、MAGMA、MemGAS、MRAgent、Hippocampus、RecMem、TiMem、TierMem、Evoking；LongMemEval 论文本身 |
| **MSC** | Multi-Session Chat，长多会话对话数据 | 跨 session 的对话理解与记忆迁移 | Memory-R1（zero-shot 迁移） |
| **REALTALK** | 真实人类对话，而非合成对话 | 更真实的 episodic recollection | REMem |
| **DialSim** | 基于电视剧 / 电影脚本的长对话模拟 | 长叙事中的记忆与问答 | A-Mem |
| **Long-MT-Bench+** | 长多轮对话 benchmark | 长对话中的事实、时间与偏好 | EMA、MemGAS |
| **PerLTQA** | 个人长期记忆 QA 数据 | 个人事实、事件与偏好回忆 | 在 LongMemEval、MemGAS、MemBench 中作为相关 benchmark 被讨论，不是这些论文的主实验集 |
| **PersonaMem** | 模拟用户在 7 类真实任务上的长期交互，长度 32K / 128K / 1M | 用户 persona、偏好演化、个性化生成 | Evoking |
| **PersonaBench** | 合成私有用户文档 + 查询 | 个性化记忆检索 | Evoking |

**这一组的关键区别：**

- LoCoMo 更像“多会话生活对话 + 多类 QA”；
- LongMemEval 更像“在线记忆系统的能力分解测试”，尤其是 knowledge update 和 abstention；
- PersonaMem 关注“用户偏好是否随时间和交互演化”；
- REALTALK 的价值是“真实对话”，不是合成脚本。

### 2.2 长上下文与合成压力测试

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **LongBench** | 双语长上下文 benchmark，含 QA、摘要、few-shot、检索、代码等 | 通用长上下文理解 | Human-inspired Episodic Memory、MemAgent |
| **LongBench-QA** | LongBench 的 QA 子集：NarrativeQA、Qasper、HotpotQA、2WikiMultihopQA、MuSiQue | 高信息密度长文 QA | MemAgent |
| **∞-Bench / InfiniteBench** | 极长上下文任务集合，含 LongBook-QA、Passkey.Retrieval 等 | 超长书、检索、passkey | Human-inspired Episodic Memory、M+ |
| **RULER-HQA** | 可控长度、可控信息密度的合成长上下文 QA | 长度外推与有效上下文利用 | MemAgent |
| **NIAH** | Needle in a Haystack，把关键事实插入大量无关文本 | 低信息密度下的精确检索 | MemAgent |
| **BEAM** | 100 个对话，长度 128K / 500K / 1M / 10M；覆盖 10 类记忆能力 | 多领域、超长对话记忆 | Beyond a Million Tokens（BEAM + LIGHT） |
| **Minerva** | 1110 个可编程记忆测试，固定 4K 上下文 | search、recall、edit、match、compare、compute、stateful processing | Minerva 论文本身 |

**这一组的关键区别：**

- LongBench / ∞-Bench 是“长上下文能力”基准；
- RULER / NIAH 是“可控合成压力测试”；
- BEAM 把长度推到 10M，并拆成 10 类记忆能力；
- Minerva 不是自然语言长文，而是把记忆拆成可组合的程序化测试。

### 2.3 Agentic、embodied、工具与 Web 环境

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **ALFWorld** | 文本化家庭环境，agent 需要完成多步家务任务 | 长程规划、状态依赖、经验复用 | G-Memory、UMEM、LightWM |
| **SciWorld / ScienceWorld** | 文本化科学实验环境 | 多步科学推理与操作 | G-Memory |
| **PDDL** | 经典规划任务 | 多 agent 规划与协作 | G-Memory |
| **HotpotQA** | 多跳 Wikipedia QA | 跨文档多跳推理 | G-Memory、MemAgent、UMEM |
| **FEVER** | 事实核验 | 证据检索与事实验证 | G-Memory |
| **GAIA** | 165 个真实世界助手任务，分 3 个难度等级 | 浏览、工具调用、长程规划、结果综合 | MemEvolve、Learning to Share |
| **AssistantBench** | 181 个真实 Web 任务，支持部分得分 | Web agent 的多步任务完成 | Learning to Share |
| **WebWalkerQA** | Web 遍历问答 | 多页面搜索与信息整合 | MemEvolve |
| **xBench-DeepSearch** | Deep search 任务 | 深度检索与研究型任务 | MemEvolve |
| **TaskCraft** | 任务生成 / agentic 任务集合 | 任务复杂度与执行 | MemEvolve |
| **BFCL-V3** | Berkeley Function Calling Leaderboard v3 | 多轮函数调用与工具使用 | Remember Me, Refine Me |
| **AppWorld** | 模拟 App 与工具环境 | 多应用任务执行 | Remember Me, Refine Me |
| **WebArena** | 真实网站风格的 Web 环境：Shopping、Reddit、Classifieds | Web agent 操作、跨站任务 | Poison Once |
| **VisualWebArena** | WebArena 的视觉版本 | 视觉 Web agent | Poison Once |
| **WebShop** | 模拟电商环境，约 118 万商品 | 商品搜索、选择、购买 | Privacy Risks、Memory Injection Attacks；MemoryArena 的 Bundled Web Shopping 基于它扩展 |
| **MemoryArena** | 4 个环境：Bundled Web Shopping、Group Travel Planning、Progressive Web Search、Math/Physics Formal Reasoning | 多 session、相互依赖、记忆-行动-环境闭环 | MemoryArena 论文本身 |

**这一组的关键区别：**

- ALFWorld / SciWorld / PDDL 测“行动中的记忆”；
- GAIA / AssistantBench / WebWalkerQA 测“研究型工具使用”；
- BFCL-V3 / AppWorld 测“工具调用与程序性经验”；
- WebArena / WebShop 测“Web 交互”，同时也是安全攻击的主要试验场。

### 2.4 个性化与推荐

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **LaMP-1 / 2M / 2N / 3** | Language Model Personalization benchmark：引用识别、电影标签、新闻分类、产品评分 | 个性化决策 | PersonaAgent |
| **LaMP-4 / 5** | 个性化新闻标题、学术标题生成 | 个性化文本生成 | PersonaAgent（附录） |
| **Amazon Books** | Amazon 图书用户-商品交互 | 推荐与用户偏好 | MemRec |
| **Amazon Goodreads** | Goodreads 图书评分与交互 | 推荐，交互更密集 | MemRec |
| **MovieTV** | 电影 / 电视交互数据 | 推荐 | MemRec |
| **Yelp** | 商户评论与用户交互 | 推荐，社区信号更强 | MemRec |

**这一组的关键区别：**

- LaMP 测“个性化决策/生成”，不是记忆检索本身；
- Amazon / Yelp 测“协作记忆是否能改善推荐排序”，指标是 Hit@K / NDCG@K，而不是 QA accuracy。

### 2.5 多模态

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **M3-Bench-robot** | 100 个机器人第一视角长视频，1276 个 QA | 机器人场景中的长期多模态记忆 | M3-Agent |
| **M3-Bench-web** | 920 个网络长视频，3214 个 QA | 跨模态、人物理解、知识提取 | M3-Agent |
| **VideoMME-long** | 长视频 QA 基准 | 长视频理解与记忆 | M3-Agent |

**这一组的关键区别：** M3-Bench 同时要求“看、听、记、推理”，并显式包含 person understanding、cross-modal reasoning、general knowledge extraction；VideoMME-long 是外部对照基准。

### 2.6 安全、隐私与记忆治理

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **MIMIC-III** | ICU 电子病历数据库 | 医疗隐私泄露、记忆注入、患者 ID 混淆 | Privacy Risks、Memory Injection Attacks |
| **eICU** | 多中心 ICU 数据库 | 药物相关记忆注入 | Memory Injection Attacks |
| **MMLU** | 57 个学科的单选题 | 通用 QA agent 的记忆注入 | Memory Injection Attacks |
| **WebShop** | 模拟电商环境 | Web agent 隐私提取与记忆注入 | Privacy Risks、Memory Injection Attacks |
| **WildChat** | 真实用户与 ChatGPT 对话 | 真实对话上的记忆注入泛化 | InjecMEM |
| **19-domain synthetic dialogues** | InjecMEM 生成的 19 个领域多轮对话 | 受控记忆污染与检索 | InjecMEM |
| **PersistBench** | 500 个样本：200 cross-domain leakage、200 sycophancy、100 beneficial memory | 什么时候该遗忘、什么时候不该受记忆影响 | PersistBench 论文本身 |

**这一组的关键区别：**

- MEXTRA 测“能不能把记忆里的私有 query 提取出来”；
- MINJA 测“能不能通过正常交互把恶意记录写进记忆，并在未来触发”；
- InjecMEM 测“记忆系统链路中的注入与检索”；
- Poison Once 测“环境注入 + 跨站任务 + 长期利用”；
- PersistBench 测“记忆不该被使用时的失败率”，与前几者相反：它关注过度记忆。

### 2.7 推理与阅读任务

| 数据集 / benchmark | 是什么 | 主要测什么 | 使用论文 |
|---|---|---|---|
| **AIME24 / AIME25** | 数学竞赛题 | 复杂数学推理 | UMEM |
| **GPQA-Diamond** | 研究生水平科学问答 | 领域科学推理 | UMEM |
| **HLE** | Humanity's Last Exam，多学科高难问题 | 复杂综合推理 | UMEM |
| **Complex-TR** | 需要复杂时间推理的阅读理解 | episodic reasoning | REMem |
| **Test of Time** | 时间语义阅读理解 | 时间相关记忆推理 | REMem |
| **NarrativeQA** | 长篇小说 / 剧本 QA | 长文事件理解 | MemAgent、Human-inspired Episodic Memory、M+ |
| **Qasper** | 学术论文 QA | 长文档理解 | MemAgent、Human-inspired Episodic Memory、M+ |
| **MuSiQue** | 多跳 QA | 多步证据组合 | MemAgent、Human-inspired Episodic Memory、M+ |
| **2WikiMultihopQA** | 多跳 Wikipedia QA | 跨文档推理 | MemAgent、Human-inspired Episodic Memory |
| **TriviaQA** | 开放域 QA | 长上下文检索与问答 | Human-inspired Episodic Memory |

---

## 3. 基线全景：它们分别在控制什么

### 3.1 六类基线

| 基线家族 | 代表 | 控制什么变量 | 常见问题 |
|---|---|---|---|
| **No-memory / full-context** | No Memory、Full Context、Full History、Offline Reading、RecentMemory、FullMemory | “不记忆”或“全部塞进上下文”的下界/上界 | token 成本极高；长上下文会出现 lost-in-the-middle |
| **Retrieval / RAG** | Naive RAG、BM25、dense retrieval、Contriever、Stella、BGE、E5、NV-Embed、Qwen3-Embedding | “只做相似度检索”的强基线 | 不会主动更新、组织、遗忘；top-k 和 chunk 策略影响很大 |
| **Memory systems** | MemGPT、MemoryBank、A-Mem、Mem0、Mem0g、MemoryOS、MemOS、LangMem、Zep/Graphiti、HippoRAG 2、Nemori、ReadAgent、LightMem、SeCom、O-mem、MemR3、GAM、Mirix、ReasoningBank | “已有记忆系统”的横向对比 | 很多是重实现；backbone、prompt、检索预算常不同 |
| **Learned policies** | Memory-SFT、Memory-R1-PPO、Memory-R1-GRPO、MemAgent w/o RL、UMEM No Train、ReMe fixed/dynamic | “学习记忆策略”是否真的有用 | 训练成本、数据泄漏、跨任务迁移常未报告 |
| **Agent frameworks** | AutoGen、DyLAN、MacNet、MetaGPT、CAMEL、ChatDev、MagenticOne、M1-Parallel、OWL、Smolagents、Cognitive Kernel-Pro、Agent KB、Flash-Searcher | “多 agent / 工具编排”带来的收益 | 框架能力与记忆能力混在一起，难以归因 |
| **Model baselines** | GPT-4o、GPT-4o-mini、GPT-4.1、GPT-5、Claude、Gemini、Qwen、Llama、Mistral、Phi、DeepSeek、Kimi、Grok | “模型本身能力” | 模型版本变化快；不同论文的 judge/backbone 不统一 |

### 3.2 常见记忆系统基线解释

| 基线 | 是什么 | 为什么常被选 |
|---|---|---|
| **MemGPT** | OS 风格的分层记忆：可写工作上下文 + 外部记忆 + 分页/换入换出 | 长期记忆系统的经典参照 |
| **MemoryBank** | 带遗忘/recency 机制的长期记忆库 | 代表“记忆衰减 + 检索”路线 |
| **A-Mem** | Zettelkasten 式原子笔记，带关键词、标签、链接和 memory evolution | 2025 年后最常用的结构化记忆基线之一 |
| **Mem0 / Mem0g** | 生产级记忆抽取、更新、检索流水线；Mem0g 增加图记忆 | 工程完整、常作为强 baseline |
| **MemoryOS** | 短/中/长期分层记忆，带用户/agent persona 维护 | 代表 OS 式记忆管理 |
| **MemOS** | 记忆操作系统，强调统一记忆管理与调度 | 系统型强基线 |
| **LangMem** | LangChain 的长期记忆模块 | 工具链成熟、易复现 |
| **Zep / Graphiti** | 带时间维度的知识图谱记忆平台 | 代表 temporal knowledge graph 路线 |
| **HippoRAG 2** | 受海马索引启发的图检索记忆 | 图结构检索的强基线 |
| **ReadAgent** | 分层阅读与压缩，把长文变成可检索的摘要 | 长文记忆的早期参照 |
| **Nemori** | 记忆系统 baseline，强调结构化记忆 | MAGMA 等论文使用 |
| **LightMem** | 轻量级长期记忆 | 面向低成本/边缘部署 |
| **SeCom** | 选择性压缩记忆 | 长对话压缩路线 |
| **O-mem** | 摘要中心型记忆 | TierMem 的 summary-centric 基线 |
| **MemR3** | 推理时检索控制器 | TierMem 的 raw/controller 基线 |
| **GAM** | 粒度感知记忆 | TierMem 的 raw/controller 基线 |
| **Mirix** | 多 agent 记忆系统 | MemoryArena 的外部记忆基线 |
| **ReasoningBank** | 推理经验记忆 | MemoryArena 的外部记忆基线 |
| **Memp** | 解耦的 Build-Retrieve-Update 记忆流水线 | UMEM 的 pipeline baseline |
| **ReMem** | 轨迹级记忆管理 | UMEM 的记忆管理 baseline |
| **Self-RAG** | 推理时自反思检索 | UMEM 的 inference-time baseline |

### 3.3 学习型基线和消融

这一类不是“另一个系统”，而是为了隔离某个设计变量：

- **Memory-SFT**：同样的记忆架构，但用监督学习替代 RL；
- **Memory-R1-PPO / GRPO**：同一框架下的两种 RL 优化；
- **MemAgent w/o RL**：去掉 RL，只保留 memory agent 结构；
- **UMEM No Train**：使用相同 prompt，但不训练 memory policy；
- **ReMe fixed / dynamic**：经验池是否在执行中动态更新；
- **w/o router、w/o causal links、w/o temporal backbone**：MAGMA / MemGAS / TierMem 的模块消融。

这类基线对 RQ1 很重要，因为它们能回答：**收益到底来自“结构”，还是来自“训练/检索策略/更多计算”？**

---

## 4. 36 篇论文的实验设置对照

### 4.1 方法论文（26 篇）

| 论文 | 任务类型 | 数据集 / benchmark | 主要对比基线 |
|---|---|---|---|
| **A-Mem**（NeurIPS 2025） | 结构化 agent memory | LoCoMo、DialSim | Full-context / LoCoMo RAG、MemGPT、MemoryBank、ReadAgent |
| **G-Memory**（NeurIPS 2025） | 多 agent 层次记忆 | ALFWorld、SciWorld、PDDL、HotpotQA、FEVER | No-memory、MetaGPT-M；AutoGen / DyLAN / MacNet 三种 MAS 框架 |
| **MemAgent**（ICLR 2026） | RL memory agent | RULER-HQA、LongBench-QA、NIAH | Qwen2.5-Instruct 7B/14B/32B、Qwen2.5-Instruct-1M、QwenLong-L1-32B、DeepSeek-R1-Distill-Qwen；MemAgent w/o RL |
| **Memory-R1**（ACL 2026） | 学习记忆管理 | LoCoMo、MSC、LongMemEval | LoCoMo RAG、A-Mem、Mem0、MemoryOS、Memory-SFT、Memory-R1-PPO / GRPO |
| **MAGMA**（ACL 2026） | 多图记忆架构 | LoCoMo、LongMemEval | Full Context、A-Mem、MemoryOS、Nemori |
| **MemEvolve**（ICML 2026） | 元进化记忆系统 | GAIA、WebWalkerQA、xBench-DeepSearch、TaskCraft | No-Memory、Voyager、ExpeL、DILU、AWM、Mobile-E、Dynamic Cheatsheet；Flash-Searcher / Smolagents / OWL / Agent KB 等 agent 框架 |
| **UMEM**（ICML 2026） | 统一记忆抽取与管理 | AIME24+25、GPQA-Diamond、HLE、HotpotQA、ALFWorld | No Memory、No Train、Self-RAG、Memp、ReMem |
| **Mem0**（ECAI 2025） | 生产级长期记忆 | LoCoMo | LoCoMo、ReadAgent、MemoryBank、MemGPT、A-Mem、LangMem、Zep、OpenAI memory、full-context；Mem0g |
| **REMem**（ICLR 2026） | episodic reasoning | LoCoMo、REALTALK、Complex-TR、Test of Time | Oracle Message、Full-Context、Qwen3-Embedding-8B、NV-Embed-v2、Mem0、Graphiti、HippoRAG 2、TISER |
| **MemGAS**（ICLR 2026） | 多粒度记忆关联 | LoCoMo、Long-MT-Bench+、LongMemEval-S、LongMemEval-M | Full History、A-Mem、HippoRAG 2；成本对比 RAPTOR、SeCom、RecurSum |
| **MRAgent**（ICML 2026） | 图记忆 + 多轮主动重构 | LoCoMo、LongMemEval | RAG、LangMem、A-Mem、MemoryOS、Mem0 |
| **Hippocampus**（MLSys 2026） | 高效可扩展记忆模块 | LoCoMo、LongMemEval-S | ReadAgent、MemoryBank、MemGPT、A-Mem、MemoryOS、MemOS |
| **ARTEM**（AAAI 2026） | 时空 episodic memory | Episodic Memory Benchmark；合成长书 Synaptic Echoes（200 章，102,870 tokens） | ICL、RAG、fine-tuning；GPT-4o / 4o-mini、Claude-3-Haiku / 3.5-Sonnet、o1 / o1-mini / o3-mini、Gemini-2-Pro / Flash / Flash-Thinking |
| **Human-inspired Episodic Memory**（ICLR 2025） | 类人 episodic memory | LongBench、∞-Bench（含 Passkey.Retrieval 到 10.2M tokens）、人类事件分割播客 | InfLLM、full-context、NV-Embed-v2 RAG；多种 base LLM |
| **M+**（ICML 2025） | 参数化长期记忆 | LongBook-QA（∞-Bench，351 本书，平均 192K tokens）、LongBook Event QA | Llama-3.1-8B-16K、Llama-3.1-8B-BM25、Llama-3.1-8B-SnapKV、Llama-3.2-3B-128K、MemoryLLM-8B |
| **LightWM**（ICML 2026） | 小模型层次工作记忆 | ALFWorld（valid unseen；valid seen 用于 schema induction） | ReAct、Simply Summarize、HiAgent、MemGPT |
| **EMA**（ACL Findings 2026） | episodic memory agent | LoCoMo、Long-MT-Bench+ | Only LLM、Naive RAG、MemoryBank、A-Mem、LightMem、SeCom、MemoryOS |
| **RecMem**（ACL Findings 2026） | 基于复现的记忆巩固 | LoCoMo、LongMemEval-S | Full Context、Naive RAG、Mem0、A-Mem、MemoryOS |
| **TiMem**（ACL Findings 2026） | 时间层次记忆巩固 | LoCoMo、LongMemEval-S | MemoryBank、Mem0、A-Mem、MemoryOS、MemOS |
| **TierMem**（COLM 2026） | 分层记忆 + 充分性路由 | LoCoMo、LongMemEval；MemoryAgentBench 用于 router 训练 | Mem0、LightMem、O-mem、MemOS、MemR3、GAM；summary-only / raw-only / router 变体 |
| **Evoking / RF-Mem**（ICLR 2026） | 个性化记忆检索 | PersonaMem（32K/128K/1M）、PersonaBench、LongMemEval | Zero Memory、Full Context、Dense Retrieval、Recollection；RF-Mem |
| **M3-Agent**（ICLR 2026） | 多模态长期记忆 | M3-Bench-robot、M3-Bench-web、VideoMME-long | Socratic Models（Gemini-1.5-Pro / GPT-4o / Qwen2.5-Omni-7B / Qwen2.5-VL-7B）、MovieChat、MA-LMM、Flash-VStream、Gemini-Agent、Gemini-GPT4o-Agent |
| **Remember Me, Refine Me**（ACL Findings 2026） | 程序性记忆 / 经验复用 | BFCL-V3、AppWorld | No Memory、A-Mem、LangMem、ReMe fixed / dynamic |
| **PersonaAgent**（ACL Findings 2026） | 个性化 agent | LaMP-1、LaMP-2M、LaMP-2N、LaMP-3；LaMP-4/5 在附录 | Prompt、ICL、RAG、PAG、ReAct、MemBank |
| **MemRec**（ACL 2026） | 协作记忆推荐 | Amazon Books、Amazon Goodreads、MovieTV、Yelp | LightGCN、SASRec、P5、Vanilla LLM、iAgent、i2Agent、AgentCF、RecBot |
| **Learning to Share / LTS**（ICML 2026） | 并行多 agent 选择性共享记忆 | GAIA、AssistantBench | MagenticOne 单团队、3-team M1-Parallel、LTS-AddAll、LTS-LLM、LTS |

### 4.2 基准 / 评测论文（6 篇）

| 论文 | 贡献类型 | 数据集 / benchmark | 主要对比对象 |
|---|---|---|---|
| **LongMemEval**（ICLR 2025） | benchmark | LongMemEval-S（约 115K tokens）、LongMemEval-M（约 1.5M tokens），500 问 | Offline Reading、ChatGPT、Coze、GPT-4o、Llama 3.1 70B/8B、Phi-3 128K / Phi-3.5 Mini；Oracle retrieval；多种 indexing/retrieval 设计 |
| **Beyond a Million Tokens**（ICLR 2026） | benchmark + method（BEAM + LIGHT） | BEAM：100 个对话，128K / 500K / 1M / 10M tokens，10 类记忆能力 | 长上下文 Qwen2.5-32B-AWQ、Llama-4-Maverick、Gemini-2.0-Flash、GPT-4.1-nano；RAG；LIGHT |
| **MemoryArena**（ICML 2026） | benchmark | Bundled Web Shopping、Group Travel Planning、Progressive Web Search、Math/Physics Formal Reasoning | 长上下文 agent（GPT-5-mini、GPT-4.1-mini、Gemini-3-flash、Claude-Sonnet-4.5）；外部记忆（MemGPT、Mem0、Mem0g、Mirix、ReasoningBank）；RAG（BM25、embedding RAG、MemoRAG、GraphRAG） |
| **PersistBench**（ICML 2026） | benchmark | 500 样本：200 cross-domain leakage、200 sycophancy、100 beneficial memory | 18 个前沿/开源模型，含 GPT-5.2、Claude-Opus-4.5、Gemini-3-Pro、Grok-4、Qwen3-235B-A22B、Kimi-K2、Llama-4-Maverick；reasoning / non-reasoning 变体 |
| **MemBench**（ACL Findings 2025） | benchmark | MemBench：participation / observation 场景，factual / reflective memory；基于 MemSim、MovieLens、Food、Goodreads | FullMemory、RetrievalMemory、RecentMemory、GenerativeAgent、MemoryBank、MemGPT、Self-Controlled Memory |
| **Minerva**（ICML 2025） | benchmark | 1110 个可编程记忆测试，4K 上下文；search / recall / edit / match / compare / compute / stateful processing | GPT-4-turbo、GPT-4o、GPT-4o-mini、Cohere Command R+、Mistral-7B、Phi-3-small/medium、LLaMA-3.1-8B、Gemma-2-9B |

### 4.3 安全与隐私论文（4 篇）

| 论文 | 攻击 / 防御类型 | 数据集 / 环境 | 主要对比对象 |
|---|---|---|---|
| **Unveiling Privacy Risks in LLM Agent Memory / MEXTRA**（ACL 2025） | 记忆提取攻击 | MIMIC-III（EHRAgent）、WebShop（RAP） | MEXTRA vs w/o aligner、w/o req、w/o demos；不同 memory size、embedding、相似度函数 |
| **Memory Injection Attacks / MINJA**（NeurIPS 2025） | 记忆注入攻击 | WebShop（RAP）、MIMIC-III / eICU（EHRAgent）、MMLU（QA Agent） | Clean memory、prior poisoning、PANDORA；adversarial training、embedding sanitization、prompt detection、system-level defense |
| **InjecMEM**（COLM 2026） | 记忆注入攻击 | 19 域合成对话、WildChat；MemoryOS、MemGPT | DPI、GCG、BadChain、Multi-GCG；LLM-as-a-Judge、ProtectAI、PromptGuard、Perplexity |
| **Poison Once, Exploit Forever / eTAMP**（COLM 2026） | 环境注入记忆 poisoning | WebArena、VisualWebArena（Shopping、Reddit、Classifieds；约 280 个跨站任务对） | Baseline Injection、Frustration Exploitation、Authority Framing；Chaos Monkey；GPT-5-mini、GPT-5.2、GPT-OSS-120B、Qwen2.5-VL-72B、Qwen3-VL-32B、Qwen3.5-122B-A10B |

---

## 5. 从这张图里能看出什么

### 5.1 评测的“事实标准”已经形成，但只覆盖一部分能力

- **LoCoMo** 是对话记忆社区最常用的横向对比集；
- **LongMemEval** 是第二个核心参照，尤其是 knowledge update、temporal reasoning、abstention；
- 两者都偏向“对话 + QA”，无法覆盖 embodied、工具调用、多 agent、多模态和安全治理。

因此，看到一篇论文只在 LoCoMo 上提升，不能推断它在 agentic 任务上也更强。

### 5.2 baseline 很多，但“同条件对比”很少

常见问题包括：

- 不同 backbone：有的用 GPT-4o，有的用 GPT-4o-mini，有的用 Qwen2.5；
- 不同 judge：GPT-4o judge / GPT-4o-mini judge / 人工 judge；
- 不同数据切分：是否排除 adversarial、是否只用子集、是否重新划分 train/val/test；
- 不同检索预算：top-k、chunk size、token budget 不一致；
- baseline 重实现：A-Mem、Mem0、MemoryOS 等经常被作者重新实现，结果可能偏离原论文。

所以本文的矩阵适合回答“**用了什么**”，不适合回答“**谁绝对更好**”。

### 5.3 结构记忆的优势集中在 multi-hop / temporal

多篇论文的共同模式：

- A-Mem 在 multi-hop、temporal 上优于 full-context，但在 single-hop、adversarial 上输；
- MAGMA 在 LoCoMo overall、temporal、adversarial 上强，但 full-context 在 single-session-assistant、knowledge-update 上更强；
- MRAgent 在 multi-hop、temporal、open-domain、single-hop 上全面强于多个记忆基线，但成本/延迟和静态图增长是代价；
- MemGAS 在 LongMemEval 上强，但在 LoCoMo 上低于 HippoRAG 2。

**可检验的假设：** 结构化记忆的收益来自“跨 session 证据整合”和“时间/冲突处理”，而不是“所有 QA 都更好”。

### 5.4 访问策略可能比存储结构更关键

MAGMA 的消融显示：去掉 adaptive policy 的下降大于去掉单个关系图；MRAgent 的收益主要来自多轮 active reconstruction，而不只是图结构。  
这直接支持 RQ1 的一个更细的拆法：

```text
memory structure × access policy × context budget
```

而不是只比较“结构记忆 vs 长上下文”。

### 5.5 成本报告仍不统一

常见成本口径：

- tokens/query；
- total token consumption；
- build time；
- search latency；
- end-to-end latency；
- GPU memory；
- storage size。

但很少有论文同时报告“构建成本 + 查询成本 + 更新成本 + 删除/回滚成本”。这会高估低频写入、长生命周期系统的实际优势。

---

## 6. 对 RQ1 的直接启示

RQ1：**记忆结构何时优于长上下文？**

基于这 36 篇论文，建议把 RQ1 的实验拆成三个轴：

### 轴 1：任务结构

- single-hop：预期 full-context 很强；
- multi-hop：结构记忆应更强；
- temporal：结构/时间图应更强；
- knowledge update：需要显式更新机制，单纯图结构不一定赢；
- adversarial / abstention：需要证据边界，结构记忆可能反而引入噪声。

### 轴 2：记忆结构

至少比较：

1. full-context；
2. BM25 / dense RAG；
3. A-Mem-like（原子笔记 + 链接 + 演化）；
4. MAGMA-like（多关系图）；
5. MRAgent-like（多轮主动重构）。

### 轴 3：访问策略

- 单轮 top-k；
- policy-guided traversal；
- 多轮 active reconstruction；
- 是否允许 abstain / escalation。

### 必须报告的指标

- QA accuracy / LLM-judge；
- tokens/query；
- build token cost；
- latency；
- storage；
- update / conflict resolution；
- 在 single-hop、multi-hop、temporal、knowledge-update、adversarial 上的分层结果。

### 建议的最小实验

```text
同一 backbone
× full-context
× BM25 / dense RAG
× A-Mem-like
× MAGMA-like
× MRAgent-like
```

数据集先选：

- LoCoMo（社区可比性）；
- LongMemEval-S（能力分解）；
- BEAM 或 MemoryArena（压力测试 / agentic 外部效度）。

---

## 7. 证据边界

- 本文覆盖 36 篇主库论文的实验设置，不等于覆盖每篇论文附录中的所有 baseline。
- 论文版本可能不同：例如 MemoryArena 的正式标题与仓库中的早期标题不同；TierMem 的正式版本标题为 “From Lossy to Verified: A Provenance-Aware Tiered Memory for Agents”。
- 某些论文的表格使用了缩写或重实现名称，本文按论文中的写法记录，不额外推断。
- 本文不把不同论文的数字放在同一张排行榜上；所有跨论文比较都应回到原 PDF 核对 backbone、judge、split、budget。
