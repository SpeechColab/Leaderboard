# Oruk Fourier 2B (`oruk_fourier_2b_en`)

- **Entity:** [Oruk](https://oruk.ai)
- **Model:** [`oruk/oruk-fourier-2b`](https://huggingface.co/oruk/oruk-fourier-2b) (pinned native BF16 revision `8c2a8871f1304aa2f634da4fb95e24438c4945b9`)
- **Parameters:** ~2B (`Qwen3ASRForConditionalGeneration` architecture, initialized from `Qwen/Qwen3-ASR-1.7B`)
- **License:** `cc-by-nc-4.0` (open weights) & self-serve OpenAI-compatible API at `https://speech-api.oruk.ai/v1/audio/transcriptions` (`$0.0080/min`)
- **Language:** English (`en`, 16 kHz mono)
- **Published Public Benchmarks (Hugging Face Open ASR Leaderboard v1.16.3, 7 default public English splits):**
  - Mean WER: **4.95%** (vs. **5.75%** base `Qwen/Qwen3-ASR-1.7B-hf`)
  - AMI-Cleaned: **6.73%** (vs. 8.31%), VoxPopuli-AA: **1.46%** (vs. 2.85%), SPGISpeech: **1.87%** (vs. 2.57%), GigaSpeech-Cleaned: **6.50%** (vs. 7.22%), Earnings22-Cleaned-AA: **5.61%** (vs. 5.84%), URGENT2024: **9.03%** (vs. 9.93%), Voice Arena Monsoon: **3.42%** (vs. 3.50%).

## Setup

Place an Oruk API key (from `https://oruk.ai/auth/signup`) in `models/oruk_fourier_2b_en/assets/API_KEY` (git-ignored) or export `ORUK_API_KEY`, then run:

```bash
ops/benchmark -m oruk_fourier_2b_en -d MINI_EN
```

For offline Hugging Face checkpoint evaluation (`transformers>=5.21`, `torch`, `soundfile`), set `ORUK_BACKEND=local`.
