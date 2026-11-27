# MEM Agent Instructions

When working inside MEM:

1. Read `STATUS.md`, `SYSTEM.md`, `README.md`, `CONTRIBUTING.md`, and `docs/multi-machine-playbook.md` before editing.
2. Confirm the active branch in `STATUS.md`; current research work uses `research/agent-memory-evidence` until merged.
3. Treat `data/*/papers.json` and `data/*/edges.json` as source data.
4. Treat `data/*/baseline-timeline.json` as the source for timeline, dataset, result, and baseline comparisons.
5. Do not invent paper metadata, DOI, venue, authors, citations, scores, or page numbers.
6. Use official records: OpenReview, ACL Anthology, AAAI OJS, PMLR, PVLDB, MLSys, Crossref, OpenAlex, Semantic Scholar match.
7. Main maps contain formal publications from 2025 onward. arXiv-only papers go to `preprints-excluded.md`.
8. Label non-CCF top-tier venues explicitly (`Top-ICLR`, `Top-COLM`, `Top-MLSys`, `ACL-Findings`, `CCF-B`).
9. Before building, run:

```bash
python3 scripts/validate_mem.py --papers data/<topic>/papers.json --edges data/<topic>/edges.json
```

10. Build with:

```bash
python3 scripts/build_research_map.py --papers data/<topic>/papers.json --edges data/<topic>/edges.json --vault vault --out maps/<topic> --topic '<Topic Name>'
```

11. Export Zotero formats with:

```bash
python3 scripts/export_zotero_formats.py --papers data/<topic>/papers.json --out-dir data/<topic> --stem <topic>
```

12. Do not overwrite the user's hand-written Obsidian notes without previewing the change. Generated paper notes are safe to rebuild; topic/idea/personal notes need care.
13. Never modify `zotero.sqlite` directly. Use BibTeX/RIS/CSL JSON export-first workflows.
14. Every paper must have `vault/10_Papers/evidence/<paper-id>-evidence.md`; keep `INDEX.md` current with `make evidence-index`.
15. Do not mark a paper `evidence-checked` from its abstract or a mainline synthesis; key numbers require PDF/page verification.
16. When adding or modifying a paper, update `baseline-timeline.json` and `个人理解/路线分类.md` when relevant.
17. Do not hand-edit generated timeline CSV, timeline note, venue audit, paper notes, Canvas, or map files. Change the source and regenerate.
18. Record system decisions in `docs/decisions/`, research process in `research-log/`, and AI assistance in `AI_USAGE.md`.
19. Before commit, run `make check`; it includes graph validation, generated artifacts, evidence index, baseline timeline, venue audit, and docs consistency.
20. Before starting work on a machine, run `git pull --rebase`; after work, commit and push the current branch.
