########python3编程输入输出#############

# 1.一行输入
def OneInput():
    # 1.1输入一个数/字符串：
    s = input()
    print(s)

    # 1.2输入一整个数组
    s = input()  # 1 2 3 4
    s = [i for i in s.split()]
    print(s)  # ['1','2','3','4']


# 2.两行输入
# 两行读取要在一行读取的基础上再进行一些操作。这里举个例子，假设第一行输入数组长度，第二行输入数组，那么读入操作分两步，首先获得数组长度，然后获取数组。
def TwoInput():
    while True:
        s = input()
        if s != "":
            length = int(s)
            nums = [int(i) for i in input().split()]
            print(length, nums)
            break
        else:
            break


def ManyInput():
    # 3.1 每行输入一个数/字符串
    while True:
        s = input()
        if s != "":
            print(s)
        else:
            break


def ManyInput2():
    # 3.2 每行输入不同的内容，如第一行输入操作个数，第二行开始输入n个数组
    data = []
    length = int(input())
    n = 0
    while n < length:
        s = input()
        if s != "":
            temp = [i for i in s.split()]
            data.append(temp)
            n = n + 1
        else:
            break
    print(data)


if __name__ == '__main__':
    ManyInput2()
