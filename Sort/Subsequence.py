'''
对于一个数组，请设计一个高效算法计算需要排序的最短子数组的长度。

给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的长度。(原序列位置从0开始标号,若原序列有序，返回0)。保证A中元素均为正整数。

测试样例：
[1,4,6,5,9,10],6
返回：2
'''


class Subsequence:
    def shortestSubsequence(self, A, n):
        left = 0
        right = 0
        min = A[n - 1]
        max = A[0]
        for i in range(1, n):
            if A[i] >= max:
                max = A[i]
            else:
                right = i
        for j in range(n - 2, -1, -1):
            if A[j] <= min:
                min = A[j]
            else:
                left = j

        if left == 0 and right == 0:
            return 0
        else:
            return right - left + 1


if __name__ == '__main__':
    s = Subsequence()
    A = [1, 4, 6, 5, 9, 10]
    output = s.shortestSubsequence(A, 6)
    print(output)
