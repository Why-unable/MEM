---
type: evidence
paper_id: storagetexperience
title: "From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/storagetexperience.pdf"
source_version: "ACL Findings 2026; DOI 10.18653/v1/2026.findings-acl.2069"
pages_checked: "1-9"
mainline: "X"
tags:
  - evidence
  - survey
  - memory-evolution
  - cross-cutting
---

# From Storage to Experience 证据卡

## 结论先行

- 这不是实验论文，而是一篇 **正式发表的综述**：把 LLM agent memory 的演化概括为 Storage → Reflection → Experience 三阶段。
- 它把碎片化的研究（OS 工程 vs 认知科学）统一到一个演化框架中。
- 它特别强调 Experience 阶段的两个机制：proactive exploration 和 cross-trajectory abstraction。

## 研究问题与定位

Agent memory 研究分散在系统、认知、RL、评测等方向，缺少统一演化视角。综述要回答：

> 记忆机制如何从“保存轨迹”演化到“提炼经验”，以及下一步是什么？

## 框架

### 三阶段

| 阶段 | 含义 |
|---|---|
| Storage | 保存 trajectory/历史 |
| Reflection | 对 trajectory 做 refine/反思 |
| Experience | 从 trajectory 抽象出可复用经验 |

### 三个驱动

1. 长程一致性
2. 动态环境
3. 持续学习

### Experience 阶段的两个机制

- Proactive exploration
- Cross-trajectory abstraction

来源：PDF p.1-6，Framework。

## 关键贡献

- 形式化定义 Storage / Reflection / Experience。
- 统一 OS 工程与认知科学视角。
- 给出下一代 memory 的设计原则和路线图。
- 把“经验抽象”作为 frontier。

来源：PDF p.1 abstract；p.6-8。

## 与主线 A–G 的关系

- **A/B**：Storage/Reflection/Experience 对应结构、策略、经验。
- **D**：consolidation 是 Reflection/Experience 的核心。
- **E**：程序性记忆是 Experience 的典型。
- **F**：需要评测 Experience，而不只是 recall。
- **G**：Experience 的 provenance/trust 更复杂。

## 对 RQ1/RQ5 的意义

- RQ1：结构记忆的演进方向是 Experience，而不是更复杂的 Storage。
- RQ5：程序性记忆/技能复用是 Experience 的核心。

## 局限

- **综述没有新实验**：所有结论是二手综合。
- **三阶段是分析框架**，不是唯一分类。
- **覆盖偏 2025–2026**：更早的认知科学/记忆研究覆盖有限。
- **没有统一评测协议**。

## 可复用点

- Storage / Reflection / Experience 三阶段框架。
- 三个驱动：长程一致性、动态环境、持续学习。
- proactive exploration / cross-trajectory abstraction。
- 作为 MEM 主线叙事骨架。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/storagetexperience.pdf`
- ACL Anthology：https://aclanthology.org/2026.findings-acl.2069/
- DOI：https://doi.org/10.18653/v1/2026.findings-acl.2069
