---
type: evidence
paper_id: "lightwm"
title: "LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "C"
tags:
  - evidence
  - mainline-c
---

# LightWM: Training-Free Hierarchical Working Memory for Small Language Model Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Ziyi Wang, Haonan Jin, Zian Wang, Wendong Wang, Lanshan Zhang
- **DOI**：null
- **arXiv**：null
- **PDF**：https://openreview.net/pdf?id=WLnpZpShzr
- **正式记录**：https://openreview.net/forum?id=WLnpZpShzr
- **主库角色**：面向小模型 agent 的免训练层次工作记忆，强调低成本与可部署性。

## 官方摘要

Small language models (SLMs) are attractive for low-cost agent deployment, and their growing capabilities make them promising for procedure-centric workloads that repeatedly execute specialized task families with similar workflows.
However, SLM agents still struggle in long-horizon interaction because limited context budgets make it difficult to reliably retain and reuse decision-relevant state across many steps.
Existing working-memory methods attempt to mitigate context growth, but their reliance on unstructured natural-language summarization can discard critical facts, introduce state drift, and compound errors in SLM execution.
We present LightWM, a training-free hierarchical working-memory framework that decomposes procedure-centric tasks into subgoals and organizes memory into task-level global memory and subtask-level local memory, where local memory directly conditions SLM action selection and is updated from new observations through structured updates.
To instantiate such memories without training, a one-time offline LLM-based induction pipeline builds reusable schemas per task family from a few successful traces, requiring no SLM parameter updates or online LLM calls.
On ALFWorld valid_unseen, Qwen3-4B reaches 0.910 success, whereas representative prompting and prior working-memory baselines under the same setting remain below 0.320.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 C 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=WLnpZpShzr
- 正式记录：https://openreview.net/forum?id=WLnpZpShzr
