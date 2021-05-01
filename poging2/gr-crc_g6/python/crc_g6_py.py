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
from gnuradio import gr
#import gnuradio.extras

class crc_g6_py(gr.basic_block):
	"""
	docstring for block crc_g6_py
	"""
	def __init__(self):
		gr.basic_block.__init__(self, name="crc_g6_py",in_sig=[numpy.byte],out_sig=[numpy.byte])
		self.poly = (1 << 16) | (1 << 12) | (1 << 5) | (1 << 0)
		#self.set_auto_consume(False)
		self.result = 0x84CF
		self.set_min_output_buffer(11)

	#def forecast(self, noutput_items, ninput_items_required):
		#setup size of input_items[i] for work call
		#for i in range(len(ninput_items_required)):
			#ninput_items_required[i] = noutput_items
			#print("i = ", i)
		#print("noutput_items = ",noutput_items)
		#ninput_items_required[0] = noutput_items - 2

	def getBitlen(self, num):
		counter = 0
		while(num > 1):
			num = num >> 1
			counter += 1
		return counter

	def doStuff(self, data):
		data = (data << 16)
		while self.getBitlen(data) > 15:
			msbPos = self.getBitlen(data)
			#print("msbPos = ", msbPos)
			data = data ^ (self.poly << (msbPos - 16))
		self.result = data

	def general_work(self, input_items, output_items):
		#output_items[0][:] = input_items[0]
		in0 = input_items[0][:len(output_items[0])]
		out = output_items[0]
		print("input  len = ", input_items)
		print("output = ", output_items)
		data = self.result
		print('')
		for i in range(len(in0)):
			data = (data << 8) | in0[i]
			out[i] = in0[i]
		self.doStuff(data)
		out[-2] = (self.result & 0b1111111100000000) >> 8
		out[-1] = self.result & 0b0000000011111111
		self.consume(0, len(input_items[0]))
		#self.consume_each(len(input_items[0]))
		return len(output_items[0])
