#!/usr/bin/env python3
import os, sys
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_num_utts', type=int, default = 1999999999, help='max number of utterances to be generated in dst dir.')
    parser.add_argument('dataset', type=str)
    parser.add_argument('dir', type=str)
    args = parser.parse_args()
    print(args, file = sys.stderr)

    dataset_info_path = os.path.join(args.dataset, 'info.json'); assert(os.path.isfile(dataset_info_path))
    audio_dir_path = os.path.join(args.dataset, 'audio'); assert(os.path.isdir(audio_dir_path))

    with open(dataset_info_path, 'r', encoding='utf-8') as dataset_info_fp:
        info = json.load(dataset_info_fp)
    
    scp_path = os.path.join(args.dir, 'wav.scp')
    trans_path = os.path.join(args.dir, 'trans.txt')
    with open(scp_path, 'w+', encoding='utf-8') as scp_fp, open(trans_path, 'w+', encoding='utf-8') as trans_fp:
        for audio in info['audios'][:args.max_num_utts]:
            for segment in audio['segments']:
                line = (
                    F"{segment['sid']}"
                    F"\t{os.path.join(os.path.abspath(args.dataset), audio['path'])}"
                )
                print(line, file = scp_fp)
                print(F"{segment['sid']}\t{segment['text']}", file = trans_fp)

    
