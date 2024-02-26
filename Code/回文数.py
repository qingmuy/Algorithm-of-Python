'''
Author: Muy lzqm04@gmail.com
Date: 2024-01-26 18:10:44
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-01-26 18:37:33
FilePath: \Code\Python\算法练习\LeetCode\回文数.py
Description: 
    复健
'''

'''
    转换为字符串，比较字符串即可
    问题：内存较大
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) != reversed(str(x)):
            return False
        else:
            return True
