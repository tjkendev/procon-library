from collections import deque

# i番目の重みws[i], 価値vs[i], 個数ms[i]
def solve(N, W, ws, vs, ms):
    V0 = max(vs)
    V = sum(v * min(V0, m) for v, m in zip(vs, ms))

    # 各品物 min(max_j{v_j}, m_i) 個までの個数制限付きナップザック問題を解く
    dp = [W+1]*(V + 1)
    dp[0] = 0
    for i in range(N):
        v = vs[i]; w = ws[i]; m = ms[i]
        c = min(V0, m)
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

    # 重さ単位における価値が大きい方から品物を並べる
    *I, = range(N)
    I.sort(key=lambda x: ws[x]/vs[x])
    *S, = [(vs[i], ws[i], ms[i]) for i in I]

    # 各価値ごとに、(W - wに貪欲に詰めた時の価値) + 価値v を求める
    def greedy():
        yield 0
        for i in range(V + 1):
            if dp[i] > W:
                continue
            rest = W - dp[i]
            r = i
            for v, w, m in S:
                m = min(m, rest // w)
                r += m * v
                rest -= m * w
            yield r
    return max(greedy())