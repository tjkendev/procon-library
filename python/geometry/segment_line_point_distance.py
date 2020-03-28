def cross2(p, q):
    return p[0]*q[1] - p[1]*q[0]
def dot2(p, q):
    return p[0]*q[0] + p[1]*q[1]
def dist2(p):
    return p[0]**2 + p[1]**2
def segment_line_dist(x, p0, p1):
    z0 = (p1[0] - p0[0], p1[1] - p0[1])
    z1 = (x[0] - p0[0], x[1] - p0[1])
    if 0 <= dot2(z0, z1) <= dist2(z0):
        return abs(cross2(z0, z1)) / dist2(z0)**.5
    z2 = (x[0] - p1[0], x[1] - p1[1])
    return min(dist2(z1), dist2(z2))**.5

# example
print(segment_line_dist((-1, -1), (0, 0), (1, 0)))
# => "1.4142135623730951"
print(segment_line_dist((0.5, 1), (0, 0), (1, 0)))
# => "1.0"
print(segment_line_dist((2, 2), (0, 0), (1, 0)))
# => "2.23606797749979"
