# Multi-Machine Setup

> 适用版本：MEM `v0.2.4`
> 当前研究分支：`research/agent-memory-evidence`
> 当前主库：52 篇论文，86 条概念关系，52/52 evidence-checked

## 1. Prerequisites

- Git
- Python 3.10+
- Obsidian
- Zotero
- GitHub SSH access

## 2. Clone and select the active branch

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
git fetch origin
git switch research/agent-memory-evidence
```

If the research branch has already been merged into `main`, switch to `main` instead. Always confirm the branch named in `STATUS.md`.

## 3. Read first

```bash
cat STATUS.md
cat docs/multi-machine-playbook.md
cat CONTRIBUTING.md
cat RESEARCH_QUESTIONS.md
cat PROVENANCE.md
```

## 4. Bootstrap external tools

```bash
bash scripts/bootstrap_scheme_a.sh
```

This creates:

```text
.tools/research-nexus
.tools/scholar-literature-maps
.tools/openalex-research-mcp
```

`.tools/` is ignored by Git and can be recreated on any machine.

## 5. Obsidian

Open this folder as an Obsidian vault:

```text
$MEM_ROOT/vault
```

Recommended entry points:

- `vault/90_System/Dashboard.md`
- `vault/20_Topics/Agent Memory 2025+.md`
- `vault/20_Topics/Mainline Overview.md`
- `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md`
- `vault/40_Maps/Agent Memory 2025+.canvas`
- `vault/10_Papers/evidence/INDEX.md`
- `个人理解/路线分类.md`

Do not commit `vault/.obsidian/workspace*.json`.

## 6. Zotero

MEM uses an export-first workflow. The current library already has 52 bibliographic items and 52 importer notes.

Start from `data/zotero/IMPORT_STATUS.md`; do not blindly re-import the full `.bib` and create duplicates.

If a new machine needs to restore the library:

1. Open Zotero.
2. Create/confirm `agent-memory-2025`.
3. Import the initial file `data/agent-memory-2025/agent-memory-2025.bib`.
4. Import only missing incremental batches:
   - `agent-memory-2025-batch2.bib`
   - `agent-memory-2025-batch3.bib`
   - `agent-memory-2025-batch4.bib`
5. Verify item count against `papers.json`.
6. Keep the four collections until deduplication and item-key backfill are complete.

Do not commit:

- `zotero.sqlite`
- `fulltext.sqlite`
- `storage/`
- PDFs

## 7. Validate and build

```bash
make check
```

`make check` now validates:

- JSON schemas
- paper graph
- generated paper notes / map / Canvas
- BibTeX / RIS export
- evidence index
- baseline timeline JSON → CSV + Obsidian note
- venue audit
- README / STATUS / ROADMAP / Dashboard consistency

Targeted commands:

```bash
make validate
make build
make export
make evidence-index
make baseline-timeline
make venue-audit
make docs-check
```

## 8. Sync workflow

Before work:

```bash
git branch --show-current
git pull --rebase
make check
```

After work:

```bash
make check
git diff --check
git status -sb
git add <files>
git commit -m "data: add paper"
git push origin <current-branch>
```

See `docs/multi-machine-playbook.md` for conflict rules and the deployment checklist.

## 9. Troubleshooting

### `papers.json` merge conflict

Prefer per-paper additions. If conflict is large, resolve the source JSON manually, then run:

```bash
make validate
make check
```

### Generated file conflict

Do not merge generated files line by line. Resolve the source conflict and regenerate:

```bash
make check
```

### Baseline timeline is stale

Do not edit the generated CSV or Obsidian note directly. Edit:

```text
data/agent-memory-2025/baseline-timeline.json
```

Then run:

```bash
make baseline-timeline
make docs-check
```

### Obsidian shows “Vault not found”

Use Obsidian's “Open folder as vault” and choose the local `vault/` directory. A vault URI cannot register a new vault before it is known to Obsidian.

### Zotero import does not appear

Use `File → Import` and choose the `.bib` or `.ris` file manually. Check `data/zotero/IMPORT_STATUS.md` before re-importing an existing batch.

### Map differs after build

Generated files are part of the repository. Run:

```bash
make check
git diff
```

Commit generated changes only when the source data changed.

## 10. Acceptance checklist

- [ ] Correct branch selected
- [ ] `make check` passes
- [ ] 52/52 evidence cards present
- [ ] baseline timeline has 52 entries
- [ ] route classification has 52 papers with tags and links
- [ ] Obsidian dashboard and timeline open
- [ ] Zotero has 52 items and no database/PDF in Git
