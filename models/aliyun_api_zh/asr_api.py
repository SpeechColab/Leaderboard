#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
The code is base on official documentation at:
    https://help.aliyun.com/document_detail/92131.html
    一句话识别RESTful API2.0
'''
# Python 2.x 引入httplib模块
# import httplib
# Python 3.x 引入http.client模块
import http.client
import json
import sys
import codecs
import time

FORMAT = 'wav'
SAMPLE_RATE = 16000

MAX_RETRY=10
RETRY_INTERVAL=1.0

PUNC = True
ITN = True
VAD = False

APPKEY = ''
with open('APPKEY', 'r') as f:
    APPKEY = f.readline().strip()

TOKEN = ''
with open('TOKEN', 'r') as f:
    TOKEN = f.readline().strip()

# 服务请求地址
URL = 'http://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/asr'
URL += '?appkey=' + APPKEY
URL += '&format=' + FORMAT
URL += '&sample_rate=' + str(SAMPLE_RATE)

if PUNC:
    URL += '&enable_punctuation_prediction=' + 'true'
if ITN:
    URL += '&enable_inverse_text_normalization=' + 'true'
if VAD:
    URL += '&enable_voice_detection=' + 'true'

sys.stderr.write('Request: ' + URL + '\n')

def recognize(audio):
    with open(audio, mode = 'rb') as f:
        audio_data = f.read()

    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    # 设置HTTP请求头部
    httpHeaders = {
        'X-NLS-Token': TOKEN,
        'Content-type': 'application/octet-stream',
        'Content-Length': len(audio_data)
    }
    # Python 2.x 请使用httplib
    # conn = httplib.HTTPConnection(host)
    # Python 3.x 请使用http.client

    text = ''
    for i in range(MAX_RETRY):
        try:
            rec = ''
            conn = http.client.HTTPConnection(host)
            #print(conn)
            conn.request(method='POST', url=URL, body=audio_data, headers=httpHeaders)
            response = conn.getresponse()
            #print(response)

            r = response.read()
            sys.stderr.write(r.decode('utf8'))
            sys.stderr.write('\n\n')
            sys.stderr.flush()

            body = json.loads(r)

            status = body['status']
            is_success = body['message']
            if status == 20000000 and is_success == 'SUCCESS':
                rec = body['result']
                text = rec
                conn.close()
                break
            else :
                sys.stderr.write('Failed recognizing, will retry.\n')
                conn.close()
                time.sleep(RETRY_INTERVAL)
        except:
            sys.stderr.write('Exception, will retry.\n')
            conn.close()
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
        if (len(l.split()) == 2): # scp format: "key\taudio"
            key, audio = l.split(maxsplit=1)
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
