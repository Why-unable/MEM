---
type: evidence
paper_id: ema
title: "EMA: An Episodic Memory Agent for Efficient and Selective Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/ema.pdf"
source_version: "ACL Findings 2026"
pages_checked: "1-9"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - episodic-memory
  - filtering
---

# EMA 证据卡

## 结论先行

- EMA 把对话抽象成 Episodic Memory Units（EMU），并用 **MemDecider** 做选择性过滤。
- MemDecider 是插件式模块：加到其他 memory baseline 上，平均降低 token **11.48%**，并提升整体性能。
- 它关注的不是“记更多”，而是“哪些 EMU 应该进入当前上下文”。

## 研究问题与定位

现有 memory-augmented 方法常把完整对话历史塞进上下文，导致冗余、噪声和延迟。EMA 要回答：

> 能否用 episodic memory unit + 选择性过滤，在保持性能的同时降低 token？

## 方法拆解

### Episodic Memory Unit

- 把对话上下文抽象成 EMU。
- EMU 组织/检索后用于 response generation。
- EMU 是事件级单元，不是原始 turn 或 session。

### MemDecider

- 一个 filtering decision module。
- 决定哪些信息应该被保留/送入上下文。
- 可插拔到其他 memory 方法。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、Long-MT-Bench+。
- Baselines：Only LLM、Naive RAG、MemoryBank、A-Mem、LightMem、SeCom、MemoryOS。
- Metrics：F1、BLEU、token consumption。

### 主要结果

- EMA 在 LoCoMo/Long-MT-Bench+ 上保持竞争力。
- MemDecider 加到其他方法上：
  - 平均 token 降低 **11.48%**
  - 部分 baseline 上降低 **12.35%**
  - 整体性能提升
- 说明 filtering 本身是有效的，不依赖 EMA 的完整 memory 结构。

来源：PDF p.1 abstract；p.5-7，Table 1-3。

### 消融

- 去掉 MemDecider：token 增加、噪声增加。
- 启发式 memory selection 不如 MemDecider。
- 说明 learned filtering > 简单规则。

来源：PDF p.7-8，Table 10-11。

## 真正的新意

1. **EMU + MemDecider 分离**：记忆单元和过滤决策分开。
2. **插件式过滤**：可加到其他 memory 系统。
3. **token–performance 联合评估**：不仅看 F1，还看 token。
4. **选择性记忆**：不是所有历史都进入上下文。

## 局限与威胁

- **过滤是查询时降噪，不是持久遗忘**。
- **主要对话 QA**：没有 action-coupled、多模态、安全。
- **MemDecider 仍是分类器**：可能误删关键证据。
- **没有长历史 storage 治理**。
- **benchmark 有限**：LoCoMo/Long-MT-Bench+。

## 与主线 D 的关系

- **TierMem**：TierMem 在粒度上升级；EMA 在上下文入口过滤。
- **RecMem**：RecMem 延迟 consolidation；EMA 过滤已检索内容。
- **Nemori**：Nemori 决定什么值得记；EMA 决定什么值得放进当前上下文。
- **LightMem**：LightMem 压缩/巩固；EMA 过滤。

## 对 RQ1 的意义

EMA 说明“过滤策略”可以独立于存储结构带来 token 收益：

- RQ1 应把 retrieval filtering 作为独立变量。
- 只看 memory bank 大小不够，还要看进入上下文的 evidence。

## 可复用点

- EMU schema。
- MemDecider 插件。
- token–performance 联合报告。
- 与多个 memory baseline 的组合实验。

## 成本

- MemDecider 降低 token 11.48%。
- 额外过滤模块的计算成本未完整报告。
- 没有 build/storage 成本表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/ema.pdf`
- ACL Findings 2026（论文记录）
