#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
The code is base on official documentation at:
    https://help.aliyun.com/document_detail/72153.html
    开发指南 -> 获取 Token
'''
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
from datetime import datetime

access_key_id = ''
access_key_secret = ''

with open('ACCESS_KEY_ID', 'r') as f:
    access_key_id = f.readline().strip()

with open('ACCESS_KEY_SECRET', 'r') as f:
    access_key_secret = f.readline().strip()

# 创建AcsClient实例
client = AcsClient(
   access_key_id,
   access_key_secret,
   "cn-shanghai"
);

# 创建request，并设置参数
request = CommonRequest()
request.set_method('POST')
request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
request.set_version('2019-02-28')
request.set_action_name('CreateToken')

response_json_bytes = client.do_action_with_exception(request)
print(response_json_bytes)
response = json.loads(response_json_bytes)

token_id = response['Token']['Id']
with open('TOKEN', 'w+') as f:
    f.write(token_id + '\n')

expire_date_sec = response['Token']['ExpireTime']
expire_date_str = datetime.fromtimestamp(int(expire_date_sec)).strftime("%A, %B %d, %Y %I:%M:%S")
with open('TOKEN_EXPIRE_TIME', 'w+') as f:
    f.write(expire_date_str + '\n')


