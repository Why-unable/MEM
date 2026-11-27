# Decisions

本文件是 ADR（Architecture Decision Record）索引。每个重要决策单独放在 `docs/decisions/`，避免多台机器同时编辑一个超长文件。

| ID | 决策 | 状态 | 日期 |
|---|---|---|---|
| [0001](docs/decisions/0001-independent-vault.md) | 使用独立 Obsidian Vault | accepted | 2026-11-19 |
| [0002](docs/decisions/0002-published-only-map.md) | 主地图只收录正式发表论文 | accepted | 2026-11-19 |
| [0003](docs/decisions/0003-conceptual-edges.md) | 地图边默认为概念关系 | accepted | 2026-11-19 |
| [0004](docs/decisions/0004-zotero-export-first.md) | Zotero 采用 export-first，不直接写数据库 | accepted | 2026-11-19 |
| [0005](docs/decisions/0005-data-layout-v0.1.md) | v0.1 使用单文件 JSON，v0.2 迁移到分片 YAML | accepted | 2026-11-19 |
| [0006](docs/decisions/0006-baseline-timeline.md) | Baseline timeline 作为可生成的横切证据层，不构造统一总榜 | accepted | 2026-11-27 |

## 何时新增 ADR

以下情况需要新增：

- 改变数据源或来源优先级
- 改变论文库 schema
- 改变 venue 分层规则
- 改变 Obsidian 目录结构
- 改变 Zotero 同步方式
- 改变地图关系语义
- 改变公开/私有数据边界

## 模板

```text
# ADR-XXXX: Title

- Status: proposed | accepted | superseded
- Date: YYYY-MM-DD
- Owners:
- Related:

## Context

## Decision

## Consequences

## Alternatives

## Validation
```
