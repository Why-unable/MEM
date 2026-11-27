# Changelog

All notable changes to MEM are documented here.

The format is based on Keep a Changelog and uses semantic versioning for the research system.

## [Unreleased]

### Added

- 2026-11-27：新增 `开题报告/` 资料包：当前首选方向 B（VikingMem 后续：记忆冲突消解、可信更新与回滚），并保留方向 A 备选、写作规范、研究设计和初稿模板。
- 2026-11-27：完成多机部署与文档一致性更新：新增 multi-machine playbook、`check_docs.py`、`build_venue_audit.py`，更新 README/ROADMAP/STATUS/CONTRIBUTING/SYSTEM/AGENTS 与 CI；`make check` 现覆盖 timeline、venue audit 和文档一致性。
- 2026-11-27：新增 `Agent Memory 2025+ Baseline Timeline`，按正式发表月份整理 52 篇论文的主结果、数据集、对比基线与同月效果顺序；新增 `baseline-timeline.json`、CSV 和可重复生成脚本。
- 2026-11-27：新增 VikingMem（PVLDB 2026，CCF-A），主库达到 52 篇；完成页码级证据卡并加入系统效率主线。
- 2026-11-27：完成 A–G 七条主线的全文扫描与综合页，新增 `vault/20_Topics/Mainline Overview.md`。
- 2026-11-27：新增 AgeMem 页码级证据卡。
- 2026-11-27：Evidence Batch 1 完成 6 篇（Memory-R1、MemAgent、LightMem、TierMem、LongMemEval、PersistBench），`evidence-checked` 达到 12/51。
- 2026-11-27：Evidence Batch 2 完成 6 篇（SeCom、HippoRAG 2、GAM、E-mem、RecMem、TiMem），`evidence-checked` 达到 18/51。
- 2026-11-27：Evidence Batch 3 完成 6 篇（MemoryOS、EverMemOS、Hippocampus、LightWM、LightMem (SLM)、SimpleMem），`evidence-checked` 达到 24/51。
- 2026-11-27：Evidence Batch 4 完成 5 篇（EM-LLM、REMem、ARTEM、EMA、Nemori），`evidence-checked` 达到 29/51；主线 D 全部完成。
- 2026-11-27：Evidence Batch 5 完成 7 篇（Evoking、PersonaAgent、M3-Agent、ReMe、ReasoningBank、MemRec、LTS），`evidence-checked` 达到 36/51；主线 E 全部完成。
- 2026-11-27：Evidence Batch 6 完成 6 篇（MemoryArena、MemBench、Minerva、BEAM、MemoryAgentBench、MemoryBench），`evidence-checked` 达到 42/51；主线 F 全部完成。
- 2026-11-27：Evidence Batch 7 完成 4 篇（MEXTRA、MINJA、InjecMEM、eTAMP），`evidence-checked` 达到 46/51；主线 G 全部完成。
- 2026-11-27：Evidence Batch 8 完成 5 篇（M+、MemEvolve、UMEM、Mem0、From Storage to Experience），`evidence-checked` 达到 51/51；全部主库论文均有逐篇 evidence。
- 2026-11-27：主库从 36 篇扩展到 51 篇，新增 15 篇正式发表论文（Batch 1: 8 篇；Batch 2: 7 篇）。
- 新增 `data/agent-memory-2025/COVERAGE_AUDIT.md`，记录覆盖审计、增补理由、暂缓候选和去重结果。
- 新增 `survey` 论文类别，用于正式发表的综述与框架论文。
- 新增 Batch 2 / Batch 3 Zotero 导入文件。

### Changed

- `papers.json` 从 36 篇增加到 51 篇；`edges.json` 从 47 条增加到 81 条。
- Zotero 现有 51 条书目 + 51 条 importer notes，分 3 个 collection。
- 正式 DOI 已回填 A-Mem、G-Memory、MAGMA、AgeMem、MemoryOS、GAM 等记录。

## [0.2.0] — 2026-11-19

### Added

- Multi-machine collaboration layer: `STATUS.md`, `CONTRIBUTING.md`, `PROVENANCE.md`, `DATA_POLICY.md`, `AI_USAGE.md`, `READING_QUEUE.md`.
- ADR index and five initial architecture decisions under `docs/decisions/`.
- Research log index and initial session log.
- JSON schemas for paper records and graph edges.
- `Makefile`, GitHub Actions validation, PR template, research-task issue template.
- Machine setup, data model, security, citation, authorship, and license files.

### Changed

- Zotero workflow is explicitly export-first.
- Multi-machine sync protocol requires `git pull --rebase` and `make check`.
- Repository version bumped to `0.2.0`.

## [0.1.0] — 2026-11-19

### Added

- Initial `MEM` personal paper research system.
- `Agent Memory 2025+` research case with 36 published papers and 47 conceptual edges.
- 36 Obsidian paper notes.
- Topic note, research synthesis, and Obsidian Canvas.
- BibTeX, RIS, CSV, and research map JSON exports.
- Scholar Literature Maps, Research Nexus, and OpenAlex MCP under `.tools/`.
- MEM-specific Codex skills for research-system and literature-map workflows.
- Validation, build, Zotero export, and Zotero CSL import scripts.
- Venue audit and preprint exclusion records.
- Initial five research questions.

### Changed

- MEM now uses an independent Obsidian vault at `MEM/vault`.
- OpenReview PDF links use stable `openreview.net/pdf?id=...` URLs.
- `ROADMAP.md` marks independent-vault setup as completed.

### Fixed

- Removed the invalid assumption that `obsidian://open?path=` can register a new vault.
- Registered `MEM/vault` in Obsidian and opened the Dashboard.
- Kept Zotero database untouched; import is handled through supported BibTeX flow.
