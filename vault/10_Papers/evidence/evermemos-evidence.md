---
type: evidence
paper_id: evermemos
title: "EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/evermemos.pdf"
source_version: "ACL 2026 Long Papers; DOI 10.18653/v1/2026.acl-long.2125"
pages_checked: "1-10"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - memory-os
  - semantic-consolidation
---

# EverMemOS 证据卡

## 结论先行

- EverMemOS 用 engram-inspired 生命周期组织记忆：Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。
- 它把“孤立记录 + 碎片检索”转成 MemCell → MemScene → 重构上下文的三阶段。
- LoCoMo 相对最强 baseline **+9.2%**，LongMemEval **+6.7%**；PersonaMem-v2 profile 稳定性 **+9.32 点**。

## 研究问题与定位

现有 memory systems 常存孤立记录、检索碎片，无法巩固经验、解决冲突。EverMemOS 要回答：

> 能否用自组织的记忆生命周期，把 episodic trace 巩固成 semantic structure，再按需重构上下文？

## 方法拆解

### Phase I · Episodic Trace Formation

- 对话流 → MemCell。
- MemCell 包含 episodic trace、atomic facts、time-bounded foresight。
- 保留事件级信息，而不是直接压成全局 summary。

### Phase II · Semantic Consolidation

- MemCell → MemScene。
- MemScene 是主题/语义结构，更新用户 profile。
- 解决冲突和长期一致性。

### Phase III · Reconstructive Recollection

- MemScene-guided agentic retrieval。
- 组合 necessary and sufficient context，而不是返回碎片。

来源：PDF p.2-6，Method。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval、PersonaMem-v2。
- Backbones：GPT-4o-mini、GPT-4.1-mini 等。
- Baselines：Zep、MemOS、MemoryOS、A-Mem 等。
- Metrics：accuracy、LLM-Judge、profile stability、tokens、latency。

### LoCoMo / LongMemEval

- 相对最强 baseline：
  - LoCoMo **+9.2%**
  - LongMemEval **+6.7%**
- 在 multi-hop、temporal、knowledge update 等类别有提升。

来源：PDF p.1 abstract；p.7-8，Table 1-2。

### Profile / conflict

- PersonaMem-v2：加入 User Profile 后整体 accuracy **+9.32 点**。
- LongMemEval knowledge update：conflict detection **+20.6%**。
- LoCoMo temporal：temporal awareness **+16.1%**（GPT-4.1-mini）。

来源：PDF p.8-9，Table 1-4。

### 成本

- 默认 one-shot：**2 次 LLM calls/query**。
- 端到端 latency **3–5 秒/query**。
- 论文 Appendix Table 8/9 有 token/storage 细分。
- MemCell 存储成本随历史增长，但比 raw text 更结构。

来源：PDF p.9-10，Appendix A.4。

## 真正的新意

1. **engram-inspired 生命周期**：trace → scene → recollection。
2. **MemCell 承载 episodic + atomic + foresight**：不是单一摘要。
3. **MemScene 作为语义巩固层**：解决碎片化和冲突。
4. **reconstructive recollection**：检索是“组合必要上下文”，不是 top-k。

## 局限与威胁

作者承认多阶段 pipeline 可能传播早期错误；以下是分析：

- **多阶段误差累积**：MemCell/MemScene 质量依赖 LLM。
- **latency/compute**：3–5s/query，且多阶段；不适合极低延迟场景。
- **没有显式遗忘/删除**：长期 MemCell/MemScene 只增不减。
- **评测仍以对话/个性化**：没有 action-coupled、多模态、安全。
- **storage 增长**：MemCell 保留原始 trace，长期部署需归档。

## 与主线 C 的关系

- **MemoryOS**：MemoryOS 是三级存储 + FIFO/page；EverMemOS 是 MemCell/MemScene 生命周期。
- **LightMem**：LightMem 用 online/offline 解耦；EverMemOS 用语义巩固。
- **Hippocampus**：Hippocampus 优化检索底层；EverMemOS 优化记忆生命周期。
- **TierMem**：TierMem 在 query time 选择 summary/raw；EverMemOS 在 consolidation 阶段构建 MemScene。

## 对 RQ1 的意义

EverMemOS 支持“结构 + 巩固 + 重构”三者组合：

- 不是单一图结构，而是 lifecycle。
- RQ1 应把 consolidation 质量和 retrieval reconstruction 分开评估。

## 可复用点

- MemCell / MemScene schema。
- Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection。
- profile stability / conflict detection / temporal awareness 三类分析。
- 2 calls/query、3–5s 的成本报告。

## 成本

- 2 LLM calls/query（默认 one-shot）。
- 3–5s/query。
- token/storage 细分见 Appendix Table 8/9（待逐项核对）。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/evermemos.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.2125/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.2125
