#!/usr/bin/env python3

from multiprocessing.dummy import Pool
from vosk import Model, KaldiRecognizer

import sys
import os
import wave
import json

print("\n\nLoading vosk model\n\n")
model = Model("/vosk-api/python/example/vosk-model-cn-0.1")

def recognize(line):
    uid, fn = line.split()
    wf = wave.open(fn, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""
    while True:
        data = wf.readframes(1000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            jres = json.loads(rec.Result())
            text = text + " " + jres['text']
    jres = json.loads(rec.FinalResult())
    text = text + " " + jres['text']
    return (uid + text)

def sbi_decoder(text, path):
    with open(file=str(path), mode = 'w', encoding='UTF-8') as result:
        for item in text:
            result.write("%s\n" % item)

def main():
    p = Pool(8)
    texts = p.map(recognize, open(sys.argv[1]).readlines())
    sbi_decoder(texts, sys.argv[2])
    print ("\n".join(texts))

main()
