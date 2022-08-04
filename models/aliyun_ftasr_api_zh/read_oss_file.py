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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("read_oss_file.py <wav_scp> <oss_out_scp>\n")
        exit(-1)

    idxList = []
    wavFile = codecs.open(sys.argv[1], 'r',  'utf8') 
    # wav OSS存放地址
    ossPath = "oss://example/wav/"
    for meta in wavFile:
        meta = meta.split()
        wavId = meta[0]
        idxList.append(wavId)
    ossWavFile = codecs.open(sys.argv[2], 'w+', 'utf8')
    for idx in idxList:
        command = 'ossutil64 sign {osspath}{idx}.wav --timeout {times}'.format(osspath=ossPath, idx=idx, times=32400)
        res = os.popen(command)
        for audio in res:
            ossWavFile.write(idx + "\t" + audio)
            break
