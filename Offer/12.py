"""
数值的整数次方
Q: 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

A: 如果用常规的算法，要注意：1.指数为负数的时候，2.底数为零且指数为负数的时候，这种情况的时候，不能直接通过底数==0来判断，计算机内表示小数有误差，只能判断他们的差的绝对值是不是在一个很小的范围内。 所以用递归好一点。{an=an/2×an/2,n为偶数an=a(n−1)/2×a(n−1)2,n为奇数{an=an/2×an/2,n为偶数an=a(n−1)/2×a(n−1)2,n为奇数 利用右移一位实现除2运算，用&1 运算，判断是否为奇数，能提高效率。

多考虑情况
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        try:

            ret = self.power_value(base, abs(exponent))
            if exponent < 0:
                return 1 / ret

        except ZeroDivisionError:
            print('Error: base is zero')
        else:
            return ret

    def power_value(self, base, ex):
        if ex == 0:
            return 1
        elif ex == 1:
            return base
        else:
            ret = self.power_value(base, ex >> 1)  # >>右移位运算符，>>1  除以2
            ret *= ret
            if ex & 1 == 1:
                ret *= base
            return ret
