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

# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

# Binary Index Tree (2-dimension)
class BIT2:
    # H*W
    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.data = [{} for i in xrange(h+1)]

    # O(logH*logW)
    def sum(self, i, j):
        s = 0
        data = self.data
        while i > 0:
            el = data[i]
            k = j
            while k > 0:
                s += el.get(k, 0)
                k -= k & -k
            i -= i & -i
        return s

    # O(logH*logW)
    def add(self, i, j, x):
        w = self.w; h = self.h
        data = self.data
        while i <= h:
            el = data[i]
            k = j
            while k <= w:
                el[k] = el.get(k, 0) + x
                k += k & -k
            i += i & -i

    # [x0, x1) x [y0, y1)
    def range_sum(self, x0, x1, y0, y1):
        return self.sum(x1, y1) - self.sum(x1, y0) - self.sum(x0, y1) + self.sum(x0, y0)

# set()のような要素の追加削除 + lower_bound() を実現するセグ木
# 追加削除される要素が先読みできる場合に利用可
E = [1, 10, 15] # 追加削除される要素のリスト (sorted)
mp = {e: i for i, e in enumerate(E)}

# 区間[L, R] := 区間[E[L], E[R]]に存在する最大要素 (なければNone)
L = len(E)
L0 = 2**(L-1).bit_length()
data = [None]*(L0*2)
# 要素eをx個追加: O(logN)
def update(e, x):
    k = mp[e]
    k += L0 - 1
    if data[k] is None:
        r = data[k] = [e, x]
    else:
        r = data[k]
        r[1] = max(0, r[1]+x)
    while k:
        k = (k - 1) // 2
        l = data[2*k+1]; r = data[2*k+2]
        if r and r[1]:
            if data[k] is r:
                return
            data[k] = r
        elif l and l[1]:
            if data[k] is l:
                return
            data[k] = l
        else:
            if data[k] is None:
                return
            data[k] = None
# v以上の要素を二分探索により検索: O(logN)
def lower_bound(v):
    f = data[0]
    if not f or f[0] < v or f[1] == 0:
        return None
    k = 0
    while k < L0 - 1:
        l = data[2*k+1]
        if l is None or l[1] == 0 or l[0] < v:
            k = 2*k+2
        else:
            k = 2*k+1
    #assert data[k][1] > 0
    return E[k - (L0 - 1)]
# 含有判定: O(1)
def contain(v):
    r = data[k + L0 - 1]
    return r and r[1] > 0
