'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-26 11:13:16
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-26 11:23:30
FilePath: \Code\Python\算法练习\LeetCode\找出字符串中第一个匹配项的下标.py
Description: 
    复健
'''

'''
    字符串可以使用in方法
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            i = 0
            while True:
                if haystack[i:i + len(needle)] == needle:
                    return i
                i += 1