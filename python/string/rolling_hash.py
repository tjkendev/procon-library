# 1-dimension Rolling Hash
class RollingHash:
    def __init__(self, s, base, MOD):
        self.s = s
        self.l = l = len(s)
        self.base = base
        self.MOD = MOD
        self.h = h = [0]*(l + 1)
        for i in range(l):
            h[i+1] = (h[i] * base + ord(s[i])) % MOD
    def get(self, l, r):
        MOD = self.MOD
        return (self.h[r] - self.h[l]*pow(self.base, r-l, MOD)) % MOD

# 非クラス版
def rolling_hash(s, base, MOD):
    l = len(s)
    h = [0]*(l + 1)
    for i in range(l):
        h[i+1] = (h[i] * base + ord(s[i])) % MOD
    return h
def get(h, l, r, base, MOD):
    return (h[r] - h[l]*pow(base, r-l, MOD)) % MOD