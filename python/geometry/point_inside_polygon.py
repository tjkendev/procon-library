from math import atan2, pi

# Ray casting algorithm
def inside_polygon(p0, qs):
    cnt = 0
    L = len(qs)
    x, y = p0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            # a point is on a segment
            return True

        if not y0 < y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        if y0 <= 0 < y1 and x0*(y1 - y0) > y0*(x1 - x0):
            cnt += 1
    return (cnt % 2 == 1)

# Winding number algorithm
def inside_polygon1(p0, qs):
    x, y = p0
    L = len(qs)
    theta = 0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            # a point is on a segment
            return True

        theta += atan2(sv, cv)
    return abs(theta) > 1
