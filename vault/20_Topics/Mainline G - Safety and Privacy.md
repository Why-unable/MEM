---
type: topic
subtype: mainline-analysis
topic: "Agent Memory 2025+"
mainline: "G"
status: full-text-scan
updated: 2026-11-27
tags:
  - topic
  - agent-memory
  - mainline-g
  - safety
  - privacy
---

# Mainline G - Safety and Privacy

> 范围：MEXTRA、MINJA、InjecMEM、eTAMP 四篇安全/隐私工作。
> 阅读方式：全文 PDF 扫描（威胁模型、攻击路径、数据集、ASR/ISR、防御实验）+ `EXPERIMENT_LANDSCAPE.md` 交叉核对。
> 说明：这四篇不是四篇“同类攻击”，而是一条逐步降低攻击者权限假设的演化链。

## 一句话结论

Agent memory 不是普通存储，而是 **安全边界**：

```text
可读 → 可提取隐私
可写 → 可注入恶意记忆
可检索 → 可被持久操控
可跨会话/跨站复用 → 攻击可以长期潜伏
```

这四篇论文共同说明：

> 记忆系统的能力（持久化、个性化、跨会话复用）与攻击面是同一个设计的两个方面。

## 攻击面演化

| 论文 | 攻击类型 | 攻击者权限 | 目标 |
|---|---|---|---|
| [MEXTRA](../10_Papers/privacy.md) | memory extraction | 黑盒查询 | 提取记忆中的隐私 |
| [MINJA](../10_Papers/injection.md) | query-only memory injection | 只能 query + 观察输出 | 注入恶意记录，诱导后续恶意推理 |
| [InjecMEM](../10_Papers/injecmem.md) | single-shot targeted injection | 一次交互，无 memory read/edit | 让目标 topic 的后续 query 输出指定内容 |
| [eTAMP](../10_Papers/poisononce.md) | environment-injected poisoning | 只能影响 agent 观察到的环境 | 跨 session、跨网站持久污染 |

演化方向：

```text
直接访问 memory
→ query-only
→ 单次交互
→ 环境观察
```

攻击者权限越来越弱，但攻击仍然可行。

## 逐篇分析

### MEXTRA：黑盒记忆提取

**问题**：agent 把私人交互存入 memory 作为 demonstrations，可能被攻击者提取。

**方法**：

- 设计 attacking prompt，诱导 agent 输出 memory 中的隐私。
- 自动生成不同知识水平下的攻击 prompt。
- 在 EHRAgent（MIMIC-III）和 RAP（WebShop）上评估。

**关键结果**（memory size=200，30 prompts）：

| Agent | EN | RN | EE | CER | AER |
|---|---:|---:|---:|---:|---:|
| EHRAgent | 50 | 55 | 0.42 | 0.83 | 0.83 |
| RAP | 26 | 27 | 0.29 | 0.87 | 0.90 |

- 去掉 aligner / requirement / demos 都会降低攻击效果，说明 prompt 结构很重要。
- memory size、embedding、similarity function 都会影响泄漏程度。

**意义**：只要 agent 能读 memory 并生成自然语言，黑盒攻击就可能提取隐私。

**局限**：两个 agent/domain；攻击依赖 prompt 设计；防御评估有限。

### MINJA：只通过 query 注入记忆

**问题**：已有 memory poisoning 往往假设攻击者能直接写 memory；现实中可能只能 query。

**方法**：

- 攻击者通过 query 和输出观察，让 agent 自己生成恶意 memory。
- bridging steps：把 victim query 与 malicious reasoning steps 连接起来。
- indication prompt + progressive shortening：逐步减少提示，使恶意记录更容易被检索。

**关键结果**：

- 3 个 agent、4 类 victim-target pair。
- 平均 injection success rate **98.2%**。
- 平均 attack success rate **76.8%**。
- 在 retrieval noise、prior poisoning、不同 embedding 下仍有效。

**意义**：攻击者不需要 memory 写权限；正常交互本身就能污染记忆。

**局限**：需要多轮攻击交互；不同 agent 的 ASR 方差较大；防御主要是 prompt detection，效果有限。

### InjecMEM：单次交互的定向注入

**问题**：如果攻击者只能进行一次交互，且不能读写 memory，是否还能让未来 query 输出指定内容？

**方法**：

- retriever-agnostic anchor：高召回 topic cues，保证 poison 被检索。
- adversarial command：短序列，优化后在不确定的 fused context、不同位置、长 prompt 下仍能操控输出。
- gradient-based coordinate search，跨模板/位置平均；支持跨 backbone 迁移。

**关键结果**：

- MemoryOS 上最高 **35.4% RSR**、**76.6% ASR**。
- 在 memory drift 下仍有效；非目标 query 基本不受影响。
- 在 MemGPT 上也有效；跨模型族迁移有限，但 command concatenation 可以同时攻击多个 backbone。

**意义**：单次写入就可能造成 topic-conditioned 的定向操控，记忆系统需要 write authorization 和 content provenance。

**局限**：主要针对存储原始交互文本的系统；对 rewrite/summarization 系统需要扩展；防御过滤会牺牲 benign utility。

### eTAMP：环境注入的跨站记忆 poisoning

**问题**：已有攻击假设直接注入 memory 或共享 memory；真实 Web agent 可能只是“看到了被污染的环境”。

**方法**：

- 通过 manipulated product page / 环境观察污染 memory。
- 攻击在后续不同网站的任务中激活。
- 三种策略：Baseline Injection、Frustration Exploitation、Authority Framing。
- 在 (Visual)WebArena 上评估。

**关键结果**：

- ASR 最高：
  - GPT-5-mini **32.5%**
  - GPT-5.2 **23.4%**
  - GPT-OSS-120B **19.5%**
- Frustration Exploitation：环境压力（dropped clicks、garbled text）使 ASR 最高提升约 **8–9x**。
- 更强的模型不一定更安全；GPT-5.2 任务能力更强但仍然脆弱。

**意义**：记忆污染可以来自环境观察，不需要直接 memory access；跨 session/跨站持久化使攻击面更大。

**局限**：WebArena 模拟环境；ASR 绝对值不高但持久性和放大效应显著；防御尚未系统评估。

## 横向比较

| 维度 | MEXTRA | MINJA | InjecMEM | eTAMP |
|---|---|---|---|---|
| 攻击目标 | 隐私提取 | 恶意推理注入 | 定向输出操控 | 跨站任务操控 |
| 权限 | 黑盒 query | query + 观察 | 单次交互 | 环境观察 |
| 持久性 | 读取时 | 多轮注入后 | memory drift 下持久 | 跨 session/跨站 |
| 主要指标 | EN/RN/EE/CER/AER | ISR/ASR | RSR/ASR | ASR/TSR |
| 防御评估 | 部分 | prompt detection 等 | retrieval filter | 有限 |
| 关键风险 | 隐私泄漏 | 记忆写入不可信 | 单次写入定向操控 | 环境不可信 |

## 六条结论

### G1：memory 是安全边界

记忆系统同时承担读写、检索和长期复用，任何一个环节都可能成为攻击入口。

**证据强度**：强。

### G2：攻击者权限假设在不断降低

从直接 memory access → query-only → 单次交互 → 环境观察，攻击仍然可行。

**证据强度**：强。

### G3：持久化会放大攻击

MINJA 的多轮注入、InjecMEM 的 memory drift、eTAMP 的跨站持久化都说明：记忆越持久，攻击越难清除。

**证据强度**：强。

### G4：能力越强不等于越安全

eTAMP 显示 GPT-5.2 任务能力更强，但仍然脆弱；安全对齐不能替代记忆治理。

**证据强度**：中等偏强（单篇，但多模型）。

### G5：现有防御主要是检索/内容过滤，缺少系统级治理

检索过滤会牺牲 benign utility；prompt detection 对 MINJA 效果有限；权限防御无法阻止环境注入。

**证据强度**：强。

### G6：遗忘、删除、回滚、provenance 是共同缺口

四篇攻击都指向同一组防御需求：

```text
write authorization
content provenance
trust scoring
expiration / TTL
deletion / rollback
audit log
permission / isolation
```

**证据强度**：强。

## 对 RQ3 的意义

RQ3（何时应该遗忘）不能只问“遗忘是否提升任务性能”，还要问：

- 遗忘是否能降低 leakage？
- 遗忘是否能消除 poisoning？
- 删除是否可审计、可回滚？
- 共享记忆的删除是否会传播？

建议把 RQ3 的指标扩展为：

```text
task accuracy
leakage rate
attack success rate
deletion success
stale-memory rate
rollback success
benign utility loss
```

## 建议的安全 memory 实验

```text
条件：
  no defense
  retrieval filter
  write authorization
  provenance/trust score
  TTL/expiration
  delete/rollback
攻击：
  MEXTRA-like extraction
  MINJA-like query-only injection
  InjecMEM-like single-shot injection
  eTAMP-like environment poisoning
指标：
  ASR / leakage / benign utility / latency / audit completeness
```

## 证据边界

- 四篇均已完成页码级证据卡。
- 攻击成功率受 agent scaffold、模型版本、prompt、数据集影响，不能直接横比。
