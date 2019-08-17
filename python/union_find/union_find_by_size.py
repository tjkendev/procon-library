N = 10**5

*p, = range(N)
size = [1]*N
def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y
def unite(x, y):
    px = root(x); py = root(y)
    if px == py:
        return 0
    sx = size[px]; sy = size[py]
    if sy < sx:
        p[py] = px
        size[px] += sy
    else:
        p[px] = py
        size[py] += sx
    return 1