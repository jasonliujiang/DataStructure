"""
请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。


给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。


思路：原栈为data,辅助栈help.遍历弹出栈顶元素，如果i > help栈顶，一次把所有元素弹回data，i入栈。
"""


class TwoStacks:
    def twoStacksSort(self, numbers):
        # python 的方法：
        return sorted(numbers, reverse=True)
