#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
录音文件识别 接口说明
https://help.aliyun.com/document_detail/90727.html
通过ossutil命令获取文件URL
egs: 为目标存储空间examplebucket下的文件exampleobject.png生成文件URL，并指定超时时间为3600秒。
     ./ossutil64 sign oss://examplebucket/exampleobject.png --timeout 3600
'''
import sys
import os
import time
import codecs
import oss2


access_key_id = ""
with open('ACCESS_KEY_ID', 'r') as f:
    access_key_id = f.readline().strip()

access_key_secret = ""
with open('ACCESS_KEY_SECRET', 'r') as f:
    access_key_secret = f.readline().strip()

def retry_upload(wavId, wavPath, ossPath, times=10):
    upload_command = "./ossutil64 cp {wav} {osspath} -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(wav=wavPath, osspath=ossPath, access_key_id=access_key_id, access_key_secret=access_key_secret)
    upload_res = os.popen(upload_command)
    for r in upload_res:
        print(wavId + "\t" + r.strip())
    re_exist = ossbucket.object_exists('wav/{wavId}.wav'.format(wavId=wavId))
    retry_flag = False
    if re_exist:
        print('{wavId} {wavPath} object exist, retry {time} times successfully.'.format(wavId=wavId, wavPath=wavPath, time=10-times))
        sign_command = "./ossutil64 sign {osspath}{idx}.wav --timeout {times} -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(osspath=ossPath, idx=wavId, times=32400, access_key_id=access_key_id, access_key_secret=access_key_secret)
        res = os.popen(sign_command)
        for audio in res:
            wavOssFile.write(wavId + "\t" + audio)
            break
        retry_flag = True
        return retry_flag
    elif times > 0:
        time.sleep(5)
        print('{wavId} {wavPath} object not exist, will retry upload {time} times.'.format(wavId=wavId, wavPath=wavPath, time=times))
        retry_flag = retry_upload(wavId, wavPath, ossPath, times=times-1)
    return retry_flag


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.stderr.write("check_wav.py <bucket_name> <wav_scp> <wav_loss_scp> <oss_out_scp>\n")
        exit(-1)

    bucketName = sys.argv[1] 
    wavFile = codecs.open(sys.argv[2], 'r',  'utf8')
    wavLossFile = codecs.open(sys.argv[3], 'w+', 'utf8')
    wavOssFile = codecs.open(sys.argv[4], 'w+', 'utf8')

    auth = oss2.Auth(access_key_id, access_key_secret)
    ossbucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', bucketName)

    bucket = "oss://{bucketName}".format(bucketName=bucketName)
    ossPath = bucket + "/wav/" 
    for meta in wavFile:
        wavmeta = meta.split()
        wavId = wavmeta[0]
        wavPath = wavmeta[1]
        
        exist = ossbucket.object_exists('wav/{wavId}.wav'.format(wavId=wavId))
        if exist:
            print('{wavId} {wavPath} object exist'.format(wavId=wavId, wavPath=wavPath))
            # 生成签名URL
            sign_command = "./ossutil64 sign {osspath}{idx}.wav --timeout {times} -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(osspath=ossPath, idx=wavId, times=32400, access_key_id=access_key_id, access_key_secret=access_key_secret)
            res = os.popen(sign_command)
            for audio in res:
                wavOssFile.write(wavId + "\t" + audio)
                break
        else:
            print('{wavId} {wavPath} object not exist'.format(wavId=wavId, wavPath=wavPath))
            retry_flag = retry_upload(wavId, wavPath, ossPath, times=10)
            if not retry_flag:
                wavLossFile.write(meta)
                wavLossFile.flush()
  
    wavFile.close()      
    wavLossFile.close()
