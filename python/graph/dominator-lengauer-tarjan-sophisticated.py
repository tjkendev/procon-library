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
    vs, semi, prt = dfs_preorder(N, G, s)
    doms = [-1]*N

    RG = [[] for i in range(N)]
    for v in range(N):
        for w in G[v]:
            RG[w].append(v)
    bucket = [[] for i in range(N)]

    *anc, = range(N)
    *label, = range(N)
    size = [1]*N; child = [-1]*N

    def s_link(v, w):
        s = w
        while child[s] != -1 and semi[label[w]] < semi[label[child[s]]]:
            ccsz = (size[child[child[s]]] if child[child[s]] != -1 else 0)
            if size[s] + ccsz >= 2*size[child[s]]:
                anc[child[s]] = s
                child[s] = child[child[s]]
            else:
                size[child[s]] = size[s]
                anc[s] = s = child[s]
        label[s] = label[w]
        size[v] += size[w]
        if size[v] < 2*size[w]:
            s, child[v] = child[v], s
        while s != -1:
            anc[s] = v
            s = child[s]
    def s_eval(v):
        if anc[v] == v:
            return label[v]
        compress(v, anc[v])
        if semi[label[anc[v]]] >= semi[label[v]]:
            return label[v]
        return label[anc[v]]
    def compress(v, w):
        if w == anc[w]:
            return w
        anc[v] = u = compress(w, anc[w])
        if semi[label[w]] < semi[label[v]]:
            label[v] = label[w]
        return u

    for w in reversed(vs[1:]):
        for v in bucket[w]:
            u = s_eval(v)
            if semi[u] < semi[v]:
                doms[v] = u
            else:
                doms[v] = w
        for v in RG[w]:
            su = semi[s_eval(v)]
            if su < semi[w]:
                semi[w] = su
        if vs[semi[w]] != prt[w]:
            bucket[vs[semi[w]]].append(w)
        else:
            doms[w] = prt[w]
        s_link(prt[w], w)
    for v in bucket[s]:
        doms[v] = s
    for w in vs[1:]:
        if doms[w] != vs[semi[w]]:
            doms[w] = doms[doms[w]]
    doms[s] = s
    return doms