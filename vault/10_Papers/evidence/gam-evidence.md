---
type: evidence
paper_id: "gam"
title: "GAM: Hierarchical Graph-based Agentic Memory for LLM Agents"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "A"
tags:
  - evidence
  - mainline-a
---

# GAM: Hierarchical Graph-based Agentic Memory for LLM Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL 2026（CCF-A）
- **年份**：2026
- **作者**：Zhaofen Wu, Hanrong Zhang, Fulin Lin, Wujiang Xu, Xinran Xu, Yankai Chen, Henry Peng Zou, Shaowen Chen, Weizhi Zhang, Xue Liu, Philip S. Yu, Hongwei Wang
- **DOI**：10.18653/v1/2026.acl-long.1600
- **arXiv**：null
- **PDF**：https://aclanthology.org/2026.acl-long.1600.pdf
- **正式记录**：https://doi.org/10.18653/v1/2026.acl-long.1600
- **主库角色**：用事件进展图 + 主题关联网络解耦记忆编码与整合，降低瞬态噪声对长期知识结构的干扰。

## 官方摘要

To sustain coherent long-term interactions, Large Language Model (LLM) agents must navigate the tension between acquiring new information and retaining prior knowledge. Current unified stream-based memory systems facilitate context updates but remain vulnerable to interference from transient noise. Conversely, discrete structured memory architectures provide robust knowledge retention but often struggle to adapt to fluid narrative evolution. To address this, we propose GAM, a hierarchical Graph-based Agentic Memory framework that explicitly decouples memory encoding from consolidation to effectively resolve the conflict between rapid context perception and stable knowledge retention. By isolating ongoing dialogue in a event progression graph and integrating it into a topic associative network only upon semantic shifts, our approach minimizes interference while preserving long-term consistency. Additionally, we introduce a Graph-guided, Multi-factor Retrieval strategy to enhance context precision. Experiments on LoCoMo and LongDialQA benchmarks indicate that our method consistently outperforms state-of-the-art baselines in both reasoning accuracy and computational efficiency.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 A 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://aclanthology.org/2026.acl-long.1600.pdf
- 正式记录：https://doi.org/10.18653/v1/2026.acl-long.1600
