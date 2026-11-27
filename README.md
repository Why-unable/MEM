# MEM — Personal Paper Research System

`MEM` 是一个面向个人研究者的本地论文研究系统。目标不是“让 AI 替我读论文”，而是把：

- 文献发现
- 论文元数据与 PDF
- 主题/方法/争议/缺口
- 个人想法与研究问题
- Zotero 与 Obsidian
- 可重复的 agent workflow

组织成一个可以持续积累、可审计、可扩展的研究基础设施。

## 当前状态

- **方案 A 已布置**：Scholar Literature Maps + Research Nexus 思路 + OpenAlex 数据底座。
- **Obsidian 已绑定独立 vault**：`MEM/vault`，Dashboard 已打开。
- **Zotero 导入已完成**：52 篇书目已导入；使用 4 个 collection（主库 + 三个 staging batch）；未直接修改 `zotero.sqlite`。
- **初始研究案例已完成**：`Agent Memory 2025+`
- 收录论文：**52 篇**
- 概念关系：**86 条**
- Obsidian Vault：`vault/`
- 研究地图：`maps/agent-memory-2025/`
- 论文元数据：`data/agent-memory-2025/papers.json`
- Zotero 导入：`data/agent-memory-2025/agent-memory-2025.bib`、`agent-memory-2025-batch2.bib`、`agent-memory-2025-batch3.bib`、`agent-memory-2025-batch4.bib`
- 研究综合：`maps/agent-memory-2025/SYNTHESIS.md`
- 逐篇证据索引：`vault/10_Papers/evidence/INDEX.md`
- 初始研究问题：`vault/30_Ideas/Agent Memory Research Questions.md`

## 协作入口

- [STATUS.md](STATUS.md)：当前状态和下一步
- [CONTRIBUTING.md](CONTRIBUTING.md)：多机协作规则
- [DECISIONS.md](DECISIONS.md)：重要决策索引
- [CHANGELOG.md](CHANGELOG.md)：系统变更
- [RESEARCH_LOG.md](RESEARCH_LOG.md)：研究过程索引
- [RESEARCH_QUESTIONS.md](RESEARCH_QUESTIONS.md)：当前研究问题
- [PROVENANCE.md](PROVENANCE.md)：来源与证据规则
- [DATA_POLICY.md](DATA_POLICY.md)：数据边界
- [AI_USAGE.md](AI_USAGE.md)：AI 使用记录
- [READING_QUEUE.md](READING_QUEUE.md)：阅读队列

## 先从哪里开始

1. 用 Obsidian 打开 `MEM/vault/`。
2. 打开 `vault/20_Topics/Agent Memory 2025+.md`。
3. 打开 `vault/40_Maps/Agent Memory 2025+.canvas` 看关系图。
4. 从 `vault/10_Papers/amem.md` 开始读第一篇论文笔记。
5. 用 `vault/90_System/Dashboard.md` 作为日常入口。

## 目录结构

```text
MEM/
├── README.md                  # 本文件
├── AGENTS.md                  # 未来 Codex 工作指令
├── SYSTEM.md                  # 系统原则、质量门槛、工作流
├── ROADMAP.md                 # 从 v0.1 到个人研究系统的路线
├── STATUS.md                  # 当前状态与下一步
├── CONTRIBUTING.md            # 多机协作规则
├── DECISIONS.md               # 决策索引
├── CHANGELOG.md               # 系统变更
├── RESEARCH_LOG.md            # 研究日志索引
├── RESEARCH_QUESTIONS.md      # 研究问题登记
├── PROVENANCE.md              # 来源与证据规范
├── DATA_POLICY.md             # 数据边界与 Git policy
├── AI_USAGE.md                # AI 使用与人工核验
├── READING_QUEUE.md           # 阅读队列
├── docs/
│   ├── data-model.md          # 数据契约
│   ├── machine-setup.md       # 多机初始化
│   └── decisions/             # ADR
├── research-log/              # 按日期/机器拆分的研究日志
├── schemas/                   # paper / graph JSON schema
├── config/
│   ├── mem.config.example.json # 可提交模板
│   ├── mem.config.json        # 本机配置（忽略）
│   └── venues.yaml            # venue 分层与 CCF-A allowlist
├── guides/
│   ├── github-landscape.md    # 已收集的 GitHub 项目与建议
│   ├── scheme-a-setup.md      # 方案 A 的安装与使用说明
│   └── zotero-obsidian.md     # Zotero/Obsidian 接入说明
├── skills/                    # 本系统自己的 Codex Skills
├── scripts/                   # 构建、导入、校验脚本
├── data/
│   ├── agent-memory-2025/     # 第一个研究案例的原始元数据
│   └── zotero/                # Zotero 导出/交换目录
├── maps/
│   └── agent-memory-2025/     # research-map.md / json / canvas / csv
├── .github/                   # CI、PR、Issue 模板
└── vault/                     # Obsidian Vault
    ├── 00_Inbox/
    ├── 10_Papers/
    ├── 20_Topics/
    ├── 30_Ideas/
    ├── 40_Maps/
    ├── 90_System/
    └── Templates/
```

## 核心命令

```bash
# 一键检查
make check

# 校验论文库
python3 scripts/validate_mem.py \
  --papers data/agent-memory-2025/papers.json \
  --edges data/agent-memory-2025/edges.json

# 重新生成 Obsidian 笔记、Canvas 和 research map
python3 scripts/build_research_map.py \
  --papers data/agent-memory-2025/papers.json \
  --edges data/agent-memory-2025/edges.json \
  --vault vault \
  --out maps/agent-memory-2025 \
  --topic 'Agent Memory 2025+'

# 安装方案 A 的外部工具（可选）
bash scripts/bootstrap_scheme_a.sh
```

## 重要说明

- 当前地图中的边是**概念关系**，不等于逐条引文关系。
- 主地图优先收录正式发表的论文；ICLR、COLM、MLSys 等顶级但非 CCF-A 的 venue 已单独标注。
- 仅 arXiv、尚未确认正式发表的系统（如 MemOS、MIRIX、Zep 等）不进入主地图，另见 `data/agent-memory-2025/preprints-excluded.md`。
- 论文笔记中的摘要来自 OpenReview / ACL Anthology / AAAI 记录，后续应以 PDF 原文复核关键数字与结论。
