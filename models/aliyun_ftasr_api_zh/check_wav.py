#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import oss2


access_key_id = ""
with open('ACCESS_KEY_ID', 'r') as f:
    access_key_id = f.readline().strip()

access_key_secret = ""
with open('ACCESS_KEY_SECRET', 'r') as f:
    access_key_secret = f.readline().strip()

if __name__ == "__main__":
    BucketName = sys.argv[1] 
    wavOssPath = codecs.open(sys.argv[2], 'r',  'utf8')
    wavOssLossPath = codecs.open(sys.argv[3], 'w+', 'utf8')

    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', BucketName)

    for wav in wavOssPath:
        idx = wav.split()[0]
        exist = bucket.object_exists('wav/{idx}.wav'.format(idx=idx))
        if exist:
            print('{} object exist'.format(wav.split()))
        else:
            print('{} object not exist'.format(wav.split()))
            wavOssLossPath.write(wav)
            wavOssLossPath.flush()
  
    wavOssPath.close()      
