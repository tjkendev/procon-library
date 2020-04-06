mod = 10**9 + 9; p = 13; q = 19

p_table = q_table = None
def prepare(L):
    global p_table, q_table
    p_table = [1]*(L+1); q_table = [1]*(L+1)
    for i in range(L):
        p_table[i+1] = p_table[i] * p % mod
        q_table[i+1] = q_table[i] * q % mod

def rolling_hash(S, W, H):
    D = [[0]*(W+1) for i in range(H+1)]
    for i in range(H):
        su = 0
        dp = D[i]
        di = D[i+1]
        si = S[i]
        for j in range(W):
            v = si[j] # v = ord(si[j]) if si[j] is str
            su = (su*p + v) % mod
            di[j+1] = (su + dp[j+1]*q) % mod
    return D
def get(S, x0, y0, x1, y1):
    P = p_table[x1 - x0]; Q = q_table[y1 - y0]
    return (S[y1][x1] - S[y1][x0] * P - S[y0][x1] * Q + S[y0][x0] * (P * Q) % mod) % mod

# example
data1 = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1],
]
data2 = [
    [1, 0, 1],
    [1, 0, 1],
]
prepare(L = 5)
rh1 = rolling_hash(data1, 5, 3)
rh2 = rolling_hash(data2, 3, 2)
print(get(rh1, 2, 0, 5, 2) == get(rh2, 0, 0, 3, 2))
# => "True"