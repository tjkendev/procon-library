# Fast Modular Exponentiation
# builtin functionのpow(x, n, mod)と同じ
def fast_mod_pow(x, n, mod):
    r = 1
    while n > 0:
        if n & 1:
            r = (r * x) % mod
        x = (x * x) % mod
        n >>= 1
    return r

