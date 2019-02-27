"""
对于两棵彼此独立的二叉树A和B，请编写一个高效算法，检查A中是否存在一棵子树与B树的拓扑结构完全相同。

给定两棵二叉树的头结点A和B，请返回一个bool值，代表A中是否存在一棵同构于B的子树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class IdenticalTree:
    def chkIdentical(self, A, B):
        listA = self.di(A)
        listB = self.di(B)
        if listB in listA:
            return True
        return False

    def di(self, A):
        if A == None:
            return "#"
        string = str(A.val)
        string += self.di(A.left)
        string += self.di(A.right)
        return string
        # write code here
