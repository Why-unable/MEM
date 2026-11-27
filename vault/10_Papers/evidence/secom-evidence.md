---
type: evidence
paper_id: "secom"
title: "On Memory Construction and Retrieval for Personalized Conversational Agents"
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

# On Memory Construction and Retrieval for Personalized Conversational Agents — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：ICLR 2025（Top-ICLR）
- **年份**：2025
- **作者**：Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Xufang Luo, Hao Cheng, Dongsheng Li, Yuqing Yang, Chin-Yew Lin, H. Vicky Zhao, Lili Qiu, Jianfeng Gao
- **DOI**：null
- **arXiv**：2502.05589
- **PDF**：https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf
- **正式记录**：https://proceedings.iclr.cc/paper_files/paper/2025/hash/e56f394bbd4f0ec81393d767caa5a31b-Abstract-Conference.html
- **主库角色**：以主题连贯的 segment 作为记忆单元，并用 prompt compression 去噪，直接研究记忆粒度对检索的影响。

## 官方摘要

To deliver coherent and personalized experiences in long-term conversations, existing approaches typically perform retrieval augmented response generation by constructing memory banks from conversation history at either the turn-level, session-level, or through summarization techniques.In this paper, we present two key findings: (1) The granularity of memory unit matters: turn-level, session-level, and summarization-based methods each exhibit limitations in both memory retrieval accuracy and the semantic quality of the retrieved content. (2) Prompt compression methods, such as LLMLingua-2, can effectively serve as a denoising mechanism, enhancing memory retrieval accuracy across different granularities. Building on these insights, we propose SeCom, a method that constructs the memory bank at segment level by introducing a conversation segmentation model that partitions long-term conversations into topically coherent segments, while applying compression based denoising on memory units to enhance memory retrieval. Experimental results show that SeCom exhibits a significant performance advantage over baselines on long-term conversation benchmarks LOCOMO and Long-MT-Bench+. Additionally, the proposed conversation segmentation method demonstrates superior performance on dialogue segmentation datasets such as DialSeg711, TIAGE, and SuperDialSeg.

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
- PDF：https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf
- 正式记录：https://proceedings.iclr.cc/paper_files/paper/2025/hash/e56f394bbd4f0ec81393d767caa5a31b-Abstract-Conference.html
