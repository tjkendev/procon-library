# a/b <= √p <= c/d を満たす a,b,c,d <= n を求める
def stern_brocot(p, n):
    la = 0; lb = 1
    ra = 1; rb = 0
    lu = ru = 1
    lx = 0; ly = 1
    rx = 1; ry = 0
    while lu or ru:
        ma = la + ra; mb = lb + rb
        if p * mb**2 < ma**2:
            ra = ma; rb = mb
            if ma <= n and mb <= n:
                rx = ma; ry = mb
            else:
                lu = 0
        else:
            la = ma; lb = mb
            if ma <= n and mb <= n:
                lx = ma; ly = mb
            else:
                ru = 0
    # lx/ly <= √p <= rx/ry
    return lx, ly, rx, ry
