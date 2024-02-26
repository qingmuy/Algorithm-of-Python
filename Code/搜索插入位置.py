'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-26 11:27:52
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-26 11:36:06
FilePath: \Code\Python\算法练习\LeetCode\搜索插入位置.py
Description: 
    复健
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target <= i:
                return nums.index(i)
        return len(nums)