---
type: evidence
paper_id: "privacy"
title: "Unveiling Privacy Risks in LLM Agent Memory"
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

# Unveiling Privacy Risks in LLM Agent Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ACL 2025（CCF-A）
- **年份**：2025
- **作者**：Bo Wang, Weiyi He, Shenglai Zeng, Zhen Xiang, Yue Xing, Jiliang Tang, Pengfei He
- **DOI**：10.48550/arXiv.2502.13172
- **arXiv**：2502.13172
- **PDF**：https://aclanthology.org/2025.acl-long.1227.pdf
- **正式记录**：https://openreview.net/forum?id=GZWGC1fDnc
- **主库角色**：记忆隐私抽取攻击，揭示长期记忆中的敏感信息泄露面。

## 官方摘要

Large Language Model (LLM) agents have become increasingly prevalent across various real-world applications. They enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks for LLM agents. In this work, we systematically investigate the vulnerability of LLM agents to our proposed Memory EXTRaction Attack (MEXTRA) under a black-box setting. To extract private information from memory, we propose an effective attacking prompt design and an automated prompt generation method based on different levels of knowledge about the LLM agent. Experiments on two representative agents demonstrate the effectiveness of MEXTRA. Moreover, we explore key factors influencing memory leakage from both the agent designer’s and the attacker’s perspectives. Our findings highlight the urgent need for effective memory safeguards in LLM agent design and deployment.

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
- PDF：https://aclanthology.org/2025.acl-long.1227.pdf
- 正式记录：https://openreview.net/forum?id=GZWGC1fDnc
