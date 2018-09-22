from math import sqrt
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
 
def solve(x1, y1, r1, x2, y2, r2):
    rr0 = (x2 - x1)**2 + (y2 - y1)**2
    xd = x2 - x1
    yd = y2 - y1
    rr1 = r1**2; rr2 = r2**2
    cv = (rr0 + rr1 - rr2)
    sv = sqrt(4*rr0*rr1 - cv**2)
    return (
        (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
        (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
    )
 
p0, p1 = sorted(solve(x1, y1, r1, x2, y2, r2))
print("%.08f %.08f %.08f %.08f" % (p0 + p1))