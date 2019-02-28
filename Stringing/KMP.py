class kmp:
    '''
    t为原字符串，p为要匹配的字符串，即t中是否包含p
    '''

    def get_kmp(self, t, p):
        i = 0
        j = 0
        next = self.get_next(p)
        while i < len(t) and j < len(p):
            if j == -1 or t[i] == p[j]:
                ++i
                ++j
            else:
                j = next[j]

        if j == len(p):
            return i - j
        else:
            return -1

    def get_next(self, p):
        next = [-1 for i in range(len(p))]
        # next[0] = -1
        i = 0
        j = -1
        while i < range(len(p)):
            if j == -1 or p[i] == p[j]:
                ++i
                ++j
                next[i] = j
            else:
                j = next[j]

        return next
