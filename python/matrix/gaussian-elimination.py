EPS = 1e-9
def gaussian_elimination(N, A, bs):
    M = [[0]*(N+1) for i in range(N)]
    for i in range(N):
        M[i][:N] = A[i]
        M[i][N] = bs[i]
    cur = 0
    for i in range(N):
        k = cur; ma = abs(M[cur][i])
        for j in range(cur+1, N):
            if ma < abs(M[j][i]):
                k = j
                ma = abs(M[j][i])
        if ma < EPS:
            continue
        if k != cur:
            M[cur], M[k] = M[k], M[cur]
        Mc = M[cur]
        for Mj in M[cur+1:]:
            if abs(Mj[i]) > EPS:
                e = Mj[i] / Mc[i]
                Mj[i] = 0
                for k in range(i+1, N+1):
                    Mj[k] -= e*Mc[k]
        cur += 1
    if cur == N:
        xs = [Mi[N] for Mi in M]
        for i in range(N-1, -1, -1):
            Mi = M[i]
            xs[i] -= sum(Mi[j] * xs[j] for j in range(i+1, N))
            xs[i] /= Mi[i]
        return 1, xs
    if any(Mi[N] > EPS for Mi in M[cur:]):
        return 0, None
    return 2, None
