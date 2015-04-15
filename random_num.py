#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import random

argvs = sys.argv
argc  = len(argvs)

if argc == 2:
    f=open("random_num","w+")
    for i in range(0,int(argvs[1])):
        f.write(str(random.randint(1,100))+"\n")
        f.close
