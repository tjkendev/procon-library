from operator import xor
# calculate a vector x s.t. Ax = b
# - A is a N×N logical matrix
# - x and b are N-dimensional logical vectors
def gaussian_elimination(N, A, bs):
    M = [[0]*(N+1) for i in range(N)]
    for i in range(N):
        M[i][:N] = A[i]
        M[i][N] = bs[i]
    cur = 0
    for i in range(N):
        if M[cur][i] == 0:
            k = cur+1
            while k < N and M[k][i] == 0:
                k += 1
            if k == N:
                continue
            M[cur], M[k] = M[k], M[cur]
        Mc = M[cur]
        for Mj in (Mj for Mj in M[cur+1:] if Mj[i]):
            Mj[i:] = map(xor, Mj[i:], Mc[i:])
        cur += 1
    if cur == N:
        # an unique solution
        xs = [Mi[N] for Mi in M]
        for i in range(N-1, -1, -1):
            Mi = M[i]
            xs[i] ^= sum(Mi[j] & xs[j] for j in range(i+1, N)) & 1
        return 1, xs
    if any(Mi[N] for Mi in M[cur:]):
        # no solution
        return 0, None
    # infinitely many solutions
    return 2, None

N = 3
A = [[1, 0, 1], [0, 1, 1], [1, 0, 0]]
bs = [1, 0, 1]
print(gaussian_elimination(N, A, bs))
# => "(1, [1, 0, 0])"