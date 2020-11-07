MOD = 10**9 + 7
N = 10**5

fact = [1]*(N+1)
rfact = [1]*(N+1)
r = 1
for i in range(1, N+1):
    fact[i] = r = r * i % MOD
rfact[N] = r = pow(fact[N], MOD-2, MOD)
for i in range(N, 0, -1):
    rfact[i-1] = r = r * i % MOD

# nPk (mod MOD) を求める
def perm(n, k):
    return fact[n] * rfact[n-k] % MOD

# nCk (mod MOD) を求める
def comb(n, k):
    return fact[n] * rfact[k] * rfact[n-k] % MOD