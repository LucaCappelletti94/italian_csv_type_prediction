#!/usr/bin/env bash
git clone https://github.com/openvenues/libpostal
cd libpostal
./bootstrap.sh
./configure
make
sudo make install
cd ..
rm -fdr libpostal