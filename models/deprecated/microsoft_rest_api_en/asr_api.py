#!/usr/bin/env python3
# Request module must be installed.
# Run pip install requests if necessary.
# doc: https://docs.azure.cn/zh-cn/cognitive-services/speech-service/rest-speech-to-text

import sys
import requests, json, time
import codecs

#def get_token(subscription_key):
#    fetch_token_url = 'https://chinaeast2.api.cognitive.azure.cn/sts/v1.0/issueToken'
#    headers = {
#        'Ocp-Apim-Subscription-Key': subscription_key
#    }
#    response = requests.post(fetch_token_url, headers=headers)
#    access_token = str(response.text)
#    print(access_token)
#
#get_token(subscription_key)

LANG='en-US'
MAX_RETRY=10
RETRY_INTERVAL=1.0

SUBSCRIPTION_KEY=''
with open('SUBSCRIPTION_KEY', 'r') as f:
    SUBSCRIPTION_KEY = f.readline().strip()

def recognize(audio):
    url='https://chinaeast2.stt.speech.azure.cn/speech/recognition/conversation/cognitiveservices/v1?language=' + LANG

    headers = {
        'Accept': 'application/json;text/xml',
        'Content-Type': 'audio/wav;codecs="audio/pcm";samplerate=16000',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'format': 'detailed'
    }

    with open(audio, 'rb') as f:
        audio_data = f.read()

    text = ''
    for i in range(MAX_RETRY):
        try:
            rec=''
            r = requests.post(url, data=audio_data, headers=headers)
            sys.stderr.write(r.text + '\n')
            sys.stderr.flush()
            rec = json.loads(r.text)['DisplayText']
            if rec != '':
                text = rec
                break
            else:
                sys.stderr.write("empty result, retrying\n")
                time.sleep(RETRY_INTERVAL)
        except:
            sys.stderr.write("exception, retrying\n")
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
