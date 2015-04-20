#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def read(file_name):
    f = open(file_name, 'r')
    return map(int, f.readlines())


class IntList():

    def __init__(self, nums):
        self.nums = nums

    def sum(self):
        return sum(self.nums)

    def size(self):
        return len(self.nums)

    def mean(self):
        return self.sum() / float(self.size())

    def median(self):
        sorted_n = sorted(self.nums)
        size = self.size()
        mid = size / 2
        if size % 2 == 1:
            return sorted_n[mid + 1]
        else:
            return (sorted_n[mid - 1] + sorted_n[mid]) / 2.0

    def set_histogram(self):
        histogram = dict()
        for num in self.nums:
            if histogram.has_key(num):
                histogram[num] += 1
            else:
                histogram[num] = 1
        self.histogram = histogram

    def mode(self):
        self.set_histogram()
        hist_pair = self.histogram.items()
        maximum = max(map(lambda x: x[1], hist_pair))
        filterd_items = filter(lambda x: x[1] == maximum, hist_pair)
        return map(lambda x: x[0], filterd_items)

    def variance(self):
        mean = self.mean()
        sigma = map(lambda x: (x - mean) ** 2, self.nums)
        return sum(sigma) / float(len(sigma))

def output(params):
    sum, mean, median, mode, variance = params
    results = [
        "合計:%d" % sum,
        "平均:%f" % mean,
        "中央値:%d" % median,
        "最頻値:" + ', '.join(map(str, mode)),
        "分散:%f" % variance
    ]
    print '\n'.join(results)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        numbers = read(file_name)
        n = IntList(numbers)
        params = [n.sum(), n.mean(), n.median(), n.mode(), n.variance()]
        output(params)

"""
import numpy as np
f = open(file_name, 'r')
x = map(int, f.readlines())
x = np.array(x)
x.sum(), np.sum(x)
x.mean(), np.mean(x)
np.median(x)
x.var(), np.var(x)
"""
