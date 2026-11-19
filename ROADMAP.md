# MEM Roadmap

## v0.1 — 可运行的个人论文研究系统

- [x] 建立 MEM 目录与原则
- [x] 布置方案 A：文献地图 + Obsidian 知识库 + 数据底座
- [x] 建立论文元数据 schema
- [x] 建立概念地图 schema
- [x] 构建 `Agent Memory 2025+` 初始地图
- [x] 生成 36 篇论文笔记
- [x] 生成 Obsidian Canvas
- [x] 生成 BibTeX / RIS / CSV
- [x] 建立校验与构建脚本

## v0.2 — 多机协作与 Zotero/Obsidian 接入（当前）

- [x] 绑定独立 Obsidian Vault 路径：`MEM/vault`
- [ ] 绑定 Zotero collection 或本地 API
- [ ] 把 36 篇论文导入 Zotero collection（导入文件已生成，等待 Zotero 确认）
- [ ] 把 PDF 附件链接回论文笔记
- [ ] 增加 Zotero item key 字段
- [ ] 建立“Zotero → MEM → Obsidian”的单向同步

### 多机协作补丁

- [x] `STATUS.md`
- [x] `CONTRIBUTING.md`
- [x] `DECISIONS.md` + ADR
- [x] `CHANGELOG.md`
- [x] `RESEARCH_LOG.md`
- [x] `RESEARCH_QUESTIONS.md`
- [x] `PROVENANCE.md`
- [x] `DATA_POLICY.md`
- [x] `AI_USAGE.md`
- [x] `READING_QUEUE.md`
- [x] JSON schemas
- [x] CI / PR / issue templates
- [x] Makefile / machine setup

## v0.3 — 自动更新与增量地图

- [ ] 每周检索新论文
- [ ] 自动检测新 venue / 新版本
- [ ] 自动生成候选论文而不是直接写入主库
- [ ] 人审后合并
- [ ] 自动生成 weekly research digest

## v0.4 — 研究问题与想法层

- [ ] 从地图缺口生成 research questions
- [ ] 建立 hypothesis / experiment / evidence 节点
- [ ] 把 ideas 连接到 papers 和 gaps
- [ ] 生成个人研究 proposal 草稿

## v1.0 — 个人论文研究系统

- [ ] 多主题地图
- [ ] 跨主题桥接
- [ ] 个人研究轨迹
- [ ] 与合作者共享的子地图
- [ ] 可审计的来源与更新记录
