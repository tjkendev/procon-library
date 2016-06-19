# -*- encoding: utf-8 -*-
# Bridge-Finding with Chain Decompositions
# 橋、二重辺連結成分分解
# g: 隣接リスト, v: 頂点数, s: 探索開始地点
#
# DFS木を求めながら橋を見つけ、グラフを縮約していく
def bridge(g, v, s=0):
    bl = [False] * v
    c_memo = [0] * v
    c_used = [False] * v
    b_g = [[] for i in xrange(v)]
    # args: v, prev-v, vs in a component
    def dfs(v, f, l):
        bcnt = fcnt = 0
        c_used[v] = True
        for t in g[v]:
            if not c_used[t]:
                ll = []
                ret = dfs(t, v, ll)
                if ret>0:
                    l += ll
                else:
                    # (v,t) : bridge
                    b_g[t] = ll
                    for u in ll:
                        b_g[u].append(t)
                    l.append(t)
                bcnt += ret
            else:
                if t==f:
                    # for multiedge
                    if fcnt==1:
                        c_memo[f] -= 1
                        bcnt += 1
                    fcnt += 1
                elif not bl[t]:
                    c_memo[t] -= 1
                    bcnt += 1
        bl[v] = True
        bcnt += c_memo[v]
        return bcnt
    dfs(s, -1, b_g[s])
    for u in b_g[s]:
        b_g[u].append(s)
    return b_g

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
    for v in xrange(V):
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

    res = sum(mins[v][0] for v in xrange(V) if v!=r and comp[group[v]])

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
