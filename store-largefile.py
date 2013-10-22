#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
filter.largefile.smudge
"""
import os
import sys
import path
import hashlib

BASE_DIR = path.path('~/Documents/develop/learn/samba_share/git_largefile').expanduser()
DATA_DIR = BASE_DIR / 'data20131011_1'

content = os.fdopen(sys.stdin.fileno(), 'rb').read()
sha = hashlib.sha1()
sha.update(content)
hd = sha.hexdigest()

dirpath = DATA_DIR / hd[:2] / hd[2:4]
dirpath.makedirs_p()
filepath = dirpath / hd[4:]
filepath.write_bytes(content)
sys.stdout.write(hd)
