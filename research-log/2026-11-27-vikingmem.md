# 2026-11-27 — VikingMem 增补

- 执行者：Codex
- 论文：VikingMem: A Memory Base Management System for Stateful LLM-Based Applications
- Venue：PVLDB 2026（Proceedings of the VLDB Endowment, Vol. 19 No. 12）
- DOI：10.14778/3827998.3828037
- 层级：CCF-A

## 完成

- 加入 `papers.json`，主库 51 → 52。
- 加入概念关系 5 条，关系 81 → 86。
- 新增 `vault/10_Papers/evidence/vikingmem-evidence.md`。
- 加入主线 C（Systems and Efficiency）。
- 更新 `个人理解/路线分类.md`：52/52 覆盖。
- 生成 Zotero batch4 导入文件并完成导入。

## 核心要点

- Memory Base：selective extraction / stateful evolution / generalizable abstraction。
- event + entity 双抽象；entity 由事件持续更新。
- topic-wise timeline + TTL + time-weighted recall。
- multi-vector reranking。
- LoCoMo：88.83 / 90.12；LongMemEval：66.36 / 75.80。
- P95 检索延迟 0.39–0.89s。

## 备注

- 正式 DOI 已核验；全文使用 arXiv 2605.29640 版本阅读，正式 PVLDB PDF 后续可补。
