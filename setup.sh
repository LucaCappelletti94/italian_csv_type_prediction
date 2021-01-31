#!/usr/bin/env bash
apt-get update -y
apt-get install -qyy apt-utils build-essential software-properties-common locales locales-all curl autoconf automake libtool python-dev pkg-config
rm -fdr libpostal
git clone https://github.com/openvenues/libpostal 
cd libpostal
./bootstrap.sh
./configure
make
make install
cd ..
rm -fdr libpostal