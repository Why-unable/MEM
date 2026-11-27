# 2026-11-27 — 多机部署与仓库文档一致性更新

- 执行者：Codex
- 范围：MEM 顶层文档、部署手册、CI、生成型审计与当前研究状态

## 完成

- 新增 `docs/multi-machine-playbook.md`：首次部署、每日同步、并行分工、冲突处理、提交与验收。
- 更新 `README.md`、`ROADMAP.md`、`STATUS.md`、`CONTRIBUTING.md`、`SYSTEM.md`、`AGENTS.md`。
- 更新 `docs/machine-setup.md`：切换到当前研究分支，补 Zotero 52 条书目状态和 baseline timeline 验收。
- 更新 `docs/data-model.md`、`docs/evidence-model.md`：加入 baseline timeline 与 venue audit 的数据契约。
- 更新 `RESEARCH_QUESTIONS.md`、`READING_QUEUE.md`：反映 52 篇主库和 52/52 evidence 状态。
- 更新 `guides/scheme-a-setup.md`、`maps/agent-memory-2025/README.md`、`data/agent-memory-2025/README.md`、`scripts/README.md`、`vault/README.md`、`data/zotero/README.md`。
- 新增 `scripts/check_docs.py`：检查论文数、关系数、evidence、timeline、route map、venue audit 与顶层文档一致性。
- 新增 `scripts/build_venue_audit.py`：从 `papers.json` 生成完整 venue 审计。
- 更新 `Makefile`：增加 `venue-audit`、`docs-check`，并纳入 `make check`。
- 更新 GitHub Actions：覆盖 `research/**`、`data/**`、`docs/**` 分支和 Pull Request。
- 新增 ADR-0006：baseline timeline 是横切证据层，不构造跨 benchmark 总榜。

## 验证

```bash
make check
```

应覆盖：

- 52 篇论文、86 条关系
- 52/52 evidence
- 52 条 baseline timeline
- 52 篇 route map 链接与标签
- 52 篇 venue audit
- README / STATUS / ROADMAP / Dashboard 文档一致性

## 仍未解决

- `papers.json` / `edges.json` 仍是单文件，需迁移 per-paper / per-edge。
- 52 张 evidence 未做人工 `verified`。
- Zotero item key 尚未回填。
- `CLAIMS.md` 和 RQ1 统一实验协议尚未建立。
