#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys

argvs = sys.argv
argc  = len(argvs)
i=0

if argc > 1:
    for i in range(1,argc):
        if ( argvs[i] == "--help"):
            print "grepのhelpです",
            quit()
    s=argvs[1]
    filename=argvs[2]
    i=0
    f=open(filename)
    for i,row in enumerate(f.readlines()):
        if( row.find(s,0,-1)!=-1):
            print(i+1)
    f.close
