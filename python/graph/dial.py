# - N頂点のグラフG
# - 辺の重みは最大W
# - 開始頂点はs
def dial(N, G, W, s):
    B = [-1]*(N*W + 1) # first
    L = [-1]*(N*W + 1) # last

    # prv, nxt: 各頂点の前後を管理
    *prv, = range(-1, N-1)
    *nxt, = range(1, N+1)

    nxt[-1] = -1
    prv[s+1] = s-1
    nxt[s-1] = (s+1 if s < N-1 else -1)
    prv[s] = nxt[s] = -1
    B[0] = L[0] = s
    B[N*W] = +(s == 0)
    L[N*W] = (N-1 if s < N-1 else N-2)

    dist = [N*W] * N
    dist[s] = 0
    for w in range(N*W):
        v = B[w]
        while v != -1:
            for x, c in G[v]:
                e = w + c
                if e < dist[x]:
                    d = dist[x]
                    dist[x] = e

                    # bucket d から 頂点x を削除
                    p = prv[x]; n = nxt[x]
                    if p != -1:
                        nxt[p] = n
                    else:
                        B[d] = n
                    if n != -1:
                        prv[n] = p
                    else:
                        L[d] = p

                    # bucket e の末尾に 頂点x を追加
                    l = L[e]
                    if l != -1:
                        nxt[l] = x
                    else:
                        B[e] = x
                    prv[x] = l; nxt[x] = -1
                    L[e] = x
            v = nxt[v]
    return dist
