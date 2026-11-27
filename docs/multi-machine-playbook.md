# MEM Multi-Machine Research Playbook

> 当前研究分支：`research/agent-memory-evidence`
> 稳定基线分支：`main`
> 适用范围：个人多机协作，以及少量协作者并行补论文、证据、综合和时间轴。

## 0. 三条铁律

1. **先同步，再修改。** 开始工作前必须 `git pull --rebase` 并跑 `make check`。
2. **source of truth 与生成物分离。** 只改源数据或手写分析；论文笔记、Canvas、BibTeX/RIS、baseline CSV/Markdown 等由脚本生成。
3. **同一高风险文件只由一个人修改。** `papers.json`、`edges.json`、`baseline-timeline.json`、README/ROADMAP/STATUS/CHANGELOG 等单文件是冲突热点。

## 1. 首次部署

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
git fetch origin
git switch research/agent-memory-evidence
python3 --version   # 3.10+
make check
```

可选安装外部工具：

```bash
bash scripts/bootstrap_scheme_a.sh
```

然后完成本机环境：

- 用该机器上的 `MEM/vault` 打开 Obsidian。
- 在 Zotero 中确认 `agent-memory-2025` 及其三个 batch collection。
- 不要把 `vault/.obsidian/workspace*.json`、`zotero.sqlite`、PDF 或 `.env` 跨机器复制进 Git。
- 详细步骤见 `docs/machine-setup.md`。

## 2. 每次开工

```bash
git branch --show-current
git status -sb
git pull --rebase
make check
```

先读：

1. `STATUS.md`：当前阶段、阻塞项和下一步。
2. `CONTRIBUTING.md`：提交与数据规则。
3. `RESEARCH_QUESTIONS.md`：当前 RQ 优先级。
4. `RESEARCH_LOG.md`：最近一轮研究过程。

## 3. Source of truth 与生成物

| 研究对象 | 源文件 | 生成物 | 冲突风险 |
|---|---|---|---|
| 论文元数据 | `data/<topic>/papers.json` | 论文笔记、CSV、BibTeX/RIS、地图、venue audit | 高 |
| 概念关系 | `data/<topic>/edges.json` | research map、Canvas、主题关系 | 高 |
| 逐篇证据 | `vault/10_Papers/evidence/<id>-evidence.md` | `INDEX.md` | 低；适合并行 |
| 时间化 baseline | `data/<topic>/baseline-timeline.json` | `baseline-timeline.csv`、Obsidian timeline note | 高 |
| Venue 审计 | `data/<topic>/papers.json` | `VENUE_AUDIT.md` | 中 |
| 研究综合 | 手写 `maps/<topic>/SYNTHESIS.md` | `vault/40_Maps/... Synthesis.md` | 中 |
| 个人路线总纲 | `个人理解/路线分类.md` | — | 高；需人工合并 |
| 硕士开题材料 | `开题报告/*.md` | — | 高；由一人统稿 |
| 决策 | `docs/decisions/*.md` | `DECISIONS.md` | 低；一 ADR 一文件 |
| 研究过程 | `research-log/*.md` | `RESEARCH_LOG.md` | 低；一任务一文件 |

## 4. 并行协作规则

### 适合并行

- 不同论文的 `evidence/<id>-evidence.md`。
- 不同日期的 `research-log/*.md`。
- 不同主题的独立目录。
- 只在本地使用的 Obsidian workspace、Zotero 数据库和 PDF。

### 必须串行或由 integrator 合并

- `papers.json`、`edges.json`、`baseline-timeline.json`。
- `README.md`、`ROADMAP.md`、`STATUS.md`、`CHANGELOG.md`。
- `个人理解/路线分类.md`。
- `开题报告/*.md`。
- `vault/40_Maps/*.canvas` 和所有生成型 Markdown。
- `Makefile`、CI workflow、schema。

### 发生冲突时

1. 先解决**源文件**冲突。
2. 生成文件冲突时，不手工逐行合并；取任意一版后重新运行脚本。
3. 运行 `make check` 和 `make docs-check`。
4. 检查 `git diff` 只包含预期变化。
5. 由一个人统一提交并推送。

## 5. 新增一篇论文

1. 只从正式 proceedings / DOI 记录进入主库。
2. 更新 `papers.json` 和必要的 `edges.json`。
3. 创建或更新 `vault/10_Papers/evidence/<id>-evidence.md`。
4. 运行 `make check` 生成论文笔记、地图、BibTeX/RIS、evidence index。
5. 更新 `baseline-timeline.json`，运行 `python3 scripts/build_baseline_timeline.py`。
6. 更新 `个人理解/路线分类.md` 中的论文链接、标签和年月。
7. 更新 `CHANGELOG.md`、`RESEARCH_LOG.md`、`AI_USAGE.md`。
8. 再次运行 `make check` 和 `make docs-check`。

## 6. 更新 baseline 时间轴

不要直接编辑以下生成文件：

- `data/<topic>/baseline-timeline.csv`
- `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md`

正确流程：

```bash
# 1. 编辑 source JSON，补 tagline 和核对后的结果
$EDITOR data/agent-memory-2025/baseline-timeline.json

# 2. 重新生成 CSV 和 Obsidian 笔记
make baseline-timeline

# 3. 检查引用、行数和文档一致性
make docs-check
```

## 7. 提交与推送

```bash
make check
git diff --check
git status -sb
git add -A
git commit -m "research: add <topic> evidence"
git push origin <current-branch>
```

提交类型：

- `data:` 论文/关系/筛选
- `research:` 证据、综合、时间轴
- `docs:` README、ROADMAP、协作规则
- `fix:` 校验、生成器、文档错误
- `chore:` 生成物重新构建

## 8. 分支与发布

- `main`：稳定、可复现、已通过 CI。
- `research/*`：研究推进和批量证据。
- `data/*`：论文增补和元数据修复。
- `docs/*`：文档与协作流程。
- `fix/*`：脚本、校验和构建修复。

当前研究尚未合并到 `main` 时，协作机器应显式切换 `research/agent-memory-evidence`，不要默认从 `main` 开始。

## 9. 部署验收清单

- [ ] `make check` 通过
- [ ] `make docs-check` 通过
- [ ] `papers.json` 与 `baseline-timeline.json` 的论文 ID 一致
- [ ] 52 篇 evidence 文件均存在且状态正确
- [ ] Obsidian 入口和 baseline timeline 链接可打开
- [ ] Zotero 条目数与主库一致，未提交数据库
- [ ] `git status` 只有预期文件
- [ ] 当前分支与远端同步

## 10. 已知协作风险

- `papers.json` / `edges.json` 仍是单文件 JSON，多人同时新增时容易冲突；后续迁移到 per-paper 分片文件。
- `个人理解/路线分类.md` 包含大量重复引用，建议由一个人统一加标签/链接。
- 不同机器的 Zotero item key 尚未回填到论文主库。
- 52 篇 evidence 是 `evidence-checked`，不是 `verified`；关键数字仍需人工抽查。
