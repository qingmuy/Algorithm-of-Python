'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-27 19:01:18
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-27 19:01:24
FilePath: \Code\Python\Algorithm-of-Python\Code\删除列表中的重复项.py
Description: 

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target = head
        while not head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return target