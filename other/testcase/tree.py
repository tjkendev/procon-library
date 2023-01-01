import random, sys
random.seed()

N = random.randint(1, 10)
sys.stdout.write("%d\n" % N)
*V, = range(1, N+1)
random.shuffle(V)
E = []
for i in range(N-1):
    j = random.randint(0, i)
    E.append("%d %d\n" % (V[j], V[i+1]))
random.shuffle(E)
sys.stdout.writelines(E)