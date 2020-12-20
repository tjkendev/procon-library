# calculate φ(n)
def euler_phi(n):
    res = n
    x = 2
    while x*x <= n:
        if n % x == 0:
            res = res // x * (x-1)
            while n % x == 0:
                n //= x
        x += 1
    if n > 1:
        res = res // n * (n-1)
    return res


# calculate φ(x) for 1 <= x <= M
M = 10**6
*phi, = range(M+1)
for x in range(2, M+1):
    if phi[x] == x:
        for y in range(x, M+1, x):
            phi[y] = phi[y] // x * (x-1)