#!/usr/bin/env python3
import os, sys
import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_num_utts', type=int, default = 1999999999, help='max number of utterances to be generated in dst dir.')
    parser.add_argument('dataset', type=str)
    parser.add_argument('dir', type=str)
    args = parser.parse_args()
    print(args, file = sys.stderr)

    metadata_path = os.path.join(args.dataset, 'metadata.tsv'); assert(os.path.isfile(metadata_path))

    utts = []
    with open(metadata_path, 'r', encoding='utf-8') as metadata_fp:
        reader = csv.DictReader(metadata_fp, delimiter='\t')
        for utt in reader:
            if float(utt['DURATION']) <= 59.9:
                utts.append(utt)
    
    with open(os.path.join(args.dir, 'wav.scp'), 'w+', encoding='utf-8') as fp:
        for utt in utts[:args.max_num_utts]:
            # convert audio path to absolute path
            print(F"{utt['ID']}\t{os.path.join(os.path.abspath(args.dataset), utt['AUDIO'])}", file = fp)

    with open(os.path.join(args.dir, 'trans.txt'), 'w+', encoding='utf-8') as fp:
        for utt in utts[:args.max_num_utts]:
            print(F"{utt['ID']}\t{utt['TEXT']}", file = fp)
