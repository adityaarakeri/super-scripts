#!/bin/bash
# Author  : Vinayak Patil 
# Purpose : This scripts helps in freeing up space on linux OS by deleting obsolote packages and kernels. 

sudo apt-get autoclean
sudo apt-get clean
sudo apt-get autoremove --purge
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | xargs sudo apt-get -y purge
