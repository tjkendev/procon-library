def incircle(P1, P2, P3):
    x1, y1 = P1; x2, y2 = P2; x3, y3 = P3

    dx1 = x2 - x1; dy1 = y2 - y1
    dx2 = x3 - x1; dy2 = y3 - y1

    d1 = ((x3 - x2)**2 + (y3 - y2)**2)**.5
    d2 = (dx2**2 + dy2**2)**.5
    d3 = (dx1**2 + dy1**2)**.5
    dsum = d1 + d2 + d3

    r = abs(dx1 * dy2 - dx2 * dy1) / dsum
    x = (x1*d1 + x2*d2 + x3*d3) / dsum
    y = (y1*d1 + y2*d2 + y3*d3) / dsum
    return x, y, r

def excircle(P1, P2, P3):
    x1, y1 = P1; x2, y2 = P2; x3, y3 = P3

    dx1 = x2 - x1; dy1 = y2 - y1
    dx2 = x3 - x1; dy2 = y3 - y1

    d1 = ((x3 - x2)**2 + (y3 - y2)**2)**.5
    d3 = (dx1**2 + dy1**2)**.5
    d2 = (dx2**2 + dy2**2)**.5

    S2 = abs(dx1 * dy2 - dx2 * dy1)

    dsum1 = - d1 + d2 + d3
    r1 = S2 / dsum1
    ex1 = (- x1*d1 + x2*d2 + x3*d3) / dsum1
    ey1 = (- y1*d1 + y2*d2 + y3*d3) / dsum1

    dsum2 = d1 - d2 + d3
    r2 = S2 / dsum2
    ex2 = (x1*d1 - x2*d2 + x3*d3) / dsum2
    ey2 = (y1*d1 - y2*d2 + y3*d3) / dsum2

    dsum3 = d1 + d2 - d3
    r3 = S2 / dsum3
    ex3 = (x1*d1 + x2*d2 - x3*d3) / dsum3
    ey3 = (y1*d1 + y2*d2 - y3*d3) / dsum3

    return (ex1, ey1, r1), (ex2, ey2, r2), (ex3, ey3, r3)

print("%.4f %.4f %.4f" % incircle((1, 0), (3, 3), (5, 1)))
# => "3.1472 1.5132 0.9472"

for c in excircle((1, 0), (3, 3), (5, 1)):
    print("%.4f %.4f %.4f" % c)
# =>
# 5.6260 3.2600 2.0407
# 3.6726 -3.7924 4.3274
# -0.8458 2.6192 2.9887
