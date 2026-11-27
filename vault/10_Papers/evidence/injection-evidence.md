---
type: evidence
paper_id: injection
title: "Memory Injection Attacks on LLM Agents via Query-Only Interaction"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/injection.pdf"
source_version: "NeurIPS 2025 conference paper"
pages_checked: "1-9"
mainline: "G"
tags:
  - evidence
  - mainline-g
  - memory-injection
  - security
---

# MINJA 证据卡

## 结论先行

- MINJA 不需要直接修改 memory bank；攻击者只通过 query + 输出观察，就能让 agent 自己写入恶意 memory。
- 它用 bridging steps + indication prompt + progressive shortening，把 victim query 与 malicious reasoning 连接起来。
- 平均 injection success rate **98.2%**，平均 attack success rate **76.8%**。

## 研究问题与定位

已有 memory poisoning 常假设攻击者能直接写 memory。MINJA 要回答：

> 只通过正常 query 交互，能否污染 memory 并影响未来任务？

## 方法拆解

### Attack pipeline

1. 攻击者用 query 诱导 agent 生成目标恶意 reasoning steps。
2. 插入 bridging steps，把 victim query 与 malicious steps 关联。
3. 用 indication prompt 引导 agent 生成类似 bridging steps。
4. Progressive shortening：逐步移除提示，使恶意记录更容易被检索。

### 评估

- 3 个 agent：EHRAgent、RAP、QA Agent。
- 4 类 victim-target pairs。
- Metrics：ISR、ASR、UD（benign utility drop）。

来源：PDF p.3-5，Method。

## 关键数字

- 平均 ISR **98.2%**。
- 平均 ASR **76.8%**。
- ASR 在不同 agent/dataset 上范围约 **43.3%–98.9%**。
- 在 retrieval noise、prior poisoning、不同 embedding 下仍有效。
- Benign utility 基本保持（UD 低）。

来源：PDF p.1 abstract；p.5-7，Table 1-4。

## 真正的新意

1. **query-only memory injection**：不需要 memory 写权限。
2. **bridging steps**：把 victim query 与恶意推理连接。
3. **progressive shortening**：提高检索命中。
4. **黑盒攻击**：只观察输出。

## 局限与威胁

- 需要多轮攻击交互。
- 不同 agent 的 ASR 方差较大。
- 防御主要靠 prompt detection，效果有限。
- 没有多模态/多 agent 共享记忆。
- 没有真正的删除/回滚防御。

## 与主线 G 的关系

- **MEXTRA**：读记忆；MINJA 写记忆。
- **InjecMEM**：单次交互定向注入。
- **eTAMP**：环境注入。
- **PersistBench**：正常记忆的安全风险。

## 对 RQ3 的意义

MINJA 说明“写入授权”是必须的：

- 没有 write authorization/provenance，正常交互就能污染记忆。
- 删除/回滚必须能定位攻击注入的 memory。

## 可复用点

- bridging steps。
- indication prompt + progressive shortening。
- ISR/ASR/UD 指标。
- 多 agent/多数据集评估。

## 成本

- 攻击成本：多轮 query 交互。
- 防御成本未系统量化。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/injection.pdf`
- NeurIPS 2025（论文记录）
