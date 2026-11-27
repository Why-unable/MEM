---
type: evidence
paper_id: "memorybench"
title: "MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems"
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

# MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICML 2026（CCF-A）
- **年份**：2026
- **作者**：Qingyao Ai, Yichen Tang, Changyue Wang, Jianming Long, Weihang Su, Yiqun Liu
- **DOI**：null
- **arXiv**：2510.17281
- **PDF**：https://raw.githubusercontent.com/mlresearch/v306/main/assets/ai26e/ai26e.pdf
- **正式记录**：https://proceedings.mlr.press/v306/ai26e.html
- **主库角色**：用用户反馈模拟框架评测 LLM 系统的持续学习与记忆能力，覆盖多领域、多语言和多任务类型。

## 官方摘要

Scaling up data, parameters, and test-time computation has been the mainstream methods to improve LLM systems (LLMsys), but their upper bounds are almost reached due to the gradual depletion of high-quality data and marginal gains obtained from larger computational resource consumption. Inspired by the abilities of human and traditional AI systems in learning from practice, constructing memory and continual learning frameworks for LLMsys has become an important and popular research direction in recent literature. Yet, existing benchmarks for LLM memory often focus on evaluating the system on homogeneous reading comprehension tasks with long-form inputs rather than testing their abilities to learn from accumulated user feedback in service time. Therefore, we propose a user feedback simulation framework and a comprehensive benchmark covering multiple domains, languages, and types of tasks to evaluate the continual learning abilities of LLMsys. Experiments show that the effectiveness and efficiency of state-of-the-art baselines are far from satisfying, and we hope this benchmark could pave the way for future studies on LLM memory and optimization algorithms. Website: https://memorybench.thuir.cn Code: https://github.com/THUIR/MemoryBench Data: https://huggingface.co/datasets/THUIR/MemoryBench Data-Full: https://huggingface.co/datasets/THUIR/MemoryBench-Full

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
- PDF：https://raw.githubusercontent.com/mlresearch/v306/main/assets/ai26e/ai26e.pdf
- 正式记录：https://proceedings.mlr.press/v306/ai26e.html
