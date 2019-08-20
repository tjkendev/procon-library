# N: 頂点数
# E = [(c, a, b), ...]: 頂点aと頂点bを重みcの辺が繋ぐ
def binarization_mst(N, E):
    L = 2*N-1
    # G: 変換後の二分木
    G = [[] for i in range(L)]
    # W: 変換後の各頂点の重み
    W = [0]*L

    *p, = range(N)
    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(x)
        return y

    E.sort()

    cur = N
    *lb, = range(N)
    for c, a, b in E:
        pa = root(a); pb = root(b)
        if pa == pb:
            continue
        W[cur] = c
        G[cur] = [lb[a], lb[b]]
        if pa < pb:
            p[pb] = pa
            lb[pa] = cur
        else:
            p[pa] = pb
            lb[pb] = cur
        cur += 1
    # assert cur == L
    return G, W