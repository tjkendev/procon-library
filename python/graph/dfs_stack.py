def dfs_stack(N, G, s):
    stk = [s]
    used = [0]*N
    R = [None]*N
    it = [0]*N
    while stk:
        v = stk[-1]
        p = stk[-2] if len(stk) > 1 else -1
        if it[v] == 0:
            used[v] = 1
            ... # A
        else:
            w = G[v][it[v]-1]
            r = R[w]
            ... # C

        while it[v] < len(G[v]):
            w = G[v][it[v]]; it[v] += 1
            ... # B1
            if used[w]:
                continue
            ... # B2
            stk.append(w)
            break
        else:
            ... # D
            R[w] = ... # E
            stk.pop()
    r0 = R[s]