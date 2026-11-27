---
type: evidence
paper_id: "minerva"
title: "Minerva: A Programmable Memory Test Benchmark for Language Models"
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

# Minerva: A Programmable Memory Test Benchmark for Language Models — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2025（CCF-A）
- **年份**：2025
- **作者**：Menglin Xia, Victor Rühle, Saravan Rajmohan, Reza Shokri
- **DOI**：10.48550/arXiv.2502.03358
- **arXiv**：2502.03358
- **PDF**：https://openreview.net/pdf?id=ib9drlZllP
- **正式记录**：https://openreview.net/forum?id=ib9drlZllP
- **主库角色**：可编程记忆测试基准，把记忆能力拆成可组合的测试程序。

## 官方摘要

How effectively can LLM-based AI assistants utilize their memory (context) to perform various tasks? Traditional data benchmarks, which are often manually crafted, suffer from several limitations: they are static, susceptible to overfitting, difficult to interpret, and lack actionable insights--failing to pinpoint the specific capabilities a model lacks when it does not pass a test. In this paper, we present a framework for automatically generating a comprehensive set of tests to evaluate models' abilities to use their memory effectively. Our framework extends the range of capability tests beyond the commonly explored (passkey, key-value, needle in the haystack) search, a dominant focus in the literature. Specifically, we evaluate models on atomic tasks such as searching, recalling, editing, matching, comparing information in context memory, performing basic operations when inputs are structured into distinct blocks, and maintaining state while operating on memory, simulating real-world data. Additionally, we design composite tests to investigate the models' ability to perform more complex, integrated tasks. Our benchmark enables an interpretable, detailed assessment of memory capabilities of LLMs.

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
- PDF：https://openreview.net/pdf?id=ib9drlZllP
- 正式记录：https://openreview.net/forum?id=ib9drlZllP
