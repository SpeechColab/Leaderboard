#!/usr/bin/env python3
# -*- coding: utf8 -*-
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
    if len(sys.argv) != 3:
        sys.stderr.write("del_oss_bucket.py <dir> <bucket_name>\n")
        exit(-1)
    print("decoding finish")
    oss_config_path = sys.argv[1]
    bucketName = sys.argv[2]

    bucket = "oss://{bucketName}".format(bucketName=bucketName)
    del_command = "./ossutil64 rm {bucket} -b -a -r -f -e oss-cn-hangzhou.aliyuncs.com -i {access_key_id} -k {access_key_secret}".format(bucket=bucket, access_key_id=access_key_id, access_key_secret=access_key_secret)
    del_res = os.popen(del_command)
    for u in del_res:
        print(u)
    time.sleep(20)
