'''
Author: Muy lzqm04@gmail.com
Date: 2024-01-27 18:04:10
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-01-27 18:47:27
FilePath: \Code\Python\算法练习\LeetCode\罗马数字转整数.py
Description: 
    复健
'''

'''
    切割字符串
    设置字典
    遍历相加

    问题：如何切割？
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        sum = 0
        for i,n in enumerate(s):
        sum += d.get(s[max(i-1, 0):i+1],d[n])
        return sum  

    思想：遍历，对于4、9之类的特殊字符，每次读取两位，如果不能寻找就加当前位
    对于开头存在特殊字符的处理：将特殊字符在字典内的值-1即可，实现对于重复加的处理
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))