#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: stack.py
@time: 2018/7/4 16:03
"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断一个栈是否为空"""
        return self.items == []

    def push(self, item):
        """在栈顶添加一个元素"""
        self.items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("nihao")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())