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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from crc_py import crc_py

class qa_crc_py (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t(self):

        # check data
        src_data = b'123456789'
        expected_out = b'0x29b1'
        crc = crc_py(2)
        snk = blocks.vector_sink_b()
        self.tb.connect(src, crc)
        self.tb.connect(crc, snk)
        self.tb.run()
        result = snk.data()
        self.assertEqual(expected_out, result)

if __name__ == '__main__':
    gr_unittest.run(qa_crc_py, "qa_crc_py.xml")
