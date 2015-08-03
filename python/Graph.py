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

