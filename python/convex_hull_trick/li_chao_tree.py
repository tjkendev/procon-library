# Li Chao Tree

N0 = 2**(M-1).bit_length()
data = [None]*(2*N0+1)

X = [10**10]*N0 # N0に持つ座標N個を入れる

def f(line, x):
    p, q = line
    return p*x + q

def _add_line(line, k, l, r):
    m = (l + r) // 2
    if data[k] is None:
        data[k] = line
        return
    lx = X[l]; mx = X[m]; rx = X[r-1]
    left = (f(line, lx) < f(data[k], lx))
    mid = (f(line, mx) < f(data[k], mx))
    right = (f(line, rx) < f(data[k], rx))
    if left and right:
        data[k] = line
        return
    if not left and not right:
        return
    if mid:
        data[k], line = line, data[k]
    if left != mid:
        _add_line(line, 2*k+1, l, m)
    else:
        _add_line(line, 2*k+2, m, r)

# 直線のみに対応する場合のadd_line: O(log N)
def add_line(line):
    return _add_line(line, 0, 0, N0)

# 線分に対応する場合のadd_line: O(log^2 N)
def add_line(line, a, b):
    L = a + N0; R = b + N0
    a0 = a; b0 = b
    sz = 1
    while L < R:
        if R & 1:
            R -= 1
            b0 -= sz
            _add_line(line, R-1, b0, b0+sz)
        if L & 1:
            _add_line(line, L-1, a0, a0+sz)
            L += 1
            a0 += sz
        L >>= 1; R >>= 1
        sz <<= 1

def query(k):
    x = X[k]
    k += N0-1
    s = 1e30
    while k >= 0:
        if data[k]:
            s = min(s, f(data[k], x))
        k = (k - 1) // 2
    return s
