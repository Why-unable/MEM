# 2026-11-27 — A–G 七条主线全文阅读分析

- 执行者：Codex
- 机器：macOS
- 范围：Agent Memory 2025+ 主库 51 篇
- 目标：对七条主线分别做一轮全文扫描、横向比较和 RQ 映射

## 输入

- `data/agent-memory-2025/papers.json`：51 篇
- `data/agent-memory-2025/edges.json`：81 条
- `data/agent-memory-2025/pdfs/`：51 个可用 PDF（ReasoningBank 未完整下载，使用摘要/实验地图）
- `maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md`：36 篇原始论文的实验设置矩阵
- 已有主线 A 证据卡与 AgeMem 证据卡

## 输出

新增：

- `vault/20_Topics/Mainline Overview.md`
- `vault/20_Topics/Mainline B - Memory Policy.md`
- `vault/20_Topics/Mainline C - Systems and Efficiency.md`
- `vault/20_Topics/Mainline D - Episodic Memory and Consolidation.md`
- `vault/20_Topics/Mainline E - Personalization Multimodal and Procedural.md`
- `vault/20_Topics/Mainline F - Evaluation.md`
- `vault/20_Topics/Mainline G - Safety and Privacy.md`
- `vault/10_Papers/evidence/agemem-evidence.md`

更新：

- `vault/20_Topics/Mainline A - Memory Architecture.md`：加入 SeCom、HippoRAG 2、GAM、E-mem
- `vault/90_System/Dashboard.md`
- `maps/agent-memory-2025/SYNTHESIS.md`
- `STATUS.md`
- `CHANGELOG.md`

## 七条主线的一句话结论

- **A 架构**：结构记忆的优势取决于粒度、关系、整合时机和访问策略的匹配。
- **B 策略**：记忆正在从模块变成 policy；遗忘仍是任务奖励而非治理。
- **C 系统**：在线/离线解耦、层次存储、压缩索引是效率的核心，但成本口径不统一。
- **D 巩固**：事件分割和“何时巩固”与“如何巩固”同等重要；压缩与原始证据需要分层共存。
- **E 扩展**：记忆对象从事实扩展到用户、视觉/听觉、技能、协作信号。
- **F 评测**：已经从单一 accuracy 分裂为多能力 profile；没有 benchmark 覆盖全部维度。
- **G 安全**：记忆是安全边界；攻击者权限假设不断降低，遗忘/删除/provenance 是共同缺口。

## 证据深度

```text
L1 metadata: 51/51
L2 experiment landscape: 36/51
L3 full-text scan: 50/51（ReasoningBank 使用摘要/实验地图）
L4 evidence card: 6/51
L5 reproduction: 0/51
```

## 未完成

- ReasoningBank 的完整 PDF 未成功下载；当前证据来自摘要与实验地图。
- B–G 的核心论文尚未逐篇建立页码级证据卡。
- `EXPERIMENT_LANDSCAPE.md` 的 15 篇新增论文实验矩阵尚未回填。
- 覆盖矩阵（Mainline F）是分析性归纳，需要后续用统一 schema 固化。

## 下一步

1. 为 B–G 各选 1–2 篇核心论文补 L4 证据卡。
2. 建立 `CLAIMS.md`，把七条主线结论转成 claim–evidence–confidence。
3. 选定 RQ1，设计统一实验协议。
4. 回填新增 15 篇的实验矩阵。
