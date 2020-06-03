def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def cross_point(p0, p1, q0, q1):
    x0, y0 = p0; x1, y1 = p1
    x2, y2 = q0; x3, y3 = q1
    dx0 = x1 - x0; dy0 = y1 - y0
    dx1 = x3 - x2; dy1 = y3 - y2
    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if -EPS < sm < EPS:
        return None
    return x0 + s*dx0/sm, y0 + s*dy0/sm
EPS = 1e-9
def convex_cut(P, line):
    q0, q1 = line
    N = len(P)
    Q = []
    for i in range(N):
        p0 = P[i-1]; p1 = P[i]
        cv0 = cross3(q0, q1, p0)
        cv1 = cross3(q0, q1, p1)
        if cv0 * cv1 < EPS:
            v = cross_point(q0, q1, p0, p1)
            if v is not None:
                Q.append(v)
        if cv1 > -EPS:
            Q.append(p1)
    return Q

P = [(0, 0), (10, 1), (1, 10)]
line = ((5, -3), (7, 8))
for x, y in convex_cut(P, line):
    print("%.4f %.4f" % (x, y))
# =>
# 0.0000 0.0000
# 5.6481 0.5648
# 6.3846 4.6154
# 1.0000 10.0000