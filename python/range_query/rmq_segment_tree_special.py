N0 = 2**(N-1).bit_length()
INF = 2**31-1
data = [INF]*(2*N0)

# 前計算
I = []; J = []
for x in range(N0, 2*N0+1):
    y = (x // (x & -x)) >> 1
    I.append((y << 1)-1 if y else 0)
    J.append(y << 1)
J.reverse()

# 従来のupdateと同じ
def update(k, x):
    k += N0
    data[k-1] = x
    while k > 1:
        k >>= 1
        data[k-1] = min(data[2*k-1], data[2*k])

# query [0, r)
def lquery(r):
    return min(map(data.__getitem__, __lquery(r)))
def __lquery(r):
    while r:
        yield I[r]
        r -= (r & -r)

# query [l, N0)
def rquery(l):
    return min(map(data.__getitem__, __rquery(l)))
def __rquery(l):
    r = N0 - l
    while r:
        yield J[r]
        r -= (r & -r)

# query [k, k+1)
def query1(k):
    return data[k+N0-1]