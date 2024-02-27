'''
Author: Muy lzqm04@gmail.com
Date: 2024-02-27 12:40:03
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-02-27 20:30:11
FilePath: \Code\Python\Algorithm-of-Python\Code\x的平方根.py
Description: custom_string_obkoro1
描述
Copyright (c) 2024 by Muy, All Rights Reserved. 
'''
'''
    给你一个非负整数x，计算并返回x的算术平方根 。
    由于返回类型是整数，结果只保留整数部分，小数部分将被舍去 。
    注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
'''
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.trunc(math.sqrt(x))