"""
变态跳台阶
Q: 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

A: 斐波那契数列的变形。f(n)=⎧⎩⎨1,1,2×f(n−1),n=0n=1n≥2f(n)={1,n=01,n=12×f(n−1),n≥2 (递推求解)
"""


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        ans = 1
        if number >= 2:
            for i in range(number - 1):
                ans = ans * 2
        return ans
