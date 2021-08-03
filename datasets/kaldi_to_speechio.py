#!/usr/bin/env python3

import os, sys
import argparse
import json
import wave

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', type=str, choices = ['ZH', 'EN'], default='ZH')
    parser.add_argument('src', type=str)
    parser.add_argument('dst', type=str)
    args = parser.parse_args()
    print(args, file = sys.stderr)

    wav_dir = os.path.join(args.src, 'wav'); assert(os.path.isdir(wav_dir))
    scp_path = os.path.join(args.src, 'wav.scp'); assert(os.path.isfile(scp_path))
    trans_path = os.path.join(args.src, 'trans.txt'); assert(os.path.isfile(trans_path))

    os.system(F'mkdir -p {args.dst}/audio && cp -r {wav_dir}/* {args.dst}/audio/')

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
    
    scp = LoadKaldiArk(scp_path)
    trans = LoadKaldiArk(trans_path)

    info = {
        'version' : 'v0.2',
        'dataset' : os.path.basename(args.dst),
        'description' : os.path.basename(args.src),
        'language' : args.language,
        'magic' : '',
        'audios' : [],
    }

    for audio_id in scp.keys():
        path = scp[audio_id].replace('wav', 'audio', 1)
        wav = wave.open(os.path.join(args.dst, path), 'r')
        audio_duration = wav.getnframes() / wav.getframerate()
        text = trans.get(audio_id)
        if text:
            audio = {
                'aid' : audio_id,
                'path' : path,
                'sample_rate' : wav.getframerate(),
                'channels' : wav.getnchannels(),
                'duration' : audio_duration,
                'segments' : [],
            }
            for s in range(0,1):
                # each audio contains only one segment
                segment_id = audio_id
                segment_duration = audio_duration

                seg = {
                    'sid': segment_id,
                    'channel': 0,
                    'begin_time' : 0.0,
                    'duration' : segment_duration,
                    'speaker' : 'N/A',
                    'text' : text,
                }

                audio['segments'].append(seg)
            info['audios'].append(audio)

        info['audios'].sort(key = lambda e : e['aid'])
    
    with open(os.path.join(args.dst, 'info.json'), 'w+', encoding = 'utf-8') as fo:
        print(json.dumps(info, indent = 4, ensure_ascii=False), file = fo)
