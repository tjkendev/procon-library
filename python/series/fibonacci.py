# O(N)
def fibonacci1(N, M):
    a = 0; b = 1
    for _ in range(N):
        a, b = b, (a + b) % M
    return a

# O(log N)
def fibonacci2(N, M):
    # R = [1, 0; 0, 1]
    RA = RD = 1; RB = RC = 0
    # X = [1, 1; 1, 0]
    XA = XB = XC = 1; XD = 0
    while N:
        if N & 1:
            # R <- RX
            RA, RB, RC, RD = (RA*XA + RB*XC) % M, (RA*XB + RB*XD) % M, (RC*XA + RD*XC) % M, (RC*XB + RD*XD) % M
        # X <- XX
        XA, XB, XC, XD = (XA**2 + XB*XC) % M, XB*(XA + XD) % M, XC*(XA + XD) % M, (XB*XC + XD**2) % M
        N >>= 1
    return RC