"""
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

方法：定义两个栈，一个存放数据，一个存放栈内最小元素的栈
"""


class Solution:
    def __init__(self):
        self.statck_data = []
        self.statck_min = []

    def push(self, node):
        # write code here
        self.statck_data.append(node)
        if not self.statck_min:
            self.statck_min.append(node)
        elif node < self.statck_min[-1]:
            self.statck_min.append(node)
        else:
            self.statck_min.append(self.statck_min[-1])

    def pop(self):
        p = self.statck_data.pop()
        self.statck_min.pop()
        return p

    def top(self):
        t = self.statck_data[-1]
        return t
        # write code here

    def min(self):
        m = self.statck_min[-1]
        # write code here
        return m
