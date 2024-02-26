'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-14 12:05:07
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-14 21:09:13
FilePath: \Code\Python\算法练习\LeetCode\合并两个有序链表.py
Description: 
    复健
'''

'''
    两个链表转化为列表
    直接进行排序
    
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = result
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        tail.next = list1 if list1 is not None else list2
        return result.next