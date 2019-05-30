#!/bin/bash 

# Get Java Kernel for Jupyter 

kernel="ijava-1.3.0.zip"

wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/$kernel

unzip $kernel 

mv $kernel /tmp 

mv install.py /tmp 

python /tmp/install.py --sys-prefix 

echo "\nCheck if java kernel is succesfully installed.\n\n" 

jupyter kernelspec list

# Remove Java Kernel Directory in current directory 
rm -rf java 
