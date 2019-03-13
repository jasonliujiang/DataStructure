"""
反转链表
Q: 输入一个链表，反转链表后，输出新链表的表头。

A: 主要注意当头结点为空或者整个链表只有一个结点时，翻转后的链表断裂，返回的翻转之后的头节点不是原来的尾节点。
所以需要一个翻转后的头节点，一个指向当前结点的指针，两个分别指向当前结点的前后结点的指针，防止断裂。也可以使用递归。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pRecerseHead = None
        pPre = None
        pNode = pHead
        while pNode is not None:
            pNext = pNode.next
            if pNode.next is None:
                pRecerseHead = pNode
            pNode.next = pPre
            pPre = pNode
            pNode = pNext

        return pRecerseHead
