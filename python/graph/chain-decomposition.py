# B, A = construct(G, N)
# B: グラフGの橋
# A: グラフGの関節点

def construct(G, N):
    P = [0]*N
    G0 = [[] for i in range(N)]
    V = []

    lb = [0]*N
    def dfs(v, p):
        P[v] = p
        V.append(v)
        lb[v] = len(V)
        for w in G[v]:
            if w == p:
                continue
            if lb[w]:
                if lb[v] < lb[w]:
                    G0[v].append(w)
                continue
            dfs(w, v)
    dfs(0, -1)

    B = []
    ap = [0]*N

    used = [0]*N
    first = 1
    used[0] = 1
    for u in V:
        if not used[u]:
            p = P[u]
            B.append((u, p) if u < p else (p, u))
            if len(G[u]) > 1:
                ap[u] = 1
            if len(G[p]) > 1:
                ap[p] = 1

        cycle = 0
        for v in G0[u]:
            w = v
            while w != u and not used[w]:
                used[w] = 1
                w = P[w]
            if w == u:
                cycle = 1

        if cycle:
            if not first:
                ap[u] = 1
            first = 0

    A = [v for v in range(N) if ap[v]]
    return B, A
