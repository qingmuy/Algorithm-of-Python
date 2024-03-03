'''
Author: Muy lzqm04@gmail.com
Date: 2024-03-03 11:11:24
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-03-03 11:11:46
FilePath: \Coded:\Note\Algorithm-of-Python\Code\环形链表.py
Description: 
描述
Copyright (c) 2024 by Muy, All Rights Reserved. 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 暴力解法
        index = 0
        while index < 10001:
            if not head:
                return False
            head = head.next
            index += 1
        return True

# 快慢指针：快的指针必定会追上慢的指针
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
            if fast == slow:
                return True
        return False