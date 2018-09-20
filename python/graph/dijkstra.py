# V: 頂点数
# g[v] = {(w, cost)}:
#     頂点vから遷移可能な頂点(w)とそのコスト(cost)
# r: 始点の頂点
 
from heapq import heappush, heappop
INF = 10**10
dist = [INF]*V
que = [(0,r)]
dist[r] = 0
while que:
    c, v = heappop(que)
    if dist[v] < c:
        continue
    for t, cost in g[v]:
        if dist[v] + cost < dist[t]:
            dist[t] = dist[v] + cost
            heappush(que, (dist[t], t))