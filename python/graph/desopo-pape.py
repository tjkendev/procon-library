# used[v]: 頂点vの状態
#  0: まだ未計算
#  1: 計算中
#  2: 計算完了 (再計算される可能性あり)

from collections import deque

INF = 10**18
def pape(G, N, s):
    dist = [INF]*N

    used = [0]*N
    used[s] = 1
    dist[s] = 0
    que = deque([s])
    while que:
        v = que.popleft()
        c = dist[v]
        for w, d in G[v]:
            if dist[w] <= c + d:
                continue
            dist[w] = c + d
            if used[w] == 0:
                que.append(w)
                used[w] = 1
            elif used[w] == 2:
                que.appendleft(w)
                used[w] = 1
        used[v] = 2
    return dist
