INF = 10**9
def minimum_steiner_tree(N, G, L, V):
    E = [[INF]*N for i in range(N)]
    for v in range(N):
        for w, d in G[v]:
            E[v][w] = d
        E[v][v] = 0

    for k in range(N):
        Ek = E[k]
        for Ei in E:
            v = Ei[k]
            Ei[:] = (min(a, v + b) for a, b in zip(Ei, Ek))

    S = [[INF]*(1 << L) for i in range(N)]
    for i in range(L):
        state = (1 << i)
        for v in range(N):
            S[v][state] = E[v][V[i]]
        S[V[i]][state] = 0
    for i in range(N):
        S[i][0] = 0

    def gen(state):
        s0 = (state - 1) & state
        while s0 != state:
            if s0 < state:
                yield s0
            s0 = (s0 - 1) & state

    us = [INF]*N
    infs = [INF]*N
    for state in range(1, 1 << L):
        ss = list(gen(state))
        us[:] = infs
        for v in range(N):
            Sv = S[v]
            u = min(Sv[s0] + Sv[s0 ^ state] for s0 in ss)
            us[:] = (min(a, b + u) for a, b in zip(us, E[v]))
        for w in range(N):
            S[w][state] = us[w]

    ALL = (1 << L) - 1
    return min(S[v][ALL] for v in range(N))


N = 5
G = [
    [(1, 1), (2, 2), (3, 7)],
    [(0, 1), (3, 4)],
    [(0, 2), (3, 2)],
    [(0, 7), (1, 4), (2, 2), (4, 1)],
    [(3, 1)],
]
L = 2
V = [0, 3]

print(minimum_steiner_tree(N, G, L, V))
# => "4"