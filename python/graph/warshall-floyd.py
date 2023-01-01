# N: 頂点数
# cost[i][j]: 頂点 v_i から頂点 v_j へ到達するための辺コストの和
N = ...
cost = [[...] for i in range(N)]

INF = 10**18
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
