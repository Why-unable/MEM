# Changelog

All notable changes to MEM are documented here.

The format is based on Keep a Changelog and uses semantic versioning for the research system.

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
