'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-28 12:27:39
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-28 18:07:39
FilePath: \Code\Python\算法练习\LeetCode\合并两个有序数组.py
Description: 

Copyright (c) 2024 by Muy, All Rights Reserved. 
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 覆盖
        # for i in range(m,m + n):
        #     nums1[i] = nums2[i - m]
        # nums1.sort()

        # 双指针
        k = m - 1
        l = n - 1
        x = m + n - 1
        while k >= 0 and l >= 0:
            if nums1[k] >= nums2[l]:
                nums1[x] = nums1[k]
                k -= 1
            else:
                nums1[x] = nums2[l]
                l -= 1
            x -= 1
        while l >= 0:
            nums1[x] = nums2[l]
            l -= 1
            x -= 1 