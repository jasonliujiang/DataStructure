'''
有一个整形数组A，请设计一个复杂度为O(n)的算法，算出排序后相邻两数的最大差值。

给定一个int数组A和A的大小n，请返回最大的差值。保证数组元素多于1个。

测试样例：
[1,2,5,4,6],5
返回：2

解题思路：先找到最小值和最大值，然后按照最小值和最大值进行划分区间（max-min）/n,
进行
'''


class Gap:
    def maxGap(self, A, n):
        # write code here
        mi = min(A)
        ma = max(A)
        l = [[] for i in range(n + 1)]
        for i in A:
            l[((i - mi) * n) // (ma - mi)].append(i)  # 计算桶号
        num = min(l[0]) - max(l[0])
        i = 0;
        j = 1
        while j < len(l):
            while l[j] == []:
                j += 1
            num = max(num, min(l[j]) - max(l[i]))  # 前一个桶的最小值-上一个桶的最大值。

            i = j
            j += 1
        return num
