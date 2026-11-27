# MEM — Personal Paper Research System

`MEM` 是一个面向个人研究者的本地论文研究系统。目标不是“让 AI 替我读论文”，而是把文献发现、论文元数据与 PDF、主题/方法/争议/缺口、个人研究问题、Zotero/Obsidian 和可重复的 agent workflow 组织成可持续积累、可审计、可多机协作的研究基础设施。

## 当前状态

- **当前版本**：`v0.2.4 — 多机研究协作与证据运营`
- **当前研究分支**：`research/agent-memory-evidence`
- **稳定基线**：`main`
- **研究案例**：`Agent Memory 2025+`
- 收录论文：**52 篇**正式发表论文
- 概念关系：**86 条**
- **逐篇 evidence**：52/52 `evidence-checked`，0 `queued`，0 `verified`
- **时间化 baseline**：52 篇均已进入时间轴，包含数据集、主结果、对照和 baseline 变化
- **开题报告资料包**：已形成选题方法、国内写作规范、推荐研究设计和初稿模板，见 `开题报告/README.md`
- **Zotero**：52 条书目 + 52 条 importer notes，分为主库与三个增量 collection；未提交 Zotero 数据库或 PDF
- **Obsidian Vault**：`vault/`
- **CI 门禁**：`make check` 同时校验论文、关系、evidence、地图、Zotero 导出、baseline 时间轴、venue audit 和文档一致性

## 协作入口

- [docs/multi-machine-playbook.md](docs/multi-machine-playbook.md)：多机开工、分工、冲突处理和部署验收
- [STATUS.md](STATUS.md)：当前阶段、完成度、阻塞项和下一步
- [ROADMAP.md](ROADMAP.md)：从 v0.1 到个人论文研究系统的路线
- [CONTRIBUTING.md](CONTRIBUTING.md)：分支、提交、生成物和评审规则
- [DECISIONS.md](DECISIONS.md)：重要决策索引
- [CHANGELOG.md](CHANGELOG.md)：系统变更
- [RESEARCH_LOG.md](RESEARCH_LOG.md)：研究过程索引
- [RESEARCH_QUESTIONS.md](RESEARCH_QUESTIONS.md)：当前研究问题
- [PROVENANCE.md](PROVENANCE.md)：来源与证据规则
- [DATA_POLICY.md](DATA_POLICY.md)：数据边界
- [AI_USAGE.md](AI_USAGE.md)：AI 使用记录
- [READING_QUEUE.md](READING_QUEUE.md)：阅读队列
- [开题报告/README.md](开题报告/README.md)：硕士开题方向、写作规范和研究设计

## 先从哪里开始

### 第二台机器

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
git fetch origin
git switch research/agent-memory-evidence
make check
```

然后：

1. 用本机路径下的 `MEM/vault/` 打开 Obsidian。
2. 从 `vault/90_System/Dashboard.md` 进入。
3. 打开 `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md` 看时间化效果与 baseline。
4. 打开 `vault/40_Maps/Agent Memory 2025+.canvas` 看概念关系图。
5. 浏览器或编辑器打开 `maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md` 看实验设置全景。
6. 按 `docs/multi-machine-playbook.md` 完成本机的 Zotero 状态确认。

### 研究阅读

1. `vault/20_Topics/Agent Memory 2025+.md`：主题页
2. `vault/20_Topics/Mainline Overview.md`：A–G 主线总览
3. `vault/10_Papers/evidence/INDEX.md`：52 篇逐篇证据索引
4. `个人理解/路线分类.md`：带 2–6 字机制标签和 evidence 直达链接的个人路线总纲
5. `vault/30_Ideas/Agent Memory Research Questions.md`：研究问题页
6. `开题报告/README.md`：把研究问题收敛为硕士开题题目

## 核心产物

| 产物 | 路径 | 说明 |
|---|---|---|
| 论文主库 | `data/agent-memory-2025/papers.json` | 主数据源 |
| 概念关系 | `data/agent-memory-2025/edges.json` | 概念边，不等同于引文边 |
| 逐篇证据 | `vault/10_Papers/evidence/*.md` | 52 张页码级 evidence 卡 |
| 研究地图 | `maps/agent-memory-2025/` | Markdown / JSON / Canvas / CSV |
| 研究综合 | `maps/agent-memory-2025/SYNTHESIS.md` | 主线、争议、空白与阅读路径 |
| 实验设置 | `maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md` | 数据集与 baseline 全景 |
| baseline 时间轴源数据 | `data/agent-memory-2025/baseline-timeline.json` | 52 篇时间化效果数据 |
| baseline 时间轴笔记 | `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md` | 生成物，面向阅读 |
| Venue 审计 | `data/agent-memory-2025/VENUE_AUDIT.md` | 从主库生成的 venue 分层清单 |
| Zotero 导入 | `data/agent-memory-2025/*.bib` / `*.ris` | export-first |
| 个人路线总纲 | `个人理解/路线分类.md` | 手写综合，含链接和机制标签 |
| 硕士开题报告 | `开题报告/` | 选题、写作规范、推荐题目和初稿模板 |

## 目录结构

```text
MEM/
├── README.md
├── AGENTS.md
├── SYSTEM.md
├── ROADMAP.md
├── STATUS.md
├── CONTRIBUTING.md
├── DECISIONS.md
├── CHANGELOG.md
├── RESEARCH_LOG.md
├── RESEARCH_QUESTIONS.md
├── PROVENANCE.md
├── DATA_POLICY.md
├── AI_USAGE.md
├── READING_QUEUE.md
├── docs/
│   ├── multi-machine-playbook.md
│   ├── data-model.md
│   ├── evidence-model.md
│   ├── machine-setup.md
│   └── decisions/
├── research-log/
├── schemas/
├── config/
├── guides/
├── skills/
├── scripts/
├── data/
│   ├── agent-memory-2025/
│   └── zotero/
├── maps/
│   └── agent-memory-2025/
├── .github/
├── 个人理解/
├── 开题报告/
└── vault/
    ├── 00_Inbox/
    ├── 10_Papers/
    │   └── evidence/
    ├── 20_Topics/
    ├── 30_Ideas/
    ├── 40_Maps/
    ├── 90_System/
    └── Templates/
```

## 核心命令

```bash
# 完整校验；提交前必须通过
make check

# 只检查文档与数据/生成物是否一致
make docs-check

# 重新生成 baseline CSV 和 Obsidian 时间轴
make baseline-timeline

# 重新生成 venue audit
make venue-audit

# 校验论文与关系
make validate

# 生成论文笔记、主题页、Canvas 和研究地图
make build

# 导出 BibTeX / RIS
make export

# 安装方案 A 的外部工具（可选）
bash scripts/bootstrap_scheme_a.sh
```

## 多机协作规则（摘要）

- 开工前：`git pull --rebase && make check`
- 只修改源文件，不直接手工修改生成物。
- 不同论文的 evidence 文件可并行；`papers.json`、`edges.json`、`baseline-timeline.json` 和顶层文档由一个人统一合并。
- 生成物冲突时，先解决源数据冲突，再重新运行生成脚本。
- 提交前：`make check` + `git diff --check` + `git status -sb`
- 详细规则见 `docs/multi-machine-playbook.md` 与 `CONTRIBUTING.md`。

## 重要说明

- 当前地图中的边是**概念关系**，不等于逐条引文关系。
- 主地图只收录正式发表论文；ICLR、COLM、MLSys、ACL Findings 和 CCF-B 均显式标注。
- 仅 arXiv、尚未确认正式发表的系统不进入主地图，另见 `data/agent-memory-2025/preprints-excluded.md`。
- 论文笔记中的摘要来自 OpenReview / ACL Anthology / AAAI / PMLR / PVLDB 等官方记录；关键实验数字应回 PDF 与页码复核。
- 52 篇目前是 `evidence-checked`，不是 `verified`。进入论文写作或对外 claim 前仍需人工抽查关键数字。
