---
type: evidence
paper_id: "ema"
title: "EMA: An Episodic Memory Agent for Efficient and Selective Memory"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "D"
tags:
  - evidence
  - mainline-d
---

# EMA: An Episodic Memory Agent for Efficient and Selective Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL Findings 2026（ACL-Findings）
- **年份**：2026
- **作者**：Hongyi Lan, Jiaqi Song, Zhengjia Zhong, Hui Li, Hong Liu, Xianming Lin, Rongrong Ji
- **DOI**：10.18653/v1/2026.findings-acl.250
- **arXiv**：null
- **PDF**：https://aclanthology.org/2026.findings-acl.250.pdf
- **正式记录**：https://openreview.net/forum?id=ZoBJWPoH9a
- **主库角色**：把对话抽象为 episodic memory unit 并做选择性记忆，降低长对话冗余。

## 官方摘要

Large Language Models (LLMs) demonstrate strong generation and reasoning abilities, but they still face challenges in long-term memory retention and multi-turn conversational consistency. Existing memory-augmented methods often incorporate full dialog histories without filtering, resulting in information redundancy and inference latency. Inspired by the episodic memory mechanism in human cognition, we abstract conversational context into Episodic Memory Units (EMUs). We then propose a comprehensive framework, Episodic Memory Agent (EMA), along with a filtering decision module called MemDecider. Specifically, EMA organizes and retrieves EMUs to support response generation, while MemDecider filters information to reduce noise and improve overall performance. Experiments on two widely-used benchmarks show that EMA maintains competitive performance, and integrating MemDecider into other methods reduces their token consumption by an average of 11.48% while effectively improving the overall performance. Code is available at https://github.com/Hongyi4221/EMA.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 D 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://aclanthology.org/2026.findings-acl.250.pdf
- 正式记录：https://openreview.net/forum?id=ZoBJWPoH9a
