# N: グラフの頂点数
# r: 始点
# G[v] = [(w, cost), ...]: 頂点vからコストcostで到達できる頂点w
INF = 10**18
def bellman_ford(N, G, r):
    dist = [INF] * N
    dist[r] = 0
    update = 1
    for _ in range(N):
        update = 0
        for v, e in enumerate(G):
            for t, cost in e:
                if dist[v] != INF and dist[v] + cost < dist[t]:
                    dist[t] = dist[v] + cost
                    update = 1
        if not update:
            break
    else:
        # 負閉路検出処理
        ...
