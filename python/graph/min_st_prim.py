# N: 頂点数
# G[v] = [w, ...]
#     グラフG上で頂点vが隣接する辺集合
N = ...
G = [[...] for i in range(N)]

from heapq import heappush, heappop, heapify
used = [0]*N
que = [(c, w) for w, c in G[0]]
used[0] = 1
heapify(que)
 
ans = 0
while que:
    cv, v = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for w, c in G[v]:
        if used[w]:
            continue
        heappush(que, (c, w))

# ansが最小全域木の解