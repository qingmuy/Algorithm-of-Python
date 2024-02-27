'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-26 17:52:28
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-26 17:55:30
FilePath: \Code\Python\Algorithm-of-Python\Code\最后一个单词的长度.py
Description: 
    复健
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])