'''
Author: Muy lzqm04@gmail.com
Date: 2023-11-25 17:53:44
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2023-12-29 09:23:01
FilePath: \Code\Python\算法练习\LeetCode\两数之和.py
Description: 
    复健训练
'''

# 双层遍历
# 内部设置判断条件if

from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[i] + nums[j] == target and i != j:
                    return[i,j]
        return[]
    

'''
    列表中的值是可以重复的，去重方法：转为set集合
    对于列表有默认方法len方法：可以获取指定列表的索引长度，获取的值即为列表的元素个数 - 1
    同时存在index方法：获取某个元素在列表中的索引（可指定范围，默认获取第一个相同的值的索引）
'''