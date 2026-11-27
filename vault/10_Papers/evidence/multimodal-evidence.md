---
type: evidence
paper_id: "multimodal"
title: "Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory"
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "E"
tags:
  - evidence
  - mainline-e
---

# Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2026（Top-ICLR）
- **年份**：2026
- **作者**：Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, Wei Li
- **DOI**：10.48550/arXiv.2508.09736
- **arXiv**：2508.09736
- **PDF**：https://openreview.net/pdf?id=PMz29A7Muq
- **正式记录**：https://openreview.net/forum?id=PMz29A7Muq
- **主库角色**：多模态长期记忆 agent，连接视觉、听觉与文本经验。

## 官方摘要

We introduce M3-Agent, a novel multimodal agent framework equipped with long-term memory. Like humans, M3-Agent can process real-time visual and auditory inputs to build and update episodic and semantic memories, gradually accumulating world knowledge. Its memory is organized in an entity-centric, multimodal manner, enabling deeper and more consistent understanding of the environment. Given an instruction, M3-Agent autonomously performs multi-turn reasoning and retrieves relevant memories to complete tasks. To evaluate memory effectiveness and memory-based reasoning in multimodal agents, we develop M3-Bench, a long-video question answering benchmark comprising 100 newly recorded robot-perspective videos (M3-Bench-robot) and 920 diverse web-sourced videos (M3-Bench-web). We annotate QA pairs designed to test capabilities essential for agent applications, such as person understanding, general knowledge extraction, and cross-modal reasoning. Experimental results show that M3-Agent, trained via reinforcement learning, outperforms the strongest baseline, a prompting agent using Gemini-1.5-pro and GPT-4o, achieving 6.7%, 7.7%, and 5.3% higher accuracy on M3-Bench-robot, M3-Bench-web and VideoMME-long, respectively. Our work advances multimodal agents toward more human-like long-term memory and provides insights for their practical design. Models, datasets and code are available at https://github.com/ByteDance-Seed/m3-agent.

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 E 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：https://openreview.net/pdf?id=PMz29A7Muq
- 正式记录：https://openreview.net/forum?id=PMz29A7Muq
