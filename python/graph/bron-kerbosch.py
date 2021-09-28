def maximum_clique(N, G):
    def dfs(V, P, X):
        if not P and not X:
            # V is a maximal clique
            return V
        u = next(iter(X or P)) # a pivot vertex
        r = set()
        for v in P - G[u]:
            r0 = dfs(V | {v}, P & G[v], X & G[v])
            if len(r) < len(r0):
                r = r0
            P.remove(v)
            X.add(v)
        return r

    # sort vertices in a degeneracy ordering
    *I, = range(N)
    I.sort(key = lambda x: len(G[x]), reverse=1)

    ans = set()
    P = set(range(N))
    X = set()
    for v in I:
        res = dfs({v}, P & G[v], X & G[v])
        if len(ans) < len(res):
            ans = res
        P.remove(v)
        X.add(v)
    return ans

# example
G = [set() for i in range(6)]
G[0] |= {1, 2, 3, 4}
G[1] |= {0, 2, 5}
G[2] |= {0, 1, 3, 4}
G[3] |= {0, 2, 4}
G[4] |= {0, 2, 3}
G[5] |= {1}
print(maximum_clique(6, G))
# => "{0, 2, 3, 4}"