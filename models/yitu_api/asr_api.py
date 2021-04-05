#!/usr/bin/env python2
# coding=utf-8
'''
code is based on official demo at:
    https://speech.yitutech.com/devdoc/shortaudio

'''

import hmac
import base64
import hashlib
import os
import time
import requests
import sys
import codecs

reload(sys)
sys.setdefaultencoding('utf-8')

# 填入语音识别url地址
ASR_URL = 'http://asr-prod.yitutech.com/v2/asr'
# 填入需要识别语音文件路径
#AUDIO_PATH = 'test.wav'
# 按照语音格式来填写，wav为pcm，（更多信息请参见开发文档https://speech.yitutech.com/devdoc/shortaudio 第2部分音频要求）
AUDIO_AUE = 'pcm'

# 填入用户DevId，（更多信息请参见开发文档https://speech.yitutech.com/devdoc/access）
with open('DEV_ID', 'r') as f:
    DevId = f.readline().strip()
# 填入DevKey，（更多信息请参见开发文档https://speech.yitutech.com/devdoc/access）
with open('DEV_KEY', 'r') as f:
    DevKey = f.readline().strip()

MAX_RETRY = 10


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("rest_api.py <in_scp> <out_trans>\n")
        exit(-1)

    SCP = sys.argv[1]
    TRANS = sys.argv[2]

    scp_file = codecs.open(SCP, 'r', 'utf8')
    trans_file = codecs.open(TRANS, 'w+', 'utf8')

    n = 0
    for l in scp_file:
        l = l.strip()
        if l == '':
            continue

        key, audio = l.split('\t')
        sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
        sys.stderr.flush()

        with open(audio, "rb") as audio_file:
            encoded_string = base64.b64encode(audio_file.read())
            basee64_file = encoded_string.decode('utf-8')

        rec_text = ''
        for i in range(MAX_RETRY):
            try:
                rec_text = ''
                # 消息头
                time_ts = str(int(time.time()))
                param_string = str(DevId) + time_ts
                sign = hmac.new(DevKey.encode(), param_string.encode(), digestmod=hashlib.sha256).hexdigest()
                headers = {'x-dev-id': str(DevId), 'x-request-send-timestamp': time_ts, 'x-signature': sign}

                # 消息实体
                lang = 1    # 默认值，更多信息请参见开发文档https://speech.yitutech.com/devdoc/shortaudio 第5部分 请求参数
                scene = 0   # 默认值，更多信息请参见开发文档https://speech.yitutech.com/devdoc/shortaudio 第5部分 请求参数
                aue = ''
                useCustomWordsIds = [] # 用户自定义热词库ID
                body = {'audioBase64': basee64_file, 'lang': lang, 'scene': scene, 'aue': AUDIO_AUE, 'useCustomWordsIds': useCustomWordsIds}

                # 发起请求
                r = requests.post(ASR_URL, json=body, headers=headers)
                if r.status_code == 200:
                    sys.stderr.write('requests rtn:{} text:{}\n'.format(r.json()['rtn'], r.json()['resultText']))
                    result = r.json()['resultText']
                    if (result != None) and (result != ''):
                        rec_text = result
                        break
                else:
                    sys.stderr.write('requests fails code:{} details:{}\n'.format(r.status_code, r.json()))
                    sys.stderr.write('will retry.\n')
                    rec_text = ''
                    time.sleep(1)
                    continue
            except:
                sys.stderr.write("exception, retrying.\n")
                rec_text = ''
                time.sleep(1)
                continue

        trans_file.write(key + '\t' + rec_text + '\n')
        trans_file.flush()
        n += 1

    scp_file.close()
    trans_file.close()

