#!/usr/bin/env bash
APP_ID=`cat APP_ID`
APP_KEY=`cat APP_KEY`
EXPIRE=36000s # 10 hrs
REQ="{ \"appid\": \"$APP_ID\", \"appkey\": \"$APP_KEY\", \"exp\": \"$EXPIRE\" }"

echo $REQ

curl -X POST \
    -H "Content-Type: application/json" \
    --data "$REQ" \
    https://api.zhiyin.sogou.com/apis/auth/v1/create_token \
    > TOKEN
