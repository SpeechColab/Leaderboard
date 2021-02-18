#!/usr/bin/env python3
import sys, os, codecs

def is_chinese_char(ch):
    if (ch >= '\u4e00') and (ch <= '\u9fa5'):
        return True
    else:
        return False

INS_ERR_SYMBOL = '*+'
DEL_ERR_SYMBOL = '*-'
SUB_ERR_SYMBOL = '*'

fi = codecs.open(sys.argv[1], 'r', 'utf8')
fo = codecs.open(sys.argv[2], 'w+', 'utf8')

for l in fi:
    key, align = l.split(maxsplit=1)
    fo.write(key + ":\n")

    ref = '    REF:'
    rec = '    REC:'
    pair_list = align.split(';')
    for pair in pair_list:
        pair = pair.split()
        if (len(pair) != 2):
            print(pair)
        else:
            ref_token = pair[0].strip()
            rec_token = pair[1].strip()

            if (ref_token == '<eps>'):
                ref_token = INS_ERR_SYMBOL
            if (rec_token == '<eps>'):
                rec_token = DEL_ERR_SYMBOL

            if (ref_token != '*+') and (rec_token != '*-'):
                if (ref_token != rec_token):
                    ref_token = SUB_ERR_SYMBOL + ref_token
                    rec_token = SUB_ERR_SYMBOL + rec_token

            # compute ASCII width
            m = 0
            for ch in ref_token:
                if is_chinese_char(ch):
                    m += 2
                else:
                    m += 1
            n = 0
            for ch in rec_token:
                if is_chinese_char(ch):
                    n += 2
                else:
                    n += 1

            # pad with space to keep same width
            if m > n:
                rec_token += ' ' * (m-n)
            elif n > m:
                ref_token += ' ' * (n-m)
            else:
                pass

            #width = max(len(ref_token), len(rec_token))
            ref += ' {}'.format(ref_token)
            rec += ' {}'.format(rec_token)

    fo.write(ref + '\n')
    fo.write(rec + '\n')


fo.close()
fi.close()
