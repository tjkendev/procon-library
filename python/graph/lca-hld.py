# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

from collections import deque
N = ...
G = [[...] for i in range(N)]

# === HLD計算処理
# 各頂点の、heavy-pathで繋ぐ1つの子頂点を決定
H = [0]*N
prv = [None]*N
def dfs(v):
    s = 1; heavy = None; m = 0
    for w in G[v]:
        prv[w] = v
        c = dfs(w)
        if m < c:
            heavy = w
            m = c
        s += c
    H[v] = heavy
    return s
dfs(0)
 
 
# グラフGをheavy-pathに沿って縮約
SS = []   # SS[k] = [v, ...]: k番目に縮約した頂点にまとめた頂点の列
D = []    # D[k] = d: k番目に縮約した頂点の深さd
L = [0]*N # L[i] = k: 縮約前の頂点v_iが属する縮約後の頂点番号k
I = [0]*N # I[i] = pos: 縮約前の頂点v_iが縮約後の列で存在する位置
que = deque([(0, 0)])
while que:
    v, d = que.popleft()
    S = []
    k = len(SS)
    while v is not None:
        I[v] = len(S)
        S.append(v)
        L[v] = k
        h = H[v]
        for w in G[v]:
            if h == w:
                continue
            que.append((w, d+1))
        v = h
    SS.append(S)
    D.append(d)

# HLDを元にした LCAのクエリ処理
def query(u, v):
    lu = L[u]; lv = L[v]
    dd = D[lv] - D[lu]
    if dd < 0:
        lu, lv = lv, lu
        v, u = u, v
        dd = -dd
 
    # assert D[lu] < D[lv]

    # 高さ合わせ
    for _ in range(dd):
        v = prv[SS[lv][0]]
        lv = L[v]
 
    # assert D[lu] == D[lv]

    # 同じ頂点に到達するまで1つずつ遡る
    while lu != lv:
        u = prv[SS[lu][0]]
        lu = L[u]
 
        v = prv[SS[lv][0]]
        lv = L[v]
 
    # 縮約後の頂点が持つ列の中で、uとvの内、前にいる方をLCAとして返す
    return u if I[u] < I[v] else v
