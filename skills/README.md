# MEM Skills

These skills are local to MEM and are intentionally small.

- `mem-research-system/` — operate the full MEM workflow.
- `mem-literature-map/` — scope, retrieve, verify, and structure a new literature map.

To use them in Codex, copy or symlink the skill folders into the Codex skills directory, or load `SKILL.md` as prompt context.

The external upstream tools are cloned into `MEM/.tools/` by `scripts/bootstrap_scheme_a.sh`:

- `research-nexus`
- `scholar-literature-maps`
- `openalex-research-mcp`

Upstream code remains under its own license; see each `.tools/*` repository.
