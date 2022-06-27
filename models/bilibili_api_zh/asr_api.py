#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
    一句话识别 python SDK
'''
import sys, json, time
import codecs
import base64
import requests
URL = "https://asr-speechio.bilibili.com/asr"


def is_alnum(c):
    """
    简单判断字符是否是英文字母数字
    """
    return c.isdigit() or 'a' <= c <= 'z' or 'A' <= c <= 'Z'


def trim(s):
    res = ''
    for i in range(len(s)):
        if s[i] == ' ':
            if 0 < i < len(s) and (is_alnum(s[i - 1]) or is_alnum(s[i + 1])):
                res += s[i]
        else:
            res += s[i]
    return res

with open('TOKEN', 'r') as f:
    token = f.readline().strip()

def recognize(audio, key):
    text = ''
    for i in range(10):
        try:
            with open(audio, "rb") as f:
                data = f.read()
                base64Wav = base64.b64encode(data)
                base64Wav = base64Wav.decode()
                param = {"wav": base64Wav, 
                        "key": key, 
                        "token": token}
                headers = {"Content-Type": 'application/json'}
                rep = requests.post(url=URL, data=json.dumps(param), headers=headers)
                text = trim(json.loads(rep.text)["text"])
                return text, True
        except Exception as e:
            sys.stderr.write("Exception %s, will retry.\n"%(e))
            sys.stderr.flush()
            continue
    return text, False

if __name__ == "__main__":

    try:
        if len(sys.argv) != 3:
            sys.stderr.write("asr_api.py <in_scp> <out_trans>\n")
            exit(-1)
        scp = sys.argv[1]
        trans = sys.argv[2]
        scpFile = codecs.open(scp, 'r', 'utf8')
        transFile = codecs.open(trans, 'w+', 'utf-8')
        for l in scpFile:
            if len(l.strip().split()) == 2:
                key, audio = l.split()
                text, flag = recognize(audio, key)
                if not flag:
                    #sys.stderr.write("Unknown error.\n")
                    sys.stderr.write("key error: " + key + '\n')
                    #break
                transFile.write(key + '\t' + text + '\n')
                transFile.flush()
            else:
                sys.stderr.write("Invalid line: " + l + "\n")
                sys.stderr.flush()
        scpFile.close()
        transFile.close()
    except Exception as e:
        sys.stderr.write(e)
