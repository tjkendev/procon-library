from bisect import bisect

def construct(N, A):
    INF = 10**9
    N0 = 2**(N-1).bit_length()
    data = [None]*(2*N0)
    for i, a in enumerate(A):
        data[N0-1+i] = [a]
    for i in range(N, N0):
        data[N0-1+i] = [INF]
    for i in range(N0-2, -1, -1):
        p = data[2*i+1]; q = data[2*i+2]
        pl = len(p); ql = len(q)
        res = [0]*(pl + ql)
        a = b = 0
        while a < pl and b < ql:
            if p[a] < q[b]:
                res[a+b] = p[a]
                a += 1
            else:
                res[a+b] = q[b]
                b += 1
        while a < pl:
            res[a+b] = p[a]
            a += 1
        while b < ql:
            res[a+b] = q[b]
            b += 1
        data[i] = res
    return N0, data

# count elements A_i s.t. A_i <= k for i in [l, r)
def query1(N0, data, l, r, k):
    L = l + N0; R = r + N0
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s += bisect(data[R-1], k-1)
        if L & 1:
            s += bisect(data[L-1], k-1)
            L += 1
        L >>= 1; R >>= 1
    return s

# count elements A_i s.t. a <= A_i < b for i in [l, r)
def query(N0, data, l, r, a, b):
    L = l + N0; R = r + N0
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            s += bisect(data[R-1], b-1) - bisect(data[R-1], a-1)
        if L & 1:
            s += bisect(data[L-1], b-1) - bisect(data[L-1], a-1)
            L += 1
        L >>= 1; R >>= 1
    return s

N = 6
A = [6, 1, 4, 5, 3, 2]
N0, data = construct(N, A)
print(query1(N0, data, 2, 5, 4))
# => "1"
print(query(N0, data, 1, 4, 3, 5))
# => "1"