# i番目の重みws[i], 価値vs[i]
def solve(N, W, ws, vs):
    # S[i] = (v, w): 価値v, 重さw
    *S, = zip(vs, ws)

    def make(S):
        T = {0: 0}
        for v, w in S:
            # 価値v, 重さw
            T0 = dict(T)
            for k, val in T.items():
                if k+w > W:
                    continue
                if k+w in T0:
                    T0[k+w] = max(T0[k+w], val + v)
                else:
                    T0[k+w] = val + v
            T = T0
        v = 0
        R = []
        for k in sorted(T):
            v = max(v, T[k])
            # (重さk, 重さk以下での価値の最大v)
            R.append((k, v))
        return R

    def solve(T0, T1):
        T0.sort()
        T1.sort(reverse=1)

        it = iter(T1); k1, v1 = next(it)
        yield 0
        for k0, v0 in T0:
            # 重さの和がW以下になるようにスライドする
            while k0 + k1 > W:
                k1, v1 = next(it)
            yield v0 + v1

    # ２つの集合に分けて、それぞれ全列挙
    T0 = make(S[:N//2])
    T1 = make(S[N//2:])

    # 2つの全列挙を元に解を求める
    return max(solve(T0, T1))
