# 部分永続Union-Find
# N: 頂点数
N = ...

# p[u]: 頂点uの親頂点
# sz[u]: 現在の親頂点uの木が含む頂点数
# H[u]: 現在の親頂点uの木の高さ
# S[u] = [(t, s), ...]:
#     時刻tに別の頂点をマージした親頂点uの木が含む頂点数s
# T[u]: 頂点uが親頂点でなくなる時刻

INF = 1e18
*p, = range(N)
sz = [1]*N
H = [1]*N
S = [[(0, 1)] for i in range(N)]
T = [INF]*N
 
def find(x, t):
    while T[x] <= t:
        x = p[x]
    return x
 
def unite(x, y, t):
    px = find(x, t)
    py = find(y, t)
    if px == py:
        return 0
    if H[py] < H[px]:
        p[py] = px
        T[py] = t
        sz[px] += sz[py]
        S[px].append((t, sz[px]))
    else:
        p[px] = py
        T[px] = t
        sz[py] += sz[px]
        S[py].append((t, sz[py]))
        H[py] = max(H[py], H[px]+1)
    return 1

from bisect import bisect
 
def size(x, t):
    y = find(x, t)
    idx = bisect(S[y], (t, INF))-1
    return S[y][idx]
