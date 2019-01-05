'''
给定一个int矩阵mat，同时给定矩阵大小nxm及待查找的数x，请返回一个bool值，代表矩阵中是否存在x。
所有矩阵中数字及x均为int范围内整数。保证n和m均小于等于1000。

矩阵按行依次递增，按列依次递增，从右上角开始索引。
'''


class Finder(object):
    def index(self, mat, n, m, x):
        i = 0
        j = m - 1
        if x < mat[0][0] or x > mat[n - 1][m - 1]:
            return False
        while x != mat[i][j]:
            if x > mat[i][j]:
                i += 1
            else:
                j -= 1

            if (i == n - 1) and (j == 0):
                if mat[i][j] == x:
                    return True
                else:
                    return False

        return True


if __name__ == '__main__':
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    f = Finder()
    out = f.index(arr, 3, 3, 10)
    print(out)
