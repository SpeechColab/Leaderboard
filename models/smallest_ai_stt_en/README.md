# Smallest AI — Pulse STT (English)

**Entity**: Smallest AI  
**Model**: Pulse  
**Language**: English (en)  
**API Docs**: https://docs.smallest.ai  

## Overview

[Pulse](https://smallest.ai) is Smallest AI's speech-to-text model supporting 38 languages. This submission evaluates English transcription accuracy via the **real-time WebSocket streaming API**.

## Model Details

| Property | Value |
|---|---|
| Architecture | Transformer-based end-to-end ASR |
| Inference | Real-time WebSocket streaming (WSS) |
| Latency | ~64ms time-to-first-transcript |
| Training data | Proprietary multilingual corpus |
| Languages | 38 languages with automatic detection |
| Features | Word timestamps, diarization, emotion detection, PII redaction |
| Endpoint | `wss://api.smallest.ai/waves/v1/pulse/get_text` |

## Setup

Place your Smallest AI API key in `assets/API_KEY`:

```bash
echo "your_api_key" > assets/API_KEY
```

Get an API key at https://smallest.ai.

## Running

```bash
./SBI /path/to/wav.scp /path/to/result_dir
```

Transcriptions are written to `result_dir/raw_rec.txt`.

## Local Validation

```bash
ops/benchmark -m smallest_ai_stt_en -d MINI_EN
```

Validated result: `%WER 0.00 [ 0 / 14, 0 ins, 0 del, 0 sub ]`
