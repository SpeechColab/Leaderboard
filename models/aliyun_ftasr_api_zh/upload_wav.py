#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
录音文件识别 接口说明
https://help.aliyun.com/document_detail/90727.html
通过ossutil命令获取文件URL
egs: 为目标存储空间examplebucket下的文件exampleobject.png生成文件URL，并指定超时时间为3600秒。
     ./ossutil64 sign oss://examplebucket/exampleobject.png --timeout 3600
'''
import os
import sys
import codecs
import time

access_key_id = ""
with open('ACCESS_KEY_ID', 'r') as f:
    access_key_id = f.readline().strip()

access_key_secret = ""
with open('ACCESS_KEY_SECRET', 'r') as f:
    access_key_secret = f.readline().strip()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.stderr.write("upload_wav.py <wav_scp> <oss_out_scp> <dir> <test_time>\n")
        exit(-1)

    wavDict = {}
    wavFile = codecs.open(sys.argv[1], 'r',  'utf8') 
    oss_config_path = sys.argv[3]
    test_time = sys.argv[4]

    # OSS bucket
    bucket = "oss://speechiotest-{test_time}/".format(test_time=test_time)
    for meta in wavFile:
        meta = meta.split()
        wavId = meta[0]
        wavPath = meta[1]
        wavDict[wavId] = wavPath
    # 创建bucket
    md_command = "./ossutil64 mb {bucket} -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(bucket=bucket, access_key_id=access_key_id, access_key_secret=access_key_secret)
    md_res = os.popen(md_command)

    time.sleep(5)
    ossPath = bucket + "wav/"
    ossWavFile = codecs.open(sys.argv[2], 'w+', 'utf8')
    for idx, wav in wavDict.items():
        # 上传文件
        upload_command = "./ossutil64 cp {wav} {osspath} -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(wav=wav, osspath=ossPath, access_key_id=access_key_id, access_key_secret=access_key_secret)
        upload_res = os.popen(upload_command) 
        # 生成签名URL
        sign_command = "./ossutil64 sign {osspath}{idx}.wav --timeout {times} -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(osspath=ossPath, idx=idx, times=32400, access_key_id=access_key_id, access_key_secret=access_key_secret)
        res = os.popen(sign_command)
        for audio in res:
            ossWavFile.write(idx + "\t" + audio)
            break
