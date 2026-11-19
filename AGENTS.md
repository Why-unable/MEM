# MEM Agent Instructions

When working inside MEM:

1. Read `STATUS.md`, `SYSTEM.md`, and `README.md` first, then `CONTRIBUTING.md` before editing.
2. Treat `data/*/papers.json` and `data/*/edges.json` as source data.
3. Do not invent paper metadata, DOI, venue, authors, or citations.
4. Use official records: OpenReview, ACL Anthology, AAAI OJS, PMLR, MLSys, Crossref, OpenAlex, Semantic Scholar match.
5. Main maps contain formal publications from 2025 onward. arXiv-only papers go to `preprints-excluded.md`.
6. Label non-CCF top-tier venues explicitly (`Top-ICLR`, `Top-COLM`, `Top-MLSys`, `ACL-Findings`, `CCF-B`).
7. Before building, run:

```bash
python3 scripts/validate_mem.py --papers data/<topic>/papers.json --edges data/<topic>/edges.json
```

8. Build with:

```bash
python3 scripts/build_research_map.py --papers data/<topic>/papers.json --edges data/<topic>/edges.json --vault vault --out maps/<topic> --topic '<Topic Name>'
```

9. Export Zotero formats with:

```bash
python3 scripts/export_zotero_formats.py --papers data/<topic>/papers.json --out-dir data/<topic> --stem <topic>
```

10. Do not overwrite the user's hand-written Obsidian notes without previewing the change. Generated paper notes are safe to rebuild; topic/idea notes may contain user edits and need care.
11. Never modify `zotero.sqlite` directly. Use BibTeX/RIS/CSL JSON export-first workflows.
12. Record system decisions in `docs/decisions/`, research process in `research-log/`, and AI assistance in `AI_USAGE.md`.
13. Run `make check` before commit and `git pull --rebase` before starting work on a machine.
