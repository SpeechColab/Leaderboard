#!/usr/bin/env python3
# coding=utf-8
'''
code is based on DUI official doc at:
    https://www.duiopen.com/docs/ct_asr_sentence
'''

import os, sys
import argparse
import time
import subprocess
import json

SERVICE_URL = 'https://lasr.duiopen.com/lasr-sentence-api/v2/sentence'

MAX_RETRY = 2
RETRY_INTERVAL=1.0

with open('PRODUCT_ID', 'r') as f:
    PRODUCT_ID = f.readline().strip()

with open('API_KEY', 'r') as f:
    API_KEY= f.readline().strip()

URL=SERVICE_URL + '?' + 'productId=' + PRODUCT_ID + '&' + 'apiKey=' + API_KEY

PARAMS='\'{"request_id":"", "audio": {"audio_type": "wav","sample_rate": 16000,"channel": 1,"sample_bytes": 2}, "asr":{"use_vad":true, "use_itn":true, "use_puctuation":true}}\''

def recognize(audio):
    for i in range(MAX_RETRY):
        cmd='curl -X POST -s -H "Content-Type: multipart/form-data"' + ' -F params=' + PARAMS + ' -F file=@' + audio + ' "' + URL + '"'
        #print(cmd)
        r = subprocess.run(cmd, shell=True, capture_output=True, encoding='utf-8')
        print(r.stdout, file=sys.stderr, flush=True)
        
        rec=''
        for s in json.loads(r.stdout)['data']['result']:
            rec += s['onebest']

        if (rec != None) and (rec != ''):
            return rec
        else:
            print("empty result or null response, retrying.", file=sys.stderr, flush=True)
            time.sleep(RETRY_INTERVAL)

    return ''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('scp_path', type=str)
    parser.add_argument('trans_path', type=str)
    args = parser.parse_args()

    num_utts = 0
    with open(args.scp_path, 'r',  encoding='utf8') as scp, open(args.trans_path, 'w+', encoding='utf8') as trans:
        lines = [ l.strip() for l in scp if l.strip() ]
        for l in lines:
            cols = l.split()
            if (len(cols) == 2):
                key, audio = cols
                print(F'{num_utts}\tkey:{key}\taudio:{audio}', file=sys.stderr, flush=True)
                text = recognize(audio)
                print(key + '\t' + text, file=trans, flush=True)
                num_utts += 1
            else:
                print(F'Invalid line: {l}', file=sys.stderr, flush=True)
