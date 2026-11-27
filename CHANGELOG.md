# Changelog

All notable changes to MEM are documented here.

The format is based on Keep a Changelog and uses semantic versioning for the research system.

## [Unreleased]

### Added

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
