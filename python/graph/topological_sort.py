# V: 頂点数
# G[v] = [w, ...]:
#    有向グラフ上の頂点vから到達できる頂点w
# deg[v]:
#    頂点vに到達できる頂点の数
V = ...
G = [[...] for i in range(V)]
deg = [...]

from collections import deque
ans = list(v for v in range(V) if deg[v] == 0)
deq = deque(ans)
used = [0] * V

while deq:
    v = deq.popleft()
    for t in g[v]:
        deg[t] -= 1
        if deg[t] == 0:
            deq.append(t)
            ans.append(t)

# ans: トポロジカル順序に並べた頂点