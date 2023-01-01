# N: 木Tの頂点数
# G[u] = [(w, c), ...]:
#   頂点uに隣接する頂点wとそれを繋ぐ辺の長さc
N = ...
G = [[...] for i in range(N)]

from collections import deque
def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in G[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    d = max(dist)
    return dist.index(d), d
u, _ = bfs(0)
v, d = bfs(u)

# パスu-vがこの木Tの直径(長さd)