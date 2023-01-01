from collections import deque

# i番目の重みws[i], 価値vs[i], 個数ms[i]
def solve(N, W, vs, ws, ms):
    V = sum(v * m for v, m in zip(vs, ms))

    # Sliding Window Minimum を用いたdpを行う
    dp = [W+1]*(V + 1)
    dp[0] = 0
    for i in range(N):
        # 価値v, 重さw, 個数m
        v = vs[i]; w = ws[i]; m = ms[i]
        c = m
        ms[i] -= c
        for k in range(v):
            que = deque()
            push = que.append
            popf = que.popleft; popb = que.pop

            for j in range((V-k)//v+1):
                a = dp[k + j*v] - j * w
                while que and a <= que[-1][1]:
                    popb()
                push((j, a))

                p, b = que[0]

                dp[k + j*v] = b + j * w
                if que and p <= j-c:
                    popf()
    return max(i for i in range(V+1) if dp[i] <= W)
