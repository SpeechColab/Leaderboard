#!/usr/bin/env python3
import base64
import requests
import json
import io, sys
import codecs
import time

FORMAT='LINEAR16'
SAMPLE_RATE=16000
LANG='zh-cmn-Hans-CN'

MAX_RETRY=10
RETRY_INTERVAL=1.0

APP_ID=''
with open('APP_ID', 'r') as f:
    APP_ID = f.readline().strip()

TOKEN=''
with open('TOKEN', 'r') as f:
    token_string = f.readline().strip()
    TOKEN = json.loads(token_string)['token']


def encode_audio(audio):
    with open(audio, "rb") as audio_file:
        encoded_string = base64.b64encode(audio_file.read())
    return encoded_string.decode('ascii')

def recognize(audio):
    data = {
        'config': {
            'encoding': FORMAT,
            'sample_rate_hertz': SAMPLE_RATE,
            'language_code': LANG
        },
        'audio': {
            'content': encode_audio(audio)
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Appid': APP_ID,
        'Authorization': 'Bearer ' + TOKEN
    }

    text = ''
    for i in range(MAX_RETRY):
        try:
            rec = ''
            r = requests.post('https://api.zhiyin.sogou.com/apis/asr/v1/recognize', data=json.dumps(data), headers=headers)
            sys.stderr.write(r.text + '\n')
            sys.stderr.flush()
            for s in json.loads(r.text)['results']:
                rec += s['alternatives'][0]['transcript']

            if rec != "":
                text = rec
                break
            else:
                sys.stderr.write("empty result, retrying.\n")
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
