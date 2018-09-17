# フェルマーテスト
import random
def fermat(k):
    for _ in xrange(1000):
        a = random.randint(2, k-1)
        if pow(a, k-1, k)!=1:
            return 0
    return 1
