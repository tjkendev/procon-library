# N: 素因数分解する数

def factorization(N):
    res = []
    x = N
    y = 2
    while y*y <= x:
        while x % y == 0:
            res.append(y)
            x //= y
        y += 1
    if x > 1:
        res.append(x)
    return res
