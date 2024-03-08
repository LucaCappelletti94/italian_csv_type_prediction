#!/usr/bin/env bash
apt-get install autoconf curl automake libtool
rm -fdr libpostal
git clone https://github.com/openvenues/libpostal 
cd libpostal
./bootstrap.sh
./configure
make -j4
make install
cd ..
rm -fdr libpostal
