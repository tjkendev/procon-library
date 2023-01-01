from math import sqrt
M = 10**6
p = [1]*(M+1)
p[0] = p[1] = 0
for x in range(2, int(sqrt(M))+1):
    if p[x]:
        for y in range(x*x, M+1, x):
            p[y] = 0