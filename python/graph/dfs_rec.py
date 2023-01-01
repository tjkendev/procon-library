def dfs_rec(N, G, s):
    used = [0]*N
    def dfs(v, p):
        used[v] = 1
        ... # A
        for w in G[v]:
            ... # B1
            if used[w]:
                continue
            ... # B2
            r = dfs(w, v)
            ... # C
        ... # D
        return ... # E
    r0 = dfs(s, -1)
