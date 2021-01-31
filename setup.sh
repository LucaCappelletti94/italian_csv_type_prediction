#!/usr/bin/env bash
rm -fdr libpostal
git clone https://github.com/openvenues/libpostal 
cd libpostal
./bootstrap.sh
./configure
make
make install
cd ..
rm -fdr libpostal