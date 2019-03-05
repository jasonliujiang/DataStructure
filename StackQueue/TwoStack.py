"""
编写一个类,只能用两个栈结构实现队列,支持队列的基本操作(push，pop)。

给定一个操作序列ope及它的长度n，其中元素为正数代表push操作，为0代表pop操作，保证操作序列合法且一定含pop操作，请返回pop的结果序列。

测试样例：
[1,2,3,0,4,0],6
返回：[1,2]
"""


class TwoStack:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def twoStack(self, ope, n):
        # write code here
        res = []
        for i in ope:
            if i > 0:
                self.stack_push.append(i)
            elif i == 0:
                if not len(self.stack_pop):
                    while len(self.stack_push):
                        self.stack_pop.append(self.stack_push.pop())

                    res.append(self.stack_pop.pop())
                else:
                    res.append(self.stack_pop.pop())

        return res


"""

"""
