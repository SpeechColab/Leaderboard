#!/usr/bin/env bash

if [ $# -ne 2 ]; then
  echo "unrar.sh <ipath_rar> <dir>"
  echo "e.g.: sh unrar.sh cctv_news.rar SPEECHIO_ASR_ZH00001"
  exit 1;
fi

ipath_rar=$1
dir=$2

rar=`basename $ipath_rar`
corpus=`basename $ipath_rar .rar`

mkdir -p $dir
cp $ipath_rar $dir/

cd $dir
unrar x $rar
if [ -d $corpus ]; then
    mv $corpus/* .
    rm -rf $corpus
fi

sed '/^\s*$/d' content.txt | awk '{print $1}' | sed -e 's:.wav::g' > keys
wc -l keys
awk '{printf "%s\twav/%s.wav\n", $1, $1}' keys > wav.scp
sed '/^\s*$/d' content.txt | sed -e 's:.wav::g' > trans.txt

# cleanup
rm keys 
rm content.txt
rm $rar
cd -


