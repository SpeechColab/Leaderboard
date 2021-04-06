#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
this code is based on official demo at:
    https://cloud.tencent.com/document/product/1093/35734
    一句话识别 python SDK
    install SDK: pip install tencentcloud-sdk-python
'''

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import base64
import sys, codecs, json, time

try:
    if len(sys.argv) != 3:
        sys.stderr.write("rest_api.py <in_scp> <out_trans>\n")
        exit(-1)

    SCP = sys.argv[1]
    TRANS = sys.argv[2]

    MAX_RETRY = 10

    #重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
    #请参考接口说明中的使用步骤1进行获取。
    secret_id = ''
    secret_key = ''
    with open('SECRET_ID', 'r') as f:
        secret_id = f.readline().strip()

    with open('SECRET_KEY', 'r') as f:
        secret_key = f.readline().strip()

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

        rec_text = ''

        #读取文件以及base64
        with open(audio, mode='rb') as f:
          data = f.read()
          dataLen = len(data)
          base64Wav = base64.b64encode(data)

        for i in range(MAX_RETRY):
            try:
                cred = credential.Credential(secret_id, secret_key)
                httpProfile = HttpProfile()
                httpProfile.endpoint = "asr.tencentcloudapi.com"
                clientProfile = ClientProfile()
                clientProfile.httpProfile = httpProfile
                client = asr_client.AsrClient(cred, "ap-shanghai", clientProfile)

                #发送请求
                req = models.SentenceRecognitionRequest()
                params = {"ProjectId":0,"SubServiceType":2,"EngSerViceType":"16k","SourceType":1,"Url":"","VoiceFormat":"wav","UsrAudioKey":"session-123", "Data":base64Wav, "DataLen":dataLen}
                req._deserialize(params)

                resp = client.SentenceRecognition(req)
                #print(resp.to_json_string())
                sys.stderr.write(resp.to_json_string())
                sys.stderr.write('\n')
                sys.stderr.flush()
                rec_text = json.loads(resp.to_json_string())['Result']
                if rec_text != '':
                    break
                sys.stderr.write('Empty result, retrying.\n')
                time.sleep(1)
            except:
                sys.stderr.write('Exception, retrying.\n')
                rec_text = ''
                time.sleep(1)
                continue

        trans_file.write(key + '\t' + rec_text + '\n')
        trans_file.flush()
        n += 1

    scp_file.close()
    trans_file.close()

except TencentCloudSDKException as err:
    print(err)
