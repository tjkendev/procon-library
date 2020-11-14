def global_minimum_cut(N, E, u0):
    res = 10**18

    # groups = [{i} for i in range(N)]

    merged = [0]*N
    for s in range(N-1):
        # minimum cut phase
        used = [0]*N
        used[u0] = 1
        costs = [0]*N
        for v in range(N):
            if E[u0][v] != -1:
                costs[v] = E[u0][v]
        order = []
        for _ in range(N-1-s):
            v = mc = -1
            for i in range(N):
                if used[i] or merged[i]:
                    continue
                if mc < costs[i]:
                    mc = costs[i]
                    v = i
            # assert v != -1

            # v: the most tightly connected vertex
            for w in range(N):
                if used[w] or E[v][w] == -1:
                    continue
                costs[w] += E[v][w]
            used[v] = 1
            order.append(v)

        v = order[-1]
        ws = 0
        for w in range(N):
            if E[v][w] != -1:
                ws += E[v][w]
        # - the current min-cut is (groups[v], V - groups[v])
        # - the weight of the cut is ws
        res = min(res, ws)

        if len(order) > 1:
            u = order[-2]
            # groups[u].update(groups[v])
            # groups[v] = None

            # merge u and v
            merged[v] = 1
            for w in range(N):
                if w != u:
                    if E[v][w] == -1:
                        continue
                    if E[u][w] != -1:
                        E[u][w] = E[w][u] = E[u][w] + E[v][w]
                    else:
                        E[u][w] = E[w][u] = E[v][w]
                E[v][w] = E[w][v] = -1
    return res

N = 8
es = [
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (0, 4, 3),
    (1, 4, 2),
    (1, 5, 2),
    (2, 6, 2),
    (3, 6, 2),
    (3, 7, 2),
    (4, 5, 3),
    (5, 6, 1),
    (6, 7, 3),
]
E = [[-1]*N for i in range(N)]
for a, b, w in es:
    E[a][b] = E[b][a] = w
print(global_minimum_cut(N, [es[:] for es in E], 1))
# => "4"
