---
type: evidence
paper_id: agemem
title: "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/agemem.pdf"
source_version: "ACL 2026 Long Papers, DOI 10.18653/v1/2026.acl-long.981"
pages_checked: "1-10"
tags:
  - evidence
  - agent-memory
  - memory-policy
  - reinforcement-learning
---

# AgeMem 证据卡

## 结论先行

- AgeMem 的关键不是再设计一种记忆结构，而是把 **LTM 和 STM 的管理操作统一成 agent policy 的 tool actions**。
- 它用三阶段 progressive RL + step-wise GRPO 训练“何时写、何时读、何时更新、何时总结、何时丢弃”，把记忆管理从外部 heuristic 变成可学习行为。
- 它直接连接 RQ1 的“访问策略”维度与 RQ3 的“何时遗忘”维度，是当前地图中最重要的 learned memory policy 论文之一。

## 研究问题与定位

现有工作通常把：

- long-term memory（LTM）：持久知识、事实、经验
- short-term memory（STM）：当前上下文、对话窗口

分开处理，依赖 heuristic 或 auxiliary controller，难以端到端优化。

AgeMem 的目标是让 LLM agent 自己学习一整套记忆管理策略，而不是由开发者预定义 remember/retrieve/forget 的时机。

## 方法拆解

### 记忆工具接口

| 工具 | 目标 | 作用 |
|---|---|---|
| ADD | LTM | 新增长期记忆 |
| UPDATE | LTM | 修改已有长期记忆 |
| DELETE | LTM | 删除过期/无用长期记忆 |
| RETRIEVE | STM | 从 LTM 取回内容到当前上下文 |
| SUMMARY | STM | 总结当前上下文 |
| FILTER | STM | 过滤无关上下文 |

来源：PDF p.4, Table 1。

### 三阶段 progressive RL

1. **Stage 1：交互与写入**  
   agent 进行日常交互，可能把有用信息写入 LTM。
2. **Stage 2：干扰与 STM 控制**  
   清空短期上下文、保留 LTM，然后注入 distractor，要求 agent 通过 FILTER / SUMMARY 等工具控制噪声。
3. **Stage 3：整合推理**  
   提出需要同时使用 STM 和 LTM 的任务，最终答案的 delayed reward 反向监督前面所有记忆决策。

关键细节：Stage 1 和 Stage 2 之间会 reset context，防止 agent 直接依赖残留上下文，迫使它真正从 LTM 检索。

来源：PDF p.5-6，Section 3.3。

### Step-wise GRPO

- 每个 query 采样 K 条完整 trajectory。
- 用 terminal reward 做 group-normalized advantage。
- 把 terminal advantage broadcast 到 trajectory 的每个 step，解决记忆操作 reward 稀疏、 discontinuous 的问题。
- 保留 GRPO 的 KL penalty。

来源：PDF p.5-6，Eq. 5-6。

### 复合奖励

总奖励由三部分组成：

- `R_task`：任务完成度
- `R_context`：STM 压缩效率、预防性总结/过滤、信息保留
- `R_memory`：LTM 存储质量、维护、检索相关性
- `P_penalty`：上下文溢出、超出交互轮数等惩罚

来源：PDF p.6，Section 3.5。

## 实验与关键数字

### 设置

- 5 个 benchmark：ALFWorld、SciWorld、PDDL、BabyAI、HotpotQA。
- Backbones：Qwen2.5-7B-Instruct、Qwen3-4B-Instruct。
- Baselines：No-Memory、LangMem、A-Mem、Mem0、Mem0g、AgeMem-noRL。
- 指标：Success Rate（ALFWorld/SciWorld/BabyAI）、Progress Rate（PDDL）、LLM-as-Judge（HotpotQA）、Memory Quality（MQ）。

### 主结果

| Backbone | 方法 | Average |
|---|---|---:|
| Qwen2.5-7B-Instruct | No-Memory | 28.05 |
| Qwen2.5-7B-Instruct | Mem0 | 37.14 |
| Qwen2.5-7B-Instruct | **AgeMem** | **41.96** |
| Qwen3-4B-Instruct | No-Memory | 43.97 |
| Qwen3-4B-Instruct | A-Mem | 45.74 |
| Qwen3-4B-Instruct | **AgeMem** | **54.31** |

来源：PDF p.8, Table 2。

论文报告：

- 相对 no-memory 提升 **49.59% / 23.52%**。
- 相对最佳 baseline（Mem0 / A-Mem）平均提升 **4.82 / 8.57 个百分点**。
- RL 相对 AgeMem-noRL 提升 **8.53 / 8.72 个百分点**。
- Memory Quality：**0.533 / 0.605**。

来源：PDF p.7-8。

### STM 效率

- Qwen2.5-7B：AgeMem 平均 **2,117 tokens**，AgeMem-RAG **2,186**，降低 **3.1%**。
- Qwen3-4B：**2,191 vs 2,310**，降低 **5.1%**。

来源：PDF p.7，Figure 3。

### Tool usage（HotpotQA，平均每 episode 调用次数）

Qwen2.5-7B：

| 工具 | noRL | GRPO |
|---|---:|---:|
| ADD | 0.92 | 1.64 |
| UPDATE | 0.00 | 0.13 |
| DELETE | 0.00 | 0.08 |
| RETRIEVE | 2.31 | 1.95 |
| SUMMARY | 1.08 | 0.82 |
| FILTER | 0.02 | 0.31 |
| Total | 4.33 | 4.92 |

解释：RL 后 agent 更主动写入/更新 LTM，减少反应式重复检索，并更主动过滤上下文。

来源：PDF p.8, Table 3。

### 消融

- 仅加 LTM（+LT）：在三个代表 benchmark 上分别提升 **+10.6% / +14.2% / +7.4%**。
- 再加 RL（+LT/RL）：HotpotQA 额外 **+6.3%**。
- 完整 AgeMem（+LT/ST/RL）：分别提升 **+13.9% / +21.7% / +16.1%**。
- Reward ablation：All-Returns 的 Judge **0.544**、MQ **0.533**、tool calls **4.92**；Answer-Only 为 **0.509 / 0.479 / 3.93**。

来源：PDF p.8-9，Figure 4，Table 4。

## 真正的新意

1. **统一 LTM/STM 管理**：不是分别设计两套策略，而是在同一个 policy 里学习。
2. **记忆操作工具化**：ADD/UPDATE/DELETE/RETRIEVE/SUMMARY/FILTER 成为 agent 的 action space。
3. **三阶段课程**：把“写入 → 抗干扰 → 整合使用”拆成渐进训练阶段。
4. **Step-wise GRPO**：把 terminal reward 分配到每个记忆决策，解决长程信用分配。

## 局限与威胁

作者明确承认（PDF p.10）：

- 当前工具集合是固定的，未来需要更细粒度控制。
- 五个 benchmark 仍是相对受控环境，尚未证明开放世界长期部署效果。

分析补充：

- 只用两个 Qwen backbone，跨模型泛化仍需验证。
- DELETE 工具存在，但没有把它作为“可审计遗忘/回滚”问题系统评测。
- 训练成本、数据构造和课程设计复杂度较高。
- 没有直接与 full-context baseline 做同 token 预算对照；它主要对比 memory systems 和 no-memory。
- reward 依赖 LLM-as-Judge，judge 偏差可能影响 policy。

## 与现有地图的关系

- **Memory-R1**：Memory-R1 训练记忆管理与使用；AgeMem 进一步把 LTM/STM 统一进同一个 policy，并显式加入 STM 控制。
- **MemAgent**：MemAgent 用 RL 压缩长上下文；AgeMem 把压缩、写入、更新、删除、检索都纳入 action space。
- **PersistBench**：PersistBench 评测“何时该忘”；AgeMem 提供可学习的 DELETE 动作，是 RQ3 的策略侧对应物。
- **LongMemEval / MemoryAgentBench**：提供长期记忆评测；AgeMem 的五 benchmark 设置更偏 agentic/embodied + QA。

## 对 RQ1 / RQ3 的意义

### RQ1

AgeMem 支持“访问策略比存储结构更关键”的假设：

- 它没有引入复杂图结构，而是把管理行为本身变成 policy。
- 这说明结构记忆的收益可能来自“会管理”，而不只是“存得多”。

### RQ3

AgeMem 是当前地图里少数把 DELETE 作为一等 action 的工作：

- 但它的 DELETE 是任务奖励驱动，不是隐私/合规/审计驱动。
- 这给 RQ3 一个清晰切口：**可学习遗忘 ≠ 可审计遗忘**。

## 可复用点

- 六类记忆工具接口：ADD / UPDATE / DELETE / RETRIEVE / SUMMARY / FILTER。
- 三阶段课程：写入 → 抗干扰 STM 控制 → 整合推理。
- Step-wise GRPO 的 terminal-advantage broadcast。
- 复合奖励：task + context + memory + penalty。
- Tool usage 统计作为行为分析指标。

## 待核对

- [ ] 核对 appendix 中 reward 公式与训练超参数。
- [ ] 核对五个 benchmark 的具体数据规模和 split。
- [ ] 检查代码/模型是否公开。
- [ ] 与 Memory-R1、MemAgent 做同 backbone / 同 token budget 对照。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/agemem.pdf`
- ACL Anthology：https://aclanthology.org/2026.acl-long.981/
- DOI：https://doi.org/10.18653/v1/2026.acl-long.981
