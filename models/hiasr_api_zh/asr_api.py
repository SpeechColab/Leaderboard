#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import wave
import grpc
import json
import sys
import codecs
import os
import time

ROOT_DIR = os.path.dirname(__file__)
sys.path.append('{}/assets'.format(ROOT_DIR))
MAX_RETRY=10
RETRY_INTERVAL=1.0

import asr_pb2, asr_pb2_grpc

with open('{}/assets/cert'.format(ROOT_DIR), 'rb') as fin:
  root = fin.read()
credentials = grpc.ssl_channel_credentials(root)


def generate_stream_request(key, audio):
  with wave.open(audio) as f:
    audio_data = f.readframes(-1)

  request = asr_pb2.Recognize_Request()
  request.session_id = key
  for i in range(0, len(audio_data), 3200):
    request.audio_data = audio_data[i:i + 3200]
    yield request


def recognize(key, audio):
  text = ""
  for _ in range(MAX_RETRY):
    try:
      with grpc.secure_channel("hiasr-wenetasr.uat.ximalaya.com:443", credentials) as channel:
        stub = asr_pb2_grpc.ASRStub(channel)
        response = stub.Recognize(generate_stream_request(key, audio))
        for r in response:
          continue
        text = json.loads(r.response_json)['nbest'][0]['sentence']
        break
    except:
      sys.stderr.write('Exception, will retry.\n')
      time.sleep(RETRY_INTERVAL)
  return text


if __name__ == '__main__':
  if len(sys.argv) != 3:
    sys.stderr.write("asr_api.py <in_scp> <out_trans>\n")
    exit(-1)

  scp = codecs.open(sys.argv[1], 'r', 'utf8')
  trans = codecs.open(sys.argv[2], 'w+', 'utf8')

  n = 0
  for l in scp:
    l = l.strip()
    if (len(l.split()) == 2):  # scp format: "key\taudio"
      key, audio = l.split(maxsplit=1)
      sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
      sys.stderr.flush()

      text = ''
      text = recognize(key, audio)

      trans.write(key + '\t' + text + '\n')
      trans.flush()
      n += 1
    else:
      sys.stderr.write("Invalid line: " + l + "\n")
      sys.stderr.flush()

  scp.close()
  trans.close()
