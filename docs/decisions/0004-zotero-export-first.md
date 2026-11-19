# ADR-0004: Zotero Uses Export-First Integration

- Status: accepted
- Date: 2026-11-19
- Owners: MEM
- Related: `data/zotero/IMPORT_STATUS.md`

## Context

Zotero's SQLite database is live and locked while the application runs. Direct database writes risk corruption and bypass Zotero's import logic. Local API access is currently disabled.

## Decision

MEM uses an export-first integration:

- Generate BibTeX / RIS from `papers.json`.
- Use Zotero's supported import flow.
- Use CSL JSON export for future reconciliation.
- Never commit `zotero.sqlite` or PDFs.

## Consequences

- Import requires one application-level confirmation.
- MEM remains safe for multi-machine use.
- A future local-API integration can be added without changing the paper schema.

## Alternatives

- Direct SQLite writes: rejected as unsafe.
- Require local API immediately: rejected because it is disabled.
