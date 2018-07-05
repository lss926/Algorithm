#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: bubble_sort.py
@time: 2018/7/5 15:19
"""


def bubbleSort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]


if __name__ == "__main__":
    alist = [26,23,17,37,45,34,59,13,68]
    bubbleSort(alist)
    print(alist)