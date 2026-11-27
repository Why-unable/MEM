# Contributing to MEM

MEM is a multi-machine research repository. The goal is to keep paper metadata, evidence, synthesis, maps, and deployment instructions reproducible.

## Before editing

```bash
git branch --show-current
git pull --rebase
make check
```

Read:

- `STATUS.md`
- `ROADMAP.md`
- `docs/multi-machine-playbook.md`
- `RESEARCH_QUESTIONS.md`
- `PROVENANCE.md`

Current research branch:

```text
research/agent-memory-evidence
```

`main` is the stable baseline. If current work has not been merged, explicitly switch to the research branch on every machine.

## Source of truth

| Object | Source of truth | Generated |
|---|---|---|
| Paper metadata | `data/<topic>/papers.json` | paper notes, CSV, BibTeX, RIS, map, venue audit |
| Conceptual edges | `data/<topic>/edges.json` | Mermaid map, Canvas, topic relations |
| Per-paper evidence | `vault/10_Papers/evidence/<paper-id>-evidence.md` | `INDEX.md` |
| Baseline timeline | `data/<topic>/baseline-timeline.json` | `baseline-timeline.csv`, Obsidian timeline note |
| Venue audit | `data/<topic>/papers.json` | `VENUE_AUDIT.md` |
| Research synthesis | hand-written `maps/<topic>/SYNTHESIS.md` | `vault/40_Maps/... Synthesis.md` |
| Personal route map | `个人理解/路线分类.md` | — |
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

Current branch map:

- `main`：stable, CI-green baseline
- `research/*`：research synthesis, evidence, timeline
- `data/*`：paper metadata and graph updates
- `docs/*`：docs and collaboration workflow
- `fix/*`：builders, validators, and data corrections

Do not commit directly to `main` once more than one person or machine is active. For solo multi-machine work, direct commits are acceptable only for small conflict-free changes.

## Sync protocol

Before work:

```bash
git pull --rebase
make check
```

After work:

```bash
make check
git diff --check
git status -sb
git add <files>
git commit -m "type(scope): short description"
git push origin <current-branch>
```

Never force-push `main`.

## Commit messages

Use conventional prefixes:

```text
feat: add paper-note workflow
data: add memory-r1 paper
research: add baseline timeline evidence
docs: update multi-machine deployment guide
fix: correct venue audit
chore: update generated map
```

## Pull requests

Every PR should answer:

- What research question or system problem does this change address?
- Which papers/sources were added or changed?
- Which claims are verified vs inferred?
- Were the baseline timeline and route classification updated?
- Was `make check` run? Did `make docs-check` pass?
- Did AI participate? If yes, is it recorded in `AI_USAGE.md`?

## Data rules

- Do not commit PDFs, Zotero SQLite databases, API keys, or private exports.
- Do not invent DOI, venue, authors, year, or citations.
- Use `PROVENANCE.md` for source hierarchy.
- Mark conceptual edges as conceptual.
- Preprints go to `preprints-excluded.md`, not the main map.
- Key numbers must have a page or table reference in evidence.
- Different metrics, datasets, and backbones are not directly comparable.

## Editing Obsidian notes

- Paper notes under `vault/10_Papers/` may be regenerated; keep manual additions in the “可扩展笔记” section only.
- Evidence notes under `vault/10_Papers/evidence/` are hand-maintained research assets and should merge per paper.
- Topic and idea notes may contain hand-written synthesis; preview diffs before rebuilding.
- `vault/.obsidian/workspace*.json` is machine-specific and ignored.
- The baseline timeline note is generated; edit only `baseline-timeline.json`.

## Parallel work and conflicts

Safe to parallelize:

- Different `<paper-id>-evidence.md` files.
- Different `research-log/*.md` files.
- Different topic directories.

Serialize or assign one integrator:

- `papers.json`
- `edges.json`
- `baseline-timeline.json`
- `个人理解/路线分类.md`
- `README.md`, `ROADMAP.md`, `STATUS.md`, `CHANGELOG.md`
- generated Canvas / map / timeline files
- `Makefile`, CI workflows, schemas

If a generated file conflicts, resolve the source conflict first and rerun:

```bash
make check
```

## Validation

Required before commit:

```bash
make check
```

Targeted checks:

```bash
make validate          # paper graph
make evidence-index    # evidence index
make baseline-timeline # timeline CSV + Obsidian note
make venue-audit       # venue audit
make docs-check        # docs vs data consistency
```

`make check` runs all of the above plus `git diff --check`.

## Review checklist

- [ ] Paper metadata verified
- [ ] Venue tier explicit
- [ ] No duplicate IDs/DOIs
- [ ] Edges have reasons
- [ ] Map builds
- [ ] Evidence status and page references checked
- [ ] Baseline timeline updated for new/revised papers
- [ ] Personal route map links and tags updated
- [ ] Obsidian links valid
- [ ] AI usage recorded
- [ ] Changelog updated for system-level changes
- [ ] Research log updated for research-level changes
- [ ] `make check` and `make docs-check` pass
