#!/usr/bin/env python3
# coding=utf-8
# Copyright  2022  Ruiqi WANG, Jinpeng LI, Jiayu DU

import sys, os, argparse
import string
from nemo_text_processing.text_normalization.normalize import Normalizer


def read_interjections(filepath):
    interjections = []
    with open(filepath) as f:
        for line in f:
            words = [ x.strip() for x in line.split(',') ]
            interjections += [ w for w in words ] + [ w.upper() for w in words ] + [ w.lower() for w in words ]
    return list(set(interjections))  # deduplicated


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('ifile', help='input filename, assume utf-8 encoding')
    p.add_argument('ofile', help='output filename')
    p.add_argument('--to_upper', action='store_true', help='convert to upper case')
    p.add_argument('--to_lower', action='store_true', help='convert to lower case')
    p.add_argument('--has_key', action='store_true', help="input text has Kaldi's key as first field.")
    p.add_argument('--log_interval', type=int, default=10000, help='log interval in number of processed lines')
    args = p.parse_args()

    ifile = open(args.ifile, 'r',  encoding = 'utf8')
    ofile = open(args.ofile, 'w+', encoding = 'utf8')

    nemo_tn_en = Normalizer(input_case='lower_cased', lang='en')

    itj = read_interjections(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interjections_en.csv')
    )
    itj_map = { x : True for x in itj }

    certain_single_quote_items = ["\"'", "'?", "'!","'.", "?'", "!'", ".'","''", "<BOS>'", "'<EOS>"]
    single_quote_removed_items = [ x.replace("'", '') for x in certain_single_quote_items ]

    n = 0
    for l in ifile:
        key = ''
        text = ''
        if args.has_key:
            cols = l.split(maxsplit=1)
            key = cols[0]
            if len(cols) == 2:
                text = cols[1].strip()
            else:
                text = ''
        else:
            text = l.strip()

        # nemo text normalization
        text = text.lower()
        text = nemo_tn_en.normalize(text)

        # Punctuations
        # NOTE(2022.10 Jiayu):
        # Single quote removal is not perfect.
        # ' need to be reserved for:
        #   abbreviations: 
        #     I'm, don't, she'd, 'cause, Sweet Child o' Mine, Guns N' Roses, ...
        #   possessions:
        #     John's, the king's, parents', ...
        text = '<BOS>' + text + '<EOS>'
        for x, y in zip(certain_single_quote_items, single_quote_removed_items):
            text = text.replace(x, y)
        text = text.lstrip('<BOS>').rstrip('<EOS>')

        puncts_to_remove = string.punctuation.replace("'", '')
        text = text.translate(str.maketrans('', '', puncts_to_remove))

        # Interjections
        text = ' '.join([ x for x in text.strip().split() if x not in itj_map ])

        # Cases
        if args.to_upper and args.to_lower:
            sys.stderr.write('text norm: to_upper OR to_lower?')
            exit(1)
        if args.to_upper:
            text = text.upper()
        if args.to_lower:
            text = text.lower()

        if args.has_key:
            ofile.write(key + '\t' + text + '\n')
        else:
            ofile.write(text + '\n')

        n += 1
        if n % args.log_interval == 0:
            sys.stderr.write("text norm: {} lines done.\n".format(n))

    sys.stderr.write("text norm: {} lines done in total.\n".format(n))

    ifile.close()
    ofile.close()
