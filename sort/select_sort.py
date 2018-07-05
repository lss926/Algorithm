#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: select_sort.py
@time: 2018/7/5 15:25
"""


def selectSort(alist):
    """选择排序"""
    n = len(alist)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if alist[j] < alist[minIndex]:
                minIndex = j
        if minIndex != i:
            alist[i], alist[minIndex] = alist[minIndex], alist[i]


if __name__ == "__main__":
    alist = [26, 23, 17, 37, 45, 34, 59, 13, 68]
    selectSort(alist)
    print(alist)