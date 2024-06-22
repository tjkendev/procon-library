from collections import deque
# s: 開始頂点
# N: 頂点数
# G: グラフ
# G[v][i] = (w, d): 辺v-wのコストは d (0 or 1)
def bfs01(N, G, s):
    dist = [10**9] * N
    S = deque([s])
    T = deque()
    dist[s] = 0

    d = 0
    while S:
        while S:
            v = S.popleft()
            for w, c in G[v]:
                if d+c < dist[w]:
                    dist[w] = d+c
                    if c:
                        T.append(w)
                    else:
                        S.append(w)
        S, T = T, S
        d += 1
