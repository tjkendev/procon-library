# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

# Euler Tour Technique
S = []
F = [0]*N
depth = [0]*N
def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        dfs(w, d+1)
        S.append(v)
dfs(0, 0)

# Disjoint Sparse Tableの構築
INF = (N, None)
 
LV = (2*N-1).bit_length()
N0 = 2**LV
table = [[None]*N0 for i in range(LV)]
 
S0 = [INF]*N0
for i, v in enumerate(S):
    S0[i] = (depth[v], v)
 
sz = N0; hf = N0 >> 1
for k in range(LV):
    table_k = table[k]
    for i in range(hf, N0, sz):
        table_k[i-1] = r = S0[i-1]
        for j in range(i-2, i-hf-1, -1):
            table_k[j] = r = min(S0[j], r)
 
        table_k[i] = r = S0[i]
        for j in range(i+1, i+hf):
            table_k[j] = r = min(S0[j], r)
    sz >>= 1; hf >>= 1
 
# LCAの計算
def query(u, v):
    if u == v:
        return u
    fu = F[u]; fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
 
    k2 = (fu ^ fv).bit_length()
    table_l = table[LV - k2]
    ans = table_l[fu]
    if fv & ((1 << k2) - 1):
        ans = min(ans, table_l[fv])
    return ans[1]