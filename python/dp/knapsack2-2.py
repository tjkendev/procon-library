def solve(N, W, ws, vs, ms):
    vs0 = []; ws0 = []
    for i in range(N):
        v = vs[i]; w = ws[i]; m = ms[i]
        b = 1
        while b <= m:
            vs0.append(v * b)
            ws0.append(w * b)
            m -= b
            b <<= 1
        if m:
            vs0.append(v * m)
            ws0.append(w * m)

    dp = [0] * (W+1)
    N0 = len(vs0)
    for i in range(N0):
        v = vs0[i]; w = ws0[i]
        for j in range(W, w-1, -1):
            dp[j] = max(dp[j-w] + v, dp[j])
    return max(dp)
