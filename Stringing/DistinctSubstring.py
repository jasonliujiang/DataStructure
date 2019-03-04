"""
对于一个字符串,请设计一个高效算法，找到字符串的最长无重复字符的子串长度。

给定一个字符串A及它的长度n，请返回它的最长无重复字符子串长度。保证A中字符全部为小写英文字符，且长度小于等于500。


定义一个map集合，记录每个点的下标和数据遍历，如果存在，则为重复，求差值，不存在相加。

"""


def longestSubstring(StringA, n):
    max_langth = 0
    dic = {}
    pre = -1#定义最后出现的重复字母的前一个下标

    for i in range(n):
        if dic.__contains__(StringA[i]):  # python2 用dic.has_key(A[i])
            if dic[StringA[i]] > pre:
                len = i - dic[StringA[i]]
                pre = dic[StringA[i]]
            else:
                len = i -pre

            max_langth = max(max_langth, len)
            dic[StringA[i]] = i
        else:
            dic[StringA[i]] = i
            len = i - pre
            max_langth = max(len, max_langth)

    return max_langth
