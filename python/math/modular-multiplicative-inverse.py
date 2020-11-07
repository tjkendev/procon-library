# Extended Euclidean Algorithm
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# find the value of x s.t. ax ≡ 1 (mod m)
# by using extended Euclidean algorithm
def inverse(a, m):
    d, x, _ = extgcd(a, m)
    if d != 1:
        # no inverse exists
        return -1
    return x % m


# Euler's totient function
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

# find the value of x s.t. ax ≡ 1 (mod m)
# by using Euler's theorem
def inverse(a, m):
    # φ(m) = m-1 if m is a prime
    phi = euler_phi(m)
    res = pow(a, phi-1, m)
    if res*a % m != 1:
        # no inverse exists
        return -1
    return res