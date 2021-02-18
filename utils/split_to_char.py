import codecs, sys 

iname = sys.argv[1]
oname = sys.argv[2]

i = codecs.open(iname, 'r', 'utf8')
o = codecs.open(oname, 'w+', 'utf8')

for l in i:
    cols = l.split()
    key = cols[0]
    rec = ''.join(cols[1:])
    o.write(key + '\t')
    for ch in rec:
        o.write(' ' + ch) 
    o.write('\n')

i.close()
o.close()
