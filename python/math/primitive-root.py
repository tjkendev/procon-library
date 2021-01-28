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


def primitive_root(n):
    # y = t = n-1 # if n is a prime
    y = t = euler_phi(n)
    ps = []
    x = 2
    while x*x <= y:
        if y % x == 0:
            while y % x == 0:
                y //= x
            ps.append(x)
        x += 1
    if y > 1:
        ps.append(y)
    g = 1
    while g < n:
        if all(pow(g, t//p, n) > 1 for p in ps):
            break
        g += 1
    return g


print(primitive_root(1000000007))
# => "5"
print(primitive_root(998244353))
# => "3"
