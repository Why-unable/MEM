# Multi-Machine Setup

## 1. Prerequisites

- Git
- Python 3.10+
- Obsidian
- Zotero
- GitHub SSH access

## 2. Clone

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
```

## 3. Read first

```bash
cat STATUS.md
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

On a different machine, the path will differ. Register the local clone's `vault/` folder.

Recommended entry points:

- `vault/90_System/Dashboard.md`
- `vault/20_Topics/Agent Memory 2025+.md`
- `vault/40_Maps/Agent Memory 2025+.canvas`

Do not commit `vault/.obsidian/workspace*.json`.

## 6. Zotero

Export-first workflow:

1. Open Zotero.
2. Create collection `MEM / Agent Memory 2025+`.
3. Import `data/agent-memory-2025/agent-memory-2025.bib`.
4. Optionally enable local API later.

Do not commit:

- `zotero.sqlite`
- `fulltext.sqlite`
- `storage/`
- PDFs

## 7. Validate and build

```bash
make validate
make build
make export
```

Or:

```bash
make check
```

## 8. Sync workflow

Before work:

```bash
git pull --rebase
```

After work:

```bash
make check
git status
git add <files>
git commit -m "data: add paper"
git push
```

## 9. Troubleshooting

### `papers.json` merge conflict

Prefer per-paper additions. If conflict is large, resolve manually and run:

```bash
make validate
```

### Obsidian shows “Vault not found”

Use Obsidian's “Open folder as vault” and choose the local `vault/` directory. A vault URI cannot register a new vault before it is known to Obsidian.

### Zotero import does not appear

Use `File → Import` and choose the `.bib` or `.ris` file manually.

### Map differs after build

Generated files are part of the repository. Run:

```bash
make build
git diff
```

Commit generated changes only when the source data changed.
