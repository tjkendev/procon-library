def reflection(line, point):
    x0, y0, x1, y1 = line
    p, q = point
    x1 -= x0; y1 -= y0
    p -= x0; q -= y0
    cv = p*x1 + q*y1
    sv = p*y1 - q*x1
    cv2 = cv**2 - sv**2
    sv2 = 2*cv*sv
    dd = (p**2 + q**2)*(x1**2 + y1**2)
    if dd == 0:
        return x0 + p, y0 + q
    return x0 + (cv2 * p - sv2 * q) / dd, y0 + (sv2 * p + cv2 * q) / dd

# example
print(reflection((0, 2, 2, 1), (0, 0)))
# => (1.6, 3.2)