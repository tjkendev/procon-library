M = 10**6
 
p = [0]*(M+60)
sM = M**0.5
for x in range(1, int(sM/2)+1):
    v = 4*x*x + 1; y = 8
    while v <= M:
        if v % 12 != 9: # v % 12 in [1, 5]
            p[v] ^= 1
        v += y; y += 8
for x in range(1, int(sM/3**0.5)+1, 2):
    v = 3*x*x + 4; y = 12
    while v <= M:
        if v % 12 == 7:
            p[v] ^= 1
        v += y; y += 8
for x in range(2, int(sM/2**0.5)+1):
    v = 2*x*(x+1)-1; y = 4*x-8
    while 0 <= y and v <= M:
        if v % 12 == 11:
            p[v] ^= 1
        v += y; y -= 8
 
for n in range(5, int(sM)+1):
    if p[n]:
        for z in range(n*n, M, n*n):
            p[z] = 0
p[2] = p[3] = 1