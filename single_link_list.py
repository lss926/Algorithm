#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: single_link_list.py
@time: 2018/7/3 16:19
"""


class SingleNode(object):
    """链表的结点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单链表"""
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
        node.next = self.__head
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
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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
    testList = SingleLinkList()
    testList.add(2)
    testList.add(3)
    testList.append(4)
    testList.insert(2,5)
    testList.travel()




