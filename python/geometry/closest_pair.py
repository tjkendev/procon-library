# 最近点対を分割統治法で求める
from math import sqrt
INF = 10**9

# cp_rec - 再帰用関数
# 入力: 配列と区間
# 出力: 距離と区間内の要素をY座標でソートした配列
def cp_rec(ps, i, n):
    if n <= 1:
        return INF, [ps[i]]
    m = n/2
    x = ps[i+m][0] # 半分に分割した境界のX座標
    # 配列を半分に分割して計算
    d1, qs1 = cp_rec(ps, i, m)
    d2, qs2 = cp_rec(ps, i+m, n-m)
    d = min(d1, d2)
    # Y座標が小さい順にmergeする
    qs = [None]*n
    s = t = idx = 0
    while s < m and t < n-m:
        if qs1[s][1] < qs2[t][1]:
            qs[idx] = qs1[s]; s += 1
        else:
            qs[idx] = qs2[t]; t += 1
        idx += 1
    while s < m:
        qs[idx] = qs1[s]; s += 1
        idx += 1
    while t < n-m:
        qs[idx] = qs2[t]; t += 1
        idx += 1
    # 境界のX座標x(=ps[i+m][0])から距離がd以下のものについて距離を計算していく
    # bは境界のX座標から距離d以下のものを集めたもの
    b = []
    for i in xrange(n):
        ax, ay = q = qs[i]
        if abs(ax - x) >= d:
            continue
        # Y座標について、qs[i]から距離がd以下のj(<i)について計算していく
        for j in xrange(len(b)-1, -1, -1):
            dx = ax - b[j][0]
            dy = ay - b[j][1]
            if dy >= d: break
            d = min(d, sqrt(dx**2 + dy**2))
        b.append(q)
    return d, qs
def closest_pair(ps):
    n = len(ps)
    return cp_rec(ps, 0, n)[0]