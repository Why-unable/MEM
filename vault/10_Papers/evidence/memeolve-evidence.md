---
type: evidence
paper_id: "memeolve"
title: "MemEvolve: Meta-Evolution of Agent Memory Systems"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "B"
tags:
  - evidence
  - mainline-b
---

# MemEvolve: Meta-Evolution of Agent Memory Systems — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Guibin Zhang, Haotian Ren, Chong Zhan, Junhao Wang, He Zhu, Wangchunshu Zhou, Shuicheng YAN
- **DOI**：10.48550/arXiv.2512.18746
- **arXiv**：2512.18746
- **PDF**：https://openreview.net/pdf?id=qpkG0eKx4v
- **正式记录**：https://openreview.net/forum?id=qpkG0eKx4v
- **主库角色**：用元进化自动设计记忆系统的结构与策略，代表“记忆系统自动设计”方向。

## 官方摘要

Self-evolving memory systems are rapidly reshaping the evolutionary paradigm of large language model (LLM)-based agents. Prior work has predominantly relied on manually engineered memory architectures to store trajectories, distill experience, and synthesize reusable tools, enabling agents to evolve on the fly within environment interactions. However, this paradigm is fundamentally constrained by the \textit{staticity} of the memory system itself: while memory facilitates agent-level evolving, the underlying memory architecture cannot be meta-adapted to diverse task contexts. To address this gap, we propose MemEvolve, a meta-evolutionary framework that jointly evolves agents’ experiential knowledge and their memory architecture, allowing agent systems not only to accumulate experience but also to progressively refine how they learn from it. To ground MemEvolve in prior work and promote openness in future self-evolving systems, we introduce EvolveLab, a unified memory codebase that distills twelve representative memory systems into a modular design space (\textit{encode}, \textit{store}, \textit{retrieve}, \textit{manage}), providing a standardized implementation substrate and a fair experimental arena. Extensive evaluations on four challenging agentic benchmarks show that MemEvolve delivers (i) substantial performance gains, improving frameworks such as SmolAgent and Flash-Searcher by up to $17.06\%$, and (ii) strong cross-task and cross-LLM generalization, yielding memory architectures that transfer effectively across diverse benchmarks and backbones.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 B 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=qpkG0eKx4v
- 正式记录：https://openreview.net/forum?id=qpkG0eKx4v
