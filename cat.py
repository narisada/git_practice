#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys

argvs = sys.argv
argc  = len(argvs)
s = ""

f=open(argvs[1])
if argc >1:
    for i in range(1,argc):
        if ( argvs[i] == "--help"):
            print "catのhelpです",
            quit()
    for i in range(1,argc):
        f=open(argvs[i])
        for row in f:
            print row,
        f.close
