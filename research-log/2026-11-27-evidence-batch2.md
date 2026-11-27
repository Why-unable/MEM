# 2026-11-27 — Evidence Batch 2

- 执行者：Codex
- 范围：SeCom、HippoRAG 2、GAM、E-mem、RecMem、TiMem
- 目标：补齐主线 A 的扩展架构与主线 D 的 consolidation 证据

## 完成

- `vault/10_Papers/evidence/secom-evidence.md`
- `vault/10_Papers/evidence/hipporag2-evidence.md`
- `vault/10_Papers/evidence/gam-evidence.md`
- `vault/10_Papers/evidence/emem-evidence.md`
- `vault/10_Papers/evidence/recmem-evidence.md`
- `vault/10_Papers/evidence/timem-evidence.md`

## 关键数字

- SeCom：LoCoMo GPT4Score 71.57 vs 65.92；Long-MT-Bench+ 88.81 vs 85.14。
- HippoRAG 2：QA Avg F1 59.8 vs NV-Embed-v2 57.0；recall@5 78.2 vs 73.4。
- GAM：GPT-4o-mini LoCoMo Avg F1 43.14；LongDialQA Qwen2.5-7B 12.55。
- E-mem：LoCoMo F1 54.17 vs GAM 45.31；total cost 3,621 vs 12,540。
- RecMem：LoCoMo construction tokens 193.2K vs Mem0 1,520.8K（-87.3%）。
- TiMem：LoCoMo 75.30；LongMemEval-S 76.88；memory tokens -52.20%。

## 状态

```text
evidence-checked: 18
queued: 33
```

## 下一步

Batch 3：MemoryOS、EverMemOS、Hippocampus、LightWM、LightMem (SLM)、SimpleMem。
