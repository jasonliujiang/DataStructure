"""
链表中倒数第k个结点
Q: 输入一个链表，输出该链表中倒数第k个结点。

A: 设置两个指针指向头节点，第一个指针向前走k-1步，走到第k个结点，
此时，第二个指针和第一个指针同时移动，当第一个指针到尾节点的时候，第二个指针指向倒数第k个结点，
注意链表为空，k为0，k大于链表的长度的情况
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0 or head == None:
            return None
        pAhead = head
        pBhead = head

        for i in range(k - 1):
            if pAhead.next is not None:
                pAhead = pAhead.next
            else:
                return None

        while pAhead.next is not None:
            pAhead = pAhead.next
            pBhead = pBhead.next

        return pBhead
