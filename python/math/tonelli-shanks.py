import random
random.seed()
def square_root(n, p):
    n %= p
    if pow(n, (p-1)//2, p) != 1:
        return -1
    q = p-1; m = 0
    while q & 1 == 0:
        q >>= 1
        m += 1
    z = random.randint(1, p-1)
    while pow(z, (p-1)>>1, p) == 1:
        z = random.randint(1, p-1)
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q+1)>>1, p)
    if t == 0:
        return 0
    while t != 1:
        m -= 1
        while pow(t, 2**m, p) != 1:
            m -= 1
            c = c * c % p
        r = r * c % p
        c = c * c % p
        t = t * c % p
    return r
print(square_root(4, 37))
# => "2" or "35"
print(square_root(6, 37))
# => "-1"