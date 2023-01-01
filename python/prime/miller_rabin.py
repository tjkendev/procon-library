# ミラーラビン素数判定法
import random
def miller_rabin(n, t):
    if n == 2:
        return 1
    if n == 1 or n & 1 == 0:
        return 0
    d = n-1
    d //= d & -d
    for _ in range(t):
        a = random.randint(1, n-1)
        t = d
        y = pow(a, t, n)
        while t != n-1 and y != 1 and y != n-1:
            y = y**2 % n
            t <<= 1
        if y != n-1 and t & 1 == 0:
            return 0
    return 1
