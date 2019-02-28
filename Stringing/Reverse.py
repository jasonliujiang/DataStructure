"""
对于一个字符串，请设计一个算法，只在字符串的单词间做逆序调整，也就是说，字符串由一些由空格分隔的部分组成，你需要将这些部分逆序。

给定一个原字符串A和他的长度，请返回逆序后的字符串。


常规思路：现以空格切分，然后对每个单词逆序，然后对所有句子逆序。
"""


class Reverse:
    def reverseSentence(self, A, n):
        # write code here
        a = A.split(' ')

        #  [::-1]  的含义是将列表或者元组的内容反转
        #  [:-1]   的含义是切片到倒数第一个元素之前的元素。
        return ' '.join(a[::-1])

