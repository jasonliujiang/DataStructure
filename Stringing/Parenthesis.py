"""
对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。

给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。


仿照栈的思想做优化

"""


def chkParenthesis(StringA, n):
    status = 0
    for i in StringA:
        if i == '(':
            status = status + 1
        elif i == ")":
            status = status - 1

        if status < 0:
            return False

    return status

    if status == 0:
        return True
    else:
        return False
