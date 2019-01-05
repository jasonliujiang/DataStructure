'''
荷兰国旗问题：有一个只由0，1，2三种元素构成的整数数组，请使用交换、原地排序而不是使用计数进行排序。

给定一个只含0，1，2的整数数组A及它的大小，请返回排序后的数组。保证数组大小小于等于500。

解决方案：
    类似用快排的思想解决
'''


class ThreeColor(object):

    def three_color(self, A, n):
        """
        :type n: range of array
        :type A: array
        """
        if (A == None or len(A) < 2):
            return A
        left = -1
        index = 0
        right = n

        while (index < right):
            if (A[index] == 0):
                left = left+1
                A[left], A[index] = A[index], A[left]
                index +=1
            elif (A[index] == 2):
                right = right-1
                A[right], A[index] = A[index], A[right]
            else:
                index = index + 1
        return A


if __name__ == '__main__':
    a = [1,1,2,0,2,1,2,2,0,1,0,2,1]
    ThreeColor = ThreeColor()
    b = ThreeColor.three_color(a,13)
    print(b)