def common_tangent_lines(x1, y1, r1, x2, y2, r2):
    result = []
    xd = x2 - x1; yd = y2 - y1

    rr0 = xd**2 + yd**2
    if (r1 - r2)**2 <= rr0:
        cv = r1 - r2
        if rr0 == (r1 - r2)**2:
            bx = r1*cv*xd/rr0
            by = r1*cv*yd/rr0
            result.append([
                (x1 + bx, y1 + by),
                (x1 - yd + bx, y1 + xd + by),
            ])
        else:
            sv = (rr0 - cv**2)**.5
            px = (cv*xd - sv*yd); py = (sv*xd + cv*yd)
            result.append([
                (x1 + r1*px/rr0, y1 + r1*py/rr0),
                (x2 + r2*px/rr0, y2 + r2*py/rr0),
            ])
            qx = (cv*xd + sv*yd); qy = (-sv*xd + cv*yd)
            result.append([
                (x1 + r1*qx/rr0, y1 + r1*qy/rr0),
                (x2 + r2*qx/rr0, y2 + r2*qy/rr0),
            ])
    if (r1 + r2)**2 <= rr0:
        cv = r1 + r2
        if rr0 == (r1 + r2)**2:
            bx = r1*cv*xd/rr0
            by = r1*cv*yd/rr0
            result.append([
                (x1 + bx, y1 + by),
                (x1 - yd + bx, y1 + xd + by),
            ])
        else:
            sv = (rr0 - cv**2)**.5
            px = (cv*xd - sv*yd); py = (sv*xd + cv*yd)
            result.append([
                (x1 + r1*px/rr0, y1 + r1*py/rr0),
                (x2 - r2*px/rr0, y2 - r2*py/rr0),
            ])
            qx = (cv*xd + sv*yd); qy = (-sv*xd + cv*yd)
            result.append([
                (x1 + r1*qx/rr0, y1 + r1*qy/rr0),
                (x2 - r2*qx/rr0, y2 - r2*qy/rr0),
            ])
    return result
