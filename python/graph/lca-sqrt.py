# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)
N = ...
G = [[...] for i in range(N)]

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
 

# ==== 平方分割の構築
INF = (N, None)
 
# sN: 1つのバケットに含む列の長さ (同時に分割するバケットの数)
sN = int(len(S)**0.5)+1
N0 = sN**2
 
S0 = [INF]*N0
for i, v in enumerate(S):
    S0[i] = (depth[v], v)
# sN個のバケットのdepth最小値を計算
GR = [min(S0[i:i+sN]) for i in range(0, N0, sN)]
 
# 各バケット内の、左端右端を含む区間のdepth最小値を計算
LV = [None]*N0; RV = [None]*N0
for i in range(0, N0, sN):
    # RV[i] = min(S0[(i//sN)*sN, i+1])
    RV[i] = r = S0[i]
    for j in range(i+1, i+sN):
        RV[j] = r = min(r, S0[j])
    # LV[i] = min(S0[i, (i//sN+1)*sN])
    LV[i+sN-1] = r = S0[i+sN-1]
    for j in range(i+sN-2, i-1, -1):
        LV[j] = r = min(r, S0[j])
 

# 平方分割を使ったLCAの計算
def query(u, v):
    fu = F[u]; fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    gu = fu // sN
    gv = fv // sN
 
    if gu == gv:
        # 同じバケットのS[fu:fv+1]のdepth最小値の頂点w
        return min(S0[fu:fv+1])[1]
 
    if gu+1 < gv:
        # fu, fvを含まないバケットgu+1, ..., gv-1のdepth最小値の頂点w
        return min(LV[fu], min(GR[gu+1:gv]), RV[fv])[1]
 
    # fu, fvを含まないバケットが存在しない(gu+1 == gv)場合のdepth最小値の頂点w
    return min(LV[fu], RV[fv])[1]