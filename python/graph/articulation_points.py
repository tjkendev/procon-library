# -*- encoding: utf-8 -*-

# 関節点(Articulation Points)
def get_articulation_points(G, N, start=0):
    v_min = [0]*N; order = [None]*N
    result = []; count = 0
    def dfs(v, prev):
        nonlocal count
        r_min = order[v] = count # 到達時にラベル
        fcnt = 0; p_art = 0
        count += 1
        for w in G[v]:
            if w == prev:
                continue
            if order[w] is None:
                ret = dfs(w, v)
                # 子の頂点が到達できたのが、自身のラベル以上の頂点のみ
                # => 頂点vは関節点
                p_art |= (order[v] <= ret)
                r_min = min(r_min, ret)
                fcnt += 1
            else:
                r_min = min(r_min, order[w])
        p_art |= (r_min == order[v] and len(G[v]) > 1)
        if (prev == -1 and fcnt > 1) or (prev != -1 and p_art):
            # 頂点startの場合は、二箇所以上の子頂点を調べたら自身は関節点
            result.append(v)
        return r_min
    dfs(start, -1)
    return result
