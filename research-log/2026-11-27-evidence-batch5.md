# 2026-11-27 — Evidence Batch 5

- 执行者：Codex
- 范围：Evoking、PersonaAgent、M3-Agent、ReMe、ReasoningBank、MemRec、LTS
- 目标：补齐主线 E 的个性化、多模态、程序性、应用与多 agent 共享证据

## 完成

- `vault/10_Papers/evidence/evoking-evidence.md`
- `vault/10_Papers/evidence/personaagent-evidence.md`
- `vault/10_Papers/evidence/multimodal-evidence.md`
- `vault/10_Papers/evidence/rememberrefine-evidence.md`
- `vault/10_Papers/evidence/reasoningbank-evidence.md`
- `vault/10_Papers/evidence/memrec-evidence.md`
- `vault/10_Papers/evidence/learnshare-evidence.md`

## 关键数字

- Evoking：PersonaMem 32K 0.6350、128K 0.5394；延迟接近 one-shot。
- PersonaAgent：LaMP-1 0.919、LaMP-2M 0.513、LaMP-2N 0.796、LaMP-3 MAE 0.241。
- M3-Agent：+6.7% / +7.7% / +5.3%（M3-Bench-robot/web、VideoMME-long）。
- ReMe：Qwen3-14B dynamic Avg@4 44.66、Pass@4 63.71。
- ReasoningBank：WebArena Gemini-2.5-flash 40.5 → 48.8；MaTTS 51.8。
- MemRec：Books/Goodreads/MovieTV/Yelp H@1 +14.91%/+28.98%/+19.75%/+15.77%。
- LTS：Qwen3-32B AssistantBench 20.3 vs 14.7，runtime -40.8%；GAIA 30.4 vs 24.8，runtime -55.0%。

## 状态

```text
evidence-checked: 36
queued: 15
```

## 下一步

Batch 6：MemoryArena、MemBench、Minerva、BEAM、MemoryAgentBench、MemoryBench。
