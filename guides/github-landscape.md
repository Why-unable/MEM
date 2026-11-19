# GitHub Landscape：Autoresearch 与个人学术研究地图

> 检索时间：2026-11-19
> 目标：找到能支撑个人研究者快速建立 academic research map 的 GitHub 项目，形态包括 Skill、工具包、MCP、md 指南和端到端 agent。

## 0. 结论

GitHub 上没有特别成熟、开箱即用的“个人学术研究地图”大项目。最贴近需求的是 2026 年出现的一批 Codex/Claude Skill 和小型工具。`autoresearch` 本身多数指“自动实验迭代”，并不等于“自动搭建文献地图”。

推荐的组合是：

```text
Scholar Literature Maps
  → 快速把陌生主题变成 20–30 篇分组文献
Research Nexus
  → 把论文、主题、想法、日志沉淀为本地 Obsidian 图
OpenAlex MCP / Local Citation Network
  → 补引文网络、作者、趋势
Zotero
  → 权威书目与 PDF 附件
```

## 1. 直接做 research map

| 项目 | 形态 | 能做什么 | 注意 |
|---|---|---|---|
| [Research Nexus](https://github.com/haowen-xiong/research-nexus) | Codex Skill + Python CLI | 在本地 Obsidian Vault 中维护 paper/topic/idea/journal 节点；支持 YAML、wikilink、图查询、审计、备份 | 最贴近“个人研究者 + Codex + 本地知识库”；很新，未见 LICENSE；不负责自动发现论文 |
| [Academic Research Graph Skill](https://github.com/watericetangcw/academic-research-graph) | Agent Skill | 从论文、概念、benchmark、repo 生成交互式节点-边图；分析脉络、争议、benchmark 使用和代码实现 | 输出 `graph.json` 和 `index.html`；MIT；主要面向 ChatGPT Skill / DeepSeek Harness |
| [Scholar Literature Maps](https://github.com/Zhgb/scholar-literature-maps) | Codex Skill / md 指南 | 中文问题 → 英文检索；生成 20–30 篇分组文献地图；种子论文追踪；研究者发现 | 非常适合 Codex；输出是分组文献，不是视觉图；未见 LICENSE |
| [Mogua 摸瓜](https://github.com/Jacksonzhang320/mogua) | Python CLI + Agent Skill | 从 DOI/标题出发，用 OpenAlex 抓引文网络，生成单文件交互式 HTML | 类似本地版 Connected Papers；MIT；项目很新 |
| [LitPilot](https://github.com/JCL988/LitPilot) | Python 工具包 | 把已有 PDF 映射到自己的文献综述结构，输出 Markdown 笔记、Excel tracker、跨论文综合 | 不负责发现论文；适合系统综述和论文写作；MIT |
| [Scientra Copilot](https://github.com/Fxsin/Scientra-Copilot) | 本地知识生态系统 | PDF 资产化、跨论文发现、gap extraction、research map、本地可追溯 | 偏重；需要 GROBID、前后端和模型配置；MIT |
| [Research Library Mapper](https://github.com/Grovesimus/Research-Library-Mapper) | Python 工具包 | 用 SPECTER2 + UMAP + HDBSCAN 把个人 PDF 库投影成 2D/3D 语义地图 | 适合“我已有大量 PDF”的场景；依赖较重；MIT |

## 2. 数据底座与成熟工具

| 项目 | 价值 | 注意 |
|---|---|---|
| [Local Citation Network](https://github.com/LocalCitationNetwork/LocalCitationNetwork.github.io) | 开源引文网络可视化；支持 OpenAlex / Semantic Scholar / Crossref / Zotero Cita | 无 LLM；手动探索；GPL-3 |
| [OpenAlex Research MCP](https://github.com/oksure/openalex-research-mcp) | 31 个工具：检索、引文网络、作者、机构、趋势、期刊/会议 preset | 研究地图的数据底座，不直接生成地图；MIT |
| [Zotero](https://www.zotero.org/) | 权威书目库、PDF 附件、引用导出 | 不是 GitHub 项目，但应作为 MEM 的书目事实源 |

## 3. Autoresearch 与全流程 AI scientist

| 项目 | 定位 | 与“研究地图”的关系 |
|---|---|---|
| [Karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 自动 ML 实验迭代 | 不是文献地图 |
| [awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | autoresearch 项目索引 | 用于继续挖工具，不是地图本身 |
| [AutoSci](https://github.com/skyllwt/AutoSci) | 记忆驱动的全生命周期科研 agent；知识 wiki + 交互图；Codex preview | 最接近“autoresearch + 研究记忆 + 图谱”的项目；偏重，内部 beta |
| [EvoMap/AutoResearch](https://github.com/EvoMap/AutoResearch) | idea → 实验 → 证据包 | 偏 AI/ML 自动实验，不是文献地图 |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 23 阶段 idea → paper | 自动写论文流水线，不是地图 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 自动科学发现 | 适合理解 AI scientist 谱系，不适合作为个人文献地图 |

## 4. Skills、md 指南与索引

| 项目 | 用途 |
|---|---|
| [Awesome Academic Research Skills](https://github.com/Jason-Mar1/awesome-academic-research-skills) | 按研究阶段组织的学术 Agent Skills 索引，双语 |
| [AI Research Skills](https://github.com/WenyuChiou/ai-research-skills) | 17 个研究生命周期 Skill：文献、设计、项目记忆、写作、协作 |
| [obsidian-research-guide](https://github.com/leilin1995/obsidian-research-guide) | 中文科研 Obsidian 指南：PARA/Zettelkasten、Zotero、Dataview、知识地图 |
| [Research Agent Skill Map](https://github.com/YanshengLuo/research-agent-skill-map) | 面向生物医学、科学计算、学术写作的 Skill 选型决策指南 |
| [SciAgentsDiscovery](https://github.com/lamm-mit/SciAgentsDiscovery) | 多 agent + 图推理 + 科学发现的研究代码，偏论文复现 |

## 5. 对 MEM 的取舍

### 采纳

- **Scholar Literature Maps**：用于“从问题到候选论文”的检索流程。
- **Research Nexus**：用于 paper/topic/idea/journal 的本地节点和关系。
- **OpenAlex MCP / Local Citation Network**：作为引文和作者数据底座。
- **Zotero + Obsidian**：书目事实源 + 阅读/写作界面。

### 暂不采纳为主线

- **AutoResearchClaw / EvoMap AutoResearch**：偏自动实验/自动写论文，不是个人研究地图。
- **AutoSci**：保留为 v0.4 之后的“研究记忆 + 自动研究”候选，不放入当前轻量方案。
- **仅 arXiv 的 memory 系统**：不进入主地图，避免把预印本误当正式发表。

## 6. 推荐组合

### 轻量个人版

```text
Scholar Literature Maps → papers.json → Research Nexus/Obsidian
```

### 可视化版

```text
Academic Research Graph 或 Mogua → HTML 图谱
```

### 长期积累版

```text
Zotero（书目）
  + MEM 论文笔记（理解）
  + Obsidian Canvas（关系）
  + OpenAlex（引文）
```

### 全流程版

```text
AutoSci / EvoMap AutoResearch
  → 在 MEM 稳定后再评估
```
