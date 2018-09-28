# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
for k in range(V):
    for i in range(V):
        for j in range(V):
            if cost[i][k]!=INF and cost[k][j]!=INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])