---
type: evidence
paper_id: "poisononce"
title: "Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents"
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

# Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：COLM 2026（Top-COLM）
- **年份**：2026
- **作者**：Mingwen Dong, Wei Zou, Miguel Romero Calvo, Shuaichen Chang, Jiang Guo, Dongkyu Lee, Xing Niu, Xiaofei Ma, Yanjun Qi, Jiarong Jiang
- **DOI**：null
- **arXiv**：null
- **PDF**：https://openreview.net/pdf?id=sfUpgUKF2Y
- **正式记录**：https://openreview.net/forum?id=sfUpgUKF2Y
- **主库角色**：环境注入的记忆 poisoning：一次污染可被长期利用，面向 Web agent。

## 官方摘要

Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions. While existing security research on memory assumes attackers can directly inject into memory storage or exploit shared memory across users, we present a more realistic threat model: contamination through environmental observation alone. We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access. A single contaminated observation (e.g., viewing a manipulated product page) silently poisons an agent's memory and activates during future tasks on different websites, bypassing permission-based defenses. Our experiments on (Visual)WebArena reveal two key findings. First, eTAMP achieves substantial attack success rates: up to 32.5\% on GPT-5-mini, 23.4\% on GPT-5.2, and 19.5\% on GPT-OSS-120B. Second, we discover Frustration Exploitation: agents under environmental stress become dramatically more susceptible, with ASR increasing up to 9 times when agents struggle with dropped clicks or garbled text.  Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance. As LLM-based agents increasingly interact with untrusted
web environments, our findings underscore the need for defenses against environment-injected memory poisoning.

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
- PDF：https://openreview.net/pdf?id=sfUpgUKF2Y
- 正式记录：https://openreview.net/forum?id=sfUpgUKF2Y
