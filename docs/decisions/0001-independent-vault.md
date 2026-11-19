# ADR-0001: Use an Independent Obsidian Vault

- Status: accepted
- Date: 2026-11-19
- Owners: MEM
- Related: `config/mem.config.json`

## Context

The machine already contains several Obsidian vaults. Writing MEM notes directly into an existing vault risks changing unrelated notes, plugin state, and workspace layout.

## Decision

MEM uses an independent vault:

```text
MEM/vault
```

The vault is registered in Obsidian and opened as a separate vault. Existing vaults are not modified.

## Consequences

- MEM can evolve its folder structure and plugins independently.
- Multi-machine sync is limited to the MEM repository.
- The user can later migrate selected MEM notes into another vault if needed.

## Alternatives

- Reuse an existing vault: rejected due to isolation and merge-conflict risk.
- Use no vault: rejected because Obsidian is part of the intended workflow.
