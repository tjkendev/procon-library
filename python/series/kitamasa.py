# (0-indexed)
# a[i] = a_i, c[i] = c_i
# a_{i+k} = c_i*a_i + c_{i+1}*a_{i+1} + ... + c_{i+k-1}*a_{i+k-1}
def solve1(m, k, C, A):
    MOD = 10**9 + 7
    C0 = [0]*k; C1 = [0]*k
    if m == 0:
        return A[0]
    C0[1] = 1

    def inc(k, C0, C1):
        C1[0] = C0[k-1] * C[0] % MOD
        for i in range(k-1):
            C1[i+1] = (C0[i] + C0[k-1]*C[i+1]) % MOD

    def dbl(k, C0, C1):
        D0 = [0]*k; D1 = [0]*k
        D0[:] = C0[:]
        for j in range(k):
            C1[j] = C0[0] * C0[j] % MOD
        for i in range(1, k):
            inc(k, D0, D1)

            for j in range(k):
                C1[j] += C0[i] * D1[j] % MOD
            D0, D1 = D1, D0
        for i in range(k):
            C1[i] %= MOD

    p = 32
    while (m >> p) & 1 == 0:
        p -= 1

    while p:
        p -= 1
        dbl(k, C0, C1)
        C0, C1 = C1, C0

        if (m >> p) & 1:
            inc(k, C0, C1)
            C0, C1 = C1, C0

    return sum(C0[i] * A[i] for i in range(k)) % MOD

# solve1の関数を展開したバージョン
def solve2(m, k, C, A):
    MOD = 10**9 + 7

    C0 = [0]*k; C1 = [0]*k
    if m == 0:
        return A[0]
    C0[1] = 1

    p = 32
    while (m >> p) & 1 == 0:
        p -= 1

    D0 = [0]*k; D1 = [0]*k
    while p:
        p -= 1

        #dbl(k, C0, C1)
        D0[:] = C0[:]
        for j in range(k):
            C1[j] = C0[0] * C0[j] % MOD
        for i in range(1, k):
            #inc(k, D0, D1)
            D1[0] = D0[k-1] * C[0] % MOD
            for j in range(k-1):
                D1[j+1] = (D0[j] + D0[k-1]*C[j+1]) % MOD

            for j in range(k):
                C1[j] += C0[i] * D1[j] % MOD
            D0, D1 = D1, D0
        for i in range(k):
            C1[i] %= MOD
        C0, C1 = C1, C0

        if (m >> p) & 1:
            #inc(k, C0, C1)
            C1[0] = C0[k-1] * C[0] % MOD
            for i in range(k-1):
                C1[i+1] = (C0[i] + C0[k-1]*C[i+1]) % MOD
            C0, C1 = C1, C0

    return sum(C0[i] * A[i] for i in range(k)) % MOD