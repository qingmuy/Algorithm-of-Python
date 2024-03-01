'''
Author: Muy lzqm04@gmail.com
Date: 2024-03-01 20:27:14
LastEditors: Muy lzqm04@gmail.com
LastEditTime: 2024-03-01 20:27:20
FilePath: \Code\Python\算法练习\LeetCode\买卖股票的最佳时机.py
Description: 
描述
Copyright (c) 2024 by Muy, All Rights Reserved. 
'''

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # 暴力解法；已经超时
        # 强行求对于某天买入某天卖出的差值并返回最小值
        # lenth = len(prices)
        # lst = []
        # for i in range(lenth):
        #     temp = []
        #     for j in range(i, lenth):
        #         temp.append(prices[i] - prices[j])
        #     lst.append(min(temp))
        # return -(min(lst))

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 锚定某天买入，推以后最大值卖出
#         # 超时
#         lenth = len(prices)
#         lst = []
#         for i in range(lenth):
#             lst.append(max(prices[j] for j in range(i, lenth)) - prices[i])
#         return max(lst)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         minprice = prices[0]
#         maxprofit = 0
#         for price in prices:
#             minprice = min(minprice, price)
#             maxprofit = max(maxprofit, price - minprice)
#         return maxprofit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans=0
        curmin=prices[0]
        for i,v in enumerate(prices):
            if v<curmin:
                curmin=v
            else:
                ans=max(ans, v-curmin)
        return ans