#!/usr/bin/python
# -*- coding: utf-8 -*-
#市也さんのコードを参考に書きました

import sys
import time
import numpy as np

def read(file_name):
    f =open(file_name,'r')
    return map(int,f.readlines())

class CalcClass():

    def __init__(self,nums):
        self.nums =nums#アトリビュートに代入

    def sum(self):
        return np.sum(self.nums)
    
    def mean(self):
        return np.mean(self.nums)
    
    def median(self):
        return np.median(self.nums)
    
    def mode(self):
        count_list = np.bincount(self.nums)
        return np.argmax(count_list)
        
    def var(self):
        return np.var(self.nums)
    
def output(l):
    sum, mean, median, mode, var, start =l
    total_time =time.time() - start
    results = [
        "合計:%d" % sum,
        "平均:%f" % mean,
        "中央値:%f" % median,
        "最頻値:%d" % mode,
        "分散:%f" % var,
        "計測時間:%f" % total_time
    ]
    print '\n'.join(results)#リストのprint

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start = time.time()
        file_name = sys.argv[1]
        num_list = read(file_name)
        num_list = np.array(num_list)#高速計算可能なnp.arrayに代入
        n = CalcClass(num_list)
        params = [n.sum(), n.mean(), n.median(), n.mode(), n.var(), start]
        output(params)
        
