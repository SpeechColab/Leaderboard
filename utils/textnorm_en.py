#!/usr/bin/env python3
# coding=utf-8
import sys, os, codecs
import argparse
import string
from nemo_text_processing.text_normalization.normalize import Normalizer


class interj:
    def __init__(self):
        self.inj_list = []
        f = open('/app/speechio/leaderboard/utils/fillers.tsv')
        words = f.readlines()
        for word in words:
            word = word.strip()
            self.inj_list.append(' '+ word+ ' ')

    def interjection(self,line):
        for item in self.inj_list:
            line = line.replace(item,' ')
        return line


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('ifile', help='input filename, assume utf-8 encoding')
    p.add_argument('ofile', help='output filename')
    p.add_argument('--to_upper', action='store_true', help='convert to upper case')
    p.add_argument('--to_lower', action='store_true', help='convert to lower case')
    p.add_argument('--has_key', action='store_true', help="input text has Kaldi's key as first field.")
    p.add_argument('--log_interval', type=int, default=10000, help='log interval in number of processed lines')
    args = p.parse_args()

    ifile = codecs.open(args.ifile, 'r', 'utf8')
    ofile = codecs.open(args.ofile, 'w+', 'utf8')
    nn = Normalizer(input_case = 'lower_cased',lang = 'en')
    ii = interj()
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
        
        # Punctuations removal
        old_chars = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' # string.punctuation except ' (e.g. in I'm, that's)
        new_chars = ' ' * len(old_chars)
        del_chars = ''
        text = text.translate(str.maketrans(old_chars, new_chars, del_chars))

        # remove interjection
        text = ' ' + text + ' '
        for i in range(3):
            text = ii.interjection(text)
        text = text.strip()

        # text normalization
        text = nn.normalize(text)
        text.replace(' oh ',' o ')

        # remove space before and after signs
        text = text.replace(' \' ','\'')
        text = text.replace(' - ','-')
        text = text.upper()
        
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
