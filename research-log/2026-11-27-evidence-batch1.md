# 2026-11-27 — Evidence Batch 1

- 执行者：Codex
- 范围：Memory-R1、MemAgent、LightMem、TierMem、LongMemEval、PersistBench
- 目标：把 6 篇 queued evidence 升级为页码级 `evidence-checked`

## 完成

- `vault/10_Papers/evidence/memoryr1-evidence.md`
- `vault/10_Papers/evidence/memagent-evidence.md`
- `vault/10_Papers/evidence/lightmem-evidence.md`
- `vault/10_Papers/evidence/tiermem-evidence.md`
- `vault/10_Papers/evidence/longmemeval-evidence.md`
- `vault/10_Papers/evidence/persistbench-evidence.md`

## 关键数字

- Memory-R1：152/81/1307 split；LLaMA-3.1-8B GRPO overall F1 45.02 / B1 37.51 / J 62.74。
- MemAgent：8K 训练 → 3.5M 外推；3.5M RULER-HQA 71.09/71.88；512K NIAH >95%。
- LightMem：LongMemEval +2.09–7.67%；总 token 最高 38x 降低；在线 token 最高 117.1x 降低。
- TierMem：LoCoMo 0.851 vs raw 0.873；input tokens -54.1%；latency -60.7%。
- LongMemEval：500 问、五能力；115K/1.5M；30%–60% 性能下降。
- PersistBench：500 样本、18 LLM；cross-domain median 53%，sycophancy median 97.8%。

## 状态

```text
evidence-checked: 12
queued: 39
```

## 未完成

- 其余 39 篇仍为 queued。
- 六篇仍有少量待核对项（训练成本、附录表格、代码版本）。

## 下一步

Batch 2：SeCom、HippoRAG 2、GAM、E-mem、RecMem、TiMem。
