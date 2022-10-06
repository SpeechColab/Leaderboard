#!/usr/bin/env python3
# coding=utf-8
# Copyright  2022  Ruiqi WANG, Jinpeng LI, Jiayu DU

import sys, os, argparse
from nemo_text_processing.text_normalization.normalize import Normalizer


def read_interjections(filepath):
    with open(filepath) as f:
        for l in f:
            words = [ x.strip() for x in l.split(',') ]
            l = [ x for x in words ] + [ w.upper() for w in words ] + [ w.lower() for w in words ]
    return list(set(l))


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
    nemo_tn = Normalizer(input_case='cased', lang='en')

    itj = read_interjections(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interjections_en.csv')
    )
    itj_map = { x : True for x in itj }

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

        # cases
        if args.to_upper and args.to_lower:
            sys.stderr.write('text norm: to_upper OR to_lower?')
            exit(1)

        if args.to_upper:
            text = text.upper()
        if args.to_lower:
            text = text.lower()

        # remove space before and after signs
        text = text.replace(' / ', '/')
        text = text.replace(' - ', '-')

        replace_list = ["\"'", "'?", "'!","'.", "?'", "!'", ".'","''"]
        for quote_item in replace_list:
            text = text.replace(quote_item, "")
        text = text.replace(", ", " ")

        # nemo text normalization
        text = nemo_tn.normalize(text)

        # Punctuations
        old_chars = '!"#%&()*/+,.:;<=>?@[]^_`{|}~'  # string.punctuation except ' (e.g. in I'm, that's)
        new_chars = ' ' * len(old_chars)
        del_chars = ''
        text = text.translate(str.maketrans(old_chars, new_chars, del_chars))
        text = text.replace(" ' ", " ").replace('-', ' ')
        
        # Interjections removal
        text = ' '.join(
            [ x for x in text.strip().split() if not itj_map.get(x) ]
        )

        # Nemo may produce inconsistent cases with our setting, convert it again
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
