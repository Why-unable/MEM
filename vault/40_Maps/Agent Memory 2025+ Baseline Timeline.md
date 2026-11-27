---
type: evidence
subtype: baseline-timeline
status: evidence-checked
checked_at: 2026-11-27
tags:
  - evidence
  - baseline
  - dataset
  - timeline
---

# Agent Memory 2025+：时间化论文效果、数据集与基线变化

> 范围：主库 52 篇正式发表论文；时间按正式 venue 的发表月份排列。
> 目标：回答三件事：同月有哪些工作、主结果如何、它们和谁比、baseline 如何演化。
> 数据源：[JSON](../../data/agent-memory-2025/baseline-timeline.json) · [CSV](../../data/agent-memory-2025/baseline-timeline.csv)
> 实验设置背景：[EXPERIMENT_LANDSCAPE](../../maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md) · 逐篇证据：[[10_Papers/evidence/INDEX|Evidence Index]]

## 0. 先看结论：目前的“最好”是条件性的

**如果只看当前最醒目的绝对分数，VikingMem 是最强候选之一：**

- LoCoMo LLM-Judge：**90.12**（GPT-4.1-mini），高于同表 Full-Context 的 86.36；GPT-4o-mini 设置下为 **88.83**。
- LongMemEval-S LLM-Judge：**75.80**（GPT-4o），高于 Zep 的 70.40；GPT-4o-mini 下为 **66.36**。
- 但它不是跨任务总冠军：LoCoMo F1 只有 **54.98**，与 TiMem、E-mem 的 54 分头部差距很小，且 backbone / judge / split 不同。

**如果按 benchmark 分别看，头部大致是：**

| Benchmark / 指标 | 头部结果 | 强对照 | 能下的判断 |
|---|---|---|---|
| LoCoMo LLM-Judge / GPT-4o-mini | VikingMem **88.83**；TiMem 75.30；Nemori 73.0；MAGMA 70.0 | Mirix 78.66；Full-Context 77.47 | VikingMem 明显领先，但 judge prompt 与 split 未统一 |
| LoCoMo LLM-Judge / GPT-4.1-mini | VikingMem **90.12**；RecMem 81.10；Nemori 80.8 | Full-Context 86.36；Mem0 62.92 | 绝对分最高，仍未与所有方法做同 backbone 对照 |
| LoCoMo LLM-Judge / Claude-Sonnet-4.5 | MRAgent **88.32** | LangMem 78.61 | active reconstruction 在强 backbone 上也有效 |
| LoCoMo LLM-Judge / Gemini-2.5-Flash | MRAgent **84.21** | Mem0 68.31 | 同一方法换 backbone 后仍是强基线 |
| LoCoMo F1 | VikingMem **54.98**；TiMem 54.40；E-mem 54.17 | GAM 45.31；Memory-R1 45.02；A-Mem 分类别互有胜负 | 54–55 是当前公开 F1 头部簇，差距不足以宣布绝对胜者 |
| LongMemEval-S | TiMem **76.88**；RecMem **76.80**；VikingMem **75.80** | Zep 70.40；MemoryOS 74.40；Full-Context 59.20–66.20 | 三篇处于同一头部区间，backbone 和指标版本不同 |
| 个性化 / 推荐 / 工具 | PersonaAgent LaMP-1 0.919；MemRec H@1 0.5882；ReMe Pass@4 69.97 | 各自任务内 baseline | 不能换算成 LoCoMo 排名 |
| 行动 / 具身 | LightWM ALFWorld 0.910；AgeMem 五任务平均 54.31；LTS GAIA 30.4 | 同设置 baseline | 记忆对“行动闭环”的收益通常更大，但任务差异也更大 |

**效率上表现最好的不是最高分论文：**

- **TierMem**：LoCoMo accuracy 0.851 vs raw-only 0.873（-2.2 pp），但 input tokens **-54.1%**、latency **-60.7%**。
- **Hippocampus**：检索加速 **1.1x–31.5x**，per-query token 降低 **1.1x–14.5x**。
- **LightMem**：LongMemEval total token 最多降低 **38x**，LoCoMo accuracy 提升区间 **6.10%–29.29%**。
- **Mem0**：相对 full-context，p95 latency **-91%**、token **-90%+**。
- **RecMem**：LongMemEval-S 76.80 且 build token 明显低于 Mem0/A-Mem，但 LoCoMo 仍低于 full-context。

> **关键警告：这不是一个可以跨论文直接排名的总榜。** 行内 `+x%` 是为了提供同月浏览顺序，可能来自不同数据集、backbone、judge、split 和检索预算；严格结论必须回到同一 benchmark + 同一指标 + 同一 backbone 的子表。

## 1. 怎么读这张时间表

1. **时间**：使用正式发表月份，不是 arXiv 首次提交月份。
2. **同月排序**：先排有明确相对提升的方法论文，再排效率、安全、benchmark 和综述；没有可换算提升的论文放在同月方法组末尾。
3. **效果列**：保留论文自己的主指标，不把 F1、accuracy、success rate、ASR 混成一个分数。
4. **baseline 变化**：记录作者实际对比了谁，以及新增了哪类基线；不等于引文关系。
5. **未报告**：用 `—` 或“无统一 headline”标注，不用估算值填空。

## 2. 月度时间轴（52 篇）

> 每月内部的顺序是“效果浏览顺序”，不是跨任务的科学排名。

### 2025-04

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/secom-evidence|SeCom]] · 主题分段 | 方法 / 效果 | LoCoMo；Long-MT-Bench+ | LoCoMo GPT4Score 71.57；Long-MT-Bench+ 88.81 | LoCoMo 最强 baseline 65.92；+5.65 pp（+8.57%） | Full History、Turn/Session、SumMem/RecurSum/ConditionMem/MemoChat；加入 topic segmentation + denoising |
| [[10_Papers/evidence/humanepisodic-evidence|EM-LLM]] · 事件边界 | 方法 / 效果 | LongBench；∞-Bench（至 10.2M tokens）；播客事件分割 | 多数任务优于 InfLLM/RAG；可检索到 10M tokens | InfLLM、full-context、NV-Embed-v2 RAG；无统一 headline 分数 | 长上下文模型 + 外部 RAG；开始把事件边界纳入 memory unit |
| [[10_Papers/evidence/longmemeval-evidence|LongMemEval]] · 五类能力 | Benchmark / 评测基准 | LongMemEval-S（约 115K）；LongMemEval-M（约 1.5M） | 500 个手工问题；5 类长期记忆能力；现有系统下降 30%–60% | 商业 assistant / long-context LLM；benchmark 论文，不做方法排名 | 把 information extraction、multi-session、temporal、knowledge update、abstention 拆开测 |

### 2025-07

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/hipporag2-evidence|HippoRAG 2]] · 图检索 | 方法 / 效果 | NQ、PopQA、MuSiQue、2Wiki、HotpotQA、LV-Eval、NarrativeQA | 平均 QA F1 59.8；passage recall@5 78.2 | NV-Embed-v2 F1 57.0 / recall 73.4；F1 +4.9% | BM25、Contriever、GTR、NV-Embed-v2、RAPTOR、GraphRAG、LightRAG、HippoRAG |
| [[10_Papers/evidence/mplus-evidence|M+]] · 参数记忆 | 方法 / 效果 | LongBook-QA（∞-Bench，351 本书，平均约 192K）；LongBook Event QA | 知识保留从 <20K 扩展到 >160K tokens | MemoryLLM、BM25、SnapKV、Llama 长上下文基线；保留长度显著扩展 | 参数化 memory + co-trained retriever；不是外部数据库 |
| [[10_Papers/evidence/privacy-evidence|MEXTRA]] · 黑盒窃忆 | 安全攻击 / 安全 | MIMIC-III（EHRAgent）；WebShop（RAP） | EHRAgent CER 0.83/AER 0.83；RAP CER 0.87/AER 0.90 | 黑盒抽取攻击；与 w/o aligner、w/o requirement、w/o demos 对照 | 从 utility accuracy 转向 memory extraction risk |
| [[10_Papers/evidence/membench-evidence|MemBench]] · 多维评测 | Benchmark / 评测基准 | MemSim、MovieLens、Food、Goodreads；participation/observation 场景 | factual/reflective × effectiveness/efficiency/capacity | FullMemory、RetrievalMemory、RecentMemory、GenerativeAgent、MemoryBank、MemGPT、SCM | 从单一 QA 分数扩展到多维度能力评测 |
| [[10_Papers/evidence/minerva-evidence|Minerva]] · 原子测试 | Benchmark / 评测基准 | 1,110 个可编程 memory tests；约 4K context | search/recall/edit/match/compare/compute/stateful 七类能力 | GPT-4-turbo/4o/4o-mini、Command R+、Mistral、Phi、LLaMA、Gemma | 从 passkey/NIAH 转向原子 + 组合 memory operation |

### 2025-10

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/mem0-evidence|Mem0]] · 抽取巩固 | 方法 / 效果 | LoCoMo | LLM-J 相对 OpenAI memory +26%；p95 latency -91%；token -90%+ | OpenAI memory、full-context；Mem0g 再提升约 +2% | ReadAgent、MemoryBank、MemGPT、A-Mem、LangMem、Zep、OpenAI memory、full-context |

### 2025-11

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/memoryos-evidence|MemoryOS]] · 三级存储 | 方法 / 效果 | LoCoMo；GVD | LoCoMo 平均 F1 +49.11%、BLEU-1 +46.18% | 相对平均 baseline；LLM calls 4.9 vs A-Mem 约 13 | MemGPT、A-Mem、TiM；引入 short/mid/long-term OS 层次 |

### 2025-12

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/gmemory-evidence|G-Memory]] · 三层团队图 | 方法 / 效果 | ALFWorld、SciWorld、PDDL、HotpotQA、FEVER | GPT-4o-mini + AutoGen 平均 57.18 vs 48.27 | No-memory 48.27；平均 +18.46%，ALFWorld +20.89 pp | No-memory、MetaGPT-M；AutoGen、DyLAN、MacNet 三种 MAS 框架 |
| [[10_Papers/evidence/amem-evidence|A-Mem]] · 卡片 | 方法 / 效果 | LoCoMo；DialSim | Temporal F1 45.85 vs 18.41；Multi-hop 27.02 vs 25.02；Adversarial 50.03 vs 69.23 | Full-context/LoCoMo RAG；分类别互有胜负，未报告 overall | Full-context、LoCoMo RAG、MemGPT、MemoryBank、ReadAgent；原子笔记成为后续常用基线 |
| [[10_Papers/evidence/injection-evidence|MINJA]] · 查询注入 | 安全攻击 / 安全 | WebShop（RAP）、MIMIC-III/eICU（EHRAgent）、MMLU（QA Agent） | 平均 ISR 98.2%；平均 ASR 76.8% | Clean memory、prior poisoning、PANDORA；prompt/embedding/system defenses | 从直接写 memory 转向 query-only 注入；加入 bridging steps 与 progressive shortening |

### 2026-01

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/artem-evidence|ARTEM]] · 时空事件 | 方法 / 效果 | Episodic Memory Benchmark；Synaptic Echoes（200 章、102,870 tokens） | Simple Recall F1 0.709；Chronological F1 0.585；Temporal query F1 0.67 | Temporal query 0.67 vs baseline 0.5（+34%） | ICL、RAG、fine-tuning；GPT-4o/4o-mini、Claude、o1/o3-mini、Gemini |

### 2026-04

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/lightmem-evidence|LightMem]] · 离线巩固 | 方法 / 效果 | LoCoMo；LongMemEval-S | LoCoMo accuracy +6.10%–29.29%；LongMemEval +2.09%–7.67%；token 最多降 38x | FullText、Naive RAG、LangMem、A-Mem、MemoryOS、Mem0 | 在线/离线解耦；A-Mem 成为最强常见基线 |
| [[10_Papers/evidence/reasoningbank-evidence|ReasoningBank]] · 推理经验 | 方法 / 效果 | WebArena、Mind2Web、SWE-Bench-Verified | WebArena SR 51.8 vs 40.5；最高约 +20% relative；steps 9.7→7.9 | No Memory、Synapse、AWM；Gemini/Claude backbones | 从轨迹记忆转向可复用 reasoning memory + MaTTS |
| [[10_Papers/evidence/remem-evidence|REMem]] · 情景推理 | 方法 / 效果 | LoCoMo、REALTALK、Complex-TR、Test of Time | LoCoMo F1 42.4/LLM-J 77.5；Complex-TR F1 83.3；Test of Time EM 93.1 | Full-Context、HippoRAG 2、Mem0、Graphiti；回忆 +3.4%、推理 +13.4 个百分点 | 加入 Graphiti、HippoRAG 2 与 refusal 指标；事件级 gist/fact 混合图 |
| [[10_Papers/evidence/beyondmillion-evidence|BEAM / LIGHT]] · 千万长测 | 方法 / 效果 | BEAM：128K–10M tokens；100 个长对话、2,000 个验证问题 | LIGHT 相对最强 baseline +3.5%–12.69% | long-context models + RAG；1M context 仍随长度退化 | 把评测压力推到 10M tokens，并加入长期 episodic + working memory |
| [[10_Papers/evidence/multimodal-evidence|M3-Agent]] · 视听实体 | 方法 / 效果 | M3-Bench-robot（100 videos）、M3-Bench-web（920 videos）、VideoMME-long | 相对最强 prompt baseline：robot +6.7%、web +7.7%、VideoMME-long +5.3% | Socratic Models、MovieChat、MA-LMM、Flash-VStream、Gemini-Agent | entity-centric episodic + semantic multimodal memory；多轮记忆推理 |
| [[10_Papers/evidence/memgas-evidence|MemGAS]] · 多粒度 | 方法 / 效果 | LoCoMo、Long-MT-Bench+、LongMemEval-S、LongMemEval-M | LongMemEval-S 60.20 vs 57.60；LongMemEval-M 45.4；LoCoMo 41.07 vs HippoRAG 2 45.62 | Full History、A-Mem、HippoRAG 2；LongMemEval +4.51%，LoCoMo 反而落后 | 多粒度关联 + GMM/PPR/router；HippoRAG 2 成为直接强基线 |
| [[10_Papers/evidence/memagent-evidence|MemAgent]] · 覆盖式记忆 | 方法 / 效果 | RULER-HQA、NIAH、LongBench-QA/SUM | 8K 训练上下文外推到 3.5M，RULER-HQA 71.09；512K NIAH >95% | QwenLong-L1-32B、Qwen2.5-1M 等在长上下文迅速退化；无统一 headline | 从更长 context window 转向固定 memory 的 RL 读写策略 |
| [[10_Papers/evidence/evoking-evidence|Evoking / RF-Mem]] · 双过程检索 | 方法 / 效果 | PersonaMem（32K/128K/1M）、PersonaBench、LongMemEval | PersonaMem overall 0.6350 / 0.5394；1M 也为最佳 overall | Zero Memory、Full Context、Dense Retrieval、Recollection；延迟 4.27–6.28ms | 双过程检索：familiarity 快路径 + recollection 慢路径；固定 budget/latency |
| [[10_Papers/evidence/memoryagentbench-evidence|MemoryAgentBench]] · 增量评测 | Benchmark / 评测基准 | 增量多轮交互任务；四类记忆能力 | 现有方法无法同时掌握四类记忆能力 | 多种 memory/retrieval 方法；benchmark 论文 | 加入 selective forgetting、test-time learning 与长程理解 |

### 2026-05

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/hippocampus-evidence|Hippocampus]] · 压缩检索 | 方法 / 效率 / Pareto | LoCoMo；LongMemEval-S（附录 M） | 检索加速 1.1x–31.5x；query token 降低 1.1x–14.5x | ReadAgent、MemoryBank、MemGPT、A-Mem、MemoryOS、MemOS；accuracy 有竞争力 | 压缩域检索：binary signature + lossless token-ID stream + DWM |

### 2026-07

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/lightwm-evidence|LightWM]] · 双层工作记忆 | 方法 / 效果 | ALFWorld valid_unseen（valid_seen 用于 schema induction） | Qwen3-4B success 0.910；同设置 baseline <0.320 | ReAct、Simply Summarize、HiAgent、MemGPT；相对提升至少约 184% | task-level + subtask-level working memory；offline schema induction |
| [[10_Papers/evidence/gam-evidence|GAM]] · 事件主题图 | 方法 / 效果 | LoCoMo；LongDialQA | LoCoMo GPT-4o-mini Avg F1 43.14；LongDialQA 12.55，比 MemoryOS +86% | MemoryBank、ReadAgent、MemGPT、MemoryOS、Mem0、A-Mem | event progression graph + topic associative network；semantic-shift consolidation |
| [[10_Papers/evidence/learnshare-evidence|LTS]] · 选择性共享 | 方法 / 效果 | AssistantBench、GAIA | Qwen3-32B：AssistantBench 20.3 vs 14.7；GAIA 30.4 vs 24.8；runtime -40.8%/-55.0% | MagenticOne、M1-Parallel、LTS-AddAll、LTS-LLM | 并行多 agent + selective memory admission；同时优化 accuracy/runtime |
| [[10_Papers/evidence/reconstructed-evidence|MRAgent]] · 主动重构 | 方法 / 效果 | LoCoMo；LongMemEval | LoCoMo LLM-J 84.21（Gemini）/88.32（Claude）；LongMemEval 72.95（Gemini） | Mem0 68.31 / LangMem 78.61；LongMemEval MemoryOS 54.92；最高 +32.83% | 从 passive top-k 转向 Cue–Tag–Content 图上的多轮 active reconstruction |
| [[10_Papers/evidence/timem-evidence|TiMem]] · 时间树 | 方法 / 效果 | LoCoMo；LongMemEval-S | LoCoMo 75.30 vs Mem0 57.79；LongMemEval-S 76.88 vs 67.56 | A-Mem、Mem0、MemoryOS、MemOS；LoCoMo +30.3%，LongMemEval +13.8% | Temporal Memory Tree + semantic-guided consolidation + complexity-aware recall |
| [[10_Papers/evidence/memrec-evidence|MemRec]] · 协作推荐 | 方法 / 效果 | Amazon Books、Amazon Goodreads、MovieTV、Yelp | H@1：Books 0.5117、Goodreads 0.3997、MovieTV 0.5882、Yelp 0.4868 | 最强 baseline i2Agent；相对提升 +14.91%–28.98% | LightGCN/SASRec/P5/Vanilla LLM/iAgent/i2Agent/AgentCF/RecBot → 协作记忆 |
| [[10_Papers/evidence/memoryr1-evidence|Memory-R1]] · RL 管理 | 方法 / 效果 | LoCoMo；MSC；LongMemEval | LLaMA-3.1-8B LoCoMo F1 45.02 / B1 37.51 / LLM-J 62.74 | MemoryOS F1 35.04；GRPO 相对 F1 +28.5%、J +30.2% | LoCoMo RAG、A-Mem、Mem0、MemoryOS、Memory-SFT；加入 PPO/GRPO memory manager |
| [[10_Papers/evidence/simplemem-evidence|SimpleMem]] · 语义压缩 | 方法 / 效果 | LoCoMo（附录含其他 benchmark） | LoCoMo 平均 F1 +26.4%；推理 token 最多降低 30x | full history、RAG、memory systems | semantic structured compression + online synthesis + intent-aware retrieval |
| [[10_Papers/evidence/rememberrefine-evidence|ReMe]] · 程序经验 | 方法 / 效果 | BFCL-V3；AppWorld | Qwen3-14B Avg@4 44.66 / Pass@4 63.71；Qwen3-32B Pass@4 69.97 | Qwen3-14B No Memory Avg@4 35.62；+25.4%；Pass@4 +16.6% | No Memory、A-Mem、LangMem、ReMe fixed/dynamic；程序性经验提炼-复用-修剪 |
| [[10_Papers/evidence/emem-evidence|E-mem]] · 局部重构 | 方法 / 效果 | LoCoMo；HotpotQA；200K+ streaming 扩展 | LoCoMo F1 54.17；比 GAM 45.31 高 8.86 点（+19.55%） | Long-Context、RAG、A-Mem、MemoryOS、LightMem、GAM | 多 agent 保留未压缩 episodic context，按需局部重构 |
| [[10_Papers/evidence/agemem-evidence|AgeMem]] · 策略化读写 | 方法 / 效果 | ALFWorld、SciWorld、PDDL、BabyAI、HotpotQA | Qwen3-4B average 54.31 vs A-Mem 45.74；Qwen2.5-7B 41.96 vs Mem0 37.14 | 最佳 baseline 提升 +8.57 / +4.82 pp；相对 +18.74% / +12.98% | No-Memory、LangMem、A-Mem、Mem0、Mem0g、AgeMem-noRL；LTM+STM 统一为 RL tool actions |
| [[10_Papers/evidence/magma-evidence|MAGMA]] · 多图策略 | 方法 / 效果 | LoCoMo；LongMemEval | LoCoMo LLM-J 0.700；LongMemEval 61.2% | LoCoMo Nemori 0.590 / full 0.481；LongMemEval Nemori 56.2 / full 55.0 | Full Context、A-Mem、MemoryOS、Nemori；多图 + adaptive policy |
| [[10_Papers/evidence/memeolve-evidence|MemEvolve]] · 元进化 | 方法 / 效果 | GAIA、WebWalkerQA、xBench-DeepSearch、TaskCraft | SmolAgent / Flash-Searcher 最高提升 17.06%；成本接近 no-memory | No-Memory、Voyager、ExPeL、DILU、AWM、Mobile-E、Dynamic Cheatsheet、agent frameworks | 从固定 memory architecture 转向 meta-evolution；跨任务/LLM 迁移 |
| [[10_Papers/evidence/nemori-evidence|Nemori]] · 预测误差 | 方法 / 效果 | LoCoMo；LongMemEval-S | LoCoMo LLM-J 73.0/80.8；LongMemEval 64.2/74.6 | Full Context 72.3/80.6；LongMemEval +16.7%/+13.7% | Full Context、LangMem、A-Mem、Zep、MemoryOS、Mem0；prediction-error distillation |
| [[10_Papers/evidence/evermemos-evidence|EverMemOS]] · 生命周期 | 方法 / 效果 | LoCoMo、LongMemEval、PersonaMem-v2 | LoCoMo 相对最强 baseline +9.2%；LongMemEval +6.7%；profile +9.32 点 | Zep、MemOS、MemoryOS、A-Mem | MemCell → MemScene → reconstructive recollection 生命周期 |
| [[10_Papers/evidence/recmem-evidence|RecMem]] · 复发巩固 | 方法 / 效果 | LoCoMo；LongMemEval-S | LoCoMo 81.10 vs full 84.18；LongMemEval 76.80 vs full 66.20 | Mem0 62.92/71.20、A-Mem 68.83/71.60；LongMemEval +3.2% vs MemoryOS | recurrence-triggered consolidation；强调 build token，而非只比 query token |
| [[10_Papers/evidence/umem-evidence|UMEM]] · 联合抽取 | 方法 / 效果 | AIME24+25、GPQA-Diamond、HLE、HotpotQA、ALFWorld | 多轮交互任务最高 +11.49 分；五 benchmark 稳定提升 | No Memory、No Train、Self-RAG、Memp、ReMem；指标含 accuracy/success | 抽取与管理联合优化；semantic neighborhood + marginal utility reward + GRPO |
| [[10_Papers/evidence/lightmem-slm-evidence|LightMem (SLM)]] · 小模型控制 | 方法 / 效果 | LoCoMo | 平均 F1 比 A-Mem 高约 2.5；检索 83ms、端到端 581ms | A-Mem 等 memory systems | 用 small language model 做记忆控制；与 LightMem 是不同论文 |
| [[10_Papers/evidence/ema-evidence|EMA]] · 查询过滤 | 方法 / 效果 | LoCoMo；Long-MT-Bench+ | 保持竞争力；MemDecider 插件平均降低 token 11.48% | Only LLM、Naive RAG、MemoryBank、A-Mem、LightMem、SeCom、MemoryOS | Episodic Memory Unit + learned query-time filtering |
| [[10_Papers/evidence/personaagent-evidence|PersonaAgent]] · 偏好闭环 | 方法 / 效果 | LaMP-1、LaMP-2M、LaMP-2N、LaMP-3；附录 LaMP-4/5 | LaMP-1 Acc 0.919；LaMP-2M 0.513；LaMP-2N 0.796；LaMP-3 MAE 0.241 | Prompt、ICL、RAG、PAG、ReAct、MemBank；均优于 baseline | persona 作为 memory-action 中介；test-time preference alignment |
| [[10_Papers/evidence/persistbench-evidence|PersistBench]] · 该忘才忘 | Benchmark / 安全 | 500 样本：200 cross-domain、200 sycophancy、100 beneficial memory | 中位失败率：cross-domain 53%、sycophancy 97.8%、beneficial-use 16.5% | 18 个 proprietary/open-weight LLMs；reasoning/non-reasoning 变体 | 从“记忆有没有用”转向“何时不该使用记忆” |
| [[10_Papers/evidence/interdependent-evidence|MemoryArena]] · 行动闭环 | Benchmark / 评测基准 | Bundled Web Shopping、Group Travel Planning、Progressive Web Search、Math/Physics Formal Reasoning | LoCoMo 接近饱和的 agent 在多 session 行动任务上表现很差 | MemGPT、Mem0、Mem0g、Mirix、ReasoningBank、BM25、embedding/Graph/MemoRAG | 从 recall QA 转向 environment feedback + action loop |
| [[10_Papers/evidence/memorybench-evidence|MemoryBench]] · 持续学习 | Benchmark / 评测基准 | MemoryBench；持续学习/长期记忆任务 | 现有 SOTA memory/continual learning 方法仍明显不足 | 多类 memory/continual learning 方法；benchmark 论文 | 把长期记忆与持续学习分开评测 |
| [[10_Papers/evidence/storagetexperience-evidence|From Storage to Experience]] · 三阶段综述 | 综述 / 综述 | 跨论文综述；无单一实验数据集 | Storage → Reflection → Experience 三阶段 | 概念综合，不做实验排名 | 把 OS 工程、认知科学与经验抽象统一成演化框架 |

### 2026-08

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/vikingmem-evidence|VikingMem]] · 事件实体 | 方法 / 效果 | LoCoMo；LongMemEval-S | LoCoMo LLM-J 88.83/90.12；LongMemEval 66.36/75.80；LoCoMo F1 54.98 | GPT-4o-mini LoCoMo：88.83 vs Mirix 78.66（+12.93%）；LongMemEval GPT-4o：75.80 vs Zep 70.40（+7.67%） | Mem0/Mem0g、Zep、RAG、Full-Context、Claude Native、OpenClaw、Mirix；加入 event/entity Memory Base |

### 2026-10

| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |
|---|---|---|---|---|---|
| [[10_Papers/evidence/tiermem-evidence|TierMem]] · 充分性路由 | 方法 / 效率 / Pareto | LoCoMo；LongMemEval；MemoryAgentBench 用于 router 训练 | LoCoMo accuracy 0.851 vs raw 0.873；input tokens -54.1%、latency -60.7% | summary-only、raw-only、router；Mem0、LightMem、O-mem、MemOS、MemR3、GAM | 从写入时固定粒度转向 query-time sufficiency routing + provenance |
| [[10_Papers/evidence/injecmem-evidence|InjecMEM]] · 单次注入 | 安全攻击 / 安全 | 19 域合成对话；WildChat；MemoryOS、MemGPT | MemoryOS 上 RSR 最高 35.4%、ASR 最高 76.6% | DPI、GCG、BadChain、Multi-GCG；LLM-Judge、ProtectAI、PromptGuard、Perplexity | 单次交互、retriever-agnostic 注入；memory drift 下仍有效 |
| [[10_Papers/evidence/poisononce-evidence|eTAMP]] · 环境投毒 | 安全攻击 / 安全 | WebArena、VisualWebArena（Shopping、Reddit、Classifieds；约 280 个跨站任务对） | 最高 ASR：GPT-5-mini 32.5%、GPT-5.2 23.4%、GPT-OSS-120B 19.5% | Baseline Injection、Frustration Exploitation、Authority Framing；Chaos Monkey | 环境观察注入；一次污染跨 session/跨站点长期利用 |

## 3. Baseline 是怎么变化的

| 阶段 | 常见数据集 | 常见 baseline | 变化 |
|---|---|---|---|
| 2025 H1 | LoCoMo、LongBench、∞-Bench、LongMemEval 开始出现 | Full-context、BM25/dense RAG、MemGPT、MemoryBank、ReadAgent | 从“塞上下文 / 简单检索”转向结构化记忆和事件分割 |
| 2025 H2 | LoCoMo 成为主战场；LongMemEval 快速普及 | A-Mem、Mem0、MemoryOS、Zep、LangMem | A-Mem 成为通用结构基线；Mem0 成为生产 pipeline 基线；MemoryOS 带入 OS/层次视角 |
| 2026 H1 | LoCoMo、LongMemEval、Long-MT-Bench+、PersonaMem、M3-Bench、GAIA | 前一代 memory systems + HippoRAG 2、MAGMA、MemGAS、MRAgent、TiMem | 基线从“有没有结构”升级为“多粒度、时间层次、active reconstruction”；开始同时报告 token/latency |
| 2026 H2 | 仍以 LoCoMo / LongMemEval 为主，但 BFCL、AppWorld、WebArena、MemoryArena 增多 | Mem0、MemoryOS、MAGMA、TiMem、GAM、Zep、full-context；安全论文加入攻击/防御基线 | 同时比较 accuracy–cost–action utility；benchmark 和攻击面被拆开；但跨论文协议仍不统一 |

**最明显的变化：**

- **从“RAG vs 结构记忆”变成“结构 × 更新策略 × 检索策略”。** 2025 年常见 baseline 还是 full-context、BM25、MemGPT、MemoryBank；到 2026 年，A-Mem、Mem0、MemoryOS 已成为新一代基础对照，MAGMA、MemGAS、MRAgent、TiMem 又成为更近的强基线。
- **从单一 accuracy 变成 accuracy + token + latency + storage + action success。** 最新系统论文很少只报一个分数；TierMem、Hippocampus、LightMem、RecMem 的核心贡献往往在 Pareto 前沿。
- **从“记忆有没有用”变成“什么时候不该用记忆”。** PersistBench、MEXTRA、MINJA、InjecMEM、eTAMP 把跨域污染、注入、隐私提取和遗忘纳入评测。
- **baseline 越来越强，但协议没有同步统一。** 同一个 A-Mem 在不同论文里可能被重实现；LoCoMo 的 judge、split、adversarial 是否纳入、检索预算都可能不同。

## 4. 数据集格局：哪些论文在用哪些数据

| 任务簇 | 主要数据集 / Benchmark | 代表论文 | 主要指标 |
|---|---|---|---|
| 长期对话记忆 | LoCoMo、LongMemEval-S/M、Long-MT-Bench+、MSC | SeCom、Mem0、MemoryOS、A-Mem、MAGMA、MemGAS、MRAgent、TiMem、RecMem、VikingMem | F1、LLM-Judge、BLEU、accuracy、token、latency |
| 人类 / 事件 / 长文 | LongBench、∞-Bench、NarrativeQA、Qasper、MuSiQue、2Wiki、Test of Time | EM-LLM、HippoRAG 2、M+、REMem、ARTEM、MemAgent、BEAM/LIGHT | F1、EM、recall、retention length |
| 行动 / 具身 | ALFWorld、SciWorld、PDDL、BabyAI | G-Memory、AgeMem、LightWM、MemoryArena | success rate、progress rate、action score |
| 工具 / Web / 研究 | BFCL-V3、AppWorld、GAIA、AssistantBench、WebArena、Mind2Web、SWE-Bench | ReMe、LTS、ReasoningBank、MemEvolve、MemoryArena | Pass@K、success rate、runtime、steps |
| 个性化 / 推荐 | LaMP、PersonaMem、PersonaBench、Amazon、Yelp、MovieTV | Evoking/RF-Mem、PersonaAgent、MemRec | accuracy、Recall@K、Hit@K、NDCG@K |
| 多模态 | M3-Bench-robot/web、VideoMME-long | M3-Agent | QA accuracy |
| 安全 / 遗忘 | MIMIC-III、eICU、WebShop、WildChat、WebArena、PersistBench | MEXTRA、MINJA、InjecMEM、eTAMP、PersistBench | ASR、ISR、CER、failure rate、beneficial memory use |

## 5. 重要反例：不要让“最好”掩盖条件

- **A-Mem** 在 temporal / multi-hop 上很强，但在 GPT-4o 的单跳和 adversarial 上输给 full-context。
- **MemGAS** 在 LongMemEval 上领先，但在 LoCoMo 上低于 HippoRAG 2（41.07 vs 45.62）。
- **RecMem** 在 LongMemEval 上超过 memory systems，但在 LoCoMo 上仍低于 full-context（81.10 vs 84.18）。
- **TierMem** 的 accuracy 比 raw-only 低 2.2 pp，价值在 54.1% token 和 60.7% latency 节省。
- **VikingMem** 的 90.12 是强结果，但 temporal weighting 在 fact-based benchmark 中默认关闭，不能据此推断所有时间敏感任务都更强。
- **LightWM** 的 0.910 是 ALFWorld 上的 procedure-centric 结果，不能外推到开放对话。
- **安全 ASR 高不等于 utility 高**：MINJA、InjecMEM、eTAMP 的“效果”是攻击成功率，不是任务正确率。

## 6. 对 MEM 的下一步

1. **建立三条独立榜单**：utility、efficiency/Pareto、safety；不要合成一个总分。
2. **统一最小比较单元**：至少固定 `benchmark + metric + backbone + judge + retrieval budget`。
3. **每个方法记录四个成本**：build token、per-query token、p50/p95 latency、storage。
4. **把 full-context 保留为常驻基线**：它能暴露结构化记忆在 single-hop、knowledge-update、adversarial 上的反例。
5. **优先补做同条件复现**：VikingMem、TiMem、RecMem、MRAgent、MAGMA 目前最值得在统一协议下复跑。

## 7. 证据入口

- 逐篇证据索引：[[10_Papers/evidence/INDEX|Per-Paper Evidence Index]]
- 实验设置与 baseline 家族：[EXPERIMENT_LANDSCAPE](../../maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md)
- 结构化数据：[baseline-timeline.json](../../data/agent-memory-2025/baseline-timeline.json)
- CSV：[baseline-timeline.csv](../../data/agent-memory-2025/baseline-timeline.csv)

