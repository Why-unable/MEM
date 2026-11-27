---
type: evidence
paper_id: "interdependent"
title: "Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "F"
tags:
  - evidence
  - mainline-f
---

# Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Zexue He, Yu Wang, Churan Zhi, Yuanzhe Hu, Tzu-Ping Chen, Lang Yin, Ze Chen, Tong Arthur Wu, Siru Ouyang, Zihan Wang, Jiaxin Pei, Julian McAuley, Yejin Choi, Alex Pentland
- **DOI**：null
- **arXiv**：2602.16313
- **PDF**：https://openreview.net/pdf?id=JHYmxqS9Jv
- **正式记录**：https://openreview.net/forum?id=JHYmxqS9Jv
- **主库角色**：MemoryArena：多 session、agent-environment 相互依赖任务中的记忆评测，检验记忆是否真正指导后续行动。

## 官方摘要

Existing evaluations of agents with memory typically assess **memorization** and **action** in isolation. One class of benchmarks evaluates memorization by testing recall of past conversations or text but fails to capture how memory is used to guide future decisions. Another class focuses on agents acting in single-session tasks without the need for long-term memory. However, in realistic settings, memorization and action are tightly coupled: agents acquire memory while interacting with the environment, and subsequently rely on that memory to solve future tasks. To capture this setting, we introduce MemoryArena, a unified evaluation gym for benchmarking agent memory in multi-session Memory-Agent-Environment loops. The benchmark consists of human-crafted agentic tasks with explicitly interdependent subtasks, where agents must learn from earlier actions and feedback by distilling experiences into memory, and subsequently use that memory to guide later actions to solve the overall task. MEMORYARENA supports evaluation across web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning, and reveals that agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting, exposing a gap in current evaluations for agents with memory.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 F 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=JHYmxqS9Jv
- 正式记录：https://openreview.net/forum?id=JHYmxqS9Jv
