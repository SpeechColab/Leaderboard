#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import sys
import codecs
import time

accessKeyId = ""
with open('accessKeyId', 'r') as f:
    accessKeyId = f.readline().strip()

accessKeySecret = ""
with open('accessKeySecret', 'r') as f:
    accessKeySecret = f.readline().strip()


if __name__ == "__main__":
    print("decoding finish")
    config_command = "./ossutil64 config -e oss-cn-hangzhou.aliyuncs.com -i {accessKeyId} -k {accessKeySecret}".format(accessKeyId=accessKeyId, accessKeySecret=accessKeySecret)
    config_res = os.popen(config_command)
    time.sleep(5)

    bucket = "oss://speechiotest"
    del_command = "./ossutil64 rm {bucket} -b -a -r -f -e oss-cn-hangzhou.aliyuncs.com".format(bucket=bucket)
    print("del_command", del_command)
    del_res = os.popen(del_command)
