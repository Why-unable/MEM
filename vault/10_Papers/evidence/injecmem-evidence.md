---
type: evidence
paper_id: injecmem
title: "InjecMEM: Memory Injection Attack on LLM Agent Memory Systems"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/injecmem.pdf"
source_version: "COLM 2026 conference paper"
pages_checked: "1-9"
mainline: "G"
tags:
  - evidence
  - mainline-g
  - memory-injection
  - security
---

# InjecMEM 证据卡

## 结论先行

- InjecMEM 只需要 **一次交互**，不需要 memory 读写权限，就能让未来目标 topic 的 query 输出指定内容。
- 它由 retriever-agnostic anchor（高召回 topic cues）和 adversarial command（短序列）组成。
- MemoryOS 上最高 **35.4% RSR**、**76.6% ASR**；在 memory drift 下仍有效，非目标 query 基本不受影响。

## 研究问题与定位

现有攻击常假设 direct memory access 或 shared memory。InjecMEM 要回答：

> 只做一次普通交互，能否让 memory 系统在未来 topic 上定向输出？

## 方法拆解

### Anchor

- 高召回 topical cues。
- 保证 poison 记录在目标 topic 上被检索。
- retriever-agnostic，适配不同 memory system。

### Adversarial command

- 短序列，优化后在不确定 fused context、不同位置、长 prompt 下仍能操控输出。
- gradient-based coordinate search，跨模板/位置平均。
- 支持跨 backbone 迁移/联合优化。

### 威胁模型

- 单次交互。
- 无 memory read/edit。
- 目标 topic + 目标输出。

来源：PDF p.2-5，Method。

## 关键数字

- MemoryOS：
  - RSR 最高 **35.4%**
  - ASR 最高 **76.6%**
- 在 MemGPT 上也有效（复用 MemoryOS 优化的 command）。
- 在 memory drift 下仍有效；非目标 query 基本不受影响。
- 跨模型族迁移有限，但 command concatenation 可同时攻击多个 backbone。

来源：PDF p.1 abstract；p.5-7，Table 1-3。

## 真正的新意

1. **single-interaction injection**：比 MINJA 更弱权限。
2. **retriever-agnostic anchor**：不依赖某个 retriever。
3. **adversarial command**：跨模板/位置/长 prompt 稳健。
4. **memory drift 下持久**。

## 局限与威胁

- 主要针对存储原始交互文本的系统；rewrite/summarization 系统需扩展。
- 跨模型族迁移有限。
- 防御过滤会牺牲 benign utility。
- 没有多模态/多 agent 共享记忆。
- ASR 绝对值仍受 backbone/context 影响。

## 与主线 G 的关系

- **MINJA**：多轮 query-only；InjecMEM 单次交互。
- **eTAMP**：环境注入；InjecMEM 直接交互注入。
- **MEXTRA**：读记忆；InjecMEM 写记忆。
- **PersistBench**：正常记忆安全风险；InjecMEM 恶意注入。

## 对 RQ3 的意义

InjecMEM 说明记忆写入需要：

- write authorization
- content provenance
- trust scoring
- retrieval-time defense
- deletion/rollback

## 可复用点

- retriever-agnostic anchor。
- adversarial command optimization。
- RSR/ASR-c/ASR-j 指标。
- memory drift 持久性测试。

## 成本

- 攻击只需一次交互 + 离线 command 优化。
- 防御成本/benign utility 损失需单独评估。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/injecmem.pdf`
- COLM 2026（论文记录）
