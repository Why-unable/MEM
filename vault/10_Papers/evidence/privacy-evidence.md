---
type: evidence
paper_id: privacy
title: "Unveiling Privacy Risks in LLM Agent Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/privacy.pdf"
source_version: "ACL 2025 Long Papers"
pages_checked: "1-9"
mainline: "G"
tags:
  - evidence
  - mainline-g
  - privacy
  - memory-extraction
---

# MEXTRA 证据卡

## 结论先行

- MEXTRA 是一种黑盒 **Memory EXTRaction Attack**：攻击者只通过 query + 输出观察，就能提取 agent memory 中的隐私。
- 在 EHRAgent（MIMIC-III）和 RAP（WebShop）上，memory size=200、30 prompts 时均能显著泄漏。
- 关键影响因素：memory size、embedding、similarity function、prompt 结构（aligner/requirement/demos）。

## 研究问题与定位

Agent 把私人交互存入 memory 作为 demonstrations，可能被攻击者提取。MEXTRA 要回答：

> 在黑盒设置下，攻击者能否通过 prompt 诱导 agent 泄漏 memory 中的隐私？

## 方法拆解

### 攻击 prompt

- 设计 attacking prompt，诱导 agent 输出 memory 内容。
- 自动生成不同知识水平下的 prompt。
- 用 aligner / requirement / demos 等组件提高攻击效果。

### 评估

- EHRAgent：医疗 EHR。
- RAP：WebShop 购物。
- Metrics：EN、RN、EE、CER、AER。
- Memory size=200，30 attacking prompts。

来源：PDF p.3-5，Method。

## 关键数字

| Agent | EN | RN | EE | CER | AER |
|---|---:|---:|---:|---:|---:|
| EHRAgent | 50 | 55 | 0.42 | 0.83 | 0.83 |
| RAP | 26 | 27 | 0.29 | 0.87 | 0.90 |

- 去掉 aligner / requirement / demos 都会降低攻击效果。
- memory size 增大、embedding/similarity 选择都会影响泄漏程度。

来源：PDF p.4，Table 1；p.5-8。

## 真正的新意

1. **黑盒 memory extraction**：不需要 memory 写权限。
2. **prompt 结构化攻击**：aligner/requirement/demos 组合。
3. **多因素分析**：memory size、embedding、similarity。
4. **真实 agent 场景**：医疗 + 购物。

## 局限与威胁

- 两个 agent/domain，泛化有限。
- 攻击依赖 prompt 设计。
- 防御评估有限。
- 没有多模态/多 agent 共享记忆。
- 没有统一的 utility/defense trade-off 表。

## 与主线 G 的关系

- **MINJA**：MEXTRA 读记忆；MINJA 写记忆。
- **InjecMEM**：单次交互定向注入。
- **eTAMP**：环境注入 poisoning。
- **PersistBench**：正常记忆的 cross-domain leakage/sycophancy。

## 对 RQ3 的意义

MEXTRA 说明“删除/隔离”必须能降低可提取性：

- 仅加 prompt guard 不足。
- 需要 provenance、access control、deletion audit。

## 可复用点

- MEXTRA prompt 结构。
- EN/RN/EE/CER/AER 指标。
- memory size/embedding/similarity 的因素分析。
- 两个真实 agent 场景。

## 成本

- 黑盒攻击成本低（30 prompts）。
- 防御成本未系统评估。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/privacy.pdf`
- ACL 2025（论文记录）
