# Union-Find data structure

N = 10**5

*p, = range(N)
def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y
def unite(x, y):
    px = root(x); py = root(y)
    if px == py:
        return 0
    if px < py:
        p[py] = px
    else:
        p[px] = py
    return 1