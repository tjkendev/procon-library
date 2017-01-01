# 領域木(kd木)
# あとでライブラリ用に書き直す
# https://gist.github.com/tjkendev/56a15738d3c8ce88d99561ceab0d5469

# SegmentTree (区間一様に足す + Minを計算)
# 定数倍がでかい
INF = 10**18+7
class SegmentTree:
    def __init__(self, n):
        self.n = n = 1 << (n-1).bit_length()
        self.dmin = [INF]*(n << 1)
        self.dadd = [0]*(n << 1)
    def __set(self, l, r, x, k, a, b):
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.dadd[k] += x
            return
        self.__set(l, (l+r)/2, x, 2*k+1, a, b)
        self.__set((l+r)/2, r, x, 2*k+2, a, b)

        self.dmin[k] = min(self.__get_value(2*k+1), self.__get_value(2*k+2))

    def __get_value(self, k):
        r = self.dmin[k]
        if r == INF:
            return self.dadd[k]
        else:
            return r + self.dadd[k]

    def set(self, a, b, x):
        self.__set(0, self.n, x, 0, a, b)

    def __get(self, l, r, k, a, b):
        if r <= a or b <= l:
            return INF-1
        if a <= l and r <= b:
            return self.__get_value(k)
        lv = self.__get(l, (l+r)/2, 2*k+1, a, b)
        rv = self.__get((l+r)/2, r, 2*k+2, a, b)
        if min(lv, rv) == INF:
            return self.dadd[k]
        return min(lv, rv) + self.dadd[k]

    def get(self, a, b):
        return self.__get(0, self.n, 0, a, b)
