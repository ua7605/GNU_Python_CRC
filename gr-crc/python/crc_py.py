#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2021 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import crcmod
from gnuradio import gr

class crc_py(gr.sync_block):
    """
    docstring for block crc_py
    """
    def __init__(self, multiple):
        gr.sync_block.__init__(self,
            name="crc_py",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
	in0 = input_items[0]
        out = output_items[0]

        xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0xffff, xorOut=0x0000)
        output: str = hex(xmodem_crc_func(in0))
        output_bytes = output.encode()
        out[:] = output_bytes
        return len(output_items[0])

