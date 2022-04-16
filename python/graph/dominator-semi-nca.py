def dfs_preorder(N, G, s):
    order = [-1]*N
    order[s] = 0
    vs = [0]*N
    vs[0] = s
    prt = [-1]*N
    stk = [s]
    it = [0]*N

    cur = 0
    while stk:
        v = stk[-1]
        while it[v] < len(G[v]):
            w = G[v][it[v]]; it[v] += 1
            if order[w] == -1:
                prt[w] = v
                stk.append(w)

                order[w] = cur = cur+1
                vs[cur] = w
                break
        else:
            stk.pop()
    return vs, order, prt

def dominator(N, G, s):
    vs, order, prt = dfs_preorder(N, G, s)
    semi = order[:]
    doms = [s]*N

    RG = [[] for i in range(N)]
    for v in range(N):
        for w in G[v]:
            RG[w].append(v)

    *anc, = range(N)
    label = order[:]
    def s_link(v, w):
        anc[w] = v
    def s_eval(v):
        if v == anc[v]:
            return label[v]
        compress(v, anc[v])
        return label[v]
    def compress(v, w):
        if w == anc[w]:
            return w
        anc[v] = u = compress(w, anc[w])
        if label[w] < label[v]:
            label[v] = label[w]
        return u

    for w in reversed(vs[1:]):
        for v in RG[w]:
            s_min = s_eval(v)
            if s_min < semi[w]:
                semi[w] = s_min
        label[w] = semi[w]
        s_link(prt[w], w)
    doms[s] = s
    for w in vs[1:]:
        x = prt[w]
        while semi[w] < order[x]:
            x = doms[x]
        doms[w] = x
    return doms