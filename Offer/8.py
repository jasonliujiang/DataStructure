"""
跳台阶
Q: 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

A: 斐波那契数列的变形，f(n)=⎧⎩⎨1,2,f(n−1)+f(n−2),n=1n=2n≥3f(n)={1,n=12,n=2f(n−1)+f(n−2),n≥3 (递推公式)

"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0, 1, 2]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]
