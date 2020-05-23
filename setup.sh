#!/usr/bin/env bash
git clone https://github.com/openvenues/libpostal  > /dev/null 2>&1
cd libpostal
./bootstrap.sh > /dev/null 2>&1
./configure > /dev/null 2>&1
make > /dev/null 2>&1
sudo make install > /dev/null 2>&1
cd ..
rm -fdr libpostal