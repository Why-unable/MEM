# 2026-11-27 — Evidence Batch 3

- 执行者：Codex
- 范围：MemoryOS、EverMemOS、Hippocampus、LightWM、LightMem (SLM)、SimpleMem
- 目标：补齐主线 C 的系统与效率证据

## 完成

- `vault/10_Papers/evidence/memoryos-evidence.md`
- `vault/10_Papers/evidence/evermemos-evidence.md`
- `vault/10_Papers/evidence/hippocampus-evidence.md`
- `vault/10_Papers/evidence/lightwm-evidence.md`
- `vault/10_Papers/evidence/lightmem-slm-evidence.md`
- `vault/10_Papers/evidence/simplemem-evidence.md`

## 关键数字

- MemoryOS：LoCoMo F1 +49.11%、BLEU-1 +46.18%；4.9 vs 13 LLM calls。
- EverMemOS：LoCoMo +9.2%、LongMemEval +6.7%；2 calls/query，3–5s。
- Hippocampus：最高 31x 检索加速、14x token 降低；约 1.3K tokens/query。
- LightWM：Qwen3-4B ALFWorld valid_unseen 0.910 vs baseline <0.320。
- LightMem (SLM)：LoCoMo F1 +2.5 over A-Mem；83ms retrieval，581ms end-to-end。
- SimpleMem：LoCoMo F1 +26.4%；推理 token 最多降 30x。

## 状态

```text
evidence-checked: 24
queued: 27
```

## 下一步

Batch 4：EM-LLM、REMem、ARTEM、EMA、Nemori。
