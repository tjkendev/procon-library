INF = 10**9
def calc(N, E, s):
    G = [[] for i in range(N)]
    for a, b, d in E:
        # x_a - x_b <= d
        G[b].append((a, d))

    INF2 = INF**2
    dist = [INF2] * N
    dist[s] = 0
    update = 1
    for _ in range(N):
        update = 0
        for v in range(N):
            for w, d in G[v]:
                if dist[v] + d < dist[w]:
                    dist[w] = dist[v] + d
                    update = 1
        if not update:
            break
    else:
        return None
    for i in range(N):
        dist[i] = min(dist[i], INF)
    # dist[i]: the maximum value of (x_i - x_s)
    return dist

N = 3
# x_1 - x_0 <= 3
# x_2 - x_1 <= 5
# x_2 - x_0 <= 10
E = [(1, 0, 3), (2, 1, 5), (2, 0, 10)]
print(calc(N, E, 0))
# => "[0, 3, 8]"