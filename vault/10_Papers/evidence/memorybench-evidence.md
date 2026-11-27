---
type: evidence
paper_id: memorybench
title: "MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/memorybench.pdf"
source_version: "ICML 2026 / PMLR 306"
pages_checked: "1-9"
mainline: "F"
tags:
  - evidence
  - mainline-f
  - benchmark
  - continual-learning
---

# MemoryBench 证据卡

## 结论先行

- MemoryBench 关注 **continual learning from user feedback**，而不是静态长上下文 recall。
- 它用用户反馈模拟框架，覆盖多领域、多语言、多任务类型，评测 LLMsys 在服务时从累计反馈中学习。
- 关键发现：现有 SOTA 在有效性和效率上都远未满足。

## 研究问题与定位

现有 memory benchmark 多在 homogeneous reading comprehension 上测长文本输入，而不是测“服务时从用户反馈中持续学习”。MemoryBench 要回答：

> LLM 系统能否在真实服务过程中，从累积的用户反馈里持续改进？

## Benchmark 设计

### 用户反馈模拟

- 构造 user feedback 序列。
- 让系统在多轮服务中积累反馈。
- 评测后续任务是否因反馈而改进。

### 覆盖

- 多领域
- 多语言
- 多任务类型

来源：PDF p.2-6，Benchmark design。

## 关键发现

- 现有 SOTA memory/continual learning 方法在 MemoryBench 上表现不理想。
- 有效性和效率都远未满足。
- 说明“长期记忆”不等于“持续学习”。

来源：PDF p.1 abstract；p.6-9，Results。

## 真正的新意

1. **user feedback simulation**。
2. **continual learning 视角**：不是静态 memory QA。
3. **多领域/多语言/多任务**。
4. **服务时学习**：更接近真实产品。

## 局限与威胁

- **更偏 LLMsys 持续学习**：与 agentic action loop 还未完全结合。
- **反馈模拟**：真实用户反馈噪声不同。
- **没有 action-coupled environment**。
- **没有安全/隐私维度**。
- **评测成本高**。

## 与主线 F 的关系

- **LongMemEval**：LongMemEval 测长期对话 memory；MemoryBench 测持续学习。
- **MemoryAgentBench**：MemoryAgentBench 有 test-time learning；MemoryBench 更偏 user feedback/continual learning。
- **MemoryArena**：MemoryArena 测 action-coupled；MemoryBench 测服务反馈。
- **PersistBench**：PersistBench 测安全失败；MemoryBench 测学习效果。

## 对 RQ1/RQ2 的意义

- RQ1：持续学习场景下，结构记忆的收益可能来自“更新”而不是“检索”。
- RQ2：跨领域/跨语言迁移可直接用 MemoryBench 评测。

## 可复用点

- user feedback simulation。
- 多领域/多语言/多任务设置。
- 持续学习有效性/效率指标。
- 与静态 memory benchmark 的对照。

## 成本

- 多轮反馈评测成本高。
- 没有统一 token/latency 表。
- 需要同时报告有效性/效率。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memorybench.pdf`
- PMLR 306（ICML 2026）
- 数据/代码：https://memorybench.thuir.cn
