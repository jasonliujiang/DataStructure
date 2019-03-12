# -*- coding:utf-8 -*-
"""
Q: 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

A: 从右上或者左下开始查找。从右上开始查找：如果数组中的数比这个整数大，向左移动一位，如果数组中的数比这个数小，向下移动一位。

"""


class Solution:
    # 二维列表
    def Find(self, target, array):
        if not array:
            return False

        row_num = len(array)
        col_num = len(array[0])

        row = 0
        col = col_num - 1
        while row < row_num and col >=0:
            if array[row][col] < target:
                row = row+1
            elif array[row][col] > target:
                col = col -1
            else:
                return True
        return False
