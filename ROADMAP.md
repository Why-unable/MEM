# MEM Roadmap

> 更新时间：2026-11-27
> 当前版本：`v0.2.4 — 多机研究协作与证据运营`
> 当前研究分支：`research/agent-memory-evidence`

## v0.1 — 可运行的个人论文研究系统（已完成）

- [x] 建立 MEM 目录与原则
- [x] 布置方案 A：文献地图 + Obsidian Vault + 数据底座
- [x] 建立论文元数据 schema
- [x] 建立概念地图 schema
- [x] 构建 `Agent Memory 2025+` 初始地图
- [x] 生成论文笔记与 Obsidian Canvas
- [x] 生成 BibTeX / RIS / CSV
- [x] 建立校验与构建脚本

## v0.2 — 多机协作与 Zotero/Obsidian 接入（已完成基础层）

- [x] 绑定独立 Obsidian Vault：`MEM/vault`
- [x] 建立多机协作文件：STATUS、CONTRIBUTING、DECISIONS、CHANGELOG、RESEARCH_LOG
- [x] 建立 PROVENANCE、DATA_POLICY、AI_USAGE、READING_QUEUE
- [x] 建立 JSON schemas、Makefile、GitHub Actions、PR / Issue 模板
- [x] Zotero export-first 流程与 52 条书目导入
- [x] 建立 4 个 Zotero collection：主库 + 三个 staging batch
- [ ] PDF 附件链接回论文笔记
- [ ] 回填 Zotero item key
- [ ] 建立 Zotero → MEM → Obsidian 的单向同步

### 多机协作补丁

- [x] `docs/machine-setup.md`：新机器初始化
- [x] `docs/multi-machine-playbook.md`：并行分工、冲突处理、部署验收
- [x] `make docs-check`：检查 README / STATUS / ROADMAP / 数据 / 生成物一致性
- [x] CI 覆盖研究分支与 Pull Request
- [ ] per-paper 分片数据迁移
- [ ] 添加机器级 lock / ownership 文件

## v0.2.4 — 多机研究协作与证据运营（当前）

### 已完成

- [x] 主库扩展到 52 篇正式发表论文
- [x] 概念关系扩展到 86 条
- [x] 52/52 论文有独立 evidence 文件，状态为 `evidence-checked`
- [x] A–G 七条主线均有综合页
- [x] `个人理解/路线分类.md` 覆盖 52/52，并带 evidence 直达链接与 2–6 字机制标签
- [x] `baseline-timeline.json` / CSV / Obsidian 笔记：按发表时间组织效果、数据集和 baseline 变化
- [x] `VENUE_AUDIT.md` 从 `papers.json` 自动生成
- [x] `make check` 覆盖 schema、论文图、地图、Zotero 导出、evidence、时间轴、venue audit、文档一致性
- [x] 新增 `开题报告/`：选题方法、写作规范、推荐题目、研究设计与初稿模板
- [x] README / STATUS / ROADMAP / Dashboard / 自动化脚本同步到当前状态

### 待完成

- [ ] 建立 `CLAIMS.md`：claim–evidence–confidence 证据矩阵
- [ ] 对 52 篇 evidence 做 `verified` 人工抽查
- [ ] 建立 RQ1 的统一实验协议：`benchmark + metric + backbone + judge + retrieval budget`
- [ ] 根据学校模板完成开题报告初稿和 pilot 实验
- [ ] 把 `papers.json` / `edges.json` 迁移为 per-paper / per-edge 分片
- [ ] 回填 16 篇新增论文到 `EXPERIMENT_LANDSCAPE.md` 的完整矩阵
- [ ] 统一 utility / efficiency / safety 三条榜单的评测口径

## v0.3 — 自动增量更新与候选论文池

- [ ] 每周检索新论文
- [ ] 自动检测新 venue / 新版本 / 正式发表状态
- [ ] 生成候选论文池，而不是直接写入主库
- [ ] 人工审核后合并
- [ ] 自动生成 weekly research digest
- [ ] 增加破图、重复、断链和引用一致性检查

## v0.4 — 研究问题、假设与实验层

- [ ] 从地图缺口生成 research questions
- [ ] 建立 hypothesis / experiment / evidence 节点
- [ ] 把 ideas 连接到 papers、gaps 和 claims
- [ ] 生成个人研究 proposal 草稿
- [ ] 建立最小实验协议和结果登记模板

## v1.0 — 个人论文研究系统

- [ ] 多主题地图
- [ ] 跨主题桥接
- [ ] 个人研究轨迹
- [ ] 与合作者共享的子地图
- [ ] 可审计的来源、证据、决策和更新记录
- [ ] 可从 claim 回溯到论文页码、数据集、baseline 和实验记录
