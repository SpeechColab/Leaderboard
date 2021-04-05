#!/usr/bin/env python3
# coding=utf-8
'''
code is based on DUI official doc at:
    https://www.duiopen.com/docs/ct_asr_sentence
'''

import os
import time
import sys
import codecs
import subprocess
import json

SERVICE_URL = 'https://lasr.duiopen.com/lasr-sentence-api/v2/sentence'

MAX_RETRY = 10
RETRY_INTERVAL=1.0

with open('PRODUCT_ID', 'r') as f:
    PRODUCT_ID = f.readline().strip()

with open('API_KEY', 'r') as f:
    API_KEY= f.readline().strip()

URL=SERVICE_URL + '?' + 'productId=' + PRODUCT_ID + '&' + 'apiKey=' + API_KEY

PARAMS='\'{"request_id":"", "audio": {"audio_type": "wav","sample_rate": 16000,"channel": 1,"sample_bytes": 2}, "asr":{"use_vad":true, "use_itn":true, "use_puctuation":true}}\''

#f = 'test.wav'
#cmd='curl -X POST -s -H "Content-Type: multipart/form-data"' + ' -F params=' + PARAMS + ' -F file=@' + f + ' "' + URL + '"'
#print(cmd)
#
#r = subprocess.getoutput(cmd)
#print(json.loads(r)['data']['result'][0]['onebest'])

def recognize(audio):
    text = ''
    for i in range(MAX_RETRY):
        try:
            rec=''
            cmd='curl -X POST -s -H "Content-Type: multipart/form-data"' + ' -F params=' + PARAMS + ' -F file=@' + audio + ' "' + URL + '"'
            # print(cmd)
            r = subprocess.getoutput(cmd)
            # print(r)
            sys.stderr.write(r + '\n')
            sys.stderr.flush()
            
            sentences = json.loads(r)['data']['result']
            for s in sentences:
                rec += s['onebest']

            if (rec != None) and (rec != ''):
                text = rec
                break
            else:
                sys.stderr.write("empty result or null response, retrying.\n")
                time.sleep(RETRY_INTERVAL)
        except:
            sys.stderr.write("exception, retrying.\n")
            time.sleep(RETRY_INTERVAL)

    return text

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("asr_api.py <in_scp> <out_trans>\n")
        exit(-1)

    scp   = codecs.open(sys.argv[1], 'r',  'utf8')
    trans = codecs.open(sys.argv[2], 'w+', 'utf8')

    n = 0
    for l in scp:
        l = l.strip()
        if (len(l.split('\t')) == 2): # scp format: "key\taudio"
            key, audio = l.split(sep="\t", maxsplit=1)
            sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
            sys.stderr.flush()

            text = ''
            text = recognize(audio)

            trans.write(key + '\t' + text + '\n')
            trans.flush()
            n += 1
        else:
            sys.stderr.write("Invalid line: " + l + "\n")
            sys.stderr.flush()

    scp.close()
    trans.close()
