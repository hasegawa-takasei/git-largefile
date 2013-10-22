#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
filter.largefile.smudge
"""
import os
import sys
import path

BASE_DIR = path.path('~/.gitasset').expanduser()
DATA_DIR = BASE_DIR / 'data'

hd = os.fdopen(sys.stdin.fileno(), 'rb').read()
if len(hd) != 40:
	sys.stdout.write(hd)
elif hd.isalnum() == False:
	sys.stdout.write(hd)
else:
	dirpath = DATA_DIR / hd[:2] / hd[2:4]
	filepath = dirpath / hd[4:]
	if os.path.exists(filepath):
		sys.stdout.write(filepath.bytes())
	else:
		sys.stdout.write(hd)

