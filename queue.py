#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: queue.py
@time: 2018/7/4 20:28
"""


class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def enqueue(self, item):
        """往队列中添加元素"""
        self.items.insert(0, item)

    def dequeue(self):
        """从队列中删除一个元素"""
        return self.items.pop()

    def size(self):
        """队列的长度"""
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())