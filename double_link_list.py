#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: double_link_list.py
@time: 2018/7/4 8:48
"""


class SingleNode(object):
    """双向链表的结点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        """在链表头部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        """在链表尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """在链表的指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            cur = self.__head
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        """从链表中删除结点"""
        if self.is_empty():
            return
        else:
            cur = self.__head
            if cur.item == item:
                if cur.next is None:
                    self.__head = None
                else:
                    cur.next.prev = None
                    self.__head = cur.next
                return
        while cur is not None:
            if cur.item == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                break
            cur = cur.next

    def search(self, item):
        """在链表中查找结点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    testList = DoubleLinkList()
    testList.add(2)
    testList.add(3)
    testList.append(4)
    testList.insert(2,5)
    testList.travel()
