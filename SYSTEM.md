# MEM Operating System

## 1. 系统目标

把一个研究主题从“零散搜索结果”变成可持续维护的研究资产：

```text
问题
→ 文献发现
→ 元数据核验
→ 论文笔记
→ 主题分类
→ 关系图
→ 争议/缺口
→ 研究想法
→ 实验或写作
```

## 2. 四层结构

### L1：Paper

一篇论文一个 Markdown 笔记。至少包含：

- 标题、作者、年份、venue
- DOI / arXiv / OpenReview / PDF
- 摘要
- 一句话定位
- 方法、实验、局限
- 与哪些论文/主题相连

### L2：Topic

一个主题页，回答：

- 这个领域有哪些主要流派？
- 哪些论文是奠基、扩展、对照或应用？
- 共识、争议和空白是什么？
- 下一步应该读什么？

### L3：Idea

个人想法页，保留：

- 原始想法
- 研究问题
- 假设
- 可能的方法
- 需要的证据
- 风险与反例

### L4：Map

地图不是装饰图，而是研究决策界面。地图必须支持：

- 按主题筛选
- 按 venue 层级筛选
- 区分核心论文与支撑论文
- 从任一节点继续扩展
- 记录“为什么连这条边”

## 3. 证据与质量门槛

### 收录门槛

- 2025-01-01 之后正式发表，优先 CCF-A。
- ICLR、COLM、MLSys 等顶级但非 CCF-A 的 venue 可收录，但必须标注 `venue_tier`。
- Findings / Workshop 论文默认不进入核心层；如收录，必须明确标注。
- 仅 arXiv 的工作进入 `preprints-excluded.md`，不进入主地图。
- 每篇论文必须有可追溯的正式记录或官方 PDF。

### 事实门槛

- 不凭模型记忆写 DOI、作者、年份、venue。
- 会议/期刊信息以 OpenReview、ACL Anthology、AAAI、PMLR、Crossref、OpenAlex 等来源交叉核验。
- 摘要可以引用官方页面；关键实验数字必须回 PDF 复核。
- 关系边如果只是概念关联，必须标明 `conceptual`，不能伪装成引文事实。

### 去重规则

优先使用 DOI、arXiv ID、OpenReview ID、DBLP key；没有标识符时再用规范化标题 + 作者 + 年份。

## 4. 推荐工作流

### A. 新主题扫描

1. 用 `skills/mem-literature-map/SKILL.md` 锁定范围。
2. 用 Scholar Literature Maps 生成 20–30 篇候选。
3. 用 OpenReview / ACL Anthology / Crossref / OpenAlex 核验。
4. 写入 `data/<topic>/papers.json`。
5. 写入 `data/<topic>/edges.json`。
6. 运行 `scripts/validate_mem.py`。
7. 运行 `scripts/build_research_map.py`。
8. 在 Obsidian 中阅读、补笔记、改边。

### B. 从一篇种子论文扩展

1. 读取种子论文的 references / citations。
2. 选 5–8 篇高相关候选。
3. 优先加入综述、奠基、反驳、复现、最新扩展。
4. 更新 `edges.json`，注明关系类型。
5. 重新构建地图。

### C. 与 Zotero 同步

1. 把目标论文加入 Zotero collection。
2. 导出 CSL JSON 到 `data/zotero/`。
3. 用 `scripts/import_zotero_csl.py` 生成中间 CSV。
4. 人工确认后合并到 `papers.json`。
5. 论文笔记中保留 Zotero item key / collection。

## 5. 命名约定

- 论文 ID：短英文 slug，例如 `amem`、`gmemory`、`longmemeval`。
- 主题目录：`data/<topic-slug>/`。
- 地图目录：`maps/<topic-slug>/`。
- Obsidian 笔记：`vault/10_Papers/<paper-id>.md`。
- 主题页：`vault/20_Topics/<Topic Name>.md`。
- Canvas：`vault/40_Maps/<Topic Name>.canvas`。

## 6. 角色分工

- **Codex**：检索、抽取、结构化、生成地图、维护脚本。
- **Scholar Literature Maps**：把研究问题变成英文优先、范围锁定的文献候选。
- **Research Nexus**：维护 Obsidian 中的 paper/topic/idea/journal 节点与关系。
- **OpenAlex MCP / Local Citation Network**：补引文、作者、趋势和引文网络。
- **Zotero**：权威书目库、PDF 附件、引用导出。
- **Obsidian**：阅读、连接、写作和个人知识图谱。
- **人**：决定研究问题、判断相关性、确认关键结论。

## 7. 多机协作层

多机协作依赖以下文件和机制：

- `STATUS.md`：当前状态和下一步
- `CONTRIBUTING.md`：分支、同步、提交、PR 规则
- `DECISIONS.md` + `docs/decisions/`：重要决策
- `CHANGELOG.md`：系统变更
- `RESEARCH_LOG.md` + `research-log/`：研究过程
- `RESEARCH_QUESTIONS.md`：研究问题和假设
- `PROVENANCE.md`：来源与证据规则
- `DATA_POLICY.md`：哪些数据可以进入 Git
- `AI_USAGE.md`：AI 参与与人工核验
- `schemas/`：机器可读数据契约
- `.github/workflows/validate.yml`：CI 校验

## 8. 证据与时间化比较层

MEM 目前有三类互补证据：

1. **Paper evidence**：`vault/10_Papers/evidence/<paper-id>-evidence.md`，一篇论文一个文件。
2. **Topic synthesis**：`maps/<topic>/SYNTHESIS.md` 与主线综合页。
3. **Baseline timeline**：`data/<topic>/baseline-timeline.json`，跨论文整理时间、数据集、主结果、baseline 变化和 2–6 字机制标签。

Baseline timeline 不是单一排行榜。严格比较需要固定：

```text
benchmark + metric + backbone + judge + retrieval budget
```

生成物：

```text
data/<topic>/baseline-timeline.csv
vault/40_Maps/<Topic> Baseline Timeline.md
```

## 9. 多机协作门禁

每台机器开工前运行：

```bash
git pull --rebase
make check
```

`make check` 必须包含文档一致性检查：

```bash
make docs-check
```

协作细节见 `docs/multi-machine-playbook.md`、`CONTRIBUTING.md` 和 `docs/machine-setup.md`。

## 10. 当前限制

- 52 篇论文的边是人工概念边，尚未逐篇做引文级核验。
- 52 张 evidence 是 `evidence-checked`，不是人工 `verified`。
- `papers.json` / `edges.json` 仍是单文件 JSON，多机同时编辑有冲突风险。
- 基线时间轴的 `delta_pct` 只用于同月浏览排序，不能作为跨 benchmark 的科学总分。
- 2026 年部分会议论文的正式 proceedings 页面可能仍在更新；使用前应再次检查官方页面。
- Zotero 已导入 52 条书目，但尚未把本机 item key 回填到 `papers.json`，也尚未建立自动同步。
- 自动更新（每日/每周）尚未启用，避免在未确认来源时污染主库。
