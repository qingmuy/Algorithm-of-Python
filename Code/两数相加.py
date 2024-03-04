'''
Author: Muy lzqm04@gmail.com
Date: 2024-01-24 23:05:59
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-03-04 21:40:13
FilePath: \Coded:\Note\Algorithm-of-Python\Code\两数相加.py
Description: 
    复健训练
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        res = result
        jw = 0      # 代表进位
        while l1 or l2:
            # 如果 l1 为空
            if not l1:
                while l2:
                    sum = l2.val + jw
                    if not l2.next:
                        if sum < 10:
                            res.val = sum
                            return result
                        else:
                            res.val = sum - 10
                            temp = ListNode(1)
                            res.next = temp
                            return result
                    l2 = l2.next
                    if sum < 10:
                        jw = 0
                        res.val = sum
                        temp = ListNode()
                        res.next = temp
                        res = temp
                    else:
                        jw = 1
                        res.val = sum -10
                        temp = ListNode()
                        res.next = temp
                        res = temp
                return result
            elif not l2:
                while l1:
                    sum = l1.val + jw
                    if not l1.next:
                        if sum < 10:
                            res.val = sum
                            return result
                        else:
                            res.val = sum - 10
                            temp = ListNode(1)
                            res.next = temp
                            return result
                    l1 = l1.next
                    if sum < 10:
                        jw = 0
                        res.val = sum
                        temp = ListNode()
                        res.next = temp
                        res = temp
                    else:
                        jw = 1
                        res.val = sum -10
                        temp = ListNode()
                        res.next = temp
                        res = temp
                return result
            
            sum = l1.val + l2.val + jw
            if not l2.next and not l1.next:
                if sum < 10:
                    res.val = sum
                    return result
                else:
                    res.val = sum - 10
                    temp = ListNode(1)
                    res.next = temp
            l1, l2 = l1.next, l2.next
            if sum < 10:
                jw = 0
                res.val = sum
                temp = ListNode()
                res.next = temp
                res = temp
            else:
                jw = 1
                res.val = sum -10
                temp = ListNode()
                res.next = temp
                res = temp
        if not l1 and not l2:
            if sum < 10:
                res.val = sum
            else:
                res.val = 1
        return result
    


# 增补法
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        res = result
        jw = 0
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + jw
            jw = sum // 10
            res.next = ListNode(sum - 10 if sum >= 10 else sum)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if jw:
            res.next = ListNode(1)
        return result.next