"""
常规二分查找
"""


def binary_search(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            # 每次移动left和right指针的时候，需要在mid的基础上+1或者-1，
            # 防止出现死循环， 程序也就能够正确的运行
            low = mid + 1
        else:
            high = mid - 1

    return 0


"""
查找第一个与key相等的元素

查找第一个相等的元素，也就是说等于查找key值的元素有好多个，返回这些元素最左边的元素下标。
"""


def findFirstEqual(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] >= key:
            high = mid - 1
        else:
            low = mid + 1

        if low < len(arr) - 1 and arr[low] == key:
            return low


"""
查找最后一个与key相等的元素
　　查找最后一个相等的元素，也就是说等于查找key值的元素有好多个，返回这些元素最右边的元素下标。
"""


def findLastEqual(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and arr[high] == key:
        return high


'''
查找最后一个等于或者小于key的元素
　　查找最后一个等于或者小于key的元素，也就是说等于查找key值的元素有好多个，返回这些元素最右边的元素下标；如果没有等于key值的元素，则返回小于key的最右边元素下标。
'''


def findLastEqualSmaller(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
        return high

# https://www.cnblogs.com/luoxn28/p/5767571.html
