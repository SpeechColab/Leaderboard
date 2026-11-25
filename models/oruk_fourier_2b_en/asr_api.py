#!/usr/bin/env python3
# coding: utf-8
"""SpeechIO Leaderboard inference runner for Oruk Fourier 2B (English).

Default mode sends audio clips to Oruk's OpenAI-compatible transcription API
(`https://speech-api.oruk.ai/v1/audio/transcriptions`, model `oruk-fourier-2b`),
which serves pinned weights `oruk/oruk-fourier-2b@8c2a8871f1304aa2f634da4fb95e24438c4945b9`.

Set `ORUK_BACKEND=local` to run directly against pinned Hugging Face weights via
`transformers>=5.21` (`Qwen3ASRForConditionalGeneration`).
"""

import os
import sys
import time
from typing import Callable, Optional

import requests

DEFAULT_API_URL = 'https://speech-api.oruk.ai/v1/audio/transcriptions'
DEFAULT_API_MODEL = 'oruk-fourier-2b'
DEFAULT_HF_REPO = 'oruk/oruk-fourier-2b'
DEFAULT_HF_REVISION = '8c2a8871f1304aa2f634da4fb95e24438c4945b9'


def _transcribe_api(
    audio_path: str,
    session: requests.Session,
    api_url: str,
    api_key: str,
    model: str,
    timeout: float = 120.0,
    max_retries: int = 5,
) -> str:
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {
        'model': model,
        'language': 'en',
        'response_format': 'json',
    }
    filename = os.path.basename(audio_path) or 'audio.wav'
    last_err: Optional[Exception] = None

    for attempt in range(max_retries):
        try:
            with open(audio_path, 'rb') as fp:
                resp = session.post(
                    api_url,
                    headers=headers,
                    files={'file': (filename, fp, 'audio/wav')},
                    data=data,
                    timeout=timeout,
                )
            if resp.status_code in (429, 500, 502, 503, 504) and attempt + 1 < max_retries:
                time.sleep(min(2 ** attempt, 16))
                continue
            resp.raise_for_status()
            payload = resp.json()
            text = payload.get('text', '')
            return ' '.join(str(text).split())
        except Exception as exc:
            last_err = exc
            if attempt + 1 < max_retries:
                time.sleep(min(2 ** attempt, 16))
                continue
            sys.stderr.write(f'[ERROR] {audio_path}: {exc}\n')
            return ''

    if last_err is not None:
        sys.stderr.write(f'[ERROR] {audio_path}: {last_err}\n')
    return ''


def _build_local_transcriber() -> Callable[[str], str]:
    import soundfile as sf
    import torch
    from transformers import AutoProcessor, Qwen3ASRForConditionalGeneration

    repo_id = os.environ.get('ORUK_HF_REPO', DEFAULT_HF_REPO)
    revision = os.environ.get('ORUK_HF_REVISION', DEFAULT_HF_REVISION)
    if torch.cuda.is_available():
        device, dtype = 'cuda', torch.bfloat16
    elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        device, dtype = 'mps', torch.bfloat16
    else:
        device, dtype = 'cpu', torch.float32

    processor = AutoProcessor.from_pretrained(repo_id, revision=revision)
    model = Qwen3ASRForConditionalGeneration.from_pretrained(repo_id, revision=revision, dtype=dtype)
    model.to(device).eval()

    def _run(audio_path: str) -> str:
        wav, _sr = sf.read(audio_path, dtype='float32', always_2d=False)
        if getattr(wav, 'ndim', 1) > 1:
            wav = wav.mean(axis=-1)
        inputs = processor.apply_transcription_request(audio=wav, language='en', return_tensors='pt')
        moved = {
            k: v.to(device=device, dtype=dtype) if getattr(v, 'is_floating_point', lambda: False)() else v.to(device)
            for k, v in inputs.items()
        }
        with torch.inference_mode():
            generated = model.generate(**moved)
        prompt_len = moved['input_ids'].shape[-1]
        text = processor.decode(generated[0, prompt_len:], return_format='transcription_only')
        return ' '.join(str(text).split())

    return _run


def main() -> int:
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: asr_api.py <in_scp> <out_trans>\n')
        return 1

    scp_path, out_path = sys.argv[1], sys.argv[2]
    backend = os.environ.get('ORUK_BACKEND', 'api').strip().lower()

    if backend == 'local':
        transcribe_fn = _build_local_transcriber()
    else:
        api_key = os.environ.get('ORUK_API_KEY', '').strip()
        if not api_key:
            sys.stderr.write(
                'ERROR: ORUK_API_KEY is not set and ./assets/API_KEY was not found.\n'
                'Put your key in models/oruk_fourier_2b_en/assets/API_KEY or set ORUK_API_KEY.\n'
            )
            return 1
        api_url = os.environ.get('ORUK_API_URL', DEFAULT_API_URL).strip()
        model_name = os.environ.get('ORUK_MODEL', DEFAULT_API_MODEL).strip()
        session = requests.Session()
        transcribe_fn = lambda p: _transcribe_api(p, session=session, api_url=api_url, api_key=api_key, model=model_name)

    with open(scp_path, 'r', encoding='utf-8') as scp_fp, open(out_path, 'w', encoding='utf-8') as out_fp:
        for idx, line in enumerate(scp_fp, start=1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                continue
            utt_id, audio_path = parts[0].strip(), parts[1].strip()
            rec_text = transcribe_fn(audio_path)
            out_fp.write(f'{utt_id}\t{rec_text}\n')
            out_fp.flush()
            if idx % 100 == 0:
                sys.stderr.write(f'[INFO] processed {idx} utterances\n')
                sys.stderr.flush()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
