from math import sqrt
def solve(cx, cy, r, x1, y1, x2, y2):
    xd = x2 - x1; yd = y2 - y1
    X = x1 - cx; Y = y1 - cy
    a = xd**2 + yd**2
    b = xd * X + yd * Y
    c = X**2 + Y**2 - r**2
    # D = 0の時は1本で、D < 0の時は存在しない
    D = b**2 - a*c
    s1 = (-b + sqrt(D)) / a
    s2 = (-b - sqrt(D)) / a
    return (x1 + xd*s1, y1 + yd*s1), (x1 + xd*s2, y1 + yd*s2)
cx, cy, r = map(int, input().split())
q = int(input())
for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())

    p0, p1 = sorted(solve(cx, cy, r, x1, y1, x2, y2))
    print("%.08f %.08f %.08f %.08f" % (p0 + p1))