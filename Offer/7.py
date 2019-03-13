"""
斐波那契数列
Q: 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39

A: 不使用递归实现数列，需要把前面两个数字存入在一个数组中,实际一直在更新。

"""


# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]
