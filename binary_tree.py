#!/usr/bin/env python
# encoding: utf-8
"""
@author: lisaisai
@file: binary_tree.py
@time: 2018/7/6 11:12
"""


class Node(object):
    """定义一个树的节点"""
    def __init__(self, item = -1, lchild = None, rchild = None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """定义一个树"""
    def __init__(self, node = None):
        self.root = node

    def add(self, item):
        """为树的节点增加一个元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                else:
                    queue.append(cur.lchild)
                if cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.rchild)

    def breadthTravel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.item, end=" ")
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)

    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.breadthTravel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)