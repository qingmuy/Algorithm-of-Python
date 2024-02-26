'''
Author: Muy lzqm04@gmail.com
Date: 2024-01-30 18:00:56
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-01-30 22:12:15
FilePath: \Code\Python\算法练习\LeetCode\有效的括号.py
Description: 
    复健
'''

'''
    转为列表
    使用字典 or 列表
    (,[,{,},],)
    回文数问题判断，不符False
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # 简单逻辑判断，如果字符串个数并非偶数则直接不闭合
        if len(s) % 2 != 0:
            print("字符串长度不符合")
            return False
        
        # 创建列表记录括号数目，转为字符串判断回文数，若非回文数直接False
        Valid = [0,0,0,0,0,0]
        for i in s:
            if i == "(":
                Valid[0] += 1
            elif i == "[":
                Valid[1] += 1
            elif i == "{":
                Valid[2] += 1
            elif i == "}":
                Valid[3] += 1
            elif i == "]":
                Valid[4] += 1
            elif i == ")":
                Valid[5] += 1
        if ''.join([str(i) for i in Valid]) != ''.join([str(i) for i in Valid])[::-1]:
            print("逻辑不符合",Valid)
            print(''.join([str(i) for i in Valid]))
            print(reversed(''.join([str(i) for i in Valid])))
            return False
        else:

            print("正确")
            return True

    isValid("([)]",s="([)]")


'''
    以上方法仍然不成熟，使用栈才是最优解
    如何使用栈的思维处理该问题？
    基本操作：进栈 出栈

    栈先入后出特点恰好与本题括号排序特点一致，
    即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，
    则遍历完所有括号后 stack 仍然为空；
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            # 字符串的长度不符合偶数
            return False
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            # 左括号则入栈
            if c in dic: stack.append(c)
            # 
            elif c != dic[stack.pop()]: 
                return False 
        return len(stack) == 0
        