#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/vincentcharpentier/Desktop/GNU_CRC_Radio/gr-crc_g6/python
export PATH=/home/vincentcharpentier/Desktop/GNU_CRC_Radio/gr-crc_g6/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/vincentcharpentier/Desktop/GNU_CRC_Radio/gr-crc_g6/build/swig:$PYTHONPATH
/usr/bin/python2 /home/vincentcharpentier/Desktop/GNU_CRC_Radio/gr-crc_g6/python/qa_crc_g6_py.py 
