"""
对于两个字符串A和B，如果A和B中出现的字符种类相同且每种字符出现的次数相同，则A和B互为变形词，请设计一个高效算法，检查两给定串是否互为变形词。

给定两个字符串A和B及他们的长度，请返回一个bool值，代表他们是否互为变形词。


解决办法，新建一个字典做词频统计

"""


class Transform:
    def chkTransform(self, A, lena, B, lenb):
        dictA = self.countDict(A, lena)
        dictB = self.countDict(B, lenb)
        return dictA == dictB

    def countDict(self, A, lena):
        dictA = {}
        for i in range(lena):
            if A[i] not in dictA:
                dictA[A[i]] = 0
            dictA[A[i]] += 1
        return dictA
