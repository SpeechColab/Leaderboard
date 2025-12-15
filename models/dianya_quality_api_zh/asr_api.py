#!/usr/bin/env python3
# coding: utf-8

import sys
import os
import time
import json
import codecs
import requests

API_KEY_FILE = 'API_KEY'
DIANYA_URL = 'https://api.dianyaai.com/api/transcribe/upload?transcribe_only=true&short_asr=true&model_name=quality'
MAX_RETRY = 5
RETRY_INTERVAL = 0.1
QPS_INTERVAL = 0.2
TIMEOUT = 30


def load_api_key():
    try:
        with open(API_KEY_FILE, 'r', encoding='utf8') as f:
            return f.readline().strip()
    except Exception as e:
        sys.stderr.write(f'Failed to load API key from {API_KEY_FILE}: {e}\n')
        sys.exit(1)


def recognize(api_key, audio_path):
    for attempt in range(MAX_RETRY):
        try:
            with open(audio_path, 'rb') as audio_file:
                files = {
                    'payload': (os.path.basename(audio_path), audio_file, 'audio/wav')
                }
                headers = {
                    'Authorization': f'Bearer {api_key}'
                }
                response = requests.post(
                    DIANYA_URL,
                    headers=headers,
                    files=files,
                    timeout=TIMEOUT,
                )

            if response.status_code != 200:
                sys.stderr.write(f'HTTP {response.status_code} from Dianya, attempt {attempt + 1}/{MAX_RETRY}.\n')
                time.sleep(RETRY_INTERVAL)
                continue

            try:
                data = response.json()
            except ValueError:
                sys.stderr.write(f'Invalid JSON response from Dianya on attempt {attempt + 1}/{MAX_RETRY}.\n')
                time.sleep(RETRY_INTERVAL)
                continue

            status = data.get('status')
            if status != 'ok':
                sys.stderr.write(f'Dianya returned non-ok status "{status}" on attempt {attempt + 1}/{MAX_RETRY}.\n')
                time.sleep(RETRY_INTERVAL)
                continue

            text = data.get('data', '')
            if text is None:
                text = ''
            return str(text).strip()

        except Exception as e:
            sys.stderr.write(f'Exception when calling Dianya on attempt {attempt + 1}/{MAX_RETRY}: {e}\n')
            time.sleep(RETRY_INTERVAL)
            continue

    sys.stderr.write(f'Failed to recognize {audio_path} after {MAX_RETRY} attempts.\n')
    return ''


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('asr_api.py <in_scp> <out_trans>\n')
        sys.exit(1)

    in_scp = sys.argv[1]
    out_trans = sys.argv[2]

    api_key = load_api_key()

    try:
        scp_file = codecs.open(in_scp, 'r', 'utf8')
    except Exception as e:
        sys.stderr.write(f'Failed to open input scp file {in_scp}: {e}\n')
        sys.exit(1)

    try:
        trans_file = codecs.open(out_trans, 'w+', 'utf8')
    except Exception as e:
        sys.stderr.write(f'Failed to open output transcription file {out_trans}: {e}\n')
        sys.exit(1)

    # 预读所有非空行以便统计总数
    lines = [line.strip() for line in scp_file if line.strip()]
    total = len(lines)

    n = 0
    for idx, line in enumerate(lines):
        if '\t' in line:
            key, audio = line.split('\t', 1)
        else:
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                sys.stderr.write(f'Invalid line in scp file (skip): {line}\n')
                continue
            key, audio = parts

        sys.stderr.write(f'{n}\tkey:{key}\taudio:{audio}\n')
        sys.stderr.flush()

        time.sleep(QPS_INTERVAL)
        rec_text = recognize(api_key, audio)

        trans_file.write(key + '\t' + rec_text + '\n')
        trans_file.flush()
        n += 1

        # 进度行，供外部脚本解析
        sys.stderr.write(f'[DY_PROGRESS] {idx + 1}/{total} {audio}\n')
        sys.stderr.flush()

    scp_file.close()
    trans_file.close()
