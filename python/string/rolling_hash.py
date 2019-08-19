# 1-dimension Rolling Hash
class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

# 非クラス版
base = 37; mod = 10**9 + 9
pw = None
def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    v = 0
    for i in range(l):
        h[i+1] = v = (v * base + ord(s[i])) % mod
    return h
# RH前に、必要な長さの最大値分のpow-tableを計算しておく
def setup_pw(l):
    global pw
    pw = [1]*(l + 1)
    v = 1
    for i in range(l):
        pw[i+1] = v = v * base % mod
def get(h, l, r):
    return (h[r] - h[l] * pw[r-l]) % mod