'''
Author: Muy lzqm04@gmail.com
Date: 2024-01-29 18:50:08
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-01-29 22:30:55
FilePath: \Code\Python\算法练习\LeetCode\最长公共前缀.py
Description: 
    复健
'''

'''
    对字符串进行遍历
    每次从首字母截取，拓展，一旦不匹配则返回值
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char = ([strs[i] for i in range(len(strs))])

        for x in range(1,len(max(strs,key = len))):
            i = set([str[:x] for str in char])
            if len(i) > 1 and x == 1:
                return ''
            elif len(i) > 1:
                return char[1][:x - 1]
            
    a = longestCommonPrefix(["flower","flow","flight"],["flower","flow","flight"])
    print(a)