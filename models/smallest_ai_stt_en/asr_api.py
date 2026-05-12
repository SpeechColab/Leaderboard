#!/usr/bin/env python3
# coding: utf8
"""
Smallest AI Pulse STT — WSS streaming transcription for SpeechColab Leaderboard.
Docs: https://docs.smallest.ai/waves/documentation/speech-to-text-pulse/realtime-web-socket/quickstart
API:  wss://api.smallest.ai/waves/v1/pulse/get_text
"""
import sys
import asyncio
import json
import time
import wave
import websockets

WSS_ENDPOINT = "wss://api.smallest.ai/waves/v1/pulse/get_text"
LANGUAGE = "en"
CHUNK_SIZE = 4096  # bytes per chunk, as recommended by Pulse docs
MAX_RETRIES = 5
RETRY_DELAY = 5
QPS_INTERVAL = 0.2  # seconds between requests to avoid rate limiting


async def transcribe_ws(audio_path: str, api_key: str) -> str:
    uri = f"{WSS_ENDPOINT}?language={LANGUAGE}"
    headers = {"Authorization": f"Bearer {api_key}"}
    final_transcripts = []

    async with websockets.connect(uri, extra_headers=headers) as ws:
        # Read raw PCM frames from WAV file (strips WAV header)
        with wave.open(audio_path) as wf:
            pcm_data = wf.readframes(wf.getnframes())

        # Stream audio in binary chunks
        for i in range(0, len(pcm_data), CHUNK_SIZE):
            await ws.send(pcm_data[i:i + CHUNK_SIZE])

        # Signal end of audio stream
        await ws.send(json.dumps({"type": "close_stream"}))

        # Collect final transcripts until server signals is_last
        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            if data.get("is_final"):
                text = data.get("transcript", "").strip()
                if text:
                    final_transcripts.append(text)

            if data.get("is_last"):
                break

    return " ".join(final_transcripts)


async def transcribe_with_retry(audio_path: str, api_key: str) -> str:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return await transcribe_ws(audio_path, api_key)
        except Exception as e:
            sys.stderr.write(f"Attempt {attempt}/{MAX_RETRIES} failed for {audio_path}: {e}\n")
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY)
            else:
                sys.stderr.write(f"All retries exhausted for {audio_path}, writing empty.\n")
                return ""
    return ""


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.stderr.write("Usage: asr_api.py <wav.scp> <output_trans> <api_key_file>\n")
        sys.exit(1)

    scp_path, out_path, key_file = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(key_file, "r") as f:
        api_key = f.read().strip()

    with open(scp_path, "r", encoding="utf8") as scp, \
         open(out_path, "w", encoding="utf8") as out:

        lines = [l.strip() for l in scp if l.strip()]
        total = len(lines)

        loop = asyncio.get_event_loop()

        for n, line in enumerate(lines):
            parts = line.split("\t", 1)
            if len(parts) != 2:
                sys.stderr.write(f"Skipping malformed line: {line}\n")
                continue

            audio_id, audio_path = parts
            sys.stderr.write(f"{n}\tid:{audio_id}\taudio:{audio_path}\n")
            sys.stderr.flush()

            time.sleep(QPS_INTERVAL)
            text = loop.run_until_complete(transcribe_with_retry(audio_path, api_key))
            out.write(f"{audio_id}\t{text}\n")
            out.flush()

            sys.stderr.write(f"[PROGRESS] {n + 1}/{total}\n")
            sys.stderr.flush()

        loop.close()
