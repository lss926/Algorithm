#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: single_cycle_link_list.py
@time: 2018/7/3 19:10
"""


class SingleNode(object):
    """链表的结点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        print(cur.item)
        while cur.next != self.__head:
            cur = cur.next
            print(cur.item)
        print("")

    def add(self, item):
        """在链表头部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            self.__head = node

    def append(self, item):
        """在链表尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """在链表的指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """从链表中删除结点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        if cur.item == item:
            if cur.next != self.__head:
                while cur.next != self.__head:
                    cur = cur.next
                cur.next = self.__head.next
                self.__head = self.__head.next
            else:
                self.__head = None
        else:
            pre = self.__head
            while cur.next != self.__head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """在链表中查找结点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    testList = SingleCycleLinkList()
    testList.add(2)
    testList.add(3)
    testList.append(4)
    testList.insert(2,5)
    testList.travel()
