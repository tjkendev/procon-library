from math import pi, atan2

def circles_intersection_area(P1, r1, P2, r2):
    x1, y1 = P1; x2, y2 = P2

    dd = (x1 - x2)**2 + (y1 - y2)**2

    if (r1 + r2)**2 <= dd:
        return 0.0

    if dd <= (r1 - r2)**2:
        return pi*min(r1, r2)**2

    p1 = (r1**2 - r2**2 + dd)
    p2 = (r2**2 - r1**2 + dd)

    S1 = r1**2 * atan2((4*dd*r1**2 - p1**2)**.5, p1)
    S2 = r2**2 * atan2((4*dd*r2**2 - p2**2)**.5, p2)
    S0 = (4*dd*r1**2 - p1**2)**.5 / 2

    return S1 + S2 - S0

print(circles_intersection_area((0, 1), 1, (1, 0), 1))
# => "0.5707963267948966"
