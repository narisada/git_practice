#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys

argvs = sys.argv
argc  = len(argvs)
s = ""
endline=10

if argc >1:
    for i in range(1,argc):
        if ( argvs[i] == "--help"):
            print "headのhelpです",
            quit()
        elif (argvs[i] =="-n"):
            if argc > i+1:
                if argvs[i+1].isdigit():
                    endline=int(argvs[i+1])
                    if argc > i+2:
                        i=i+2
                    else:
                        break
                else:
                    print("無効な行数です")
                    quit()
            else:
                print("オプションには行数が必要です")
                quit()
        else:
            filename=argvs[i]
    i=0
    f=open(filename)
    for row in f.readlines():
        i=i+1
        if i > endline:
            break
        print row,
    f.close
