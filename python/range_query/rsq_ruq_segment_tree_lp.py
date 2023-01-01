# N: 処理する区間の長さ
N = ...

LV = (N-1).bit_length()
N0 = 2**LV
data = [0]*(2*N0)
lazy = [None]*(2*N0)
 
def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1
 
# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = lazy[2*i] = data[2*i-1] = data[2*i] = v >> 1
        lazy[i-1] = None
 
# 区間[l, r)をxに更新
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)
 
    L = N0 + l; R = N0 + r
    v = x
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = v
        if L & 1:
            lazy[L-1] = data[L-1] = v
            L += 1
        L >>= 1; R >>= 1; v <<= 1
    for i in ids:
        data[i-1] = data[2*i-1] + data[2*i]
 
# 区間[l, r)内の合計を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r
 
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s += data[R-1]
        if L & 1:
            s += data[L-1]
            L += 1
        L >>= 1; R >>= 1
    return s