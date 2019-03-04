"""
实现一个栈的逆序，但是只能用递归函数和这个栈本身的pop操作来实现，而不能自己申请另外的数据结构。

给定一个整数数组A即为给定的栈，同时给定它的大小n，请返回逆序后的栈。

测试样例：
[4,3,2,1],4
返回：[1,2,3,4]


"""


class stackreverse:
    # 获取栈底元素
    def get(self, stack):
        res = stack.pop()
        if not len(stack):
            return res
        else:
            last = self.get(stack)
            stack.append(res)
            return last

    def reverseStack(self, A):
        # 简单实现：

        # 递归思想实现：
        if not len(A):
            return
        else:
            res = self.get(A)
            self.reverseStack(A)
            A.append(res)

        # return A


if __name__ == '__main__':
    A = [230, 272, 224, 399, 126]
    stackreverse.reverseStack(A)
    print(A)
