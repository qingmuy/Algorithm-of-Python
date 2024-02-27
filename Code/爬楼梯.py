'''
    该题目涉及动态规划
    使用数学思维：联想到斐波那契数列
    建立数学函数：若爬上n层台阶，有f(n)种方法
    其最后一次跳跃只有两种方法：跳一步和跳两步
    所以f(n) = f(n - 1) + f(n - 2)
    对于起步，很容易计算f(0) = 1,f(1) = 1
    叠加即可计算
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 1 , 1
        for _ in range(n - 1):
            a , b = b , a + b
        return b