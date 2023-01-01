# cross product: (b - a)×(c - a)
def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

# O(N)
def inside_convex_polygon0(p0, qs):
    L = len(qs)
    D = [cross3(qs[i-1], p0, qs[i]) for i in range(L)]
    return all(e >= 0 for e in D) or all(e <= 0 for e in D)

# O(log N)
def inside_convex_polygon(p0, qs):
    L = len(qs)
    left = 1; right = L
    q0 = qs[0]
    while left+1 < right:
        mid = (left + right) >> 1
        if cross3(q0, p0, qs[mid]) <= 0:
            left = mid
        else:
            right = mid
    if left == L-1:
        left -= 1
    qi = qs[left]; qj = qs[left+1]
    v0 = cross3(q0, qi, qj)
    v1 = cross3(q0, p0, qj)
    v2 = cross3(q0, qi, p0)
    if v0 < 0:
        v1 = -v1; v2 = -v2
    return 0 <= v1 and 0 <= v2 and v1 + v2 <= v0

qs = [(-2, 0), (0, -2), (2, 0), (0, 2)]
print(inside_convex_polygon((0, 0), qs))
# => "True"
print(inside_convex_polygon((1, 1), qs))
# => "True"
print(inside_convex_polygon((2, 2), qs))
# => "False"