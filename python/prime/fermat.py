# -*- encoding: utf-8 -*-

# フェルマーテスト
# - カーマイケル数には弱い
def fermat(k):
    for t in xrange(1000):
        a = randint(2, k-1)
        if pow(a, k-1, k)!=1:
            return 0
    return 1
