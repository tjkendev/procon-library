# G is a tree
def lca(N, G, s, QS):
    res = [-1]*len(QS)

    A = [[] for i in range(N)]
    for i, (u, v) in enumerate(QS):
        if u == v:
            res[i] = u
            continue
        A[u].append((v, i))
        A[v].append((u, i))

    # disjoint data structure
    *prt, = range(N)
    def root(x):
        if x == prt[x]:
            return x
        prt[x] = x = root(prt[x])
        return x
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            prt[py] = px
            return px
        else:
            prt[px] = py
            return py

    anc = [-1]*N
    # DFS (non-recursive)
    stk = [s]
    *it, = map(len, G)
    while stk:
        v = stk[-1]
        if anc[v] == -1:
            anc[v] = v
        else:
            anc[unite(v, G[v][it[v]])] = v

        while it[v]:
            it[v] -= 1
            w = G[v][it[v]]
            if anc[w] == -1:
                stk.append(w)
                break
        else:
            for w, i in A[v]:
                if anc[w] != -1 and res[i] == -1:
                    res[i] = anc[root(w)]
            stk.pop()
    return res
