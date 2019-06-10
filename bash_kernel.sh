#!/bin/bash 

bashK="https://github.com/takluyver/bash_kernel"
git clone $bashK
# Python 3.x >= 3.0 
pip install bash_kernel
python -m bash_kernel.install
rm -rf bash_kernel
