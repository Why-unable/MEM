---
type: evidence
paper_id: poisononce
title: "Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/poisononce.pdf"
source_version: "COLM 2026 conference paper"
pages_checked: "1-9"
mainline: "G"
tags:
  - evidence
  - mainline-g
  - memory-poisoning
  - web-agent
---

# eTAMP 证据卡

## 结论先行

- eTAMP 证明 **环境观察本身** 就能污染 memory：一次被操纵的网页/观察，可能在后续不同网站的任务中激活。
- 它不需要 direct memory access，也不需要 shared memory；威胁模型比 MINJA/InjecMEM 更现实。
- ASR 最高：GPT-5-mini **32.5%**、GPT-5.2 **23.4%**、GPT-OSS-120B **19.5%**；Frustration Exploitation 可把 ASR 放大到约 **8–9x**。

## 研究问题与定位

现有 memory poisoning 假设 direct injection 或 shared memory。eTAMP 要回答：

> 只通过环境观察（例如 manipulated product page），能否实现跨 session、跨站点的持久污染？

## 方法拆解

### 环境注入

- 攻击者操纵 agent 观察到的网页/内容。
- agent 把观察写入 memory。
- 后续不同网站/任务中，memory 被检索并触发恶意 action。

### 三种策略

1. Baseline Injection
2. Frustration Exploitation
3. Authority Framing

### 评测

- WebArena / VisualWebArena：Shopping、Reddit、Classifieds。
- 约 280 个跨站任务对。
- Models：GPT-5-mini、GPT-5.2、GPT-OSS-120B、Qwen2.5-VL-72B、Qwen3-VL-32B、Qwen3.5-122B-A10B。

来源：PDF p.3-6，Method。

## 关键数字

| 模型 | 最高 ASR |
|---|---:|
| GPT-5-mini | **32.5%** |
| GPT-5.2 | **23.4%** |
| GPT-OSS-120B | **19.5%** |

- Frustration Exploitation：ASR 提升约 **8x**（GPT-5-mini 3.6% → 32.5%）；论文摘要称最高 9x。
- 更强模型不一定更安全：GPT-5.2 任务能力更强但仍脆弱。
- 跨站点方向影响 ASR（如 Shopping→Reddit 9.5% 等）。

来源：PDF p.1 abstract；p.7-8，Table 1-2。

## 真正的新意

1. **environment-injected poisoning**：不需要 memory 写权限。
2. **cross-session + cross-site**：一次污染长期利用。
3. **Frustration Exploitation**：环境压力放大攻击。
4. **capability ≠ security**：更强模型仍脆弱。

## 局限与威胁

- WebArena 模拟环境。
- ASR 绝对值不高，但持久性和放大效应显著。
- 防御未系统评估。
- 没有多用户共享记忆。
- 没有多模态真实网页的完整覆盖。

## 与主线 G 的关系

- **MINJA**：query-only 多轮注入。
- **InjecMEM**：单次交互定向注入。
- **eTAMP**：环境观察注入。
- **PersistBench**：正常记忆安全风险。

## 对 RQ3 的意义

eTAMP 说明“记忆来源可信度”必须成为一等字段：

- 环境观察不可信；
- 需要 provenance/trust/sandbox；
- 删除必须能追踪到污染源。

## 可复用点

- 环境注入威胁模型。
- Frustration Exploitation。
- ASR/TSR/awareness 指标。
- 跨站点任务对。

## 成本

- 攻击成本：一次环境观察。
- 防御成本未系统量化。
- 评测依赖 WebArena/VisualWebArena。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/poisononce.pdf`
- COLM 2026（论文记录）
