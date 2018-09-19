# FMT用のパラメタ
omega = 103
n = 2**18
P = 5880*n + 1
rev = pow(omega, P-2, P)

# バタフライ演算としてのbit反転処理
# in-placeで計算するために利用
def bit_reverse(d):
    n = len(d)
    ns = n>>1; nss = ns>>1
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

# FMTをループで計算
def fmt_bu(A, n, base, half, Q):
    N = n
    m = 1
    while n>1:
        n >>= 1
        # ω^{2m} ≡ 1 となるω
        w = pow(base, n, Q)
        wk = 1
        for j in range(m):
            for i in range(j, N, 2*m):
                # U = g(ω^{2k}), V = ω^k * h(ω^{2k})
                U = A[i]; V = (A[i+m]*wk) % Q
                A[i] = (U + V) % Q
                # half = ω^{N/2}
                A[i+m] = (U + V*half) % Q
            wk = (wk * w) % Q
        m <<= 1
    return A

# FMTの順変換
def fmt(f, l, Q=P):
    if l == 1: return f
    A = f[:]
    # bit反転
    bit_reverse(A)
    return fmt_bu(A, n, omega, pow(omega, n/2, Q), Q)

# FMTの逆変換
def ifmt(F, l, Q=P):
    if l == 1: return F
    A = F[:]
    # bit反転
    bit_reverse(A)
    # 逆変換なので、ωの代わりにω^{-1}を渡す
    f = fmt_bu(A, n, rev, pow(rev, n/2, Q), Q)
    # Nで割って返す
    n_rev = pow(n, Q-2, Q)
    return [(e * n_rev) % Q for e in f]

# FMTを利用した畳込み処理
def convolute(a, b, l, Q=P):
    A = fmt(a, l, Q)
    B = fmt(b, l, Q)
    C = [(s * t) % Q for s, t in zip(A, B)]
    c = ifmt(C, l, Q)
    return c