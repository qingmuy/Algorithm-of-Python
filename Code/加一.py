'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-26 18:37:16
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-26 19:05:06
FilePath: \Code\Python\Algorithm-of-Python\Code\加一.py
Description: 
    
'''

# 列表为主体
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else
            
        return digits
    
# 数据为主题
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 计算出该数字为多少:列表字符串转数字
        nums = ""
        while digits:
            nums = nums + str(digits.pop(0))
        nums = int(nums) + 1
        return [int(x) for x in str(nums)]