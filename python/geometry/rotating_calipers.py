# キャリパー法(Rotating Calipers法)
# 凸多角形を回転しながら走査し、最遠点対を求める
from math import sqrt
def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def rotating_calipers(ps):
    qs = convex_hull(ps)
    n = len(qs)
    if n == 2:
        return dist(qs[0], qs[1])
    i = j = 0
    for k in range(n):
        if qs[k] < qs[i]: i = k
        if qs[j] < qs[k]: j = k
    res = 0
    si = i; sj = j
    while i != sj or j != si:
        res = max(res, dist(qs[i], qs[j]))
        if cross(qs[i], qs[i-n+1], qs[j], qs[j-n+1]) < 0:
            i = (i + 1) % n
        else:
            j = (j + 1) % n
    return res