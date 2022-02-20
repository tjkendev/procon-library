# N: クエリ処理する列のサイズ
N = ...

data = [0]*(N+1)

def init(A):
    data[1:] = A
    for i in range(1, N):
        if i + (i & -i) <= N:
            data[i + (i & -i)] += data[i]

def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k
 
def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

# 二分探索
N0 = 2**(N-1).bit_length()
def lower_bound(x):
    w = i = 0
    k = N0
    while k:
        if i+k <= N and w + data[i+k] <= x:
            w += data[i+k]
            i += k
        k >>= 1
    return i+1