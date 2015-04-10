#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys

argvs = sys.argv
argc  = len(argvs)
s = ""


if argc >1:
    for i in range(1,argc):
        if ( argvs[i] == "--help"):
            print "echoのhelpです",
            quit()
    for i in range(1,argc):
        print argvs[i],
            
print ""
