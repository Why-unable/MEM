---
type: evidence
paper_id: "persistbench"
title: "PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?"
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

# PersistBench: When Should Long-Term Memories Be Forgotten by LLMs? — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Sidharth Pulipaka, Oliver Chen, Manas Sharma, Taaha Saleem Bajwa, Vyas Raina, Ivaxi Sheth
- **DOI**：10.48550/arXiv.2602.01146
- **arXiv**：2602.01146
- **PDF**：https://openreview.net/pdf?id=Z7Rhzk13NT
- **正式记录**：https://openreview.net/forum?id=Z7Rhzk13NT
- **主库角色**：评测“何时应该遗忘”，把记忆持久化边界变成显式研究对象。

## 官方摘要

Conversational assistants are increasingly integrating long-term memory with large language models (LLMs). This persistence of memories, e.g., the user is vegetarian, can enhance personalization in future conversations. However, the same persistence can also introduce safety risks that have been largely overlooked. Hence, we introduce \textbf{PersistBench} to measure the extent of these safety risks. We identify two long-term memory-specific risks: \textit{cross-domain leakage}, where LLMs inappropriately inject context from the long-term memories; and \textit{memory-induced sycophancy}, where stored long-term memories insidiously reinforce user biases. We evaluate 18 frontier and open-source LLMs on our benchmark. Our results reveal a surprisingly high failure rate across these LLMs - a median failure rate of $53\%$ on cross-domain samples and $97\%$ on sycophancy samples. To address this, our benchmark encourages the development of more robust and safer long-term memory usage in frontier conversational systems.

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
- PDF：https://openreview.net/pdf?id=Z7Rhzk13NT
- 正式记录：https://openreview.net/forum?id=Z7Rhzk13NT
