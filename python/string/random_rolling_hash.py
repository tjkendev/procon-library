# Random Rolling Hash
import random, math
random.seed()
def gen(a, b, num):
    result = set()
    while 1:
        while 1:
            v = random.randint(a, b)//2*2+1
            if v not in result:
                break
        for x in range(3, int(math.sqrt(v))+1, 2):
            if v % x == 0:
                break
        else:
            result.add(v)
            if len(result) == num:
                break
    return result
class RH():
    def __init__(self, s, base, mod):
        self.base = base
        self.mod = mod
        self.rev = pow(base, mod-2, mod)

        l = len(s)
        self.h = h = [0]*(l+1)
        tmp = 0
        for i in range(l):
            num = ord(s[i])
            tmp = (tmp*base + num) % mod
            h[i+1] = tmp
    def calc(self, l, r):
        return (self.h[r] - self.h[l] + self.mod) * pow(self.rev, l, self.mod) % self.mod
class RRH():
    def __init__(self, s, num=10):
        # 2 ~ 1000の間の乱数でnum個のハッシュをとる
        param = (2, 10**3, num)
        MOD = 10**9+7
        self.rhs = [RH(s, p, MOD) for p in gen(*param)]
    def calc(self, l, r):
        return [rh.calc(l, r) for rh in self.rhs]

# usage: RRH("abcd")