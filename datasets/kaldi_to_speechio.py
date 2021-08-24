#!/usr/bin/env python3

import os, sys
import argparse
import csv
import wave

def LoadKaldiArk(path):
    d = {}
    with open(path, 'r', encoding = 'utf-8') as f:
        for line in [ l.strip() for l in f if l.strip() ]:
            key, content = line.split(maxsplit=1)
            if d.get(key) == None:
                d[key] = content
            else:
                print(F'ERROR: found duplicated key {key}', file = sys.stderr)
                raise RuntimeError
    return d

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src', type=str)
    parser.add_argument('dst', type=str)
    args = parser.parse_args()
    print(args, file = sys.stderr)

    # load wav.scp
    if os.path.isfile(os.path.join(args.src, 'wav.scp')):
        wavscp = LoadKaldiArk(os.path.join(args.src, 'wav.scp'))
    else:
        raise RuntimeError(F"Cannot find scp file {os.path.join(args.src, 'wav.scp')}")

    # load text/trans.txt
    if os.path.isfile(os.path.join(args.src, 'text')):
        utt2text = LoadKaldiArk(os.path.join(args.src, 'text'))
    elif os.path.isfile(os.path.join(args.src, 'trans.txt')):
        utt2text = LoadKaldiArk(os.path.join(args.src, 'trans.txt'))
    else:
        text_path = {}

    # load utt2spk
    if os.path.isfile(os.path.join(args.src, 'utt2spk')):
        utt2spk = LoadKaldiArk(os.path.join(args.src, 'utt2spk'))
    else:
        utt2spk = {}

    # load utt2dur
    if os.path.isfile(os.path.join(args.src, 'utt2dur')):
        utt2dur = LoadKaldiArk(os.path.join(args.src, 'utt2dur'))
    else:
        utt2dur = {}

    # rename audio dir
    wav_dir = os.path.join(args.src, 'wav'); assert(os.path.isdir(wav_dir))
    os.system(F'mkdir -p {args.dst}/audio && cp -r {wav_dir}/* {args.dst}/audio/')

    utts = []
    for uttid in wavscp.keys():
        audio = wavscp[uttid].replace('wav', 'audio', 1)
        if utt2dur:
            duration = utt2dur.get(uttid)
        else:
            wav = wave.open(os.path.join(args.dst, audio), 'r')
            duration = wav.getnframes() / wav.getframerate()
        utt = {
                'ID' : uttid,
                'AUDIO' : audio,
                'DURATION' : duration,
        }
        if utt2spk:
            utt['SPEAKER'] = utt2spk.get(uttid)
        if utt2text:
            utt['TEXT'] = utt2text.get(uttid)
        utts.append(utt)
    utts.sort(key = lambda e: e['ID'])

    with open(os.path.join(args.dst, 'metadata.tsv'), 'w+', encoding = 'utf-8') as fo:
        csv_header_fields = ['ID', 'AUDIO', 'DURATION']
        if utt2spk:
            csv_header_fields.append('SPEAKER')
        if utt2text:
            csv_header_fields.append('TEXT')

        csv_writer = csv.DictWriter(fo, delimiter='\t', fieldnames=csv_header_fields)
        csv_writer.writeheader()
        for audio in utts:
            csv_writer.writerow(audio)
