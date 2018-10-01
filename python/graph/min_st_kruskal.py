# E = [(cost, v, w), ...]
#   G上の全ての辺(v, w)とそのcostを含むlist

# Union-Findを使うことで頂点間の連結判定を行う
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
 
E.sort()
ans = 0
for c, v, w in E:
    if unite(v, w):
        ans += c

# ansが最小全域木の解