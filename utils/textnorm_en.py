#!/usr/bin/env python3
# coding=utf-8
import sys, os, codecs
import argparse
import string

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
        old_chars = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' # includes all EN punctuations, except ' (e.g. in I'm, that's)
        new_chars = ' ' * len(old_chars)
        del_chars = ''
        text = text.translate(str.maketrans(old_chars, new_chars, del_chars))

        # 
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
