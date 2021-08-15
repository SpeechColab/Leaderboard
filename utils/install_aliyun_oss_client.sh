#!/usr/bin/env bash

ossbin=utils/oss

if [ `uname -s` == 'Linux' ]; then
  wget -O $ossbin http://gosspublic.alicdn.com/ossutil/1.7.1/ossutil64 || exit 1
elif [ `uname -s` == 'Darwin' ]; then
  curl -o $ossbin http://gosspublic.alicdn.com/ossutil/1.7.1/ossutilmac64 || exit 1
fi

if [ -f $ossbin ]; then
  chmod 755 $ossbin
  echo "$0: Done"
  exit 0
else
  echo "ERROR: failed downloading oss tool."
  exit -1
fi