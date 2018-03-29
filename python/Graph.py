# -*- encoding: utf-8 -*-
# Bridge-Finding with Chain Decompositions
# 橋、二重辺連結成分分解
# g: 隣接リスト, v: 頂点数, s: 探索開始地点
#
# DFS木を求めながら橋を見つけ、グラフを縮約していく
def bridge_finding(G, N, start=0):
    fin = [False] * N
    v_cnts = [0] * N
    used = [False] * N
    bG = [[] for i in range(N)] # 縮約後のグラフ
    bV = [[] for i in range(N)] # 各ノードに縮約される元頂点
    def dfs(v, prev, edges, conts):
        cur_c = prev_c = 0
        used[v] = True
        conts.append(v)
        for w in G[v]:
            if used[w]:
                if w==prev:
                    # (v, prev)の多重辺対応
                    if prev_c == 1:
                        v_cnts[prev] -= 1
                        cur_c += 1
                    prev_c += 1
                elif not fin[w]:
                    v_cnts[w] -= 1
                    cur_c += 1
            else:
                w_edges = []; w_conts = []
                ret = dfs(w, v, w_edges, w_conts)
                if ret > 0:
                    edges += w_edges
                    conts += w_conts
                else:
                    # (v, w)は橋
                    bG[w] = w_edges
                    for u in w_edges:
                        bG[u].append(w)
                    bV[w] = w_conts
                    edges.append(w)
                cur_c += ret
        fin[v] = True
        cur_c += v_cnts[v]
        return cur_c
    dfs(start, -1, bG[start], bV[start])
    for u in bG[start]:
        bG[u].append(start)
    return bG#, bV

# 単純に橋となる辺を返す
def bridge(G, N):
    result = set()
    label = [None]*N
    gen = 0
    cost = [0]*N
    def dfs(u, p):
        nonlocal gen
        res = 0
        for v in G[u]:
            if v == p:
                continue
            if label[v] is not None:
                if label[v] < label[u]:
                    cost[v] += 1
                    res += 1
            else:
                label[v] = gen; gen += 1
                r = dfs(v, u)
                if r == 0:
                    result.add((u, v) if u < v else (v, u))
                res += r
        res -= cost[u]
        return res
    for v in range(N):
        if not label[v]:
            label[v] = gen; gen += 1
            r = dfs(v, -1)
            assert r == 0, r
    return result

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

# Chu-Liu/Edmonds' Algorithm
# 最小全域有向木を再帰的に求める
# V: 頂点数, es: 辺集合, r: 根となる頂点番号
# 辺１つ(s->tのコストw)は(s, t, w)のlistを持つ
# 頂点は0..V-1
# 解説付きコード
# -> https://gist.github.com/tjkendev/231897301fde67d4a81f51c3f0873936
def solve(V, es, r):
    mins = [(10**18, -1)]*V
    for s, t, w in es:
        mins[t] = min(mins[t], (w, s))
    mins[r] = (-1, -1)

    group = [0]*V
    comp = [0]*V
    cnt = 0

    used = [0]*V
    for v in range(V):
        if not used[v]:
            chain = []
            cur = v
            while cur!=-1 and not used[cur]:
                chain.append(cur)
                used[cur] = 1
                cur = mins[cur][1]
            if cur!=-1:
                cycle = 0
                for e in chain:
                    group[e] = cnt
                    if e==cur:
                        cycle = 1
                        comp[cnt] = 1
                    if not cycle:
                        cnt += 1
                if cycle:
                    cnt += 1
            else:
                for e in chain:
                    group[e] = cnt
                    cnt += 1

    if cnt == V:
        return sum(map(lambda x:x[0], mins)) + 1

    res = sum(mins[v][0] for v in range(V) if v!=r and comp[group[v]])

    n_es = []
    for s, t, w in es:
        gs = group[s]; gt = group[t]
        if gs == gt:
            continue
        if comp[gt]:
            n_es.append((gs, gt, w - mins[t][0]))
        else:
            n_es.append((gs, gt, w))
    return res + solve(cnt, n_es, group[r])

# 強連結成分分解(SCC)
# グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

