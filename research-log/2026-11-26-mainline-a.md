# 2026-11-26 — 主线 A 全文证据冲刺

- 执行者：Codex
- 机器：macOS
- 研究主题：Agent Memory 2025+
- 主线：A — Memory Architecture
- 时间范围：2026-11-26

## 目标

把主线 A 从“摘要级论文笔记”推进到“可核查的全文证据卡”，并为 RQ1（结构记忆 vs 长上下文）建立第一版证据矩阵。

## 全文获取

| 论文 | 来源 | 本地文件 | 页数 |
|---|---|---|---:|
| A-Mem | arXiv 2502.12110 | `data/agent-memory-2025/pdfs/amem.pdf` | 28 |
| G-Memory | arXiv 2506.07398 | `data/agent-memory-2025/pdfs/gmemory.pdf` | 24 |
| MAGMA | ACL Anthology 2026.acl-long.1709 | `data/agent-memory-2025/pdfs/magma.pdf` | 18 |
| MemGAS | ICLR 2026 proceedings | `data/agent-memory-2025/pdfs/memgas.pdf` | 37 |
| MRAgent | arXiv 2606.06036 | `data/agent-memory-2025/pdfs/reconstructed.pdf` | 22 |

说明：

- PDF 被 `.gitignore` 的 `*.pdf` 忽略，不进入 Git。
- 文本抽取结果保存在 `/tmp/mem-mainline-a/text/`，不进入仓库。
- A-Mem、G-Memory 使用 arXiv 版本，首页标记 `Preprint`；正式 NeurIPS 2025 camera-ready 未复核。
- MAGMA、MemGAS 使用正式 proceedings 版本。
- MRAgent PDF 标注 ICML 2026 / PMLR 306。

## 阅读产出

新增：

- `vault/10_Papers/evidence/amem-evidence.md`
- `vault/10_Papers/evidence/gmemory-evidence.md`
- `vault/10_Papers/evidence/magma-evidence.md`
- `vault/10_Papers/evidence/memgas-evidence.md`
- `vault/10_Papers/evidence/reconstructed-evidence.md`
- `vault/20_Topics/Mainline A - Memory Architecture.md`

## 主要发现

1. 主线 A 的演进是“组织 → 关系 → 粒度 → 访问策略”，不是单纯增加存储。
2. 结构化记忆在多跳、时间/因果、对抗性任务上占优。
3. 长上下文仍是强 baseline：A-Mem 在 GPT-4o 的 single-hop/adversarial、MAGMA 在 LongMemEval 的 single-session-assistant/knowledge-update 上均输给 full-context。
4. 访问策略的消融贡献通常大于单一结构组件：MAGMA 去掉 adaptive policy 降 0.063；MemGAS 去掉 router 降 3.6 judge points；MRAgent 的 reasoning vs no-reasoning 差异稳定。
5. 五篇论文都没有显式遗忘/删除/回滚机制，这是 RQ3 的直接入口。
6. 成本口径不统一：有的报 tokens/query，有的报 tokens/sample，有的只报 build time；不能直接横比。

## 失败与未完成

- OpenReview 的 `curl` 请求被 challenge 拦截；改用 ICLR proceedings 和 arXiv 获取全文。
- A-Mem/G-Memory 的正式 camera-ready 未复核。
- 图 5/图 6 的部分数值在 PDF 文本抽取中不完整，MRAgent ablation 需要人工看图核对。
- `papers.json` 的 DOI 仍是 arXiv DOI，需要更新为正式 DOI。
- 没有开始写 `CLAIMS.md`；当前先放在主线综合页的“五条证据结论”里。

## 决定

- 证据卡放在 `vault/10_Papers/evidence/`，不修改生成型 `vault/10_Papers/<id>.md`。
- 主线综合页放在 `vault/20_Topics/Mainline A - Memory Architecture.md`。
- 不把不同论文的分数直接排名；只做“类别胜负”和“机制解释”。

## 下一步

1. 用正式 camera-ready 复核 A-Mem/G-Memory。
2. 更新 A-Mem、G-Memory、MAGMA 的正式 DOI。
3. 把主线综合页整理成 `CLAIMS.md` 的 claim-evidence 表。
4. 选 RQ1，设计最小实验：full context / RAG / A-Mem-like / MAGMA-like / MRAgent-like。
5. 补 LongMemEval、MemBench、Minerva 的评测方法。
