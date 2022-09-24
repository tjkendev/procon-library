def dsu_on_tree(N, G, Prop):
    order = []
    prt = [-1]*N

    que = [0]
    pn = [-1]*N
    used = [0]*N
    used[0] = 1
    while que:
        v = que.pop()
        for w in G[v]:
            if used[w]:
                continue
            used[w] = 1
            que.append(w)
            prt[w] = v
        pn[v] = len(order)
        order.append(v)

    sz = [0]*N
    tmp_ps = [[i] for i in range(N)]
    # heavy paths
    h_ps = []
    for v in reversed(order):
        p = prt[v]
        m_sz = 0
        h = -1
        s = 1
        for w in G[v]:
            if p == w:
                continue
            if m_sz < sz[w]:
                m_sz = sz[w]
                h = w
            s += sz[w]
        if h != -1:
            tmp_ps[v] = tmp_ps[h]
            tmp_ps[v].append(v)
            for w in G[v]:
                if w == p or w == h:
                    continue
                h_ps.append(tmp_ps[w])
        sz[v] = s
    h_ps.append(tmp_ps[0])

    ans = [-1]*N
    ph = Prop()
    for path in h_ps:
        h = -1
        for v in path:
            p = prt[v]

            for w in G[v]:
                if w == p or w == h:
                    continue
                for c in order[pn[w]:pn[w] + sz[w]]:
                    ph.add(c)
            ph.add(v)
            ans[v] = ph.get(v)
            h = v

        # 削除操作で初期化する
        for c in order[pn[v]:pn[v] + sz[v]]:
            ph.remove(c)
        # 一括で初期化する場合 (更新した箇所のみ更新する)
        # ph.reset()
    return ans
