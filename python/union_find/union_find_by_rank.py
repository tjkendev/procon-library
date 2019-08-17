N = 10**5

*p, = range(N)
rank = [1]*N
def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y
def unite(x, y):
    px = root(x); py = root(y)
    if px == py:
        return 0
    rx = rank[px]; ry = rank[py]
    if ry < rx:
        p[py] = px
    elif rx < ry:
        p[px] = py
    else:
        p[py] = px
        rank[px] += 1
    return 1
