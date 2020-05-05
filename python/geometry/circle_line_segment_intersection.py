def intersection(cx, cy, r, P1, P2):
    x1, y1 = P1; x2, y2 = P2

    xd = x2 - x1; yd = y2 - y1
    X = x1 - cx; Y = y1 - cy
    a = xd**2 + yd**2
    b = xd * X + yd * Y
    c = X**2 + Y**2 - r**2

    f0 = c; f1 = a+2*b+c
    if (f0 >= 0 and f1 <= 0) or (f0 <= 0 and f1 >= 0):
        return True
    return -a <= b <= 0 and b**2 - a*c >= 0 and (f0 >= 0 or f1 >= 0)

print(intersection(2, 0, 1, (-2, 0), (0, 0)))
# => "False"
print(intersection(0, 0, 1, (-2, 0), (0, 0)))
# => "True"
print(intersection(0, 0, 2, (-2, 0), (0, 0)))
# => "True"
print(intersection(0, 0, 3, (-2, 0), (0, 0)))
# => "False"