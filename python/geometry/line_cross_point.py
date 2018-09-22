def solve(x0, y0, x1, y1, x2, y2, x3, y3):
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if s < 0:
        s = -s
        sm = -sm
    if s == 0:
        x = x0
        y = y0
    else:
        x = x0 + s*dx0/sm
        y = y0 + s*dy0/sm
    return x, y

for t in range(int(input())):
    print("%.09f %.09f" % solve(*map(int, input().split())))