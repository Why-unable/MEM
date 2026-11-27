---
type: evidence
paper_id: mem0
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/mem0.pdf"
source_version: "ECAI 2025 conference paper"
pages_checked: "1-9"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - production-memory
  - extraction
---

# Mem0 证据卡

## 结论先行

- Mem0 是生产级 extract → consolidate → retrieve 记忆流水线；Mem0g 增加 graph memory。
- LoCoMo 上相对 OpenAI memory，LLM-as-a-Judge 提升 **26%**；Mem0g 比 base Mem0 再高约 **2%**。
- 相对 full-context，p95 latency **-91%**，token cost **-90%+**。

## 研究问题与定位

多 session 对话中固定上下文窗口导致不一致。Mem0 要回答：

> 能否用可扩展的 extract/consolidate/retrieve 流水线，兼顾长期一致性和部署成本？

## 方法拆解

### 基础 Mem0

1. 从对话中抽取 salient memory。
2. 持续 consolidate/update。
3. 按 query 检索相关 memory。
4. 生成回答。

### Mem0g

- 在 base Mem0 上增加 graph memory。
- 捕捉对话元素之间的关系。
- 约 +2% overall score。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmark：LoCoMo。
- Baselines：LoCoMo、ReadAgent、MemoryBank、MemGPT、A-Mem、LangMem、Zep、OpenAI memory、full-context；Mem0g。
- Metrics：LLM-as-a-Judge、p95 latency、token cost。

### 结果

- LLM-J 相对 OpenAI memory **+26%**。
- Mem0g 比 base Mem0 overall **+~2%**。
- p95 latency **-91%** vs full-context。
- token cost **-90%+** vs full-context。
- 在 single-hop、temporal、multi-hop、open-domain 四类上均优于现有 memory systems。

来源：PDF p.1 abstract；p.6-8，Table 1-2。

## 真正的新意

1. **生产级 extract-consolidate-retrieve**。
2. **Mem0g**：graph memory 作为可选增强。
3. **latency/token 双成本优化**。
4. **六类 baseline 的系统对比**。

## 局限与威胁

- **extraction 质量依赖 LLM**。
- **graph 变体增加复杂度**。
- **主要是 LoCoMo**：没有 action-coupled、多模态、安全。
- **没有显式遗忘/删除/审计**。
- **长期 storage/维护成本未完整报告**。

## 与主线 C 的关系

- **LightMem**：LightMem 更强调 online/offline 解耦；Mem0 是生产流水线。
- **MemoryOS**：MemoryOS 层次存储；Mem0 条目抽取/巩固。
- **SimpleMem**：压缩；Mem0 抽取。
- **Hippocampus**：底层检索；Mem0 上层 pipeline。

## 对 RQ1 的意义

Mem0 是“生产 baseline”：

- 结构记忆可以在 accuracy 和 latency/token 上都优于 full-context。
- 但评测主要是 LoCoMo，需要跨 benchmark 验证。

## 可复用点

- extract/consolidate/retrieve pipeline。
- Mem0g graph variant。
- LLM-J + p95 latency + token cost 三指标。
- 六类 baseline 对比。

## 成本

- p95 latency -91%。
- token cost -90%+。
- 具体 build/storage 成本需回附录核对。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/mem0.pdf`
- ECAI 2025（论文记录）
