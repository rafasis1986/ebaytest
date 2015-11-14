# -*- coding: utf-8 -*-
'''
Created on Oct 28, 2015

@author: rtorres
'''

import subprocess

from tools.ebay import bulk_categories


def init_db():
    subprocess.call("rm *.html", shell=True)
    bulk_categories()
