omega = 139
n = 2**9
P = 1359*n + 1
rev = pow(omega, P-2, P)

def bit_reverse(d):
    n = len(d)
    ns = n >> 1
    nss = ns >> 1
    ns1 = ns + 1
    i = 0
    for j in range(0, ns, 2):
        if j<i:
            d[i], d[j] = d[j], d[i]
            d[i+ns1], d[j+ns1] = d[j+ns1], d[i+ns1]
        d[i+1], d[j+ns] = d[j+ns], d[i+1]
        k = nss; i ^= k
        while k > i:
            k >>= 1; i ^= k
    return d

def fmt_bu(A, n, base, half, Q):
    N = n
    m = 1
    while n > 1:
        n >>= 1
        w = pow(base, n, Q)
        wk = 1
        for j in range(m):
            for i in range(j, N, 2*m):
                U = A[i]; V = (A[i+m]*wk) % Q
                A[i] = (U + V) % Q
                A[i+m] = (U + V*half) % Q
            wk = (wk * w) % Q
        m <<= 1
    return A

def fmt2d(f, l, Q=P):
    tmp = [None]*n
    for i in range(n):
        A = list(f[i])
        bit_reverse(A)
        tmp[i] = fmt_bu(A, n, omega, pow(omega, n//2, Q), Q)
    *tmp, = zip(*tmp)
    F = [None]*n
    for i in range(n):
        A = list(tmp[i])
        bit_reverse(A)
        F[i] = fmt_bu(A, n, omega, pow(omega, n//2, Q), Q)
    *F, = zip(*F)
    return F

def ifmt2d(F, l, Q=P):
    tmp = [None]*n
    for i in range(n):
        A = list(F[i])
        bit_reverse(A)
        tmp[i] = fmt_bu(A, n, rev, pow(omega, n//2, Q), Q)
    *tmp, = zip(*tmp)
    f = [None]*n
    for i in range(n):
        A = list(tmp[i])
        bit_reverse(A)
        f[i] = fmt_bu(A, n, rev, pow(omega, n//2, Q), Q)
    *f, = zip(*f)
    n2_rev = pow(n*n, (Q-2), Q)
    F1 = [[(e * n2_rev) % Q for e in fi] for fi in f]
    return F1

def convolute2d(a, b, l, Q=P):
    A = fmt2d(a, l, Q)
    B = fmt2d(b, l, Q)
    C = [[(s * t) % Q for s, t in zip(Ai, Bi)] for Ai, Bi in zip(A, B)]
    c = ifmt2d(C, l, Q)
    return c
