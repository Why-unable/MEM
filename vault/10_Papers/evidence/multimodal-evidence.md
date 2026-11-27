---
type: evidence
paper_id: multimodal
title: "Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/multimodal.pdf"
source_version: "ICLR 2026 conference paper"
pages_checked: "1-9"
mainline: "E"
tags:
  - evidence
  - mainline-e
  - multimodal
  - episodic-memory
---

# M3-Agent 证据卡

## 结论先行

- M3-Agent 把长期记忆扩展到 **视觉 + 听觉 + 文本**：实时处理多模态输入，构建 entity-centric episodic/semantic memory。
- 它用 RL 训练多轮推理和记忆检索，并发布 M3-Bench：100 个 robot-perspective 视频 + 920 个 web 视频。
- 相对最强 prompting baseline（Gemini-1.5-Pro + GPT-4o），M3-Bench-robot **+6.7%**、M3-Bench-web **+7.7%**、VideoMME-long **+5.3%**。

## 研究问题与定位

多模态 agent 需要跨时间积累视觉/听觉经验，但现有 memory 主要是文本。M3-Agent 要回答：

> 能否用一个 entity-centric 多模态长期记忆，支持实时感知、记忆更新和多轮推理？

## 方法拆解

### Entity-centric multimodal memory

- 记忆以 entity 为中心组织。
- 同时包含 episodic（具体经历）和 semantic（稳定知识）。
- 支持视觉/听觉/文本输入。

### Multi-turn reasoning

- 给定 instruction，agent 自主进行多轮推理。
- 检索相关记忆，组合跨模态证据。
- 训练方式：RL。

来源：PDF p.2-6，Method。

## 实验与关键数字

### 设置

- Benchmarks：M3-Bench-robot（100 videos）、M3-Bench-web（920 videos）、VideoMME-long。
- Baselines：Socratic Models（Gemini-1.5-Pro / GPT-4o / Qwen2.5-Omni / Qwen2.5-VL）、MovieChat、MA-LMM、Flash-VStream、Gemini-Agent、Gemini-GPT4o-Agent。
- Metrics：QA accuracy。

### 结果

| Benchmark | M3-Agent 相对最强 baseline |
|---|---:|
| M3-Bench-robot | **+6.7%** |
| M3-Bench-web | **+7.7%** |
| VideoMME-long | **+5.3%** |

来源：PDF p.1 abstract；p.7-8，Table 1。

### 分析

- Entity-centric memory 对 person understanding、general knowledge、cross-modal reasoning 都有帮助。
- 多轮推理比单轮检索更适合长视频。

来源：PDF p.7-9。

## 真正的新意

1. **entity-centric 多模态记忆**：不是文本 chunk。
2. **episodic + semantic 多模态**：视觉/听觉经验也可长期保留。
3. **M3-Bench**：robot + web 两类长视频 benchmark。
4. **RL 训练多轮记忆推理**。

## 局限与威胁

- **视频 QA 为主**：不是通用多模态 agent。
- **存储/检索成本高**：视频/音频记忆比文本大。
- **隐私风险**：视觉/听觉长期记忆可能包含敏感信息。
- **没有显式遗忘/删除**：多模态记忆只增不减。
- **benchmark 新**：与文本 memory benchmark 不可直接比较。

## 与主线 E 的关系

- **Evoking/PersonaAgent**：文本个性化；M3-Agent 多模态个性化。
- **MemRec**：推荐领域；M3-Agent 视频理解。
- **TierMem**：文本 summary/raw；M3-Agent 需要多模态证据层。
- **MemoryAgentBench**：目前主要是文本；M3-Agent 暴露多模态评测缺口。

## 对 RQ1 的意义

M3-Agent 说明“记忆单元”可以是 entity，而不是文本 chunk：

- 多模态任务中，entity-centric 结构可能比文本 RAG 更有效。
- RQ1 的多模态扩展需要新的 evidence recall 和隐私指标。

## 可复用点

- entity-centric multimodal memory schema。
- episodic + semantic 多模态分层。
- M3-Bench-robot/web。
- 多轮记忆推理训练。

## 成本

- 多模态存储/检索成本未在正文完整量化。
- RL 训练成本未汇总。
- 没有统一 token/latency 表（视频 token 计费不同）。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/multimodal.pdf`
- ICLR 2026（论文记录）
- 代码/数据：https://github.com/ByteDance-Seed/m3-agent
