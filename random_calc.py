#!/usr/bin/python 
# -*- coding: utf-8 -*-
#tst

import sys

argvs = sys.argv
argc  = len(argvs)
tmp = 0
dict={}
keys=0
sum_of_r=0
mean_of_r=0
median_of_r=0
mode_of_r=[]
variance_of_r=0
if argc ==2:
    f=open(argvs[1])
    lines=f.readlines()#ファイルの行数がリストとして格納される
    f.close
    lines.sort()
    lines =map(int,lines)
    n=len(lines)
    sum_of_r=sum(lines)
    mean_of_r= sum_of_r / n
    if n % 2 == 0:
        median_of_r=lines[n/2]
    else:
        median_of_r=(lines[(n+1)/2]+lines[(n-1)/2])/2
    for i,x in enumerate(lines):
        tmp =tmp +pow((x - mean_of_r),2)
        if dict.has_key(x):
            dict[x]=dict[x]+1
        else:
            dict[x]=1#{num,出現回数}
            keys=keys+1
    variance_of_r=tmp/n
    max_n=max(dict.values())#最大の出現回数
    items=dict.items()#辞書をタプルのリストとして格納
    for i in range(keys):
        tuple=items[i]#各タプルの取り出し
        if (tuple[1]==max_n):
            mode_of_r=mode_of_r + [tuple[0]]
    print "合計:%d" % sum_of_r
    print "平均:%d" % mean_of_r
    print "中央値:%d" % median_of_r
    print "最頻値:", 
    for i in mode_of_r:
        print "%d"% i,
    print ""
    print "分散:%d" % variance_of_r
