#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import asyncio
import queue
import sys
import codecs
import time
import base64
import hashlib
import hmac
import json
import wave

import websockets
from websockets import client as ws_client


HAS_HOST: str = "wss://everest-stream.ximalaya.com"
URL = "/eop-websocket-service/api/v1/asr/stream"
MODEL = "ZH_HQ"
MAX_RETRY = 10

if len(sys.argv) != 3:
    sys.stderr.write("asr_api.py <in_scp> <out_trans>\n")
    exit(-1)

scp = codecs.open(sys.argv[1], 'r', 'utf8')
trans = codecs.open(sys.argv[2], 'w+', 'utf8')

# 重要：<Your AppKey>、<Your SecretKey>需要替换成客户自己的账号信息
# 前往珠峰AI开放平台https://everest-ai.ximalaya.com/申请个人开发者接入审核通过后创建应用获取
app_key = ''
secret_key = ''
with open('APP_KEY', 'r') as f:
    app_key = f.readline().strip()

with open('SECRET_KEY', 'r') as f:
    secret_key = f.readline().strip()


async def get_resp(ws, key: str, is_open_event, fail_queue):
    times = 0
    while True:
        try:
            data = await ws.recv()
            times += 1
            if times == 0:
                sys.stderr.write(f"uid:{key}, recv:{times}st pack:{data}" + '\n')
            else:
                sys.stderr.write(f"uid:{key}, recv:{times}st pack:{data}" + '\n')
            json_data = json.loads(data)
            code = json_data["code"]
            if code == 130:
                is_open_event.set()
            if code == 202001:
                text = json_data["data"]["nbest"][0]["sentence"]
                trans.write(key + '\t' + text + '\n')
                trans.flush()
            if code == 202002:
                times -= 1
                recv = json_data["data"]
                sys.stderr.write(f"uid:{key}, recv last pack, recv:{recv}, times:{times}, closed now......" + '\n')
                await ws.close()
                break
        except websockets.exceptions.ConnectionClosedError:
            sys.stderr.write(f"uid:{key}, connection closed" + '\n')
            fail_queue.put(1)
            break
        except Exception as e:
            sys.stderr.write(f"uid:{key}, e:{e}" + '\n')
            fail_queue.put(1)
            break


async def recognize(key, audio):
    send_times = 10
    t_last_cost_most = 0
    with wave.open(audio) as f:
        audio_data = f.readframes(-1)
    for _ in range(MAX_RETRY):
        fail_queue = queue.Queue()
        url = HAS_HOST + URL + get_handshake_params(app_key, secret_key, MODEL)
        async with ws_client.connect(url, ping_timeout=6000, open_timeout=6000, timeout=6000) as ws:
            is_open_event = asyncio.Event()
            recv_coro = asyncio.get_event_loop().create_task(get_resp(ws, key, is_open_event, fail_queue))
            # 等待握手完成
            try:
                await asyncio.wait_for(is_open_event.wait(), 10)
            except asyncio.TimeoutError:
                sys.stderr.write(f"uid:{key}, handShake timeout, retry it!" + '\n')
                await asyncio.sleep(0.1)
                continue
            sys.stderr.write(f"uid:{key}, handShake is success!" + '\n')
            init_pack = {
                "cmd": "start",
            }
            await ws.send(json.dumps(init_pack, ensure_ascii=False))
            pcm_data_len = len(audio_data)
            pack_size = 3200 if isinstance(audio_data, bytes) else 1600
            send_times = pcm_data_len // pack_size
            sys.stderr.write(f"uid:{key}, send 1st pack!" + '\n')
            for i in range(send_times):
                if i + 1 < send_times:
                    pack_size_cur = pack_size * i
                    audio = audio_data[pack_size_cur: pack_size_cur + pack_size]
                else:
                    audio = audio_data[pack_size_cur:]
                if isinstance(audio, bytes):
                    await ws.send(audio)
                else:
                    await ws.send(json.dumps({"audio": audio}))
            await ws.send(json.dumps({"cmd": "stop"}))
            sys.stderr.write(f"uid:{key}, send stop cmd" + '\n')
            t_send_last = time.time()
            await recv_coro
            if not fail_queue.empty():
                await ws.close()
                continue
            t_last_cost = time.time() - t_send_last
            if t_last_cost > t_last_cost_most:
                t_last_cost_most = t_last_cost
            return t_last_cost_most


def get_handshake_params(app_key: str, secret_key: str, model: str):
    # 创建一个包含URI参数的字典
    params = {
        'appKey': app_key,
        'mode': 1,
        'timestamp': int(time.time() * 1000),
        'model': model
    }
    # 按照参数名称对字典进行排序
    sorted_params = sorted(params.items())
    # 构建URI字符串
    uri = '&'.join([f"{key}={value}" for key, value in sorted_params])
    sign = calculate_signature(uri, secret_key)
    return "?" + uri + "&sign=" + sign


def calculate_signature(sorted_params: str, seed: str):
    # base64加密
    params_encoded_str = base64.b64encode(sorted_params.encode('utf-8'))
    # 创建HMAC对象
    hmac_obj = hmac.new(seed.encode("utf-8"), params_encoded_str, hashlib.sha1)
    # 计算HMAC值
    hmac_value = hmac_obj.digest()
    # HMAC值md5加密
    # 创建MD5哈希对象
    md5_hash = hashlib.md5()
    # 更新哈希对象以处理输入数据
    md5_hash.update(hmac_value)
    # 计算MD5哈希值并将其表示为十六进制字符串
    md5_hex = md5_hash.hexdigest()
    return md5_hex


if __name__ == '__main__':
    n = 0
    for l in scp:
        l = l.strip()
        if len(l.split()) == 2:  # scp format: "key\taudio"
            key, audio = l.split(maxsplit=1)
            sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
            sys.stderr.flush()
            asyncio.get_event_loop().run_until_complete(
                recognize(key, audio)
            )
            n += 1
        else:
            sys.stderr.write("Invalid line: " + l + "\n")
            sys.stderr.flush()

    scp.close()
    trans.close()
