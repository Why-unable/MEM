# Agent Memory 2025+ — Retrieval Protocol

## 范围

- 时间：2025-01-01 至 2026-11-19
- 对象：LLM/agent 的长期记忆、episodic memory、memory policy、记忆整合、记忆评测、记忆安全
- 发表门槛：正式发表的 CCF-A 优先；ICLR、COLM、MLSys 等顶级但非 CCF-A 的 venue 单独标注
- 排除：仅 arXiv、workshop-only、无法核验 venue 的工作不进入主地图

## 检索源

1. **OpenReview API**
   - `https://api2.openreview.net/notes/search`
   - 用于 NeurIPS、ICLR、ICML、COLM、MLSys 等 venue 的 accepted papers。
2. **ACL Anthology**
   - 官方 PDF 与 `2025.acl-*` / `2026.acl-*` / `2026.findings-acl.*`
   - 用于核验 ACL 正会与 Findings。
3. **AAAI OJS**
   - 官方 DOI / PDF，用于 AAAI 2026。
4. **Semantic Scholar API**
   - `paper/search/match` endpoint 用于标题匹配、DOI/arXiv ID、citation count 辅助核验。
5. **Crossref / OpenAlex**
   - 作为补充来源；本次遇到 429 限流，所以没有把 OpenAlex 作为唯一裁决源。

## OpenReview 检索词

- agent memory
- memory agent
- long-term memory
- episodic memory
- memory system
- memory management
- memory retrieval
- memory consolidation
- memory benchmark
- memory poisoning
- multi-agent memory
- memory reasoning
- working memory
- agentic memory
- memory augmented agent
- experience memory
- memory editing
- forgetting agent memory
- memory safety agent
- memory injection agent
- memory evaluation agent
- personalized memory LLM
- shared memory multi-agent

## 筛选规则

1. `venue` 必须包含 2025 或 2026。
2. 排除 `Submitted to ...`、`Withdrawn Submission`、`Desk Rejected`、`Workshop`、`ARR`。
3. 排除与 agent memory 无关的通用 memory 论文（GPU memory、KV cache、video memory、RL episodic control 等）。
4. 优先保留：
   - 记忆架构：A-Mem、G-Memory、MAGMA、MemGAS、Memory is Reconstructed
   - 记忆策略：MemAgent、Memory-R1、MemEvolve、UMEM
   - 系统与效率：Mem0、Hippocampus、LightWM、Learning to Share
   - 情景记忆与整合：Human-inspired Episodic Memory、REMem、ARTEM、EMA、RecMem、TiMem、TierMem
   - 个性化/多模态/程序性记忆：Evoking User Memory、PersonaAgent、Multimodal Memory、Remember Me Refine Me
   - 评测：LongMemEval、Beyond a Million Tokens、Benchmarking Agent Memory、PersistBench、MemBench、Minerva
   - 安全：Unveiling Privacy Risks、Memory Injection Attacks、InjecMEM、Poison Once

## 当前结果

- 候选：约 1,750 条 OpenReview notes（多轮去重后）
- 正式发表主库：36 篇
- 关系边：47 条
- 其中 CCF-A：17 篇
- Top-ICLR：8 篇
- ACL Findings：6 篇
- Top-COLM：3 篇
- Top-MLSys：1 篇
- CCF-B（ECAI）：1 篇

## 已知限制

- OpenReview 的 `venue` 字段有时区分主会、Findings、Workshop；本库已按字段筛选，但仍建议投稿前复核官方 proceedings。
- ACL Anthology 的批量摘要下载较慢，本次主要通过 OpenReview + 官方 ACL PDF 链接核验。
- 2026 年部分会议 proceedings 可能仍在更新；本库使用 OpenReview 的 accepted venue 记录和官方 PDF 作为当前证据。
- 关系边是概念关系，不是完整的 citation graph。
