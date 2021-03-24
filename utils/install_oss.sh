#!/usr/bin/env bash

if [ `uname -s` == 'Linux' ]; then
  wget -O oss http://gosspublic.alicdn.com/ossutil/1.7.1/ossutil64 || exit 1
elif [ `uname -s` == 'Darwin' ]; then
  curl -o oss http://gosspublic.alicdn.com/ossutil/1.7.1/ossutilmac64 || exit 1
fi

if [ -f oss ]; then
  chmod 755 oss
  echo "$0: Done"
  exit 0
else
  echo "ERROR: failed downloading oss tool."
  exit -1
fi
