#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: insert_sort.py
@time: 2018/7/5 16:53
"""


def insertSort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


if __name__ == "__main__":
    alist = [26, 23, 17, 37, 45, 34, 59, 13, 68]
    insertSort(alist)
    print(alist)