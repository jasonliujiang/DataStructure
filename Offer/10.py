"""
矩形覆盖 Q: 我们可以用2 1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？
A: 依然是斐波那契数列的变形。代码参考跳台阶。
"""


# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]
