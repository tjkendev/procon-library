# i番目の重みws[i], 価値vs[i]
def solve(N, W, ws, vs):
    # V = 全ての品物の価値の総和
    V = sum(vs)
    
    # 初期値は価値0以外の重さを上限より大きく
    dp = [W+1] * (V + 1)
    dp[0] = 0
    for i in range(N):
        # 価値v, 重さw
        v = vs[i]; w = ws[i]
        for j in range(V, v-1, -1):
            dp[j] = min(dp[j-v] + w, dp[j])

    # 重さが上限以下の価値のうち、最大の価値が解
    return max(i for i in range(V+1) if dp[i] <= W)