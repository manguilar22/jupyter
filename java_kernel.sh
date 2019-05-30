#!/bin/bash 

# Java Kernel for Jupyter (Version) 
kernel="ijava-1.3.0.zip"

# Download Java Kernel
wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/$kernel

# Unzip Java Kernel zip 
unzip $kernel 

# Move installation files 
mv $kernel /tmp 

mv install.py /tmp 

# You need python3 
# Python3.x >= 3.0
python /tmp/install.py --sys-prefix 

# List Kernels Installed 
echo "\nCheck if java kernel is succesfully installed.\n\n" 

jupyter kernelspec list

# Remove Java Kernel Directory in current directory 
rm -rf java 
