# Bridge-Finding
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
