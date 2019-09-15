N = ... # 頂点数
G = ... # 木


# Euler Tour Technique
S = []
FS = [0]*N
depth = [0]*N
def dfs(v, p, d):
    depth[v] = d
    FS[v] = len(S)
    S.append(v)
    for w in G[v]:
        if w == p:
            continue
        dfs(w, v, d+1)
        S.append(v)
dfs(0, -1, 0)
 
# Sparse Table
L = len(S)
lg = [0]*(L + 1)
for i in range(2, L+1):
    lg[i] = lg[i >> 1] + 1
st = [None]*(lg[L] + 1)
st0 = st[0] = S
b = 1
for i in range(lg[L]):
    st0 = st[i+1] = [p if depth[p] <= depth[q] else q for p, q in zip(st0, st0[b:])]
    b <<= 1
 
# LCA O(1)
def query(u, v):
    x = FS[u]; y = FS[v]
    if x > y:
        x, y = y, x
    l = lg[y - x + 1]
    px = st[l][x]; py = st[l][y - (1 << l) + 1]
    return px if depth[px] <= depth[py] else py