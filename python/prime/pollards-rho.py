def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def pollard_rho(n, a, x0):
    # use f(x) = x^2 + a (mod n)
    f = lambda x: (x**2 + a) % n
    x = y = x0
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(n, abs(x - y))
    # return failure (-1) if d == n
    return d if d < n else -1

# with Brent's improvement
def pollard_rho(n, a, x0):
    # use f(x) = x^2 + a (mod n)
    f = lambda x: (x*x + a) % n
    x = y = ys = x0; r = 1; q = 1
    m = 100
    d = 1
    while d == 1:
        x = y
        for i in range(r):
            y = f(y)
        for k in range(0, r, m):
            ys = y
            for i in range(min(m, r-k)):
                y = f(y)
                q = q * abs(x - y) % n
            d = gcd(n, q)
            if d != 1:
                break
        r <<= 1
    if d == n:
        while d == 1:
            ys = f(ys)
            d = gcd(n, abs(x - ys))
    # return failure (-1) if d == n
    return d if d < n else -1

print(pollard_rho(1000000009 * 1000000007, 1, 2))
# => "1000000009"
print(pollard_rho(2 * 3 * 5 * 17, 1, 2))
# => "6"
print(pollard_rho(1000000007, 1, 2))
# => "-1"