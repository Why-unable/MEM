# Contributing to MEM

MEM is a multi-machine research repository. The goal is to keep paper metadata, notes, maps, and research decisions reproducible.

## Before editing

On every machine:

```bash
git pull --rebase
make check
```

Read:

- `STATUS.md`
- `DECISIONS.md`
- `RESEARCH_QUESTIONS.md`
- `PROVENANCE.md`

## Source of truth

| Object | Source of truth | Generated |
|---|---|---|
| Paper metadata | `data/<topic>/papers.json` | paper notes, CSV, BibTeX, RIS |
| Conceptual edges | `data/<topic>/edges.json` | Mermaid map, Canvas |
| Research questions | `RESEARCH_QUESTIONS.md` and `vault/30_Ideas/` | — |
| Decisions | `docs/decisions/*.md` | `DECISIONS.md` |
| Research process | `research-log/*.md` | `RESEARCH_LOG.md` |
| Current state | `STATUS.md` | — |

Do not hand-edit generated files unless the build script is also updated.

## Branching

Use short branches:

```text
research/agent-memory-rq1
data/agent-memory-paper-additions
docs/multi-machine-workflow
fix/map-builder
```

Do not commit directly to `main` once more than one person or machine is active. For solo multi-machine work, direct commits are acceptable only for small, conflict-free changes.

## Sync protocol

Before work:

```bash
git pull --rebase
```

After work:

```bash
make check
git status
git add <files>
git commit -m "type(scope): short description"
git push
```

Never force-push `main`.

## Commit messages

Use conventional prefixes:

```text
feat: add paper-note workflow
data: add memory-r1 paper
docs: record RQ1 decision
fix: correct venue audit
chore: update generated map
```

## Pull requests

Every PR should answer:

- What research question or system problem does this change address?
- Which papers/sources were added or changed?
- Which claims are verified vs inferred?
- Was `make check` run?
- Did AI participate? If yes, record it in `AI_USAGE.md`.

## Data rules

- Do not commit PDFs, Zotero SQLite databases, API keys, or private exports.
- Do not invent DOI, venue, authors, year, or citations.
- Use `PROVENANCE.md` for source hierarchy.
- Mark conceptual edges as conceptual.
- Preprints go to `preprints-excluded.md`, not the main map.

## Editing Obsidian notes

- Paper notes under `vault/10_Papers/` may be regenerated; keep manual changes in the “可扩展笔记” section only.
- Topic and idea notes may contain hand-written synthesis; preview diffs before rebuilding.
- `vault/.obsidian/workspace*.json` is machine-specific and ignored.

## Validation

Required before commit:

```bash
make validate
make build
make export
```

or:

```bash
make check
```

## Review checklist

- [ ] Paper metadata verified
- [ ] Venue tier explicit
- [ ] No duplicate IDs/DOIs
- [ ] Edges have reasons
- [ ] Map builds
- [ ] Obsidian links valid
- [ ] AI usage recorded
- [ ] Changelog updated for system-level changes
- [ ] Research log updated for research-level changes
