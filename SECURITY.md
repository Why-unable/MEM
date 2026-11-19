# Security Policy

## Do not commit

- API keys
- Zotero local API keys
- private PDFs
- Zotero databases
- personal notes that are not intended for publication

## Reporting

If a secret or private document is committed, rotate the secret and remove it from Git history before pushing.

## Local API

Zotero local API credentials are machine-local. Use `.env` or the OS credential store.
