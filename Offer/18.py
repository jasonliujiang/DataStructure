"""
二叉树的镜像
Q:操作给定的二叉树，将其变换为源二叉树的镜像。

A: 先前序遍历这棵树的每个节点，如果遍历到的节点有子节点，就交换它的子节点，当交换完所有非叶节点的左右子节点后，得到树的镜像。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return
        if root.left == None and root.right == None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.Mirror(root.left)
        self.Mirror(root.right)
