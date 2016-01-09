# -*- encoding: utf-8 -*-

# フェルマーテスト
# - カーマイケル数には弱い
def fermat(k):
    for t in xrange(1000):
        a = randint(2, k-1)
        if pow(a, k-1, k)!=1:
            return 0
    return 1

# ミラーラビン素数判定法
def miller_rabin(n):
    if n==2: return 1
    if n==1 or n&1==0: return 0
    d = n-1
    d /= d & -d
    for k in xrange(1000):
        a = randint(1, n-1)
        t = d
        y = pow(a, t, n)
        while t!=n-1 and y!=1 and y!=n-1:
            y = y**2 % n
            t <<= 1
        if y!=n-1 and t&1==0: return 0
    return 1
