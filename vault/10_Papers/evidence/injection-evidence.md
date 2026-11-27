---
type: evidence
paper_id: "injection"
title: "Memory Injection Attacks on LLM Agents via Query-Only Interaction"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "G"
tags:
  - evidence
  - mainline-g
---

# Memory Injection Attacks on LLM Agents via Query-Only Interaction — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：NeurIPS 2025（CCF-A）
- **年份**：2025
- **作者**：Shen Dong, Shaochen Xu, Pengfei He, Yige Li, Jiliang Tang, Tianming Liu, Hui Liu, Zhen Xiang
- **DOI**：10.52202/085713-1554
- **arXiv**：2503.03704
- **PDF**：https://openreview.net/pdf?id=QINnsnppv8
- **正式记录**：https://openreview.net/forum?id=QINnsnppv8
- **主库角色**：query-only 记忆注入攻击，说明只通过查询交互也能污染 agent 记忆。

## 官方摘要

Agents powered by large language models (LLMs) have demonstrated strong capabilities in a wide range of complex, real-world applications.
However, LLM agents with a compromised memory bank may easily produce harmful outputs when the past records retrieved for demonstration are malicious.
In this paper, we propose a novel Memory INJection Attack, MINJA, without assuming that the attacker can directly modify the memory bank of the agent.
The attacker injects malicious records into the memory bank by only **interacting with the agent via queries and output observations**.
These malicious records are designed to elicit a sequence of malicious reasoning steps corresponding to a different target query during the agent's execution of the victim user's query.
Specifically, we introduce a sequence of *bridging steps* to link victim queries to the malicious reasoning steps.
During the memory injection, we propose an *indication prompt* that guides the agent to autonomously generate similar bridging steps, with a *progressive shortening strategy* that gradually removes the indication prompt, such that the malicious record will be easily retrieved when processing later victim queries.
Our extensive experiments across diverse agents demonstrate the effectiveness of MINJA in compromising agent memory.
With minimal requirements for execution, MINJA enables any user to influence agent memory, highlighting the risk.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 G 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=QINnsnppv8
- 正式记录：https://openreview.net/forum?id=QINnsnppv8
