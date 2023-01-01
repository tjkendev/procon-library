from collections import deque

# i番目の重みws[i], 価値vs[i], 個数ms[i]
def solve(N, W, ws, vs, ms):
    S = [0]*(W+1)
    for i in range(N):
        # 価値v, 重さw, 個数m
        v = vs[i]; w = ws[i]; m = ms[i]
        for k in range(w):
            # 0 ≤ k ≤ w-1
            que = deque()
            for j in range((W - k) // w + 1):
                # 各 p = k + j*w について計算
                # 重さpの価値を重さkを基準にして管理するため、(価値v) × j を引く
                # (重さpの価値は重さkのものにi番目の品物をj個入れたものとみなす)
                v0 = S[k + j*w] - j*v
                while que and que[-1][1] <= v0:
                    que.pop()
                que.append((j, v0))

                # 重さp の価値の最大 = (区間内について、重さkを基準にした価値の最大) + (価値v) × j
                S[k + j*w] = que[0][1] + j*v

                # m個前の要素を取り除く
                if que and que[0][0] <= j-m:
                    que.popleft()
    return max(S)
