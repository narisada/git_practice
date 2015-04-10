#echo.py

import sys

argvs = sys.argv
argc  = len(argvs)

if  argc >1:
    for i in range(1,argc):
      print argvs[i]



