#!/usr/bin/env python3

# MIT License
#
# Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import os
from lib.banner import __version__

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--phone', metavar="<phone>", dest='phone', type=str, help='The phone number to scan.')

parser.add_argument('-i', '--input', metavar="<inputfile>", dest="inputfile", type=str, help='List of phone numbers to scan.')

parser.add_argument('-o', '--output', metavar="<outputfile>", dest="outputfile", type=str, help='Output to save scan results.')

parser.add_argument('-s', '--scanner', metavar="<scanner>", dest="scanner", type=str, default="all", help='The scanner to use.')

parser.add_argument('--recon', action='store_true', help='Launch custom format reconnaissance.')

parser.add_argument('--no-ansi', action='store_true', help='Disable colored output.')

parser.add_argument('-u', '--update', action='store_true', help='Update Phonia Toolkit.')

args = parser.parse_args()
