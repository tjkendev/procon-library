L = 10**5
MOD = 10**9 + 7

fact = [1]*(L+1)
rfact = [1]*(L+1)
r = 1
for i in range(1, L+1):
    fact[i] = r = r * i % MOD
rfact[L] = r = pow(fact[L], MOD-2, MOD)
for i in range(L, 0, -1):
    rfact[i-1] = r = r * i % MOD

def comb(n, k):
    return fact[n] * rfact[n-k] * rfact[k] % MOD

def catalan1(n, k):
    return (fact[n+k] * (n-k+1) % MOD) * (rfact[k] * rfact[n+1] % MOD) % MOD

def catalan2(n, k):
    if k == 0:
        return 1
    return (comb(n+k, k) - comb(n+k, k-1)) % MOD

# O(N^2)
def precalc_catalan(N):
    C = [[1]*(i+1) for i in range(N+1)]
    for n in range(1, N+1):
        C1 = C[n]; C0 = C[n-1]
        C1[0] = 1
        C1[1] = n
        for k in range(2, n):
            C[n][k] = (C1[k-1] + C0[k]) % MOD
        C1[n] = C1[n-1]
    return C
