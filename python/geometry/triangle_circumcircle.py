def circumcircle(P1, P2, P3):
    x1, y1 = P1; x2, y2 = P2; x3, y3 = P3
    a = 2*(x1 - x2); b = 2*(y1 - y2); p = x1**2 - x2**2 + y1**2 - y2**2
    c = 2*(x1 - x3); d = 2*(y1 - y3); q = x1**2 - x3**2 + y1**2 - y3**2
    det = a*d - b*c
    x = d*p - b*q; y = a*q - c*p
    if det < 0:
        x = -x; y = -y; det = -det
    x /= det; y /= det
    r = ((x - x1)**2 + (y - y1)**2)**.5
    return x, y, r

print("%.4f %.4f %.4f" % circumcircle((0, 0), (1, 0), (0, 1)))
# => "0.5000 0.5000 0.7071"