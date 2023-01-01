x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
 
from math import sqrt
 
def solve(x1, y1, r1, x2, y2, r2):
    result = []
    xd = x2 - x1; yd = y2 - y1
 
    rr0 = xd**2 + yd**2
    if (r1 - r2)**2 <= rr0:
        # 共通外接線
        cv = r1 - r2
        if rr0 == (r1 - r2)**2:
            # 円が内接する場合 => 共通外接線は1本
            result.append((x1 + r1*cv*xd/rr0, y1 + r1*cv*yd/rr0))
        else:
            sv = sqrt(rr0 - cv**2)
            # (x1, y1) + r1/r0*R(±θ)(x2 - x1, y2 - y1)
            result.append((x1 + r1*(cv*xd - sv*yd)/rr0, y1 + r1*(sv*xd + cv*yd)/rr0))
            result.append((x1 + r1*(cv*xd + sv*yd)/rr0, y1 + r1*(-sv*xd + cv*yd)/rr0))
    if (r1 + r2)**2 <= rr0:
        # 共通内接線
        cv = r1 + r2
        if rr0 == (r1 + r2)**2:
            # 円が外接する場合 => 共通内接線は1本
            result.append((x1 + r1*cv*xd/rr0, y1 + r1*cv*yd/rr0))
        else:
            sv = sqrt(rr0 - cv**2)
            # (x1, y1) + r1/r0*R(±θ)(x2 - x1, y2 - y1)
            result.append((x1 + r1*(cv*xd - sv*yd)/rr0, y1 + r1*(sv*xd + cv*yd)/rr0))
            result.append((x1 + r1*(cv*xd + sv*yd)/rr0, y1 + r1*(-sv*xd + cv*yd)/rr0))
    return result
 
result = sorted(solve(x1, y1, r1, x2, y2, r2))
if result:
    print("\n".join("%.08f %.08f" % p for p in result))