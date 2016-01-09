# Fast Modular Exponentiation
# builtin functionのpow(x, n, mod)と同じ
def fast_mod_pow(x, n, mod):
    r = 1
    while n>0:
        if n&1:
            r = (r * x) % mod
        x = (x * x) % mod
        n >>= 1
    return r

# gcd(greatest common divisor)
def gcd(m, n):
    if m<n: return gcd(n, m)
    r = m%n
    return gcd(n, r) if r else n
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a%b)
        y -= (a/b)*x
        return d, x, y
    else:
        return a, 1, 0
