# 2026-11-27 — Agent Memory 主库深度扩展

- 执行者：Codex
- 机器：macOS
- 研究主题：Agent Memory 2025+
- 目标：按 MEM 的正式发表门槛，系统补充 2025–2026 高相关论文，并检查现有地图的 baseline 覆盖缺口。

## 触发问题

用户发现 LightMem 未收录，并指出 AgeMem 是 CCF-A 正式主会长文。初步检查确认：

- LightMem 是 ICLR 2026，应该进入主图。
- AgeMem 是 ACL 2026 Long Papers，DOI `10.18653/v1/2026.acl-long.981`，应该进入主图。
- 这不是单篇遗漏，而是“系统 baseline / 评测基准 / 记忆管理训练”整层覆盖不足。

## Batch 1（8 篇）

- LightMem（ICLR 2026）
- SeCom（ICLR 2025）
- MemoryOS（EMNLP 2025 Main）
- HippoRAG 2（ICML 2025）
- SimpleMem（ICML 2026）
- GAM（ACL 2026）
- ReasoningBank（ICLR 2026）
- MemoryAgentBench（ICLR 2026）

## Batch 2（7 篇）

- AgeMem（ACL 2026 Long）
- E-mem（ICML 2026）
- EverMemOS（ACL 2026 Long）
- Nemori / What Deserves Memory（ACL 2026 Long）
- LightMem (SLM)（ACL 2026 Long）
- MemoryBench（ICML 2026）
- From Storage to Experience（ACL Findings 2026，综述）

## AgeMem 证据卡

已下载 AgeMem 官方 ACL PDF，并完成首张 Batch 2 证据卡：

- `vault/10_Papers/evidence/agemem-evidence.md`
- 覆盖六类记忆工具、三阶段 RL、step-wise GRPO、五个 benchmark 的关键数字和局限。

## 去重与修正

- 发现 MemoryArena 已经以 `interdependent` 为 ID 存在于主库；其官方 PDF 标题没有 `MemoryArena:` 前缀，因此没有重复添加，只补强 role 和 arXiv 字段。
- 发现两个不同的 LightMem：
  - ICLR 2026 `LightMem: Lightweight and Efficient Memory-Augmented Generation`
  - ACL 2026 `Lightweight LLM Agent Memory with Small Language Models`
  两者不是同一篇，引用时必须区分。
- 发现 “What Deserves Memory” 的框架名是 Nemori，和 MAGMA 等论文中的 Nemori baseline 对应。

## 验证方式

- OpenAlex：标题、作者、venue、摘要交叉核对。
- Crossref：ACL / EMNLP DOI 核验。
- ICLR / PMLR / ACL Anthology：官方 proceedings PDF 与 landing page。
- 官方 PDF 首页：作者名核对。
- 不使用模型记忆直接填写 DOI、venue 或 authors。

## 结果

```text
论文：36 → 51
关系：47 → 81
CCF-A：17 → 26
Top-ICLR：8 → 12
CCF-B：1 → 2
ACL Findings：6 → 7
```

Zotero：

```text
51 bibliographic items
51 importer notes
0 PDF attachments
3 collections
```

## 未完成

- 新增 15 篇大多尚未补全文证据卡。
- Zotero 三个 collection 尚未合并。
- `papers.json` / `edges.json` 仍是单文件，多机并发编辑前需要迁移为 per-paper 文件。
- 预印本 MemOS、MIRIX、Zep、O-Mem、STALE 等仍未确认正式 venue。

## 下一步

1. 为 LightMem、AgeMem、EverMemOS、Nemori 补证据卡。
2. 建立“记忆管理/训练”主线（AgeMem、Memory-R1、MemAgent、MemEvolve）。
3. 建立“记忆评测”对照表（LongMemEval、MemoryAgentBench、MemoryBench、MemoryArena、PersistBench、MemBench）。
4. 继续监控 2026 后续会议与期刊，但保持正式发表门槛。
