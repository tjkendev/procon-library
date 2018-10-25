from collections import deque
from heapq import heappush, heappop

INF = 10**30
def Johnson(G, N):
    h = [0]*N

    update = 1
    for i in range(N):
        update = 0
        for v in range(N):
            d = h[v]
            for w, c in G[v]:
                if c + d < h[w]:
                    h[w] = d + c
                    update = 1
        if not update:
            break
    else:
        return None

    for v in range(N):
        d = h[v]
        g = G[v]
        for j, (w, c) in enumerate(g):
            g[j] = (w, c + d - h[w])

    D = []
    for i in range(N):
        dst = [INF]*N
        dst[i] = 0
        que = [(0, i)]
        while que:
            cost, v = heappop(que)
            if dst[v] < cost:
                continue
            for w, c in G[v]:
                if cost + c < dst[w]:
                    dst[w] = r = cost + c
                    heappush(que, (r, w))
        v = h[i]
        for j in range(N):
            if dst[j] == INF:
                dst[j] = INF
            else:
                dst[j] -= v - h[j]
        D.append(dst)

    return D