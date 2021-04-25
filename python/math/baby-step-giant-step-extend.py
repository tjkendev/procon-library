# Extended Euclidean Algorithm
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# X^K ≡ Y (mod M) となるような K を求める
def solve(X, Y, M):
    c = 0
    # gcd(X, M) = 1 となるまで処理
    d, rX, _ = extgcd(X, M)
    while d > 1:
        if Y % d > 0:
            if Y == 1:
                return c
            # 解なし
            return -1
        c += 1
        M //= d
        Y = (Y // d * rX) % M
        d, rX, _ = extgcd(X, M)

    sq = int(M**.5) + 1
    D = {1: 0}

    # Baby-step
    Z = 1
    for i in range(sq):
        Z  = Z * X % M
        D[Z] = i + 1
    if Y in D:
        return D[Y] + c

    # Giant-step
    R = extgcd(Z, M)[1] % M # R = X^(-sq)
    for i in range(1, sq+1):
        Y = Y * R % M
        if Y in D:
            return D[Y] + i*sq + c
    return -1

X = 3; Y = 193; MOD = 10**9 + 7
r = solve(X, Y, MOD)
assert pow(X, r, MOD) == Y, (pow(X, r, MOD), Y)

X = 21; Y = 192; MOD = (10**9 + 7) * 3
r = solve(X, Y, MOD)
assert pow(X, r, MOD) == Y, (pow(X, r, MOD), Y)