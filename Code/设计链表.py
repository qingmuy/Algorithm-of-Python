'''
Author: Muy lzqm04@gmail.com
Date: 2024-03-06 18:03:24
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-03-06 19:27:02
FilePath: \Coded:\Note\Algorithm-of-Python\Code\设计链表.py
Description: 
    中等
Copyright (c) 2024 by Muy, All Rights Reserved. 
'''

class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        prenode = Node()
        self.head = prenode

    def get(self, index: int) -> int:
        # 根据索引获取当前的值
        headnode = self.head.next
        while index > 0:
            if not headnode:
                return -1
            headnode = headnode.next
            index -= 1
        if not headnode:
            return -1
        return headnode.val

    def addAtHead(self, val: int) -> None:
        # 增添头节点
        prenode = self.head
        temp = Node(val=val)
        temp.next = prenode.next
        prenode.next = temp

    def addAtTail(self, val: int) -> None:
        # 添加尾节点
        headnode = self.head
        while headnode and headnode.next:
            headnode = headnode.next
        headnode.next = Node(val = val)

    def addAtIndex(self, index: int, val: int) -> None:
        # 根据索引添加元素：如果 index 比长度更大，该节点将 不会插入 到链表中。
        headnode = self.head    # 此处代表虚拟节点
        for i in range(index):
            if not headnode:
                return
            headnode = headnode.next
        if not headnode:
            return
        temp = Node(val, headnode.next if headnode.next else None)
        headnode.next = temp
        

    def deleteAtIndex(self, index: int) -> None:
        # 根据索引删除元素：如果下标有效，则删除链表中下标为 index 的节点。
        # 三种情况：删除正常元素、删除最后一个元素、删除越界节点
        headnode = self.head    # 此处代表虚拟节点
        for i in range(index):
            if not headnode:
                return
            headnode = headnode.next
        if not headnode:
            return
        elif headnode and not headnode.next:
            headnode.next = None
        else:
            headnode.next = headnode.next.next