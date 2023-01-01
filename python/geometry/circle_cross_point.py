# the crossing points of two circles
def circles_cross_points(x1, y1, r1, x2, y2, r2):
    rr0 = (x2 - x1)**2 + (y2 - y1)**2
    xd = x2 - x1
    yd = y2 - y1
    rr1 = r1**2; rr2 = r2**2
    cv = (rr0 + rr1 - rr2)
    sv = (4*rr0*rr1 - cv**2)**.5
    return (
        (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
        (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
    )

# tangent points on a circle (x1, y1, r1) from a point (x2, y2)
def circle_tangent_points(x1, y1, r1, x2, y2):
    dd = (x1 - x2)**2 + (y1 - y2)**2
    r2 = (dd - r1**2)**.5
    return circles_cross_points(x1, y1, r1, x2, y2, r2)

p0, p1 = circles_cross_points(0, 0, 10, 6, 5, 10)
print("(%.4f, %.4f) (%.4f, %.4f)" % (p0 + p1))
# => "(-2.8935, 9.5722) (8.8935, -4.5722)"

p0, p1 = circle_tangent_points(0, 0, 10, 20, 15)
print("(%.4f, %.4f) (%.4f, %.4f)" % (p0 + p1))
# => "(-2.2991, 9.7321) (8.6991, -4.9321)"