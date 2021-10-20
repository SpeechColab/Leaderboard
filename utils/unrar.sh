if [ $# -ne 2 ]; then
  echo "unrar.sh <dataset_rar> <dataset_dir>"
  echo "e.g.: sh unrar.sh cctv_news.rar cctv_news"
  exit 1;
fi

dataset_rar=$1
#dir=$2

rar=`basename $dataset_rar`
corpus=`basename $dataset_rar .rar`

mkdir -p $corpus
cp $dataset_rar $corpus/

cd $corpus
unrar x $rar
if [ -d $corpus ]; then
    mv $corpus/* .
    rm -rf $corpus
fi

sed '/^\s*$/d' content.txt | awk '{print $1}' | sed -e 's:.wav::g' > keys
wc -l keys
awk '{printf "%s\twav/%s.wav\n", $1, $1}' keys > wav.scp
sed '/^\s*$/d' content.txt | sed -e 's:.wav::g' > trans.txt
cd -
